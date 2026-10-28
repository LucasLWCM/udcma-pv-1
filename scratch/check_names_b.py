import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/current_block_b.html', 'r', encoding='utf-8') as f:
    b = f.read()

names = re.findall(r'<div class="t-name">([^<]+)</div>', b)
print("Names in current_block_b.html:")
for n in names:
    print(" -", n)

names_in_cards = re.findall(r'<!--\s*(?:DESTAQUE\s*\d+:|\d+\.)\s*([^->]+)-->', b)
print("\nCard comments:")
for c in names_in_cards:
    print(" *", c.strip())
