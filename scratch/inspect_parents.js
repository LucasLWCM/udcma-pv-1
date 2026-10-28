const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

const pos = content.indexOf('pricingCtaBtn');
console.log('Parent snippet (1000 chars before):\n', content.slice(pos - 1000, pos));
