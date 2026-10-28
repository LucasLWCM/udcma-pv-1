import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

# Let's verify start markers of each section
markers = [
    ('hero', '<section id="hero">'),
    ('pain', '<section id="pain">'),
    ('errors', '<section id="errors">'),
    ('product', '<section id="product">'),
    ('bonus', '<section id="bonus">'),
    ('testimonials_b', '<!-- SEÇÃO: Depoimentos WhatsApp (Bloco B) -->'),
    ('pricing', '<!-- ═══════════════════════════════════\n       SEÇÃO: PREÇO / CTA 1'),
    ('social_proof', '<!-- ═══════════════════════════════════\n       SEÇÃO: PROVA SOCIAL'),
    ('for_who', '<!-- ═══════════════════════════════════\n       SEÇÃO: PARA QUEM É / NÃO É'),
    ('about', '<!-- ═══════════════════════════════════\n       SEÇÃO: AUTOR'),
    ('guarantee', '<!-- ═══════════════════════════════════\n       SEÇÃO: GARANTIA + CTA 2 (DOBRA 10 P12)'),
    ('closing', '<!-- ═══════════════════════════════════\n       SEÇÃO: COPY FINAL PERSUASÃO (DOBRA 11 P12)'),
    ('faq', '<!-- ═══════════════════════════════════\n       SEÇÃO: FAQ + CTA 3'),
    ('footer', '<!-- ═══════════════════════════════════\n       FOOTER')
]

positions = {}
for name, m in markers:
    pos = p12.find(m)
    if pos == -1:
        print(f"ERROR: Marker not found for {name}: {repr(m[:40])}")
    else:
        positions[name] = pos
        print(f"{name}: found at pos {pos}")
