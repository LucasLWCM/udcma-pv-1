import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

# 1. Search for CSS
c_idx = p12.find('/* ── Prova Social ── */')
print('CSS Prova Social found at:', c_idx)
if c_idx != -1:
    next_c = p12.find('/* ──', c_idx + 20)
    print('Next CSS section at:', next_c)
    print(p12[c_idx:next_c])

# 2. Search for HTML
h_idx = p12.find('<section id="social-proof">')
print('\nHTML #social-proof found at:', h_idx)
if h_idx != -1:
    next_h = p12.find('</section>', h_idx) + len('</section>')
    print('HTML bounds:', h_idx, next_h)
    print(p12[h_idx-100:next_h+100])
