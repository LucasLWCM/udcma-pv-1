import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

pos_css_start = p12.find('/* ── Seção Dor / Ciclo (P12 - Dobra 2) ── */')
# Find the next major section comment in CSS
import re
for m in re.finditer(r'/\* ── [^*]+ ── \*/', p12[pos_css_start+50:]):
    print("Found next comment:", m.group(0), "at offset", m.start())
    break

# Also check for DOBRA in CSS
for m in re.finditer(r'DOBRA\s*\d+', p12[pos_css_start+50:]):
    print("Found DOBRA comment:", m.group(0), "at offset", m.start())
    break
