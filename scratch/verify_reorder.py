import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/test_reordered.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Check sequence of sections in HTML
sections = re.findall(r'<section\b[^>]*id="([^"]+)"', html)
print("Detected sections order in test_reordered.html:")
for i, s in enumerate(sections):
    print(f" {i+1}. {s}")

expected_order = [
    'hero',
    'pain',
    'errors',
    'product',
    'bonus',
    'testimonials-block-b',
    'pricing',
    'guarantee',
    'for-who',
    'social-proof',
    'about',
    'closing',
    'faq'
]

assert sections == expected_order, f"Sections order mismatch!\nExpected: {expected_order}\nGot: {sections}"
print("\n✅ SECTIONS ORDER IS 100% CORRECT!")

# 2. Check all key texts
texts = [
    # Guarantee
    "7 DIAS DE GARANTIA",
    "Você tem 7 dias para pedir seu dinheiro de volta.",
    "Quero aproveitar a garantia!",
    "Mais de 3 mil",
    "alunos",
    "0,70%",
    "de reembolso na Hotmart",
    "ACESSO IMEDIATO",
    # For Who
    "Essa série é para quem quer:",
    "Essa série NÃO é para você que:",
    "Dominar o Pensamento Estoico",
    # Social Proof
    "VOCÊ ESTARÁ A FRENTE DE 95% DAS PESSOAS",
    'Em 60 minutos você vai entender mais sobre estoicismo do que pessoas que "estudam" há anos.',
    "(e você está a um clique disso)",
    "Carlos Henrique Ramos",
    "Cristiane de Matteos de Aragão",
    "Chalice de Albuquerque Pinheiro",
    "Fabio José de Alencar",
    # About
    "Quem é",
    "Rafa Barbosa?",
    # Closing
    "Você ainda vai ficar assistindo os outros aprofundando e vivendo o estoicismo enquanto você só coleciona frases?",
    "Todo mundo fala que estoicismo muda vidas.",
    "A real?",
    # FAQ
    "DÚVIDAS MAIS IMPORTANTES:",
    "O que exatamente vou receber?",
    # Pricing & Timer
    "VEJA TUDO QUE VOCÊ VAI RECEBER:",
    "countdown-timer",
    "offerEndTime_v1",
    # Testimonials B
    "VOCÊ NÃO VAI ACREDITAR NO QUE OS ALUNOS ESTÃO DIZENDO"
]

print("\n=== Checking texts presence ===")
for t in texts:
    assert t in html, f"Missing text: {t}"
print(f"✅ All {len(texts)} key text phrases are present!")

# 3. Check checkout links
checkout_links = re.findall(r'href="https://pay\.hotmart\.com/X108154869T\?off=953h3rmf"', html)
print(f"\nCheckout links count: {len(checkout_links)} (Expected 5)")
assert len(checkout_links) == 5, f"Expected 5 checkout links, got {len(checkout_links)}"
print("✅ All 5 checkout links verified!")

# 4. Check Timer logic
assert 'const timerEl = document.getElementById("countdown-timer");' in html
assert 'localStorage.getItem("offerEndTime_v1")' in html
print("✅ Timer code intact!")
