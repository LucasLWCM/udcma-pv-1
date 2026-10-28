import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12_content = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    orig_content = f.read()

# 1. Check tag balance in p12
tags_to_check = ['div', 'section', 'span', 'h2', 'p', 'a', 'svg', 'circle', 'script', 'style']
for t in tags_to_check:
    open_count = len(re.findall(rf'<{t}\b', p12_content, re.IGNORECASE))
    close_count = len(re.findall(rf'</{t}>', p12_content, re.IGNORECASE))
    print(f"Tag <{t}>: open={open_count}, close={close_count}, balanced={open_count == close_count}")

# 2. Extract #guarantee section in p12
m_p12 = re.search(r'(<section id="guarantee"[\s\S]*?</section>)', p12_content)
m_orig = re.search(r'(<section id="guarantee"[\s\S]*?</section>)', orig_content)

if not m_p12 or not m_orig:
    print("Error: Could not extract guarantee sections")
    sys.exit(1)

p12_guarantee = m_p12.group(1)
orig_guarantee = m_orig.group(1)

print("\n--- P12 GUARANTEE SECTION ---")
print(p12_guarantee)

# 3. Check exact required copy items
copy_items = [
    '7',
    'DIAS DE GARANTIA',
    'Você tem 7 dias para pedir seu dinheiro de volta.',
    'Sem perguntas. Sem complicação.',
    'Quero aproveitar a garantia!',
    'Acesso IMEDIATO e VITALÍCIO',
    'https://pay.hotmart.com/X108154869T?off=953h3rmf',
    'Mais de 3 mil',
    'alunos',
    '0,70%',
    'de reembolso na Hotmart',
    '<!-- ATUALIZAR: dados conferidos em 27/10/2026. Alunos somam Hotmart e outras plataformas; o reembolso é só da Hotmart. -->'
]

print("\n--- COPY VERIFICATION ---")
all_found = True
for item in copy_items:
    found = item in p12_guarantee
    print(f"[{'PASS' if found else 'FAIL'}] '{item}'")
    if not found:
        all_found = False

# 4. Check forbidden words
forbidden = ['chargeback', 'vendas', '2.997', '2997']
for word in forbidden:
    if word in p12_guarantee:
        print(f"WARNING: forbidden word '{word}' found in guarantee section!")
    else:
        print(f"[PASS] Forbidden word '{word}' NOT present.")

print(f"\nAll copy items present and correct: {all_found}")
