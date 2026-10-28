import sys

sys.stdout.reconfigure(encoding='utf-8')

# Let's check how cards are structured currently in p12/index.html
with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

pos_cards = p12.find('<ul class="pain-list">')
pos_cards_end = p12.find('</ul>', pos_cards)
cards_block = p12[pos_cards:pos_cards_end]

print("Found cards block, length:", len(cards_block))
