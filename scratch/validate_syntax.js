const fs = require('fs');
const vm = require('vm');

const html = fs.readFileSync('p12/index.html', 'utf8');

const scriptRegex = /<script\b[^>]*>([\s\S]*?)<\/script>/gi;
let match;
let index = 1;
let errors = 0;

while ((match = scriptRegex.exec(html)) !== null) {
  const code = match[1];
  if (!code.trim()) continue;
  try {
    new vm.Script(code);
    console.log(`Script #${index}: Syntax OK (${code.length} chars)`);
  } catch (err) {
    console.error(`Script #${index}: Syntax ERROR!`, err.message);
    errors++;
  }
  index++;
}

if (errors === 0) {
  console.log('\nAll inline scripts are valid JS!');
} else {
  console.error(`\nFound ${errors} syntax errors!`);
  process.exit(1);
}
