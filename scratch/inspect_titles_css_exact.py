import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Check Title 1 tag in index.html
t1_pos = orig.find('VOCÊ ESTARÁ A FRENTE DE 95%')
if t1_pos != -1:
    tag_start = orig.rfind('<', 0, t1_pos)
    tag_end = orig.find('>', t1_pos) + 1
    print("Title 1 tag in index.html:", orig[tag_start:tag_end])

# Check Title 2 tag in index.html
t2_pos = orig.find('DEPOIMENTOS RETIRADOS DA PLATAFORMA DA SÉRIE')
if t2_pos != -1:
    tag_start = orig.rfind('<', 0, t2_pos)
    tag_end = orig.find('>', t2_pos) + 1
    print("Title 2 tag in index.html:", orig[tag_start:tag_end])

# Check CSS in index.html for .for-who-col h3
m_for_who_h3 = re.findall(r'([^{}]*for-who[^{}]*h3[^{}]*\{[^}]+\})', orig)
print("\nfor-who h3 CSS in index.html:")
for m in m_for_who_h3:
    print(m)

# Check all h2 styles in index.html
m_h2 = re.findall(r'([^{}]*h2[^{}]*\{[^}]+\})', orig)
print("\nAll h2 CSS in index.html:")
for m in m_h2:
    print(m)
