import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

# Find sections
sections = re.findall(r'<section\s+id=[\'"]([^\'"]+)[\'"]', p12)
print("Sections in P12:", sections)

# Locate Dobra 6 and Dobra 8 HTML
for sec_id in ['testimonials-hotmart', 'pricing', 'social-proof']:
    pos = p12.find(f'id="{sec_id}"')
    if pos != -1:
        line_no = p12[:pos].count('\n') + 1
        print(f"Section #{sec_id} starts around line {line_no}")
