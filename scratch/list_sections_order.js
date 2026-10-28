const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

const matches = [...content.matchAll(/<section[^>]*id=["']([^"']*)["'][^>]*>/gi)];
console.log('Sections in p12/index.html:');
matches.forEach((m, i) => {
  console.log(`${i+1}. id="${m[1]}" (index: ${m.index})`);
});
