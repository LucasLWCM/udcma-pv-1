import { spawn } from 'child_process';
import fs from 'fs';

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9337;

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function main() {
  const chrome = spawn(CHROME_PATH, [
    `--remote-debugging-port=${PORT}`,
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--window-size=1200,800',
    'about:blank'
  ]);

  let wsUrl = null;
  for (let i = 0; i < 30; i++) {
    await sleep(200);
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

  const viewports = [360, 390, 768, 1200];
  const allResults = {};

  for (const width of viewports) {
    await sendPage("Emulation.setDeviceMetricsOverride", {
      width,
      height: 900,
      deviceScaleFactor: 2,
      mobile: width < 1000
    });

    // Scroll to pain section and trigger visibility
    await sendPage("Runtime.evaluate", {
      expression: `
        document.getElementById('pain').scrollIntoView();
        document.querySelectorAll('.pain-card').forEach(c => c.classList.add('is-visible'));
      `
    });
    await sleep(600);

    const evalResult = await sendPage("Runtime.evaluate", {
      expression: `
        (() => {
          const wrapper = document.querySelector('.pain-timeline-wrapper');
          const cards = Array.from(document.querySelectorAll('.pain-card'));
          const nodes = Array.from(document.querySelectorAll('.svg-node-wrap'));

          return cards.map((card, i) => {
            const cardInner = card.querySelector('.pain-card-inner');
            const cardRect = cardInner.getBoundingClientRect();
            const cardCenterY = cardRect.top + cardRect.height / 2;
            
            let nodeCenterY = null;
            if (nodes[i]) {
              const circle = nodes[i].querySelector('.svg-node-bg');
              if (circle) {
                const circleRect = circle.getBoundingClientRect();
                nodeCenterY = circleRect.top + circleRect.height / 2;
              }
            }

            return {
              index: i,
              cardHeight: Math.round(cardRect.height * 10) / 10,
              cardCenterY: Math.round(cardCenterY * 10) / 10,
              nodeCenterY: nodeCenterY !== null ? Math.round(nodeCenterY * 10) / 10 : null,
              diff: nodeCenterY !== null ? Math.round((cardCenterY - nodeCenterY) * 10) / 10 : null
            };
          });
        })()
      `,
      returnByValue: true
    });

    allResults[width] = evalResult.result.value;

    // Take screenshot at 390px
    if (width === 390) {
      const clipRes = await sendPage("Runtime.evaluate", {
        expression: `
          (() => {
            const el = document.getElementById('pain');
            const rect = el.getBoundingClientRect();
            return { x: rect.x, y: rect.y + window.scrollY, width: rect.width, height: rect.height };
          })()
        `,
        returnByValue: true
      });
      const clip = clipRes.result.value;
      const ss = await sendPage("Page.captureScreenshot", {
        format: 'png',
        clip: {
          x: 0,
          y: clip.y,
          width: 390,
          height: Math.min(clip.height, 950),
          scale: 1
        }
      });
      fs.writeFileSync('scratch/before_pain_390.png', Buffer.from(ss.data, 'base64'));
    }
  }

  fs.writeFileSync('scratch/diagnose_before.json', JSON.stringify(allResults, null, 2));
  console.log('Diagnostic BEFORE results:');
  console.log(JSON.stringify(allResults, null, 2));

  await send("Browser.close");
  chrome.kill();
}

main().catch(console.error);
