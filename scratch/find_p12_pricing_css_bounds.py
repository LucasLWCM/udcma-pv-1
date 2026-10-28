import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

idx = p12.find('/* ── Seção Preço ── */')
# find next comment /* ── ... ── */
next_comm = p12.find('/* ──', idx + 25)
print('Old pricing CSS starts at:', idx)
print('Next section comment starts at:', next_comm)
print(p12[idx:next_comm])
