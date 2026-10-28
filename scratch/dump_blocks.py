import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

# Dobra 6: from line 6535 to 7068
pos6_start = p12.find('<!-- SEÇÃO: Depoimentos Hotmart -->')
if pos6_start == -1:
    pos6_start = p12.find('id="testimonials-hotmart"')
    pos6_start = p12.rfind('<section', 0, pos6_start)

pos6_end = p12.find('<!-- ═══════════════════════════════════\n       SEÇÃO: PREÇO / CTA 1', pos6_start)

block6 = p12[pos6_start:pos6_end]
with open('scratch/current_block_b.html', 'w', encoding='utf-8') as f:
    f.write(block6)
print(f"Current Block B length: {len(block6)} chars")

# Dobra 8: from social-seam-line to for-who
pos8_start = p12.find('<div class="social-seam-line"')
pos8_end = p12.find('<!-- ═══════════════════════════════════\n       SEÇÃO: PARA QUEM É / NÃO É', pos8_start)

block8 = p12[pos8_start:pos8_end]
with open('scratch/current_block_a.html', 'w', encoding='utf-8') as f:
    f.write(block8)
print(f"Current Block A length: {len(block8)} chars")
