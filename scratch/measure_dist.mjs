import { spawn } from 'child_process';

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9344;

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function main() {
  const chrome = spawn(CHROME_PATH, [
    `--remote-debugging-port=${PORT}`,
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--window-size=390,844',
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

  await sendPage("Page.navigate", { url: "http://localhost:8080/p12/index.html" });
  await sleep(1500);

  const res = await sendPage("Runtime.evaluate", {
    expression: `
      (() => {
        const links = Array.from(document.querySelectorAll('a[href*="pay.hotmart.com"]'));
        return links.map((l, i) => {
          const rect = l.getBoundingClientRect();
          const pageY = rect.top + window.scrollY;
          return {
            index: i,
            text: l.innerText.trim(),
            className: l.className,
            pageY: Math.round(pageY),
            height: Math.round(rect.height)
          };
        });
      })()
    `,
    returnByValue: true
  });

  console.log('Hotmart Links Positions:', JSON.stringify(res.result.value, null, 2));

  await send("Browser.close");
  chrome.kill();
}

main().catch(console.error);
