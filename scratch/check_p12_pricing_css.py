import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

idx = p12.find('/* ── Seção Preço ── */')
if idx != -1:
    print('Found /* ── Seção Preço ── */ in p12 at:', idx)
    print(p12[idx:idx+2500])
else:
    print('Not found as /* ── Seção Preço ── */, searching #pricing in style')
    import re
    m = re.search(r'#pricing\s*\{', p12)
    if m:
        print('Found #pricing at:', m.start())
        print(p12[m.start()-50:m.start()+1000])
