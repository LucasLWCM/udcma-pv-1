import { spawn } from 'child_process';
import fs from 'fs';

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9339;

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function run() {
  const chrome = spawn(CHROME_PATH, [
    `--remote-debugging-port=${PORT}`,
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    'about:blank'
  ]);

  let wsUrl = null;
  for (let i = 0; i < 30; i++) {
    await sleep(200);
    try {
      const res = await fetch(`http://127.0.0.1:${PORT}/json/version`);
      if (res.ok) {
        wsUrl = (await res.json()).webSocketDebuggerUrl;
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

  await new Promise(r => pageWs.onopen = r);

  function sendPage(method, params = {}) {
    return new Promise((resolve, reject) => {
      const id = idCounter++;
      pagePending.set(id, { resolve, reject });
      pageWs.send(JSON.stringify({ id, method, params }));
    });
  }

  await sendPage("Page.enable");
  await sendPage("Runtime.enable");

  const viewports = [360, 390, 768, 1280];

  for (const width of viewports) {
    await sendPage("Emulation.setDeviceMetricsOverride", {
      width,
      height: 900,
      deviceScaleFactor: 2,
      mobile: width < 1000
    });

    await sendPage("Runtime.evaluate", {
      expression: `
        document.getElementById('pain').scrollIntoView();
      `
    });
    await sleep(1000);

    // Get section clip
    const secBox = await sendPage("Runtime.evaluate", {
      expression: `
        (() => {
          const el = document.getElementById('pain');
          const r = el.getBoundingClientRect();
          return { x: r.left, y: r.top, width: r.width, height: r.height };
        })()
      `,
      returnByValue: true
    });

    const box = secBox.result.value;

    const shot = await sendPage("Page.captureScreenshot", {
      format: "png",
      clip: {
        x: Math.max(0, box.x),
        y: Math.max(0, box.y),
        width: box.width,
        height: Math.min(box.height, 2000),
        scale: 1
      }
    });
    fs.writeFileSync(`scratch/d2_after_${width}.png`, Buffer.from(shot.data, 'base64'));

    // Zoom on bullets 2, 4, 6 and return curve
    const zoomInfo = await sendPage("Runtime.evaluate", {
      expression: `
        (() => {
          const cards = Array.from(document.querySelectorAll('.pain-card'));
          const wrapper = document.querySelector('.pain-timeline-wrapper');
          const wRect = wrapper.getBoundingClientRect();
          const b2 = cards[1].querySelector('.pain-node-bullet').getBoundingClientRect();
          const b4 = cards[3].querySelector('.pain-node-bullet').getBoundingClientRect();
          const b6 = cards[5].querySelector('.pain-node-bullet').getBoundingClientRect();
          return {
            b2: { x: b2.left - 20, y: b2.top - 20, width: 140, height: 72 },
            b4: { x: b4.left - 20, y: b4.top - 20, width: 140, height: 72 },
            b6: { x: b6.left - 20, y: b6.top - 20, width: 140, height: 72 },
            bottomLoop: { x: wRect.left - 10, y: b6.bottom - 10, width: 90, height: 90 },
            topLoop: { x: wRect.left - 10, y: cards[0].getBoundingClientRect().top - 40, width: 90, height: 80 }
          };
        })()
      `,
      returnByValue: true
    });

    const z = zoomInfo.result.value;

    for (const [key, clip] of Object.entries(z)) {
      if (clip.y >= 0) {
        const zShot = await sendPage("Page.captureScreenshot", {
          format: "png",
          clip: {
            x: Math.max(0, clip.x),
            y: Math.max(0, clip.y),
            width: clip.width,
            height: clip.height,
            scale: 2
          }
        });
        fs.writeFileSync(`scratch/d2_after_${width}_${key}.png`, Buffer.from(zShot.data, 'base64'));
      }
    }
  }

  console.log("After screenshots saved successfully.");
  await send("Browser.close");
  chrome.kill();
}

run().catch(console.error);
