import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

matches = [m.start() for m in re.finditer(r'depoimentos\s+retirados', p12, re.IGNORECASE)]
for m in matches:
    print('Match at', m, ':')
    print(p12[m-100:m+300])
    print('='*50)
