import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

with open('scratch/current_block_a.html', 'r', encoding='utf-8') as f:
    a = f.read()

with open('scratch/current_block_b.html', 'r', encoding='utf-8') as f:
    b = f.read()

# 1. Extract chat stream from Block A
pos_stream_start = a.find('<div class="social-chat-stream"')
pos_stream_end = a.find('</div>\n    </div>\n  </section>')
if pos_stream_end == -1:
    pos_stream_end = a.find('</div>\r\n    </div>\r\n  </section>')
if pos_stream_end == -1:
    # fallback
    pos_stream_end = a.rfind('</article>') + len('</article>\n\n      </div>')

chat_stream_html = a[pos_stream_start:pos_stream_end].strip()

# Add loading="lazy" to Print 1
chat_stream_html = chat_stream_html.replace(
    'width="400" height="400" decoding="async">',
    'width="400" height="400" loading="lazy" decoding="async">'
)

# 2. Extract testimonials content and script from Block B
pos_h2_b = b.find('<h2 class="testimonials-title">')
pos_header_end = b.find('</div>', pos_h2_b) + len('</div>')
pos_script_b = b.find('<script>')
pos_sec_close_b = b.rfind('</section>', 0, pos_script_b)

testimonials_body_html = b[pos_header_end:pos_sec_close_b].strip()
testimonials_script_html = b[pos_script_b:].strip()

# In testimonials script, update any reference to 'testimonials-hotmart' if needed:
# The section in Block A will be #social-proof, so we can do:
# var sec = document.getElementById('social-proof') || document.getElementById('testimonials-hotmart');
testimonials_script_html = testimonials_script_html.replace(
    "var sec = document.getElementById('testimonials-hotmart');",
    "var sec = document.getElementById('social-proof') || document.getElementById('testimonials-hotmart');"
)

# 3. Build NEW BLOCO B (antes do preço)
# Golden seam line before it + Dark background + New approved Title + WhatsApp Chat Stream
new_block_b = f'''<!-- SEÇÃO: Depoimentos WhatsApp (Bloco B) -->
  <!-- ══════════════════════════════════════════════════════════════════════════
       BLOCO B: PROVA SOCIAL WHATSAPP (P12)
       Prints originais em alta nitidez, layout conversacional e animação leve
       ══════════════════════════════════════════════════════════════════════════ -->
  <div class="testimonials-b-seam-line" id="blockBSeamLine" aria-hidden="true">
    <div class="seam-line-draw"></div>
  </div>

  <section id="testimonials-block-b" class="testimonials-whatsapp-block">
    <div class="testimonials-glow" aria-hidden="true"></div>

    <div class="container">
      <div class="testimonials-header-row">
        <h2 class="testimonials-title">VOCÊ NÃO VAI ACREDITAR NO QUE OS ALUNOS ESTÃO DIZENDO</h2>
      </div>

      {chat_stream_html}
    </div>
  </section>

  <script>
    /* ═════════════════════════════════════════════════════════════════════════
       SCRIPT: BLOCO B — PROVA SOCIAL WHATSAPP (P12)
       Linha de transição e entrada escalonada dos prints
       ═════════════════════════════════════════════════════════════════════════ */
    (function () {{
      var blockB = document.getElementById('testimonials-block-b');
      if (!blockB) return;

      var isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      var seamLine = document.getElementById('blockBSeamLine');
      var chatStream = document.getElementById('socialChatStream');

      if (isReducedMotion) {{
        if (seamLine) seamLine.classList.add('is-drawn');
        return;
      }}

      if (chatStream) chatStream.classList.add('js-animate-cards');

      // 1. Linha de transição dourada
      if (seamLine && 'IntersectionObserver' in window) {{
        var seamObs = new IntersectionObserver(function (entries, observer) {{
          entries.forEach(function (entry) {{
            if (entry.isIntersecting) {{
              seamLine.classList.add('is-drawn');
              observer.unobserve(entry.target);
            }}
          }});
        }}, {{ threshold: 0.2 }});
        seamObs.observe(seamLine);
      }} else if (seamLine) {{
        seamLine.classList.add('is-drawn');
      }}

      // 2. Entrada dos prints como mensagens de chat
      if (chatStream && 'IntersectionObserver' in window) {{
        var cards = Array.prototype.slice.call(chatStream.querySelectorAll('.chat-bubble-card'));
        var chatObs = new IntersectionObserver(function (entries, observer) {{
          entries.forEach(function (entry) {{
            if (entry.isIntersecting) {{
              cards.forEach(function (c, idx) {{
                setTimeout(function () {{
                  c.classList.add('is-arrived');
                }}, idx * 180);
              }});
              observer.unobserve(entry.target);
            }}
          }});
        }}, {{ threshold: 0.15 }});
        chatObs.observe(chatStream);
      }} else if (chatStream) {{
        var cardsFallback = chatStream.querySelectorAll('.chat-bubble-card');
        for (var j = 0; j < cardsFallback.length; j++) {{
          cardsFallback[j].classList.add('is-arrived');
        }}
      }}
    }})();
  </script>
'''

