import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

s1 = content.find('/* ── Seção Preço ── */')
print('s1:', s1)

# Find what comes after
if s1 != -1:
    print('Snippet from s1:')
    print(content[s1:s1+200])
    s2 = content.find('/* ──', s1+20)
    print('Next /* ── at:', s2)
    if s2 != -1:
        print('Snippet from s2:')
        print(content[s2:s2+100])
