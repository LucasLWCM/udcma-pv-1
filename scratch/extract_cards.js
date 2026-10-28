const fs = require('fs');
const html = fs.readFileSync('scratch/dobra2_current_html.html', 'utf8');
const cardRegex = /<li class="pain-card"[\s\S]*?<\/li>/g;
let match;
let i = 0;
while ((match = cardRegex.exec(html)) !== null) {
  console.log(`CARD ${i}:`);
  const textMatch = match[0].match(/<span class="pain-text">([\s\S]*?)<\/span>/);
  if (textMatch) {
    console.log('Text:', textMatch[1].replace(/\r?\n/g, ' ').trim());
  }
  i++;
}
