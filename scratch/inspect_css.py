import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

print("--- ORIGINAL CSS FOR TITLES ---")
# Let's search index.html for .social-headline, .bonus-title, .for-who
for sel in ['.social-headline', '.bonus-title', '.for-who-col h3', '.for-who-card-title', 'h2', 'h3']:
    matches = re.findall(r'(' + re.escape(sel) + r'\s*\{[^}]+\})', orig)
    for m in matches:
        print(m)
        print()

print("--- P12 CSS FOR TITLES ---")
for sel in ['.social-headline', '#social-proof h2', '.bonus-title', '.for-who-card-title']:
    matches = re.findall(r'(' + re.escape(sel) + r'\s*\{[^}]+\})', p12)
    for m in matches:
        print(m)
        print()
