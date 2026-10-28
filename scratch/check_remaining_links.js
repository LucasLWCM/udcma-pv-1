const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

const rest = content.slice(283583);
const reg = /<a[^>]*href=["']([^"']*)["'][^>]*>([\s\S]*?)<\/a>/gi;
let m;
while ((m = reg.exec(rest)) !== null) {
  console.log('Link after 283583:');
  console.log('href:', m[1], 'text:', m[2].replace(/<[^>]+>/g, '').trim().replace(/\r?\n/g, ' '));
}
