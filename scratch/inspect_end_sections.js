const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

const closingPos = content.indexOf('<section id="closing">');
console.log('From closingPos to end of HTML:');
const bodyEnd = content.indexOf('</body>');
const snippet = content.slice(closingPos, bodyEnd);

// Let's print sections in this range
const sectionMatches = [...snippet.matchAll(/<section[^>]*id=["']([^"']*)["'][^>]*>/gi)];
sectionMatches.forEach(m => console.log('Section id:', m[1]));

// Let's print all <a> in this range
const aMatches = [...snippet.matchAll(/<a[^>]*href=["']([^"']*)["'][^>]*>([\s\S]*?)<\/a>/gi)];
aMatches.forEach(m => console.log('Link:', m[1], 'Text:', m[2].replace(/<[^>]+>/g, '').trim().replace(/\r?\n/g, ' ')));
