const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

const faqPos = content.indexOf('<section id="faq">');
console.log(content.slice(faqPos, faqPos + 1500));
