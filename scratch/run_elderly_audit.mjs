import { spawn } from 'child_process';
import fs from 'fs';

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9333;

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function main() {
  console.log("Launching headless Chrome on port", PORT);
  const chrome = spawn(CHROME_PATH, [
    `--remote-debugging-port=${PORT}`,
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--window-size=375,812',
    '--hide-scrollbars',
    'about:blank'
  ]);

  chrome.stderr.on('data', d => {});
  chrome.stdout.on('data', d => {});

  let wsUrl = null;
  for (let i = 0; i < 30; i++) {
    await sleep(300);
    try {
      const res = await fetch(`http://127.0.0.1:${PORT}/json/version`);
      if (res.ok) {
        const data = await res.json();
        wsUrl = data.webSocketDebuggerUrl;
        break;
      }
    } catch (e) {}
  }

  if (!wsUrl) {
    console.error("Could not connect to Chrome CDP");
    chrome.kill();
    process.exit(1);
  }

  console.log("Connected to Chrome via CDP:", wsUrl);
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

  // Create new target (page)
  const target = await send("Target.createTarget", { url: "http://localhost:8080/p12/index.html" });
  const pageTargetId = target.targetId;

  // Connect to page target
  const pageWs = new WebSocket(`ws://127.0.0.1:${PORT}/devtools/page/${pageTargetId}`);
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

  // Set device metrics to mobile 375x812
  await sendPage("Emulation.setDeviceMetricsOverride", {
    width: 375,
    height: 812,
    deviceScaleFactor: 2,
    mobile: true
  });

  await sendPage("Page.enable");
  await sendPage("Runtime.enable");

  // Wait for page to fully load
  console.log("Waiting for page load...");
  await sleep(2500);

  // Evaluate script to collect all distinct text types and calculate contrast
  const auditCode = `
  (() => {
    // Luminance calculation according to WCAG 2.1
    function getLuminance(r, g, b) {
      const [rs, gs, bs] = [r, g, b].map(c => {
        c = c / 255;
        return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
      });
      return 0.2126 * rs + 0.7152 * gs + 0.0722 * bs;
    }

    function getContrast(rgb1, rgb2) {
      const l1 = getLuminance(rgb1.r, rgb1.g, rgb1.b);
      const l2 = getLuminance(rgb2.r, rgb2.g, rgb2.b);
      const brightest = Math.max(l1, l2);
      const darkest = Math.min(l1, l2);
      return (brightest + 0.05) / (darkest + 0.05);
    }

    function parseRgb(colorStr) {
      if (!colorStr) return { r: 0, g: 0, b: 0, a: 1 };
      const m = colorStr.match(/rgba?\\((\\d+),\\s*(\\d+),\\s*(\\d+)(?:,\\s*([\\d.]+))?\\)/);
      if (m) {
        return {
          r: parseInt(m[1]),
          g: parseInt(m[2]),
          b: parseInt(m[3]),
          a: m[4] !== undefined ? parseFloat(m[4]) : 1
        };
      }
      return { r: 0, g: 0, b: 0, a: 1 };
    }

    function blend(fg, bg) {
      return {
        r: Math.round(fg.r * fg.a + bg.r * (1 - fg.a)),
        g: Math.round(fg.g * fg.a + bg.g * (1 - fg.a)),
        b: Math.round(fg.b * fg.a + bg.b * (1 - fg.a)),
        a: 1
      };
    }

    function getEffectiveBg(el) {
      let cur = el;
      let bgStack = [];
      while (cur && cur !== document.documentElement) {
        const st = window.getComputedStyle(cur);
        const bg = parseRgb(st.backgroundColor);
        if (bg.a > 0) {
          bgStack.push(bg);
          if (bg.a >= 0.98) break;
        }
        cur = cur.parentElement;
      }
      // default page background is black / very dark in P12
      let finalBg = { r: 10, g: 10, b: 10, a: 1 };
      for (let i = bgStack.length - 1; i >= 0; i--) {
        finalBg = blend(bgStack[i], finalBg);
      }
      return finalBg;
    }

    // Traverse elements and collect structured entries
    const results = [];
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_ELEMENT, null);
    
    // Check viewport meta
    const viewportMeta = document.querySelector('meta[name="viewport"]')?.getAttribute('content') || '';
    const blocksZoom = /user-scalable\\s*=\\s*no|maximum-scale\\s*=\\s*1(\\b|\\.0)/i.test(viewportMeta);

    const seenTexts = new Set();

    while (walker.nextNode()) {
      const el = walker.currentNode;
      if (['SCRIPT', 'STYLE', 'SVG', 'PATH', 'NOSCRIPT', 'IFRAME', 'BR', 'HR'].includes(el.tagName)) continue;

      // Check if it directly contains meaningful text
      const directText = Array.from(el.childNodes)
        .filter(n => n.nodeType === Node.TEXT_NODE)
        .map(n => n.textContent.trim())
        .join(' ');
      
      const fullText = el.textContent.trim();
      if (!fullText) continue;

      // Only evaluate leaf or text-bearing elements
      const hasChildElementsWithText = Array.from(el.children).some(c => c.textContent.trim().length > 0 && !['EM', 'STRONG', 'B', 'I', 'SPAN', 'MARK'].includes(c.tagName));
      if (hasChildElementsWithText) continue;

      const st = window.getComputedStyle(el);
      if (st.display === 'none' || st.visibility === 'hidden' || st.opacity === '0') continue;

      // Deduplicate identical role and text
      const snippet = fullText.slice(0, 70).replace(/\\s+/g, ' ');
      const key = el.tagName + '|' + (el.className || '') + '|' + snippet;
      if (seenTexts.has(key)) continue;
      seenTexts.add(key);

      const fg = parseRgb(st.color);
      const bg = getEffectiveBg(el);
      const ratio = getContrast(fg, bg);

      const fontSizePx = parseFloat(st.fontSize);
      const fontWeight = st.fontWeight;
      const fontFamily = st.fontFamily.split(',')[0].replace(/['"]/g, '').trim();

      // Classify element
      let type = 'Leitura';
      const tag = el.tagName.toLowerCase();
      const parentTag = el.parentElement ? el.parentElement.tagName.toLowerCase() : '';
      const cls = (el.className + ' ' + (el.parentElement?.className || '')).toLowerCase();

      if (['h1', 'h2'].includes(tag) || cls.includes('headline') || cls.includes('title')) {
        type = 'Título';
      } else if (['h3', 'h4', 'h5', 'h6'].includes(tag) || cls.includes('subhead') || cls.includes('subtitle')) {
        type = 'Subtítulo / Apoio';
      } else if (tag === 'button' || tag === 'a' && cls.includes('btn')) {
        type = 'Botão';
      } else if (tag === 'a' || cls.includes('link') || cls.includes('sub')) {
        type = 'Link / Micro-copy';
      } else if (tag === 'em' || tag === 'i' || st.fontStyle === 'italic') {
        type = 'Itálico';
      } else if (fontSizePx <= 15 || snippet.startsWith('(') || cls.includes('badge') || cls.includes('micro') || cls.includes('small')) {
        type = 'Texto Pequeno';
      }

      // Identify section
      let section = el.closest('section')?.id || el.closest('header')?.id || el.closest('footer')?.id || '';
      if (!section) {
        let cur = el;
        while (cur && cur !== document.body) {
          if (cur.id) { section = cur.id; break; }
          cur = cur.parentElement;
        }
      }

      // Criteria flags
      const isReading = (type === 'Leitura' || type === 'Itálico');
      const flaggedSize = isReading && fontSizePx < 18;
      const flaggedContrast = ratio < 4.5;

      results.push({
        section: section || 'geral',
        tag: el.tagName.toLowerCase(),
        classes: el.className ? '.' + el.className.trim().split(/\\s+/).slice(0, 2).join('.') : '',
        snippet,
        type,
        fontFamily,
        fontWeight,
        fontSizePx: Math.round(fontSizePx * 10) / 10,
        fgColor: st.color,
        bgColor: 'rgb(' + bg.r + ',' + bg.g + ',' + bg.b + ')',
        ratio: Math.round(ratio * 100) / 100,
        flaggedSize,
        flaggedContrast
      });
    }

    return {
      viewportMeta,
      blocksZoom,
      elementsCount: results.length,
      results
    };
  })()
  `;

  const evalResult = await sendPage("Runtime.evaluate", {
    expression: auditCode,
    returnByValue: true,
    awaitPromise: true
  });

  console.log("Audit complete. Writing results to scratch/elderly_audit.json...");
  fs.writeFileSync('scratch/elderly_audit.json', JSON.stringify(evalResult.result.value, null, 2), 'utf-8');

  // Close chrome
  await send("Browser.close");
  chrome.kill();
  console.log("Done!");
}

main().catch(err => {
  console.error("Error running audit:", err);
  process.exit(1);
});
