import { spawn } from 'child_process';

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9335;

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

  for (const width of [360, 390, 768]) {
    await sendPage("Emulation.setDeviceMetricsOverride", {
      width,
      height: 800,
      deviceScaleFactor: 2,
      mobile: width < 1000
    });
    // Scroll down to pain section to trigger observer
    await sendPage("Runtime.evaluate", {
      expression: `
        document.getElementById('pain').scrollIntoView();
      `
    });
    await sleep(800);

    const evalResult = await sendPage("Runtime.evaluate", {
      expression: `
        (() => {
          const wrapper = document.querySelector('.pain-timeline-wrapper');
          const wrapperRect = wrapper.getBoundingClientRect();
          const cards = Array.from(document.querySelectorAll('.pain-card'));
          const nodes = Array.from(document.querySelectorAll('.svg-node-wrap'));
          const svg = document.querySelector('.pain-cycle-svg');
          const svgRect = svg ? svg.getBoundingClientRect() : null;

          return cards.map((card, i) => {
            const cardInner = card.querySelector('.pain-card-inner');
            const cardRect = cardInner.getBoundingClientRect();
            const cardCenterY = cardRect.top + cardRect.height / 2;
            
            // node circle center
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
              diff: nodeCenterY !== null ? Math.round((cardCenterY - nodeCenterY) * 10) / 10 : null,
              cardTransform: window.getComputedStyle(card).transform
            };
          });
        })()
      `,
      returnByValue: true
    });

    console.log(`=== Viewport ${width}px ===`);
    console.table(evalResult.result.value);
  }

  await send("Browser.close");
  chrome.kill();
}

main().catch(console.error);
