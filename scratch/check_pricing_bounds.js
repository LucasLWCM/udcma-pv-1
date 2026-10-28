const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

const pPos = content.indexOf('<section id="pricing">');
const pEnd = content.indexOf('</section>', pPos);
const gPos = content.indexOf('<section id="guarantee">');
console.log('Pricing start:', pPos, 'Pricing end:', pEnd);
console.log('Guarantee start:', gPos);
console.log('Is guarantee inside pricing?', gPos < pEnd);
console.log('pBtn index:', content.indexOf('id="pricingCtaBtn"'));
