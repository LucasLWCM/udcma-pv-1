import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. VOCÊ ESTARÁ A FRENTE DE 95% DAS PESSOAS
p1 = c.find('VOCÊ ESTARÁ A FRENTE')
start1 = c.rfind('<h', 0, p1)
end1 = c.find('>', p1) + 1
print("Title 1 HTML tag in p12:", c[start1:end1])
line_start = c.rfind('\n', 0, start1)
print("Context line:", c[line_start:end1+50])

# 2. DEPOIMENTOS RETIRADOS DA PLATAFORMA DA SÉRIE
p2 = c.find('DEPOIMENTOS RETIRADOS')
start2 = c.rfind('<h', 0, p2)
end2 = c.find('>', p2) + 1
print("\nTitle 2 HTML tag in p12:", c[start2:end2])
line_start2 = c.rfind('\n', 0, start2)
print("Context line:", c[line_start2:end2+50])
