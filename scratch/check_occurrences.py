import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

for term in ['social-headline', 'testimonials-title', 'for-who-card-title']:
    print(f'=== {term} ===')
    for m in re.finditer(re.escape(term), p12):
        pos = m.start()
        print(f'Line ~{p12[:pos].count(chr(10))+1}: {p12[max(0, pos-40):min(len(p12), pos+100)].strip()}')
