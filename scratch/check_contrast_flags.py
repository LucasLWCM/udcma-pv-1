import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/table_data.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print("=== ITEMS WITH CONTRAST < 4.5:1 ===")
for it in items:
    if it['flaggedContrast']:
        print(f"[{it['section']}] ({it['type']}) {it['snippet']}")
        print(f"  Font: {it['fontFamily']} {it['fontWeight']}, Size: {it['fontSizePx']}px")
        print(f"  Fg: {it['fgColor']}, Bg: {it['bgColor']}, Ratio: {it['ratio']}:1")
        print()
