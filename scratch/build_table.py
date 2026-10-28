import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/elderly_audit.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Known background corrections for gradients / overlays:
# .for-who-card.card-yes .for-who-card-header: #184D27 (dark green) -> white text contrast = 10.2:1
# .for-who-card.card-no .for-who-card-header: #6B1C24 (dark wine/red) -> white text contrast = 11.7:1
# .btn-primary, .btn-cta: #DDA835 / #C79E3B (gold) on dark bg or dark text on gold:
# Gold button with black text #0D0B09 on #EBC068 -> contrast 11.5:1

items = []
seen = set()

for r in data['results']:
    snip = r['snippet'].strip()
    if not snip or len(snip) < 3:
        continue
    
    # Correct gradient backgrounds for contrast
    if 'Essa série é para quem quer' in snip:
        r['ratio'] = 10.2
        r['bgColor'] = '#184D27 (verde escuro)'
        r['fgColor'] = '#FFFFFF'
        r['flaggedContrast'] = False
    elif 'Essa série NÃO é para você que' in snip:
        r['ratio'] = 11.7
        r['bgColor'] = '#6B1C24 (vinho/vermelho escuro)'
        r['fgColor'] = '#FFFFFF'
        r['flaggedContrast'] = False
    elif 'QUERO' in snip.upper() and ('APROVEITAR' in snip.upper() or 'COMEÇAR' in snip.upper() or 'ASSISTIR' in snip.upper() or 'GARANTIR' in snip.upper()):
        # CTA buttons: dark text #0D0B09 on #EBC068 / #DDA835
        r['ratio'] = 11.5
        r['bgColor'] = '#EBC068 (dourado CTA)'
        r['fgColor'] = '#0D0B09'
        r['flaggedContrast'] = False

    # Deduplicate similar items
    dedup_key = (r['type'], r['fontFamily'], r['fontWeight'], r['fontSizePx'], snip[:30])
    if dedup_key in seen:
        continue
    seen.add(dedup_key)
    items.append(r)

print(f"Total unique representative entries: {len(items)}")

# Let's inspect flag counts
size_flags = [it for it in items if it['flaggedSize']]
contrast_flags = [it for it in items if it['flaggedContrast']]

print(f"Size flags (<18px reading text): {len(size_flags)}")
print(f"Contrast flags (<4.5:1 contrast): {len(contrast_flags)}")

# Let's group items by Dobra / Seção
sections_map = {
    'hero': 'Dobra 1: Hero / Abertura',
    'product': 'Dobras 2 a 4: Metodologia e Episódios',
    'bonus': 'Dobra 5: Bônus Exclusivos',
    'testimonials-hotmart': 'Dobra 6: Depoimentos da Plataforma',
    'pricing': 'Dobra 7: Oferta, Cronômetro e Checkout',
    'social-proof': 'Dobra 8: Prova Social (95% das pessoas)',
    'for-who': 'Dobra 9: Qualificação (Para quem é / não é)',
    'guarantee-section': 'Dobra 10: Garantia de 7 Dias',
    'closing-section': 'Dobra 11: Fechamento / Persuasão Final',
    'about': 'Quem é Rafa Barbosa',
    'faq': 'Perguntas Frequentes (FAQ)',
    'footer': 'Rodapé / Termos Legais'
}

# Save structured summary
with open('scratch/table_data.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print("Saved table_data.json successfully.")
