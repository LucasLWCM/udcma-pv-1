import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/table_data.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Group by Section
# Let's map section ids or names to orderly readable labels
section_order = [
    ('hero', 'Dobra 1: Hero / Topo'),
    ('product', 'Dobras 2, 3 e 4: Metodologia e Episódios'),
    ('bonus', 'Dobra 5: Bônus Exclusivos'),
    ('testimonials-hotmart', 'Dobra 6: Depoimentos da Plataforma'),
    ('pricing', 'Dobra 7: Oferta, Itens Inclusos e Checkout'),
    ('social-proof', 'Dobra 8: Prova Social (95% das pessoas)'),
    ('for-who', 'Dobra 9: Qualificação (Cards Para quem é / NÃO é)'),
    ('guarantee', 'Dobra 10: Garantia de 7 Dias'),
    ('closing', 'Dobra 11: Fechamento / Persuasão Final'),
    ('about', 'Quem é Rafa Barbosa'),
    ('faq', 'Perguntas Frequentes (FAQ)'),
    ('footer', 'Rodapé / Avisos Legais')
]

# Specific background and contrast adjustments for known visual elements:
for it in items:
    s = it['snippet'].lower()
    sec = it['section'].lower()
    
    # Guarantee section #guarantee-section background is dark (#0B0A0D)
    if '3 mil alunos' in s or 'reembolso na hotmart' in s or 'dias de garantia' in s:
        it['section'] = 'guarantee'
        it['bgColor'] = '#0B0A0D'
        it['fgColor'] = '#F5F0E8'
        it['ratio'] = 17.5
        it['flaggedContrast'] = False
        
    # Closing section background is #0B0A0D
    if 'assistindo os outros' in s or 'todo mundo fala' in s or 'a real?' in s:
        it['section'] = 'closing'
        it['bgColor'] = '#0B0A0D'
        it['fgColor'] = '#FAF6EE'
        it['ratio'] = 18.2
        it['flaggedContrast'] = False

    # Hero section
    if 'marco aurélio' in s or 'em 3 episódios' in s or 'filosofia prática' in s:
        it['section'] = 'hero'

    # Normalize section names
    if 'testimonials' in sec:
        it['section'] = 'testimonials-hotmart'
    elif 'guarantee' in sec:
        it['section'] = 'guarantee'
    elif 'closing' in sec:
        it['section'] = 'closing'

# Let's select key representative rows for each section to provide a comprehensive, complete, yet readable table
# Categories:
# 1. Títulos
# 2. Subtítulos / Apoio
# 3. Textos de Leitura (parágrafos explicativos, depoimentos)
# 4. Textos Pequenos (legendas, disclaimer, bônus, micro-copy, "(sem aula chata em slide)")
# 5. Itálicos
# 6. Botões
# 7. Links

def format_row(r):
    # Status
    flags = []
    is_reading = r['type'] in ['Leitura', 'Itálico']
    if is_reading and r['fontSizePx'] < 18:
        flags.append(f"⚠️ Leitura < 18px ({r['fontSizePx']}px)")
    if r['ratio'] < 4.5:
        flags.append(f"⚠️ Contraste < 4,5:1 ({r['ratio']}:1)")
    
    status = " / ".join(flags) if flags else "✅ Adequado"
    
    # Truncate snippet
    snip = r['snippet'].replace('|', '—').strip()
    if len(snip) > 48:
        snip = snip[:45] + '...'
    
    ratio_str = f"{r['ratio']:.1f}:1" if isinstance(r['ratio'], (int, float)) else str(r['ratio'])
    
    return f"| {r['type']} | `{snip}` | {r['fontFamily']} | {r['fontWeight']} | {r['fontSizePx']} px | {ratio_str} | {status} |"

# Filter representative elements
grouped = {}
for code, name in section_order:
    grouped[code] = []

for it in items:
    sec = it['section']
    # find best matching section
    matched = False
    for code, name in section_order:
        if code in sec:
            grouped[code].append(it)
            matched = True
            break
    if not matched:
        grouped['hero'].append(it)

output_lines = []
for code, name in section_order:
    sec_items = grouped[code]
    if not sec_items:
        continue
    output_lines.append(f"\n### {name}")
    output_lines.append("| Categoria | Exemplo de Texto | Fonte | Peso | Tam. Mobile | Contraste | Avaliação (Público Idoso) |")
    output_lines.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
    
    # Dedup by (type, fontSizePx, fontFamily)
    seen_sec = set()
    for it in sec_items:
        key = (it['type'], it['fontSizePx'], it['fontFamily'], it['fontWeight'])
        # keep up to 2 examples per type
        count = sum(1 for k in seen_sec if k[0] == it['type'])
        if count >= 3 and it['type'] == 'Leitura':
            continue
        if key in seen_sec:
            continue
        seen_sec.add(key)
        output_lines.append(format_row(it))

result_md = "\n".join(output_lines)
with open('scratch/elderly_table.md', 'w', encoding='utf-8') as f:
    f.write(result_md)

print("Generated scratch/elderly_table.md successfully!")
