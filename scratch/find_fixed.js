const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

const regex = /position\s*:\s*(fixed|sticky)/gi;
let m;
while ((m = regex.exec(content)) !== null) {
  console.log(`Position ${m[1]} at ${m.index}:`);
  console.log(content.slice(Math.max(0, m.index - 50), m.index + 120).replace(/\r?\n/g, ' '));
}
