import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    for target in ['VOCÊ ESTARÁ A FRENTE', 'DEPOIMENTOS RETIRADOS', 'Essa série é para quem quer:', 'Essa série NÃO é para você que:']:
        if target in line:
            print(f"Line {i+1}: {line.strip()}")
            # print surrounding lines
            for j in range(max(0, i-5), min(len(lines), i+6)):
                print(f"  {j+1}: {lines[j].rstrip()}")
            print("-" * 50)
