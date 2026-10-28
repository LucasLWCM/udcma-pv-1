import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

s_idx = p12.find('<section id="for-who">')
e_idx = p12.find('</section>', s_idx) + len('</section>')
sec_code = p12[s_idx:e_idx]

checks = [
    # Card 1 (yes)
    ("Card 1 Title", "Essa série é para quem quer:"),
    ("Card 1 Item 1 bold", "Dominar o Pensamento Estoico"),
    ("Card 1 Item 1 italic", "(fixando o conhecimento, sem esquecimento)"),
    ("Card 1 Item 2 bold", "Aprender as principais ideias de Marco Aurélio"),
    ("Card 1 Item 2 italic", "(mesmo que nunca tenha estudado filosofia antes)"),
    ("Card 1 Item 3 bold 1", "Viver o Estoicismo"),
    ("Card 1 Item 3 italic", "(de maneira natural e consistente)"),
    ("Card 1 Item 3 bold 2", "em seus hábitos e conversas"),
    # Card 2 (no)
    ("Card 2 Title", "Essa série NÃO é para você que:"),
    ("Card 2 Item 1 bold 1", "Quer um curso acadêmico"),
    ("Card 2 Item 1 italic", "(longo e complexo)"),
    ("Card 2 Item 1 bold 2", "em filosofia clássica"),
    ("Card 2 Item 2 bold", 'Acha que "filosofia de verdade" precisa ser chata e incompreensível'),
    ("Card 2 Item 3 bold", "Prefere só colecionar frases motivacionais"),
    ("Card 2 Item 3 italic", "(que muitas vezes nem são dos Estoicos)"),
]

all_ok = True
for label, val in checks:
    if val in sec_code:
        print(f"[OK] {label}: exact match '{val}'")
    else:
        print(f"[FAIL] {label}: '{val}' not found!")
        all_ok = False

if all_ok:
    print("\nALL DOBRA 9 COPY CHECKS PASSED 100%!")
else:
    sys.exit(1)
