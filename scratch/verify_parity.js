const fs = require('fs');

const b = fs.readFileSync('p12/index.backup_before_floating.html', 'utf8');
const c = fs.readFileSync('p12/index.html', 'utf8');

// Check timers
console.log('Timer in before:', b.includes('countdown-timer'));
console.log('Timer in after:', c.includes('countdown-timer'));

// Check strike original price
console.log('Strike price in before:', b.includes('strikeOriginalPrice'));
console.log('Strike price in after:', c.includes('strikeOriginalPrice'));

// Check mainPriceDisplay
console.log('Main price in before:', b.includes('mainPriceDisplay'));
console.log('Main price in after:', c.includes('mainPriceDisplay'));

// Check hotmart link URLs
const bLinks = [...b.matchAll(/href=["'](https:\/\/pay\.hotmart\.com[^"']*)["']/g)].map(m => m[1]);
const cLinks = [...c.matchAll(/href=["'](https:\/\/pay\.hotmart\.com[^"']*)["']/g)].map(m => m[1]);
console.log('Hotmart links count before:', bLinks.length);
console.log('Hotmart links count after (includes floating):', cLinks.length);
console.log('Are all original links identical?');
let allSame = true;
for (let i = 0; i < bLinks.length; i++) {
  if (bLinks[i] !== cLinks[i]) allSame = false;
}
console.log('All original links identical:', allSame);
console.log('New floating link URL identical:', cLinks[cLinks.length - 1] === bLinks[0]);
