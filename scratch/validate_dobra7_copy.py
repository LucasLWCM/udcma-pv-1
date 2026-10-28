import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

start = p12.find('<section id="pricing">')
end = p12.find('</section>', start) + len('</section>')
pricing_block = p12[start:end]

checks = [
    ('Title', 'VEJA TUDO QUE VOCÊ VAI RECEBER:'),
    ('Item 1 text', '3 episódios cinematográficos'),
    ('Item 1 note', '(sem aula chata em slide)'),
    ('Item 1 price', 'R$ 97,00'),
    ('Item 2 text', 'Acesso VITALÍCIO ao conteúdo'),
    ('Item 2 note', '(só para quem comprar esse mês)'),
    ('Item 2 price', 'R$ INESTIMÁVEL'),
    ('Bonus 1', 'Bônus 1 —'),
    ('Bonus 1 title', 'O Roteiro Estoico'),
    ('Bonus 1 price', 'R$ 47,00'),
    ('Bonus 2', 'Bônus 2 —'),
    ('Bonus 2 title', 'O Estoico em Campo'),
    ('Bonus 2 price', 'R$ 67,00'),
    ('Bonus 3', 'Bônus 3 —'),
    ('Bonus 3 title', 'Sementes Matinais (12 meses)'),
    ('Bonus 3 price', 'R$ 19,00'),
    ('Bonus 4', 'Bônus 4 —'),
    ('Bonus 4 title', 'Noites de Pórtico'),
    ('Bonus 4 price', 'R$ 67,00'),
    ('Total value label', 'Valor total:'),
    ('Total value old', 'R$ 297,00'),
    ('Timer text', 'Após o cronômetro zerar, o valor vai para R$ 97,00'),
    ('Callout', 'Hoje você garante tudo isso por apenas:'),
    ('Original price line part 1', 'de '),
    ('Original price line part 2', 'R$ 297,00'),
    ('Original price line part 3', ' por:'),
    ('Price', 'R$29,90'),
    ('CTA button', 'Quero dominar o estoicismo'),
    ('CTA button link', 'https://pay.hotmart.com/X108154869T?off=953h3rmf'),
    ('Guarantee line', 'Acesso VITALÍCIO · 7 dias de garantia'),
    ('Guarantee link', 'https://pay.hotmart.com/X108154869T?off=953h3rmf'),
    ('Mockup image src', '../img/ref/mckp6.webp'),
    ('Mockup alt', 'Série Um Dia Com Marco Aurélio Mockup'),
    ('Seal image src', '../img/ref/tqbbyxdw.png'),
    ('Seal alt', 'Compra Segura Hotmart'),
]

all_passed = True
print("--- VERIFYING DOBRA 7 COPY ---")
for label, text in checks:
    if text in pricing_block:
        print(f"[OK] {label}: found exact match '{text}'")
    else:
        print(f"[FAIL] {label}: '{text}' NOT found in pricing block!")
        all_passed = False

# Verify 297,90 is NOT present
if '297,90' in pricing_block:
    print("[FAIL] 297,90 is still present in Dobra 7!")
    all_passed = False
else:
    print("[OK] 297,90 is completely absent (corrected to 297,00 as approved)")

# Verify no extra text
prohibited = ['economize', 'desconto de', 'off', 'compre agora', 'vagas limitadas']
for p in prohibited:
    if p in pricing_block.lower():
        print(f"[FAIL] Prohibited text found: '{p}'")
        all_passed = False

if all_passed:
    print("\nALL COPY AND ATTRIBUTE CHECKS PASSED 100%!")
else:
    print("\nSOME CHECKS FAILED!")
    sys.exit(1)
