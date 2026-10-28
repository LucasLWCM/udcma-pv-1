const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

// Find start of Dobra 2 CSS
const cssCommentStart = content.lastIndexOf('/*', 17619);
console.log('CSS block start around:', cssCommentStart);
console.log(content.slice(cssCommentStart - 50, cssCommentStart + 200));

// Find end of Dobra 2 CSS
// Look for next major section comment after 26382
const cssNextSection = content.indexOf('/* ═══', 26000);
console.log('CSS next section around:', cssNextSection);
if (cssNextSection !== -1) {
  console.log(content.slice(cssNextSection, cssNextSection + 150));
}

// Find HTML section
const htmlSectionStart = content.lastIndexOf('<section', 153008);
const htmlSectionEnd = content.indexOf('</section>', 153008) + 10;
console.log('HTML section from', htmlSectionStart, 'to', htmlSectionEnd);
console.log('HTML snippet:\n', content.slice(htmlSectionStart, htmlSectionStart + 300));
console.log('HTML end snippet:\n', content.slice(htmlSectionEnd - 300, htmlSectionEnd));

// Check if there's a script inside or after
const scriptInside = content.slice(htmlSectionStart, htmlSectionEnd).indexOf('<script');
console.log('Script inside section?', scriptInside);
if (scriptInside !== -1) {
  console.log('Script starts at:', htmlSectionStart + scriptInside);
}
