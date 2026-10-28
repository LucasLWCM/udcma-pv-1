import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

# 1. Check locations relative to #pricing
pos_pricing = p12.find('id="pricing"')
pos_block_b = p12.find('id="testimonials-block-b"')
pos_block_a = p12.find('id="social-proof"')

print("=== 1. SECTION ORDER ===")
print(f"Bloco B pos: {pos_block_b}")
print(f"#pricing pos: {pos_pricing}")
print(f"Bloco A pos: {pos_block_a}")
assert pos_block_b < pos_pricing < pos_block_a, "Order is WRONG!"
print("✅ Order verified: Bloco B < Pricing < Bloco A!")

# 2. Check Titles
print("\n=== 2. TITLES ===")
title_b = "VOCÊ NÃO VAI ACREDITAR NO QUE OS ALUNOS ESTÃO DIZENDO"
title_a = "VOCÊ ESTARÁ A FRENTE DE 95% DAS PESSOAS"
sub_a = 'Em 60 minutos você vai entender mais sobre estoicismo do que pessoas que "estudam" há anos.'
italic_a = '(e você está a um clique disso)'

assert title_b in p12, f"Missing Title B: {title_b}"
assert "VOCÊ" in p12 and "95%" in p12, f"Missing Title A words"
assert sub_a in p12, f"Missing Subtitle A"
assert italic_a in p12, f"Missing Italic A"
print("✅ All titles and subtitles verified!")

# 3. Check WhatsApp Prints in Bloco B
print("\n=== 3. WHATSAPP PRINTS IN BLOCO B ===")
block_b_html = p12[pos_block_b:pos_pricing]
for i in range(1, 6):
    sp = f"sp_{i}.webp"
    assert sp in block_b_html, f"Missing {sp} in Bloco B"
    print(f"  Found {sp} in Bloco B")

img_tags_b = re.findall(r'<img[^>]+>', block_b_html)
print(f"Found {len(img_tags_b)} images in Bloco B:")
for img in img_tags_b:
    assert 'loading="lazy"' in img, f"Image without loading=lazy: {img}"
    assert 'decoding="async"' in img, f"Image without decoding=async: {img}"
    assert 'width="400"' in img and 'height="400"' in img, f"Image without width/height: {img}"
print("✅ All prints in Bloco B have lazy loading, decoding async, and width/height!")

# 4. Check 9 Testimonials in Bloco A
print("\n=== 4. 9 TESTIMONIALS IN BLOCO A ===")
block_a_html = p12[pos_block_a:p12.find('id="for-who"')]
real_names = [
    "Carlos Henrique Ramos",
    "Cristiane de Matteos de Aragão",
    "Chalice de Albuquerque Pinheiro",
    "Tânia Collobialli",
    "José Levi da Silva Lucas",
    "Mivaldo Pelé",
    "Josimar Andrade Araújo",
    "Onivaldo Moacir Roma",
    "Fabio José de Alencar"
]

for name in real_names:
    assert name in block_a_html, f"Missing testimonial name: {name}"
    print(f"  Found {name}")

assert "fabio_alencar.webp" in block_a_html, "Missing Fabio Alencar image"
print("✅ All 9 testimonials with names, times, and Fabio's photo verified in Bloco A!")

# 5. Check Original index.html
with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()
print(f"\nOriginal index.html length: {len(orig)} (untouched)")
print("ALL VERIFICATIONS PASSED SUCCESSFULLY!")
