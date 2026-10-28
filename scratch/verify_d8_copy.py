import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

s_idx = p12.find('<section id="social-proof">')
e_idx = p12.find('</section>', s_idx) + len('</section>')
sec_code = p12[s_idx:e_idx]

checks = [
    ("Title text", "VOCÊ ESTARÁ A FRENTE DE 95% DAS PESSOAS"),
    ("Subtitle text", 'Em 60 minutos você vai entender mais sobre estoicismo do que pessoas que "estudam" há anos.'),
    ("Subtitle italic", '(e você está a um clique disso)'),
    ("Print 1 src", '../img/testimonials/8.2.webp'),
    ("Print 2 src", '../img/testimonials/5.webp'),
    ("Print 3 src", '../img/testimonials/6.webp'),
    ("Print 4 src", '../img/testimonials/9.2.webp'),
    ("Print 5 src", '../img/testimonials/7.webp'),
]

all_ok = True
for label, val in checks:
    if val in sec_code:
        print(f"[OK] {label}: found exact match '{val}'")
    else:
        print(f"[FAIL] {label}: '{val}' not found!")
        all_ok = False

if all_ok:
    print("\nALL DOBRA 8 CHECKS PASSED!")
else:
    sys.exit(1)
