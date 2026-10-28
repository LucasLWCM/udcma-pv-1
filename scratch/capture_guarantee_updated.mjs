import { spawn } from 'child_process';
import fs from 'fs';

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9348;

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

  for (const width of [390, 768]) {
    await sendPage("Emulation.setDeviceMetricsOverride", {
      width,
      height: 900,
      deviceScaleFactor: 2,
      mobile: width < 1000
    });

    await sendPage("Runtime.evaluate", {
      expression: `
        (() => {
          const sec = document.getElementById('guarantee');
          sec.scrollIntoView({ block: 'center' });
        })()
      `
    });
    await sleep(600);

    const rRes = await sendPage("Runtime.evaluate", {
      expression: `
        (() => {
          const card = document.querySelector('.guarantee-card');
          const r = card.getBoundingClientRect();
          return {
            x: Math.max(0, r.left + window.scrollX - 10),
            y: Math.max(0, r.top + window.scrollY - 10),
            width: r.width + 20,
            height: r.height + 20
          };
        })()
      `,
      returnByValue: true
    });
    const clip = rRes.result.value;

    const shot = await sendPage("Page.captureScreenshot", {
      format: "png",
      clip: { x: clip.x, y: clip.y, width: clip.width, height: clip.height, scale: 2 },
      captureBeyondViewport: true
    });
    fs.writeFileSync(`scratch/guarantee_updated_${width}.png`, Buffer.from(shot.data, 'base64'));
  }

  console.log("Guarantee screenshots saved.");
  await send("Browser.close");
  chrome.kill();
}

run().catch(console.error);
