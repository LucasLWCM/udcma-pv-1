import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('mckp6')
print('mckp6 found at:', idx)
if idx != -1:
    print('Snippet:')
    print(content[idx-100:idx+200])

# Also check if img/ref/mckp6.webp exists locally
import os
for p in ['img/ref/mckp6.webp', '../img/ref/mckp6.webp']:
    print(f'Path {p} exists? {os.path.exists(p)}')
