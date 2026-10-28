import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx_root = c.find(':root')
print(c[idx_root:idx_root+800])
