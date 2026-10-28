import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Font links
font_links = re.findall(r'<link[^>]+fonts[^>]+>', orig)
for l in font_links:
    print("Font link:", l)

# Root font vars
root_m = re.search(r':root\s*\{([^}]+)\}', orig)
if root_m:
    print("\nRoot variables:")
    for line in root_m.group(1).splitlines():
        if 'font' in line or 'cta' in line:
            print(" ", line.strip())

# Look for h2 general style
h2_m = re.findall(r'h2\s*\{([^}]+)\}', orig)
for h in h2_m:
    print("\nh2 style:", h.strip())

# Specifically look at the 4 titles:
# 1. "VOCÊ ESTARÁ A FRENTE DE 95% DAS PESSOAS"
# 2. "DEPOIMENTOS RETIRADOS DA PLATAFORMA DA SÉRIE"
# 3. "Essa série é para quem quer:"
# 4. "Essa série NÃO é para você que:"
sections = ['#comparison', '#testimonials', '#for-who']
for s in sections:
    s_idx = orig.find(s + ' ')
    if s_idx == -1:
        s_idx = orig.find(s + '{')
    if s_idx == -1:
        s_idx = orig.find(s)
    print(f"\nCSS near {s}:")
    print(orig[s_idx:s_idx+600])
