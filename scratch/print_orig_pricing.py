import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

start = orig.find('<section id="pricing">')
end = orig.find('</section>', start) + len('</section>')

pricing_html = orig[start:end]
print("--- EXACT ORIGINAL PRICING HTML ---")
print(pricing_html)

# Also check for occurrences of 297,90
print("\n--- OCCURRENCES OF 297,90 IN INDEX.HTML ---")
import re
for m in re.finditer(r'297[.,]90', orig):
    print(f"Found {m.group(0)} at position {m.start()}: {orig[m.start()-40:m.end()+40]}")
