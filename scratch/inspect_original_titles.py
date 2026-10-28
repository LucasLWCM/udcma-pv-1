import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Let's search for the titles in index.html and their classes/CSS
titles = [
    'VOCÊ ESTARÁ A FRENTE DE 95%',
    'DEPOIMENTOS RETIRADOS DA PLATAFORMA DA SÉRIE',
    'Essa série é para quem quer:',
    'Essa série NÃO é para você que:'
]

for t in titles:
    idx = orig.find(t)
    if idx != -1:
        print(f"\n=================== Title: '{t}' ===================")
        print("HTML snippet:")
        print(orig[max(0, idx-100):min(len(orig), idx+200)])
    else:
        print(f"Title '{t}' not found directly, searching case-insensitive...")
        m = re.search(re.escape(t), orig, re.IGNORECASE)
        if m:
            print(f"Found case-insensitive at {m.start()}:")
            print(orig[max(0, m.start()-100):min(len(orig), m.start()+200)])

# Inspect heading font family across index.html
print("\n=================== Headings in index.html CSS ===================")
m_h2 = re.findall(r'([^{}]*h2[^{}]*\{[^}]+\})', orig)
for h in m_h2[:10]:
    print(h)
