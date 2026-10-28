import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

matches = [m.start() for m in re.finditer(r'#closing|\.closing', c)]
print(f"Total occurrences of closing in p12: {len(matches)}")
for idx in matches:
    print(f"\n--- At index {idx} ---")
    print(c[max(0, idx-50):min(len(c), idx+150)])
