import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

with open('p12/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

s_idx = content.find('<section id="for-who">')
e_idx = content.find('</section>', s_idx) + len('</section>')
sec_code = content[s_idx:e_idx]

tags = ['div', 'section', 'video', 'picture', 'h3', 'ul', 'li', 'span', 'strong', 'em', 'noscript']
for t in tags:
    opens = len(re.findall(r'<' + t + r'\b', sec_code))
    closes = len(re.findall(r'</' + t + r'\b', sec_code))
    print(f"{t}: {opens} open, {closes} close")
    if opens != closes:
        print(f"ERROR: {t} tags mismatched!")
        sys.exit(1)

print("\nALL DOBRA 9 TAGS BALANCED!")
