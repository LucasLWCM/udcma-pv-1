import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

s_idx = content.find('<section id="social-proof">')
e_idx = content.find('</section>', s_idx) + len('</section>')
sec_code = content[s_idx:e_idx]

import re
tags = ['div', 'section', 'article', 'picture', 'h2', 'p', 'span', 'strong', 'em']
for t in tags:
    opens = len(re.findall(r'<' + t + r'\b', sec_code))
    closes = len(re.findall(r'</' + t + r'\b', sec_code))
    print(f"{t}: {opens} open, {closes} close")
    if opens != closes:
        print(f"ERROR: {t} tags mismatched!")
        sys.exit(1)

print("\nALL DOBRA 8 TAGS PERFECTLY BALANCED!")
