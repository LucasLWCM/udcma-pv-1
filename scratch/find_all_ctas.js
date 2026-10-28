const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

// Find all <a> tags that lead to checkout or have class btn-cta / cta
const regex = /<a[^>]*href=["']([^"']*)["'][^>]*>([\s\S]*?)<\/a>/gi;
let match;
let count = 0;
while ((match = regex.exec(content)) !== null) {
  const href = match[1];
  const innerText = match[2].replace(/<[^>]+>/g, '').trim();
  const fullTag = match[0];
  if (href.includes('hotmart') || href.includes('checkout') || fullTag.includes('btn-cta') || fullTag.includes('cta')) {
    count++;
    console.log(`\n[CTA Link ${count}] (index: ${match.index})`);
    console.log(`Href: ${href}`);
    console.log(`Text: "${innerText}"`);
    console.log(`Full tag preview: ${fullTag.slice(0, 150).replace(/\r?\n/g, ' ')}...`);
  }
}
