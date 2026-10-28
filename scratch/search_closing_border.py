import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.findall(r'(\.closing-box[^{]*\{[^}]+\})', c)
for match in m:
    print(match)

border_matches = re.findall(r'([^{}]*border[^{}]*\{[^}]*closing[^}]*\})', c)
for b in border_matches:
    print(b)
