import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

titles = [
    'VOCÊ ESTARÁ A FRENTE DE 95%',
    'DEPOIMENTOS RETIRADOS DA PLATAFORMA',
    'Essa série é para quem quer:',
    'Essa série NÃO é para você que:'
]

for t in titles:
    pos = c.find(t)
    if pos != -1:
        start = c.rfind('<', 0, pos)
        end = c.find('>', pos) + 1
        print(f"\nTarget: '{t}'")
        print("HTML tag:", c[start:end])
        # Find tag name and class
        tag_match = re.match(r'<(\w+)[^>]*class="([^"]+)"', c[start:end])
        if tag_match:
            tag, cls = tag_match.groups()
            print(f"Tag: {tag}, Class: {cls}")
            for single_cls in cls.split():
                # find in css
                css_m = re.findall(rf'([^{{}}]*\.{single_cls}[^{{}}]*\{{[^}}]+\}})', c)
                for r in css_m:
                    print(f"  CSS rule for .{single_cls}:\n{r.strip()}")
        else:
            print("Tag match failed on:", c[start:end])
