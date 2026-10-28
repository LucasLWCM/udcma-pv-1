import fs from 'fs';

let content = fs.readFileSync('p12/index.html', 'utf8');

const targetCRLF = '              <span class="stat-num">0,70%</span>\r\n              <span class="stat-label">de reembolso na Hotmart</span>';
const replacementCRLF = '              <span class="stat-label">Reembolso</span>\r\n              <span class="stat-num">menor que 1%</span>';

const targetLF = '              <span class="stat-num">0,70%</span>\n              <span class="stat-label">de reembolso na Hotmart</span>';
const replacementLF = '              <span class="stat-label">Reembolso</span>\n              <span class="stat-num">menor que 1%</span>';

if (content.includes(targetCRLF)) {
  content = content.replace(targetCRLF, replacementCRLF);
  fs.writeFileSync('p12/index.html', content, 'utf8');
  console.log('Successfully replaced (CRLF)');
} else if (content.includes(targetLF)) {
  content = content.replace(targetLF, replacementLF);
  fs.writeFileSync('p12/index.html', content, 'utf8');
  console.log('Successfully replaced (LF)');
} else {
  console.error('Target content not found!');
  process.exit(1);
}
