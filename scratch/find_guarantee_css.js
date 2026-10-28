const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

let idx = 0;
while ((idx = content.indexOf('#guarantee', idx)) !== -1) {
  console.log('Match #guarantee at', idx, ':\n', content.slice(idx, idx + 250).replace(/\r?\n/g, ' '));
  idx += 10;
}
