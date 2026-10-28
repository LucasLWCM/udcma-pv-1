import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

import re
style_m = re.search(r'<style>([\s\S]*?)</style>', orig)
if style_m:
    css = style_m.group(1)
    print("Total style length in index.html:", len(css))
    # Look for social-headline, bonus-title, for-who
    for term in ['social-headline', 'bonus-title', 'for-who', 'for-who-col']:
        matches = re.findall(rf'([^{{}}]*{term}[^{{}}]*\{{[^}}]+\}})', css)
        print(f"\n--- Matches for {term} in style ({len(matches)}) ---")
        for m in matches:
            print(m.strip())
