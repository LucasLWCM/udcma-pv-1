const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

const aMatches = [...content.matchAll(/<a[^>]*href=["']([^"']*)["'][^>]*>([\s\S]*?)<\/a>/gi)];
console.log('Total <a> tags in p12/index.html:', aMatches.length);
aMatches.forEach((m, i) => {
  console.log(`[Link ${i+1}] href: ${m[1]} | class: ${m[0].match(/class=["']([^"']*)["']/)?.[1]} | id: ${m[0].match(/id=["']([^"']*)["']/)?.[1]} | text: ${m[2].replace(/<[^>]+>/g, '').trim().replace(/\r?\n/g, ' ')}`);
});

const btnMatches = [...content.matchAll(/<button[^>]*>([\s\S]*?)<\/button>/gi)];
console.log('\nTotal <button> tags in p12/index.html:', btnMatches.length);
btnMatches.forEach((m, i) => {
  console.log(`[Button ${i+1}] class: ${m[0].match(/class=["']([^"']*)["']/)?.[1]} | id: ${m[0].match(/id=["']([^"']*)["']/)?.[1]} | text: ${m[1].replace(/<[^>]+>/g, '').trim().replace(/\r?\n/g, ' ')}`);
});
