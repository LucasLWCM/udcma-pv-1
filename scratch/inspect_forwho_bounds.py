import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

s1 = content.find('/* ── Para quem é / não é ── */')
print('s1:', s1)
if s1 != -1:
    s2 = content.find('/* ──', s1+20)
    print('s2:', s2)
    if s2 != -1:
        print(repr(content[s2:s2+60]))
