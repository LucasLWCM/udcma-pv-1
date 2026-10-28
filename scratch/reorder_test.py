import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

# Markers
m_pricing_start = p12.find('<!-- ═══════════════════════════════════\n       SEÇÃO: PREÇO / CTA 1')
m_social_start  = p12.find('<!-- ═══════════════════════════════════\n       SEÇÃO: PROVA SOCIAL')
m_for_who_start = p12.find('<!-- ═══════════════════════════════════\n       SEÇÃO: PARA QUEM É / NÃO É')
m_about_start   = p12.find('<!-- ═══════════════════════════════════\n       SEÇÃO: AUTOR')
m_guarantee_start = p12.find('<!-- ═══════════════════════════════════\n       SEÇÃO: GARANTIA + CTA 2 (DOBRA 10 P12)')
m_closing_start = p12.find('<!-- ═══════════════════════════════════\n       SEÇÃO: COPY FINAL PERSUASÃO (DOBRA 11 P12)')
m_faq_start     = p12.find('<!-- ═══════════════════════════════════\n       SEÇÃO: FAQ + CTA 3')

# Extract exact blocks
# Part 1: Top of page up to the end of pricing
part_top = p12[:m_social_start]

# Block pricing
block_pricing = p12[m_pricing_start:m_social_start]

# Block social proof (Bloco A)
block_social = p12[m_social_start:m_for_who_start]

# Block for who
block_for_who = p12[m_for_who_start:m_about_start]

# Block about
block_about = p12[m_about_start:m_guarantee_start]

# Block guarantee
block_guarantee = p12[m_guarantee_start:m_closing_start]

# Part bottom: from closing to end of file
part_bottom = p12[m_closing_start:]

print("Length of top:", len(part_top))
print("Length of social:", len(block_social))
print("Length of for_who:", len(block_for_who))
print("Length of about:", len(block_about))
print("Length of guarantee:", len(block_guarantee))
print("Length of bottom:", len(part_bottom))

# ── Clean up seam lines and dividers in blocks to match new neighbors ──

# Block guarantee:
# Preceded by pricing (light). Needs guarantee-seam-line with seam-line-draw.
# Remove old divider at the top of guarantee if any
clean_guarantee = block_guarantee.strip()
if clean_guarantee.endswith('<div class="section-divider"></div>'):
    clean_guarantee = clean_guarantee[:-len('<div class="section-divider"></div>')].strip()

new_block_guarantee = f'''  <!-- ══════════════════════════════════════════════════════════════════════════
       DOBRA 8: GARANTIA + CTA 2 (P12)
       Linha dourada de emenda com o cartão branco de preço
       ══════════════════════════════════════════════════════════════════════════ -->
  <div class="guarantee-seam-line" id="guaranteeSeamLine" aria-hidden="true">
    <div class="seam-line-draw"></div>
  </div>

  {clean_guarantee}
'''

# Block for-who:
# Preceded by guarantee (dark). Needs discrete dark seam divider.
clean_for_who = block_for_who.strip()
if clean_for_who.endswith('<div class="section-divider"></div>'):
    clean_for_who = clean_for_who[:-len('<div class="section-divider"></div>')].strip()

new_block_for_who = f'''  <div class="dark-seam-divider" aria-hidden="true">
    <div class="dark-seam-line"></div>
  </div>

  {clean_for_who}
'''

# Block social:
# Preceded by for-who (dark).
# In block_social, remove the old .social-seam-line (which was meant for pricing->social)
# and replace with dark-seam-divider.
clean_social = block_social.strip()
clean_social = re.sub(r'<div class="social-seam-line"[\s\S]*?</div>\s*</div>', '', clean_social).strip()
if clean_social.endswith('<div class="section-divider"></div>'):
    clean_social = clean_social[:-len('<div class="section-divider"></div>')].strip()

new_block_social = f'''  <div class="dark-seam-divider" aria-hidden="true">
    <div class="dark-seam-line"></div>
  </div>

  {clean_social}
'''

# Block about:
# Preceded by social (dark). Needs discrete dark seam divider.
clean_about = block_about.strip()
if clean_about.endswith('<div class="section-divider"></div>'):
    clean_about = clean_about[:-len('<div class="section-divider"></div>')].strip()

new_block_about = f'''  <div class="dark-seam-divider" aria-hidden="true">
    <div class="dark-seam-line"></div>
  </div>

  {clean_about}
'''

# New order of blocks:
# part_top (1. hero, 2. pain, 3. errors, 4. product, 5. bonus, 6. testimonials_b, 7. pricing)
# 8. new_block_guarantee
# 9. new_block_for_who
# 10. new_block_social
# 11. new_block_about
# part_bottom (12. closing, 13. faq, 14. footer, scripts)

reordered = (
    p12[:m_social_start] +
    new_block_guarantee + '\n\n' +
    new_block_for_who + '\n\n' +
    new_block_social + '\n\n' +
    new_block_about + '\n\n' +
    part_bottom
)

# Also ensure CSS for guarantee-seam-line and dark-seam-divider is present
css_additions = '''
    /* ── TRANSIÇÃO OFERTA (CLARO) PARA GARANTIA (ESCURO) ── */
    .guarantee-seam-line {
      position: relative;
      width: 100%;
      height: 2px;
      background: rgba(199, 158, 59, 0.15);
      overflow: hidden;
      z-index: 5;
    }

    .guarantee-seam-line .seam-line-draw {
      position: absolute;
      left: 0;
      top: 0;
      height: 100%;
      width: 100%;
      background: linear-gradient(90deg, transparent 0%, #C79E3B 20%, #F5DE9C 50%, #C79E3B 80%, transparent 100%);
      box-shadow: 0 0 14px rgba(199, 158, 59, 0.5);
      transform: scaleX(0);
      transform-origin: left center;
      transition: transform 1.2s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .guarantee-seam-line.is-drawn .seam-line-draw {
      transform: scaleX(1);
    }

    /* ── EMENDAS ENTRE BLOCOS ESCUROS CONSECUTIVOS ── */
    .dark-seam-divider {
      width: 100%;
      padding: clamp(24px, 3.5vw, 42px) 0;
      display: flex;
      justify-content: center;
      align-items: center;
      background: #0E0E0E;
      position: relative;
      z-index: 2;
    }

    .dark-seam-line {
      width: min(85%, 880px);
      height: 1px;
      background: linear-gradient(90deg, transparent 0%, rgba(199, 158, 59, 0.22) 50%, transparent 100%);
    }
'''

# Wire up guarantee seam line in guarantee script
reordered = reordered.replace(
    "var card = section.querySelector('.guarantee-card');",
    '''var card = section.querySelector('.guarantee-card');
    var seamLine = document.getElementById('guaranteeSeamLine');
    if (seamLine && 'IntersectionObserver' in window && !prefersReduced) {
      var seamObs = new IntersectionObserver(function (entries, observer) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            seamLine.classList.add('is-drawn');
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.2 });
      seamObs.observe(seamLine);
    } else if (seamLine) {
      seamLine.classList.add('is-drawn');
    }'''
)

pos_style = reordered.find('</style>')
final_reordered = reordered[:pos_style] + css_additions + reordered[pos_style:]

with open('scratch/test_reordered.html', 'w', encoding='utf-8') as f:
    f.write(final_reordered)

print("Saved scratch/test_reordered.html successfully! Length:", len(final_reordered))
