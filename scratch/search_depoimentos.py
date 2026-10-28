import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

import re
m = re.findall(r'[^\n]*DEPOIMENTOS[^\n]*', orig, re.IGNORECASE)
print("Matches for DEPOIMENTOS in index.html:")
for match in m:
    print(" ", match.strip())

m2 = re.findall(r'[^\n]*PLATAFORMA[^\n]*', orig, re.IGNORECASE)
print("\nMatches for PLATAFORMA in index.html:")
for match in m2:
    print(" ", match.strip())
