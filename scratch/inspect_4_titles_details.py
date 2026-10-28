import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

def find_context(html, phrase, label):
    pos = html.find(phrase)
    if pos != -1:
        print(f"\n=== {label} for '{phrase}' ===")
        # find the tag enclosing it
        tag_start = html.rfind('<', 0, pos)
        tag_end = html.find('>', pos) + 1
        tag_line = html[tag_start:tag_end]
        print("Enclosing tag:", tag_line)
        # print surrounding HTML
        print("Context:\n", html[max(0, pos-120):min(len(html), pos+160)])
    else:
        print(f"\n=== {label} for '{phrase}' NOT FOUND ===")

targets = [
    'VOCÊ ESTARÁ A FRENTE DE 95% DAS PESSOAS',
    'DEPOIMENTOS RETIRADOS DA PLATAFORMA DA SÉRIE',
    'Essa série é para quem quer:',
    'Essa série NÃO é para você que:'
]

for t in targets:
    find_context(orig, t, "ORIGINAL (index.html)")
    find_context(p12, t, "P12 (p12/index.html)")
