import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/test_reordered.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('id="guarantee"')
print(html[pos:pos+2500])
