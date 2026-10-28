const fs = require('fs');

const orig = fs.readFileSync('p12/index.backup_before_d2_fix.html', 'utf8');
const curr = fs.readFileSync('p12/index.html', 'utf8');

function extractCards(content) {
  const painStart = content.indexOf('<section id="pain">');
  const painEnd = content.indexOf('</section>', painStart);
  const painHtml = content.slice(painStart, painEnd);
  
  const matches = [...painHtml.matchAll(/<li class="pain-card"[\s\S]*?<\/li>/g)];
  return matches.map((m, i) => {
    const textMatch = m[0].match(/<span class="pain-text">([\s\S]*?)<\/span>/);
    const iconMatch = m[0].match(/<svg class="pain-icon"[\s\S]*?<\/svg>/);
    return {
      index: i,
      text: textMatch ? textMatch[1].trim() : '',
      icon: iconMatch ? iconMatch[0].trim() : ''
    };
  });
}

const origCards = extractCards(orig);
const currCards = extractCards(curr);

console.log('Total original cards:', origCards.length);
console.log('Total current cards:', currCards.length);

let identical = true;
for (let i = 0; i < origCards.length; i++) {
  const o = origCards[i];
  const c = currCards[i];
  const textMatches = o.text === c.text;
  const iconMatches = o.icon === c.icon;
  console.log(`Card ${i}: text matches? ${textMatches} | icon matches? ${iconMatches}`);
  if (!textMatches || !iconMatches) identical = false;
}

console.log('ALL CARDS AND TEXTS 100% IDENTICAL:', identical);
