import { spawn } from 'child_process';
import fs from 'fs';

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9351;

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function testViewport(width) {
  const chrome = spawn(CHROME_PATH, [
    `--remote-debugging-port=${PORT}`,
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    `--window-size=${width},850`,
    'about:blank'
  ]);

  let wsUrl = null;
  for (let i = 0; i < 30; i++) {
    await sleep(150);
    try {
      const res = await fetch(`http://127.0.0.1:${PORT}/json/version`);
      if (res.ok) {
        const data = await res.json();
        wsUrl = data.webSocketDebuggerUrl;
        break;
      }
    } catch (e) {}
  }

  const ws = new WebSocket(wsUrl);
  let idCounter = 1;
  const pending = new Map();

  ws.onmessage = (event) => {
    const msg = JSON.parse(event.data);
    if (msg.id && pending.has(msg.id)) {
      const { resolve, reject } = pending.get(msg.id);
      pending.delete(msg.id);
      if (msg.error) reject(msg.error);
      else resolve(msg.result);
    }
  };

  await new Promise(r => ws.onopen = r);

  function send(method, params = {}) {
    return new Promise((resolve, reject) => {
      const id = idCounter++;
      pending.set(id, { resolve, reject });
      ws.send(JSON.stringify({ id, method, params }));
    });
  }

  const target = await send("Target.createTarget", { url: "http://localhost:8080/p12/index.html" });
  const pageWs = new WebSocket(`ws://127.0.0.1:${PORT}/devtools/page/${target.targetId}`);
  await new Promise(r => pageWs.onopen = r);

  const pagePending = new Map();
  pageWs.onmessage = (event) => {
    const msg = JSON.parse(event.data);
    if (msg.id && pagePending.has(msg.id)) {
      const { resolve, reject } = pagePending.get(msg.id);
      pagePending.delete(msg.id);
      if (msg.error) reject(msg.error);
      else resolve(msg.result);
    }
  };

  function sendPage(method, params = {}) {
    return new Promise((resolve, reject) => {
      const id = idCounter++;
      pagePending.set(id, { resolve, reject });
      pageWs.send(JSON.stringify({ id, method, params }));
    });
  }

  await sendPage("Page.enable");
  await sendPage("Runtime.enable");

  await sendPage("Emulation.setDeviceMetricsOverride", {
    width,
    height: 850,
    deviceScaleFactor: 2,
    mobile: width < 1000
  });

  await sendPage("Page.navigate", { url: "http://localhost:8080/p12/index.html" });
  await sleep(1500);

  // Helper to check floating state
  async function checkState(label) {
    const res = await sendPage("Runtime.evaluate", {
      expression: `
        (() => {
          const wrap = document.getElementById('floatingCtaWrap');
          const btn = document.getElementById('floatingCtaBtn');
          const pBtn = document.getElementById('pricingCtaBtn');
          const isVisible = wrap ? wrap.classList.contains('is-visible') : false;
          const rect = wrap ? wrap.getBoundingClientRect() : null;
          const btnRect = btn ? btn.getBoundingClientRect() : null;
          return {
            isVisible,
            scrollY: Math.round(window.scrollY),
            opacity: wrap ? window.getComputedStyle(wrap).opacity : null,
            pointerEvents: wrap ? window.getComputedStyle(wrap).pointerEvents : null,
            btnWidth: btnRect ? Math.round(btnRect.width) : null,
            btnHeight: btnRect ? Math.round(btnRect.height) : null,
            btnHref: btn ? btn.href : null,
            btnText: btn ? btn.innerText.trim() : null
          };
        })()
      `,
      returnByValue: true
    });
    return { label, ...res.result.value };
  }

  const steps = [];

  // 1. Top of page
  steps.push(await checkState('1. Top of page (scroll 0)'));

  // 2. Scroll to pricing
  await sendPage("Runtime.evaluate", {
    expression: `document.getElementById('pricingCtaBtn').scrollIntoView({ block: 'center' });`
  });
  await sleep(400);
  steps.push(await checkState('2. At pricing CTA (pricing visible)'));

  // 3. Scroll past pricing to for-who section
  await sendPage("Runtime.evaluate", {
    expression: `document.getElementById('for-who').scrollIntoView({ block: 'center' });`
  });
  await sleep(400);
  steps.push(await checkState('3. Past pricing at for-who (no CTA visible)'));

  // Take screenshot while visible
  if (width === 390 || width === 1200) {
    const ss = await sendPage("Page.captureScreenshot", {
      format: 'png',
      clip: {
        x: 0,
        y: 0,
        width,
        height: 850,
        scale: 1
      }
    });
    fs.writeFileSync(`C:/Users/lucas/.gemini/antigravity-ide/brain/8c32631a-d8e5-4716-b40e-7620b429403f/floating_cta_visible_${width}.png`, Buffer.from(ss.data, 'base64'));
  }

  // 4. Scroll to closing section
  await sendPage("Runtime.evaluate", {
    expression: `document.getElementById('closing').scrollIntoView({ block: 'start' });`
  });
  await sleep(400);
  steps.push(await checkState('4. At closing section (no CTA visible)'));

  // 5. Scroll to FAQ final CTA
  await sendPage("Runtime.evaluate", {
    expression: `document.querySelector('#faq a.btn-cta').scrollIntoView({ block: 'center' });`
  });
  await sleep(400);
  steps.push(await checkState('5. At FAQ final CTA (final CTA visible)'));

  // 6. Scroll back up to closing
  await sendPage("Runtime.evaluate", {
    expression: `document.getElementById('closing').scrollIntoView({ block: 'center' });`
  });
  await sleep(400);
  steps.push(await checkState('6. Back up at closing (reappears)'));

  // 7. Scroll back up to hero
  await sendPage("Runtime.evaluate", {
    expression: `document.getElementById('hero').scrollIntoView({ block: 'start' });`
  });
  await sleep(400);
  steps.push(await checkState('7. Back up at hero (hides)'));

  // 8. Test anchor load directly to #closing
  await sendPage("Page.navigate", { url: "http://localhost:8080/p12/index.html#closing" });
  await sleep(1000);
  steps.push(await checkState('8. Direct load at #closing anchor'));

  await send("Browser.close");
  chrome.kill();
  return steps;
}

async function main() {
  const allResults = {};
  for (const w of [360, 390, 768, 1200]) {
    console.log(`Running floating CTA tests for ${w}px...`);
    allResults[w] = await testViewport(w);
  }
  console.log('RESULTS:\n', JSON.stringify(allResults, null, 2));
}

main().catch(console.error);
