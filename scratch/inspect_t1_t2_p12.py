import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Title 1: "VOCÊ ESTARÁ A FRENTE DE 95% DAS PESSOAS"
pos1 = c.find('VOCÊ ESTARÁ A FRENTE')
if pos1 != -1:
    start1 = c.rfind('<', 0, pos1)
    end1 = c.find('>', pos1) + 1
    print("Title 1 HTML tag in p12:", c[start1:end1])
    tag_m = re.search(r'class="([^"]+)"', c[start1:end1])
    if tag_m:
        print("Classes:", tag_m.group(1))
        for cls in tag_m.group(1).split():
            m = re.findall(rf'([^{{}}]*\.{cls}[^{{}}]*\{{[^}}]+\}})', c)
            for r in m:
                print(f"  CSS for .{cls}:\n{r.strip()}")

# Title 2: "DEPOIMENTOS RETIRADOS DA PLATAFORMA DA SÉRIE"
pos2 = c.find('DEPOIMENTOS RETIRADOS')
if pos2 != -1:
    start2 = c.rfind('<', 0, pos2)
    end2 = c.find('>', pos2) + 1
    print("\nTitle 2 HTML tag in p12:", c[start2:end2])
    tag_m = re.search(r'class="([^"]+)"', c[start2:end2])
    if tag_m:
        print("Classes:", tag_m.group(1))
        for cls in tag_m.group(1).split():
            m = re.findall(rf'([^{{}}]*\.{cls}[^{{}}]*\{{[^}}]+\}})', c)
            for r in m:
                print(f"  CSS for .{cls}:\n{r.strip()}")
