import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12_content = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    orig_content = f.read()

# 1. Check tag balance in p12
tags_to_check = ['div', 'section', 'span', 'h2', 'p', 'strong', 'em', 'script', 'style']
for t in tags_to_check:
    open_count = len(re.findall(rf'<{t}\b', p12_content, re.IGNORECASE))
    close_count = len(re.findall(rf'</{t}>', p12_content, re.IGNORECASE))
    print(f"Tag <{t}>: open={open_count}, close={close_count}, balanced={open_count == close_count}")

# 2. Extract #closing section in p12 and index.html
m_p12 = re.search(r'(<section id="closing"[\s\S]*?</section>)', p12_content)
m_orig = re.search(r'(<section id="closing"[\s\S]*?</section>)', orig_content)

if not m_p12 or not m_orig:
    print("Error: Could not extract closing sections")
    sys.exit(1)

p12_closing = m_p12.group(1)
orig_closing = m_orig.group(1)

print("\n--- P12 CLOSING SECTION ---")
print(p12_closing)

# 3. Clean tags to compare exact plain text
def get_clean_text(html):
    # normalize whitespace and remove all tags
    text = re.sub(r'<br\s*/?>', '\n', html)
    text = re.sub(r'<[^>]+>', '', text)
    lines = [re.sub(r'\s+', ' ', line).strip() for line in text.split('\n')]
    return '\n'.join([line for line in lines if line])

p12_clean = get_clean_text(p12_closing)
orig_clean = get_clean_text(orig_closing)

print("\n--- PLAIN TEXT COMPARISON ---")
print("Original:")
print(repr(orig_clean))
print("\nP12:")
print(repr(p12_clean))
print(f"\nExact text match: {orig_clean == p12_clean}")

# 4. Check specific key lines
key_lines = [
    'Você ainda vai ficar assistindo os outros aprofundando e vivendo o estoicismo',
    'enquanto você só coleciona frases?',
    'Todo mundo fala que estoicismo muda vidas.',
    'Mas ninguém mostra o que fazer quando ele não funciona pra você.',
    'Você já comprou livros. Já assistiu vídeos. Já salvou dezenas de posts.',
    'Mas se ainda não mudou, é porque tá faltando a peça certa.',
    'A real?',
    'Quem entende estoicismo de verdade não é quem consome mais.',
    'É quem tem o plano certo.',
    'E o plano tá aqui.',
    'Um Dia com Marco Aurélio.',
    'Agora é contigo.',
    'Vai continuar só acumulando... ou vai viver esse dia?'
]

print("\n--- LINE CHECK ---")
for line in key_lines:
    found = line in p12_clean
    print(f"[{'PASS' if found else 'FAIL'}] '{line}'")
