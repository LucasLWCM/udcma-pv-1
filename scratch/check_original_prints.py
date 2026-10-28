import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

pos = orig.find('id="social-proof"')
if pos != -1:
    snippet = orig[pos:pos+4000]
    imgs = re.findall(r'<img[^>]+>', snippet)
    print(f"Found {len(imgs)} imgs in original social-proof:")
    for img in imgs:
        print(img)
