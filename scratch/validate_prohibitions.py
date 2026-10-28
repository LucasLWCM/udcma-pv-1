import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

start = p12.find('<section id="pricing">')
end = p12.find('</section>', start) + len('</section>')
pricing_block = p12[start:end]

# Strip HTML tags to check only visible text
visible_text = re.sub(r'<[^>]+>', ' ', pricing_block)

prohibited = ['economize', 'desconto de', 'compre agora', 'vagas limitadas', '50% off', '60% off', '90% off']
all_passed = True
for p in prohibited:
    if p in visible_text.lower():
        print(f"[FAIL] Prohibited visible text found: '{p}'")
        all_passed = False
    else:
        print(f"[OK] No prohibited phrase '{p}'")

if all_passed:
    print("\nALL VISIBLE TEXT PROHIBITION CHECKS PASSED!")
