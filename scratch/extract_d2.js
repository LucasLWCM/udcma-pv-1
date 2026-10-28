const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

const cssStart = content.lastIndexOf('/* ═══', 17619);
// Find next major section comment after 26000
const cssNext = content.indexOf('/* ═══', 27000);

console.log('CSS Dobra 2:');
console.log('Start:', cssStart, 'End:', cssNext);
fs.writeFileSync('scratch/dobra2_current_css.css', content.slice(cssStart, cssNext));
console.log('Wrote dobra2_current_css.css, size:', content.slice(cssStart, cssNext).length);

// Also let's inspect Dobra 2 HTML
const htmlStart = content.indexOf('<section id="pain">');
const htmlEnd = content.indexOf('</section>', htmlStart) + 10;
fs.writeFileSync('scratch/dobra2_current_html.html', content.slice(htmlStart, htmlEnd));
console.log('Wrote dobra2_current_html.html, size:', htmlEnd - htmlStart);
