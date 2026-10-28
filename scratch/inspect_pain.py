import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

pos_html = p12.find('id="pain"')
print("pos of id=pain:", pos_html)
if pos_html != -1:
    line_no = p12[:pos_html].count('\n') + 1
    print("line of id=pain:", line_no)

# Find Dobra 2 in CSS
for m in re.finditer(r'dobra\s*2\b', p12, re.IGNORECASE):
    pos = m.start()
    line = p12[:pos].count('\n') + 1
    print(f"Match 'Dobra 2' at line {line}: {p12[pos-30:pos+100].strip()}")
