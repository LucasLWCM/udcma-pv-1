import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

m = re.search(r'<h2 class="testimonials-title">([^<]+)</h2>', p12)
if m:
    print('Title B in HTML:', repr(m.group(1)))
