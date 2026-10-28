const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

const pStart = content.indexOf('<section id="pricing">');
const gStart = content.indexOf('<section id="guarantee">');
const fStart = content.indexOf('<section id="for-who">');

console.log('--- PRICING (first 500 chars) ---');
console.log(content.slice(pStart, pStart + 500));
console.log('--- GUARANTEE (first 500 chars) ---');
console.log(content.slice(gStart, gStart + 500));
