const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

const pBtnPos = content.indexOf('id="pricingCtaBtn"');
console.log('pricingCtaBtn at:', pBtnPos);
const gSecPos = content.indexOf('id="guarantee"');
console.log('guarantee at:', gSecPos);

console.log('Is pricingCtaBtn before guarantee in HTML?', pBtnPos < gSecPos);
console.log('Difference in chars:', gSecPos - pBtnPos);