# 4. Build NEW BLOCO A (depois do preço)
# Golden seam line after price + Dark background + Original Title & Subtitle + 9 Text Testimonials
header_block_a = '''<div class="social-header-block">
        <h2 class="social-headline" id="socialHeadline">
          <span class="word-split">VOCÊ</span>
          <span class="word-split">ESTARÁ</span>
          <span class="word-split">A</span>
          <span class="word-split">FRENTE</span>
          <span class="word-split">DE</span>
          <span class="word-split">95%</span>
          <span class="word-split">DAS</span>
          <span class="word-split">PESSOAS</span>
        </h2>
        <p class="social-sub">
          Em 60 minutos você vai entender mais sobre estoicismo do que pessoas que "estudam" há anos.<br>
          <strong><em>(e você está a um clique disso)</em></strong>
        </p>
      </div>'''

new_block_a = f'''<div class="social-seam-line" id="socialSeamLine" aria-hidden="true">
    <div class="seam-line-draw"></div>
  </div>

  <section id="social-proof" class="testimonials-text-block">
    <div class="social-proof-glow" aria-hidden="true"></div>

    <div class="testimonials-container">
      {header_block_a}

      {testimonials_body_html}
  </section>

  {testimonials_script_html}
'''

# 5. Remove the duplicate script at line 7824
old_scr8_pattern = r'<script>\s*/\* ═════════════════════════════════════════════════════════════════════════\s*SCRIPT: DOBRA 8 — PROVA SOCIAL WHATSAPP[\s\S]*?</script>'
p12_clean = re.sub(old_scr8_pattern, '', p12)

# 6. Replace Block A first
pos8_start = p12_clean.find('<div class="social-seam-line" id="socialSeamLine"')
pos8_end = p12_clean.find('<!-- ═══════════════════════════════════\n       SEÇÃO: PARA QUEM É / NÃO É', pos8_start)

p12_step1 = p12_clean[:pos8_start] + new_block_a + p12_clean[pos8_end:]

# 7. Replace Block B
pos6_start = p12_step1.find('<!-- SEÇÃO: Depoimentos Hotmart -->')
pos6_end = p12_step1.find('<!-- ═══════════════════════════════════\n       SEÇÃO: PREÇO / CTA 1', pos6_start)

p12_step2 = p12_step1[:pos6_start] + new_block_b + p12_step1[pos6_end:]

# 8. Add CSS rules for Block B seam line and responsive enhancements
css_enhancement = '''
    /* ── BLOCO B (SEAM LINE & LAYOUT) ── */
    .testimonials-b-seam-line {
      position: relative;
      width: 100%;
      height: 2px;
      background: rgba(199, 158, 59, 0.15);
      overflow: hidden;
      z-index: 5;
    }

    .testimonials-b-seam-line .seam-line-draw {
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

    .testimonials-b-seam-line.is-drawn .seam-line-draw {
      transform: scaleX(1);
    }

    #testimonials-block-b {
      position: relative;
      background: #0E0E0E;
      padding: clamp(64px, 8vw, 110px) 0 clamp(72px, 9vw, 120px);
      overflow: hidden;
      width: 100%;
    }

    #testimonials-block-b .container {
      max-width: 1080px;
      margin: 0 auto;
      padding: 0 20px;
      position: relative;
      z-index: 2;
    }

    @media (min-width: 1120px) {
      .social-chat-stream {
        display: grid;
        grid-template-columns: repeat(3, 1fr) !important;
        max-width: 1120px !important;
        gap: 28px 28px !important;
      }

      .chat-bubble-card:nth-child(even) {
        margin-top: 0 !important;
      }

      .chat-bubble-card:nth-child(5) {
        grid-column: 2 / span 1 !important;
        max-width: 100% !important;
        margin-top: 0 !important;
      }
    }
'''

pos_style = p12_step2.find('</style>')
p12_final = p12_step2[:pos_style] + css_enhancement + p12_step2[pos_style:]

with open('p12/index.html', 'w', encoding='utf-8') as f:
    f.write(p12_final)

print("Successfully written updated p12/index.html! Total length:", len(p12_final))
