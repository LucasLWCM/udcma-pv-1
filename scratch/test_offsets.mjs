import { spawn } from 'child_process';

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9336;

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function main() {
  const chrome = spawn(CHROME_PATH, [
    `--remote-debugging-port=${PORT}`,
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--window-size=360,800',
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

  function send(method, params = {}) {
    return new Promise((resolve, reject) => {
      const id = idCounter++;
      pending.set(id, { resolve, reject });
      ws.send(JSON.stringify({ id, method, params }));
    });
  }

  await new Promise(r => ws.onopen = r);
  await send('Page.enable');
  await send('Runtime.enable');

  await send('Emulation.setDeviceMetricsOverride', {
    width: 360,
    height: 800,
    deviceScaleFactor: 2,
    mobile: true
  });

  await send('Page.navigate', { url: 'http://localhost:8080/p12/index.html' });
  await sleep(1000);

  const evalRes = await send('Runtime.evaluate', {
    expression: `
      (function() {
        const wrapper = document.querySelector('.pain-timeline-wrapper');
        const cards = Array.from(document.querySelectorAll('.pain-card'));
        return cards.map((c, i) => {
          const rect = c.getBoundingClientRect();
          const wrapRect = wrapper.getBoundingClientRect();
          return {
            index: i,
            offsetTop: c.offsetTop,
            offsetParentClass: c.offsetParent ? c.offsetParent.className : null,
            offsetHeight: c.offsetHeight,
            computedCenterY: c.offsetTop + c.offsetHeight / 2,
            rectCenterY: (rect.top - wrapRect.top) + rect.height / 2,
            diff: ((rect.top - wrapRect.top) + rect.height / 2) - (c.offsetTop + c.offsetHeight / 2)
          };
        });
      })()
    `,
    returnByValue: true
  });

  console.log(JSON.stringify(evalRes.result.value, null, 2));

  ws.close();
  chrome.kill();
}

main().catch(console.error);
