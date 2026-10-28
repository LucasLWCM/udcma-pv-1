const fs = require('fs');

const p12 = fs.readFileSync('p12/index.html', 'utf8');

// Backup p12/index.html
fs.writeFileSync('p12/index.backup_before_d2_fix.html', p12);
console.log('Created backup p12/index.backup_before_d2_fix.html');

// 1. Locate CSS
const cssStart = p12.indexOf('/* ── Seção Dor / Ciclo (P12 - Dobra 2) ── */');
const cssEnd = p12.indexOf('/* ── Seção Erros (P12 - Dobra 3) ── */');
if (cssStart === -1 || cssEnd === -1) {
  throw new Error('CSS markers not found');
}

// 2. Locate HTML
const htmlStart = p12.indexOf('<section id="pain">');
const htmlEnd = p12.indexOf('</section>', htmlStart) + 10;
if (htmlStart === -1 || htmlEnd === -1) {
  throw new Error('HTML markers not found');
}

// 3. Locate JS
const jsStart = p12.indexOf('<!-- Script da Dobra 2:', htmlEnd);
const jsEnd = p12.indexOf('</script>', jsStart) + 9;
if (jsStart === -1 || jsEnd === -1) {
  throw new Error('JS markers not found');
}

console.log('All markers verified successfully:');
console.log('CSS:', cssStart, 'to', cssEnd);
console.log('HTML:', htmlStart, 'to', htmlEnd);
console.log('JS:', jsStart, 'to', jsEnd);
