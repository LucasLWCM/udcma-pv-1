import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's inspect where Dobra 6 starts and ends
pos6_start = content.find('<!-- SEÇÃO: Depoimentos Hotmart -->')
pos6_end = content.find('<!-- ═══════════════════════════════════\n       SEÇÃO: PREÇO / CTA 1', pos6_start)

# Dobra 8 starts and ends
pos8_start = content.find('<div class="social-seam-line" id="socialSeamLine"')
pos8_end = content.find('<!-- ═══════════════════════════════════\n       SEÇÃO: PARA QUEM É / NÃO É', pos8_start)

print(f"Dobra 6: {pos6_start} to {pos6_end} (length: {pos6_end - pos6_start})")
print(f"Dobra 8: {pos8_start} to {pos8_end} (length: {pos8_end - pos8_start})")
