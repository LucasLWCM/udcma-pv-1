import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

links = re.findall(r'href=[\'"]([^\'"]*hotmart[^\'"]*)[\'"]', p12)
print("Hotmart checkout links:")
for l in set(links):
    print(" -", l, f"(count: {links.count(l)})")
