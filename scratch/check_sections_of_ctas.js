const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

const reg = /<a[^>]*href=["'][^"']*hotmart[^"']*["'][^>]*>([\s\S]*?)<\/a>/gi;
let m;
let i = 0;
while ((m = reg.exec(content)) !== null) {
  const sectionStart = content.lastIndexOf('<section', m.index);
  const sectionMatch = content.slice(sectionStart, sectionStart + 80).match(/id=["']([^"']*)["']/);
  const sectionId = sectionMatch ? sectionMatch[1] : 'unknown';
  const text = m[1].replace(/<[^>]+>/g, '').trim().replace(/\r?\n/g, ' ');
  console.log(`Link ${i}: section="${sectionId}", text="${text}"`);
  i++;
}
