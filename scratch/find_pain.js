const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

// Search for pain in CSS
let idx = 0;
console.log('Occurrences of ".pain-" or "#pain":');
while ((idx = content.indexOf('.pain-', idx)) !== -1) {
  console.log(`Pos ${idx}: ${content.slice(Math.max(0, idx - 40), idx + 80).replace(/\r?\n/g, ' ')}`);
  idx += 1000; // jump
}

const scriptIdx = content.indexOf('initPainTimeline');
console.log('initPainTimeline at:', scriptIdx);
if (scriptIdx !== -1) {
  console.log('Script context:', content.slice(scriptIdx - 100, scriptIdx + 200).replace(/\r?\n/g, ' '));
}
