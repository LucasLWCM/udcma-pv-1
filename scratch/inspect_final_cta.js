const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

const pos = content.indexOf('Quero acesso imediato e vitalício');
console.log('Final CTA at:', pos);
console.log('Surrounding code (600 chars):\n', content.slice(pos - 300, pos + 300));
