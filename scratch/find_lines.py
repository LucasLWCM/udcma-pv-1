import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('Total lines in p12/index.html:', len(lines))
for idx, line in enumerate(lines):
    if 'DEPOIMENTOS RETIRADOS' in line:
        print(f'Found at line {idx+1}: {line.strip()[:80]}')
    if 'marquee-control' in line or 'pause' in line.lower():
        print(f'Pause/marquee mention at line {idx+1}: {line.strip()[:80]}')
