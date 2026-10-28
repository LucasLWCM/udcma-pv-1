import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

s_idx = orig.find('Viver o Estoicismo')
print("repr from index.html:")
print(repr(orig[s_idx-30:s_idx+120]))

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

s_p12 = p12.find('Viver o Estoicismo')
print("repr from p12/index.html:")
print(repr(p12[s_p12-30:s_p12+120]))
