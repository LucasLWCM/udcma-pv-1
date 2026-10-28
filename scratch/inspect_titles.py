import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

targets = [
    'VOCÊ ESTARÁ A FRENTE DE 95% DAS PESSOAS',
    'Depoimentos retirados da plataforma da série',
    'DEPOIMENTOS RETIRADOS DA PLATAFORMA DA SÉRIE',
    'Essa série é para quem quer:',
    'Essa série NÃO é para você que:'
]

print("=== ORIGINAL ===")
for t in targets:
    pos = orig.find(t)
    if pos != -1:
        snippet = orig[max(0, pos-120):min(len(orig), pos+150)]
        print(f"[{t}]")
        print(snippet.strip())
        print("-" * 40)

print("\n=== P12 ===")
for t in targets:
    pos = p12.find(t)
    if pos != -1:
        snippet = p12[max(0, pos-120):min(len(p12), pos+150)]
        print(f"[{t}]")
        print(snippet.strip())
        print("-" * 40)
