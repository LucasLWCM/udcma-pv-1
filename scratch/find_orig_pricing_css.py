import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

import re
css_pricing = re.findall(r'(\/\*.*?pricing.*?\*\/[\s\S]*?)(?=\/\*|$)', orig, re.IGNORECASE)
print(f"Pricing CSS comments found: {len(css_pricing)}")
for i, c in enumerate(css_pricing[:3]):
    print(f"--- Comment #{i+1} ---")
    print(c[:500])

# Also search for #pricing in CSS
p_idx = orig.find('#pricing {')
if p_idx == -1:
    p_idx = orig.find('#pricing')
print(f"#pricing in index.html at: {p_idx}")
if p_idx != -1:
    print(orig[p_idx-100:p_idx+800])
