import { spawn } from 'child_process';

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9340;

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

  // TEST 1: Initial load portrait 390x844
  await sendPage("Emulation.setDeviceMetricsOverride", {
    width: 390,
    height: 844,
    deviceScaleFactor: 2,
    mobile: true
  });
  await sendPage("Page.navigate", { url: "http://localhost:8080/p12/index.html" });
  await sleep(1000);

  // TEST 2: Screen Rotation to Landscape 844x390
  console.log('Testing Screen Rotation: 390x844 -> 844x390 (landscape)...');
  await sendPage("Emulation.setDeviceMetricsOverride", {
    width: 844,
    height: 390,
    deviceScaleFactor: 2,
    mobile: true,
    screenOrientation: { type: 'landscapePrimary', angle: 90 }
  });
  await sleep(500);

  const rotateEval = await sendPage("Runtime.evaluate", {
    expression: `
      (() => {
        const cards = Array.from(document.querySelectorAll('.pain-card'));
        return cards.map((card, i) => {
          const cardInner = card.querySelector('.pain-card-inner');
          const cardRect = cardInner.getBoundingClientRect();
          const cardCenterY = cardRect.top + cardRect.height / 2;
          const bullet = card.querySelector('.pain-node-bullet .svg-node-bg');
          const bulletRect = bullet.getBoundingClientRect();
          const bulletCenterY = bulletRect.top + bulletRect.height / 2;
          return {
            index: i,
            cardHeight: Math.round(cardRect.height * 10) / 10,
            cardCenterY: Math.round(cardCenterY * 10) / 10,
            bulletCenterY: Math.round(bulletCenterY * 10) / 10,
            diff: Math.round((cardCenterY - bulletCenterY) * 10) / 10
          };
        });
      })()
    `,
    returnByValue: true
  });
  console.log('Landscape rotation results:');
  console.table(rotateEval.result.value);

  // TEST 3: ResizeObserver dynamic card content expansion
  console.log('Testing ResizeObserver: dynamically expanding card 2 content...');
  await sendPage("Runtime.evaluate", {
    expression: `
      (() => {
        const card2Text = document.querySelectorAll('.pain-card .pain-text')[2];
        card2Text.innerText += ' [Texto adicional longo para testar se o ResizeObserver reajusta o centro da bolinha e a linha SVG perfeitamente sem desalinhar nenhum card]';
      })()
    `
  });
  await sleep(400);

  const roEval = await sendPage("Runtime.evaluate", {
    expression: `
      (() => {
        const cards = Array.from(document.querySelectorAll('.pain-card'));
        const trackPath = document.getElementById('svg-descent-track');
        return {
          trackD: trackPath.getAttribute('d'),
          cards: cards.map((card, i) => {
            const cardInner = card.querySelector('.pain-card-inner');
            const cardRect = cardInner.getBoundingClientRect();
            const cardCenterY = cardRect.top + cardRect.height / 2;
            const bullet = card.querySelector('.pain-node-bullet .svg-node-bg');
            const bulletRect = bullet.getBoundingClientRect();
            const bulletCenterY = bulletRect.top + bulletRect.height / 2;
            return {
              index: i,
              cardHeight: Math.round(cardRect.height * 10) / 10,
              cardCenterY: Math.round(cardCenterY * 10) / 10,
              bulletCenterY: Math.round(bulletCenterY * 10) / 10,
              diff: Math.round((cardCenterY - bulletCenterY) * 10) / 10
            };
          })
        };
      })()
    `,
    returnByValue: true
  });
  console.log('ResizeObserver card expansion results:');
  console.table(roEval.result.value.cards);
  console.log('Track path d updated:', roEval.result.value.trackD);

  await send("Browser.close");
  chrome.kill();
}

main().catch(console.error);
