import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. "VOCÊ ESTARÁ A FRENTE DE 95% DAS PESSOAS"
t1_idx = c.find('VOCÊ ESTARÁ A FRENTE')
print(f"Title 1 in p12 at {t1_idx}:")
print(c[t1_idx-100:t1_idx+150])

# 2. "DEPOIMENTOS RETIRADOS DA PLATAFORMA DA SÉRIE"
t2_idx = c.find('DEPOIMENTOS RETIRADOS')
print(f"\nTitle 2 in p12 at {t2_idx}:")
print(c[t2_idx-100:t2_idx+150])

# 3 & 4: "Essa série é para quem quer:" and "Essa série NÃO é para você que:"
t3_idx = c.find('Essa série é para quem quer:')
print(f"\nTitle 3 in p12 at {t3_idx}:")
print(c[t3_idx-100:t3_idx+150])

t4_idx = c.find('Essa série NÃO é para você que:')
print(f"\nTitle 4 in p12 at {t4_idx}:")
print(c[t4_idx-100:t4_idx+150])

# Let's see the CSS rules for these in p12
print("\n=== CSS in p12 for these titles ===")
for cls in ['social-headline', 'comparison-headline', 'testimonials-section-title', 'for-who-card-title', 'section-title']:
    m = re.findall(rf'([^{{}}]*{cls}[^{{}}]*\{{[^}}]+\}})', c)
    for rule in m:
        print(rule.strip())
        print("-" * 30)
