const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

// Find all occurrences of FAQ or Dúvidas or Perguntas
const terms = ['dúvida', 'faq', 'perguntas', 'garantia', 'closing', 'assistindo'];
terms.forEach(term => {
  let idx = 0;
  while ((idx = content.toLowerCase().indexOf(term, idx)) !== -1) {
    console.log(`Found '${term}' at ${idx}: ${content.slice(idx, idx + 80).replace(/\r?\n/g, ' ')}`);
    idx += term.length + 10;
  }
});
