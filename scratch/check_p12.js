const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

let idx = 0;
console.log('Occurrences of DOBRA 2:');
while ((idx = content.indexOf('DOBRA 2', idx)) !== -1) {
  console.log(`Pos ${idx}: ${content.slice(Math.max(0, idx - 20), idx + 80).replace(/\r?\n/g, ' ')}`);
  idx += 7;
}

const painIdx = content.indexOf('id="pain"');
console.log('id="pain" at:', painIdx);
const errorsIdx = content.indexOf('id="errors"');
console.log('id="errors" at:', errorsIdx);
