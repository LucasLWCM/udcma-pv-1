const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

let idx = 0;
while ((idx = content.indexOf('sales-toast', idx)) !== -1) {
  console.log(`sales-toast at ${idx}:`, content.slice(Math.max(0, idx - 40), idx + 80).replace(/\r?\n/g, ' '));
  idx += 12;
}
