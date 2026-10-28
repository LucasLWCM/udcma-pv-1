import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('id="guarantee"')
if idx != -1:
    print('Surrounding HTML (before and after #guarantee):')
    print(c[idx-400:idx+900])
