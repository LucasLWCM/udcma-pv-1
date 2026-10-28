import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

import re
matches = re.findall(r'<img\b[^>]*src=[\'"]([^\'"]*testimonials[^\'"]*)[\'"][^>]*>', orig, re.IGNORECASE)
for m in matches:
    print('Found in index.html:', m)

# Also check p12/index.html
with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

matches_p12 = re.findall(r'<img\b[^>]*src=[\'"]([^\'"]*testimonials[^\'"]*)[\'"][^>]*>', p12, re.IGNORECASE)
print('\nIn p12/index.html:')
for m in matches_p12:
    print('Found in p12:', m)
