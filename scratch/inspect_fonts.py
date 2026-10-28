import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

fonts = re.findall(r'font-family:\s*([^;]+);', c)
from collections import Counter
print("Common font-families in p12:")
for f, count in Counter(fonts).most_common(10):
    print(f"  {f.strip()}: {count}")

h_styles = re.findall(r'(h2[^{]*\{[^}]+\})', c)
print("\nSample h2 styles:")
for h in h_styles[:5]:
    print(h)
