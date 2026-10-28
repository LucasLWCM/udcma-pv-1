import { spawn } from 'child_process';
import fs from 'fs';

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9341;

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

    // Make sure pain is rendered and animations triggered
    await sendPage("Runtime.evaluate", {
      expression: `document.getElementById('pain').scrollIntoView();`
    });
    await sleep(600);

    const targets = [
      { key: "bullet_2", cardIdx: 1 },
      { key: "bullet_4", cardIdx: 3 },
      { key: "bullet_6", cardIdx: 5 }
    ];

    for (const t of targets) {
      await sendPage("Runtime.evaluate", {
        expression: `
          (() => {
            const card = document.querySelectorAll('.pain-card')[${t.cardIdx}];
            card.scrollIntoView({ block: 'center' });
          })()
        `
      });
      await sleep(200);

      const clipRes = await sendPage("Runtime.evaluate", {
        expression: `
          (() => {
            const card = document.querySelectorAll('.pain-card')[${t.cardIdx}];
            const b = card.querySelector('.pain-node-bullet');
            const cInner = card.querySelector('.pain-card-inner');
            const rB = b.getBoundingClientRect();
            const rC = cInner.getBoundingClientRect();
            return {
              x: Math.max(0, rB.left - 24),
              y: Math.max(0, rB.top - 20),
              width: Math.min(220, rC.left + 140 - (rB.left - 24)),
              height: 72
            };
          })()
        `,
        returnByValue: true
      });

      const clip = clipRes.result.value;
      const shot = await sendPage("Page.captureScreenshot", {
        format: "png",
        clip: {
          x: clip.x,
          y: clip.y,
          width: clip.width,
          height: clip.height,
          scale: 2
        }
      });
      fs.writeFileSync(`scratch/zoom_${width}_${t.key}.png`, Buffer.from(shot.data, 'base64'));
    }

    // Capture bottom return curve
    await sendPage("Runtime.evaluate", {
      expression: `
        (() => {
          const cards = document.querySelectorAll('.pain-card');
          cards[5].scrollIntoView({ block: 'center' });
        })()
      `
    });
    await sleep(200);
    const bottomRes = await sendPage("Runtime.evaluate", {
      expression: `
        (() => {
          const wrapper = document.querySelector('.pain-timeline-wrapper');
          const cards = document.querySelectorAll('.pain-card');
          const b6 = cards[5].querySelector('.pain-node-bullet').getBoundingClientRect();
          const wRect = wrapper.getBoundingClientRect();
          return {
            x: Math.max(0, wRect.left - 12),
            y: Math.max(0, b6.top - 10),
            width: 140,
            height: 90
          };
        })()
      `,
      returnByValue: true
    });
    const bottomClip = bottomRes.result.value;
    const bottomShot = await sendPage("Page.captureScreenshot", {
      format: "png",
      clip: {
        x: bottomClip.x,
        y: bottomClip.y,
        width: bottomClip.width,
        height: bottomClip.height,
        scale: 2
      }
    });
    fs.writeFileSync(`scratch/zoom_${width}_bottom_curve.png`, Buffer.from(bottomShot.data, 'base64'));

    // Capture top return curve
    await sendPage("Runtime.evaluate", {
      expression: `
        (() => {
          const cards = document.querySelectorAll('.pain-card');
          cards[0].scrollIntoView({ block: 'center' });
        })()
      `
    });
    await sleep(200);
    const topRes = await sendPage("Runtime.evaluate", {
      expression: `
        (() => {
          const wrapper = document.querySelector('.pain-timeline-wrapper');
          const cards = document.querySelectorAll('.pain-card');
          const b1 = cards[0].querySelector('.pain-node-bullet').getBoundingClientRect();
          const wRect = wrapper.getBoundingClientRect();
          return {
            x: Math.max(0, wRect.left - 12),
            y: Math.max(0, b1.top - 55),
            width: 140,
            height: 95
          };
        })()
      `,
      returnByValue: true
    });
    const topClip = topRes.result.value;
    const topShot = await sendPage("Page.captureScreenshot", {
      format: "png",
      clip: {
        x: topClip.x,
        y: topClip.y,
        width: topClip.width,
        height: topClip.height,
        scale: 2
      }
    });
    fs.writeFileSync(`scratch/zoom_${width}_top_curve.png`, Buffer.from(topShot.data, 'base64'));
  }

  console.log("All detailed zooms captured successfully.");
  await send("Browser.close");
  chrome.kill();
}

run().catch(console.error);
