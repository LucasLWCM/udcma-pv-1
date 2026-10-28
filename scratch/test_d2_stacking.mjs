import { spawn } from 'child_process';

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9338;

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

  const results = {};

  for (const width of [360, 390, 768, 1280]) {
    await sendPage("Emulation.setDeviceMetricsOverride", {
      width,
      height: 900,
      deviceScaleFactor: 2,
      mobile: width < 1000
    });

    await sendPage("Runtime.evaluate", {
      expression: `document.getElementById('pain').scrollIntoView();`
    });
    await sleep(800);

    const evalResult = await sendPage("Runtime.evaluate", {
      expression: `
        (() => {
          const cards = Array.from(document.querySelectorAll('.pain-card'));

          return cards.map((c, i) => {
            const bullet = c.querySelector('.pain-node-bullet');
            bullet.scrollIntoView({ block: 'center' });
            
            const rect = bullet.getBoundingClientRect();
            const cx = rect.left + rect.width / 2;
            const cy = rect.top + rect.height / 2;
            const elAtPoint = document.elementFromPoint(cx, cy);

            const cInner = c.querySelector('.pain-card-inner').getBoundingClientRect();
            const conn = c.querySelector('.pain-node-connector').getBoundingClientRect();
            const cardCenterY = cInner.top + cInner.height / 2;
            const connCenterY = conn.top + conn.height / 2;

            return {
              viewport: ${width},
              bulletIdx: i + 1,
              elementTag: elAtPoint ? elAtPoint.tagName : null,
              elementClass: elAtPoint ? (elAtPoint.getAttribute('class') || '') : null,
              isBullet: elAtPoint ? !!elAtPoint.closest('.pain-node-bullet') : false,
              cardCenterY: Math.round(cardCenterY * 10) / 10,
              connCenterY: Math.round(connCenterY * 10) / 10,
              connectorDiffY: Math.round((connCenterY - cardCenterY) * 10) / 10
            };
          });
        })()
      `,
      returnByValue: true
    });

    results[width] = evalResult.result.value;
  }

  console.log(JSON.stringify(results, null, 2));

  await send("Browser.close");
  chrome.kill();
}

run().catch(console.error);
