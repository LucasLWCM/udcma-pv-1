const fs = require('fs');

const p12 = fs.readFileSync('p12/index.html', 'utf8');

// Find Dobra 2 boundaries
const cssStart = p12.indexOf('/* ── Seção Dor / Ciclo (P12 - Dobra 2) ── */');
const cssEnd = p12.indexOf('/* ── Seção Erros (P12 - Dobra 3) ── */');

const htmlStart = p12.indexOf('<section id="pain">');
const htmlEnd = p12.indexOf('</section>', htmlStart) + 10;

const jsStart = p12.lastIndexOf('<script', p12.indexOf('svg-descent-track', htmlEnd));
const jsEnd = p12.indexOf('</script>', jsStart) + 9;

console.log('CSS:', cssStart, cssEnd, cssEnd - cssStart);
console.log('HTML:', htmlStart, htmlEnd, htmlEnd - htmlStart);
console.log('JS:', jsStart, jsEnd, jsEnd - jsStart);
