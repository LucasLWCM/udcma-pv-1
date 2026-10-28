const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

const regex = /addEventListener\s*\(\s*['"]click['"]\s*,\s*function/g;
let m;
while ((m = regex.exec(content)) !== null) {
  console.log(`Click listener at ${m.index}:`);
  console.log(content.slice(Math.max(0, m.index - 80), m.index + 150).replace(/\r?\n/g, ' '));
}
