import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# 1. "VOCÊ ESTARÁ A FRENTE DE 95% DAS PESSOAS"
idx1 = orig.find('VOCÊ ESTARÁ A FRENTE')
print("Title 1 in index.html:")
print(orig[idx1-100:idx1+150])

# 2. "DEPOIMENTOS RETIRADOS DA PLATAFORMA DA SÉRIE"
idx2 = orig.find('DEPOIMENTOS RETIRADOS')
print("\nTitle 2 in index.html:")
print(orig[idx2-100:idx2+150])

# 3. "Essa série é para quem quer:"
idx3 = orig.find('Essa série é para quem quer:')
print("\nTitle 3 in index.html:")
print(orig[idx3-100:idx3+150])

# 4. "Essa série NÃO é para você que:"
idx4 = orig.find('Essa série NÃO é para você que:')
print("\nTitle 4 in index.html:")
print(orig[idx4-100:idx4+150])

# Now find their CSS classes and selectors in index.html
print("\n=== CSS Search in index.html ===")
for term in ['comparison', 'testimonials', 'for-who', 'qualification', 'target']:
    m = re.findall(rf'([^{{}}]*{term}[^{{}}]*\{{[^}}]+\}})', orig, re.IGNORECASE)
    print(f"Matches for {term}: {len(m)}")
    for r in m[:5]:
        print(r)
