import { spawn } from 'child_process';
import fs from 'fs';

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9339;

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function runTest(width) {
  const chrome = spawn(CHROME_PATH, [
    `--remote-debugging-port=${PORT}`,
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    `--window-size=${width},900`,
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
    height: 900,
    deviceScaleFactor: 2,
    mobile: width < 1000
  });

  await sendPage("Page.navigate", { url: "http://localhost:8080/p12/index.html" });
  await sleep(1500);

  // Scroll to pain section
  await sendPage("Runtime.evaluate", {
    expression: `
      document.getElementById('pain').scrollIntoView({ behavior: 'instant' });
    `
  });
  await sleep(800);

  // Measure card vs dot positions
  const evalResult = await sendPage("Runtime.evaluate", {
    expression: `
      (() => {
        const wrapper = document.querySelector('.pain-timeline-wrapper');
        const cards = Array.from(document.querySelectorAll('.pain-card'));
        const trackPath = document.getElementById('svg-descent-track');
        const loopPath = document.getElementById('svg-loop-path');
        const loopArrow = document.getElementById('svg-loop-arrow');

        const trackD = trackPath ? trackPath.getAttribute('d') : '';
        const loopD = loopPath ? loopPath.getAttribute('d') : '';

        const cardMeasures = cards.map((card, i) => {
          const cardInner = card.querySelector('.pain-card-inner');
          const cardRect = cardInner.getBoundingClientRect();
          const cardCenterY = cardRect.top + cardRect.height / 2;
          
          const bullet = card.querySelector('.pain-node-bullet');
          const circle = bullet ? bullet.querySelector('.svg-node-bg') : null;
          let bulletCenterY = null;
          let bulletCenterX = null;
          if (circle) {
            const circleRect = circle.getBoundingClientRect();
            bulletCenterY = circleRect.top + circleRect.height / 2;
            bulletCenterX = circleRect.left + circleRect.width / 2;
          }

          return {
            index: i,
            cardHeight: Math.round(cardRect.height * 10) / 10,
            cardCenterY: Math.round(cardCenterY * 10) / 10,
            bulletCenterY: bulletCenterY !== null ? Math.round(bulletCenterY * 10) / 10 : null,
            bulletCenterX: bulletCenterX !== null ? Math.round(bulletCenterX * 10) / 10 : null,
            diff: bulletCenterY !== null ? Math.round((cardCenterY - bulletCenterY) * 10) / 10 : null
          };
        });

        return {
          cardMeasures,
          trackD,
          loopD
        };
      })()
    `,
    returnByValue: true
  });

  // Capture screenshot of pain section
  const clipRes = await sendPage("Runtime.evaluate", {
    expression: `
      (() => {
        const el = document.getElementById('pain');
        const rect = el.getBoundingClientRect();
        return { x: rect.x, y: rect.y, width: rect.width, height: rect.height };
      })()
    `,
    returnByValue: true
  });
  const clip = clipRes.result.value;
  const ss = await sendPage("Page.captureScreenshot", {
    format: 'png',
    clip: {
      x: 0,
      y: clip.y > 0 ? clip.y : 0,
      width: width,
      height: Math.min(clip.height, 900),
      scale: 1
    }
  });
  
  const ssPath = `scratch/real_after_${width}.png`;
  fs.writeFileSync(ssPath, Buffer.from(ss.data, 'base64'));
  if (width === 390 || width === 1200) {
    fs.writeFileSync(`C:/Users/lucas/.gemini/antigravity-ide/brain/8c32631a-d8e5-4716-b40e-7620b429403f/after_dobra2_${width}.png`, Buffer.from(ss.data, 'base64'));
  }

  await send("Browser.close");
  chrome.kill();
  return evalResult.result.value;
}

async function main() {
  const results = {};
  for (const w of [360, 390, 768, 1200]) {
    console.log(`Running AFTER verification for ${w}px...`);
    results[w] = await runTest(w);
  }
  console.log('REAL AFTER RESULTS:');
  console.log(JSON.stringify(results, null, 2));
}

main().catch(console.error);
