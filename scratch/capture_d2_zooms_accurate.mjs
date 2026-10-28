import { spawn } from 'child_process';
import fs from 'fs';

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9342;

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
      expression: `document.getElementById('pain').scrollIntoView();`
    });
    await sleep(600);

    const clipsRes = await sendPage("Runtime.evaluate", {
      expression: `
        (() => {
          const cards = Array.from(document.querySelectorAll('.pain-card'));
          const wrapper = document.querySelector('.pain-timeline-wrapper');
          const sx = window.scrollX;
          const sy = window.scrollY;

          function getDocRect(el) {
            const r = el.getBoundingClientRect();
            return {
              x: r.left + sx,
              y: r.top + sy,
              width: r.width,
              height: r.height
            };
          }

          const b2 = getDocRect(cards[1].querySelector('.pain-node-bullet'));
          const b4 = getDocRect(cards[3].querySelector('.pain-node-bullet'));
          const b6 = getDocRect(cards[5].querySelector('.pain-node-bullet'));
          const w = getDocRect(wrapper);
          const c1 = getDocRect(cards[0]);
          const c6 = getDocRect(cards[5]);

          return {
            bullet_2: { x: b2.x - 22, y: b2.y - 20, width: 140, height: 72 },
            bullet_4: { x: b4.x - 22, y: b4.y - 20, width: 140, height: 72 },
            bullet_6: { x: b6.x - 22, y: b6.y - 20, width: 140, height: 72 },
            bottom_curve: { x: w.x - 10, y: c6.y + c6.height - 40, width: 140, height: 95 },
            top_curve: { x: w.x - 10, y: c1.y - 45, width: 140, height: 85 }
          };
        })()
      `,
      returnByValue: true
    });

    const clips = clipsRes.result.value;

    for (const [key, clip] of Object.entries(clips)) {
      const shot = await sendPage("Page.captureScreenshot", {
        format: "png",
        clip: {
          x: Math.max(0, clip.x),
          y: Math.max(0, clip.y),
          width: clip.width,
          height: clip.height,
          scale: 2
        },
        captureBeyondViewport: true
      });
      fs.writeFileSync(`scratch/zoom_${width}_${key}.png`, Buffer.from(shot.data, 'base64'));
    }
  }

  console.log("All precise zoom screenshots saved successfully.");
  await send("Browser.close");
  chrome.kill();
}

run().catch(console.error);
