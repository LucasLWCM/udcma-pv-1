const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

const jsStart = content.lastIndexOf('<script', 159310);
const jsEnd = content.indexOf('</script>', 159310) + 9;

console.log('Script around 159310:');
console.log('Start:', jsStart, 'End:', jsEnd);
console.log(content.slice(jsStart, jsEnd));
