import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

idx = p12.find('/* ── Copy final ── */')
if idx != -1:
    print("--- CSS for closing in p12 ---")
    print(p12[idx:idx+1500])

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

idx_orig = orig.find('/* ── Copy final ── */')
if idx_orig != -1:
    print("--- CSS for closing in index.html ---")
    print(orig[idx_orig:idx_orig+1500])
