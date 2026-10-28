import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

dividers = re.findall(r'(\.section-divider[^{]*\{[^}]+\})', c)
print("Section divider styles:")
for d in dividers:
    print(d)

lines = re.findall(r'(@keyframes\s+[^\{]+line[^\}]+\})', c, re.IGNORECASE)
print("\nLine keyframes:")
for l in lines:
    print(l)
