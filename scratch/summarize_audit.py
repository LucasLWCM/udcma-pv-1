import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/elderly_audit.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=== CHECKING THE 4 UPDATED TITLES ===")
targets = ['95%', 'DEPOIMENTOS RETIRADOS', 'Essa série é para quem', 'Essa série NÃO é para']
for r in data['results']:
    for target in targets:
        if target.lower() in r['snippet'].lower() and (r['type'] == 'Título' or r['type'] == 'Subtítulo / Apoio'):
            print(f"- Snippet: {r['snippet']}")
            print(f"  Type: {r['type']}")
            print(f"  Font: {r['fontFamily']}")
            print(f"  Weight: {r['fontWeight']}")
            print(f"  Mobile Size: {r['fontSizePx']}px")
            print(f"  Color: {r['fgColor']} / Bg: {r['bgColor']}")
            print(f"  Contrast: {r['ratio']}:1")
            print()
