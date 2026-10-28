import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

# 1. Read the extracted blocks
with open('scratch/current_block_a.html', 'r', encoding='utf-8') as f:
    orig_a = f.read()

with open('scratch/current_block_b.html', 'r', encoding='utf-8') as f:
    orig_b = f.read()

print("Original Block A length:", len(orig_a))
print("Original Block B length:", len(orig_b))

# ── Extract the 5 WhatsApp prints from Block A ──
# <div class="social-chat-stream" id="socialChatStream"> ... </div>
m_chat = re.search(r'(<!-- Fluxo conversacional de prints WhatsApp -->[\s\S]*?<div class="social-chat-stream" id="socialChatStream">[\s\S]*?</div>\s*</div>)', orig_a)
if not m_chat:
    print("ERROR: could not find social-chat-stream in Block A")
    sys.exit(1)

chat_stream_html = m_chat.group(1)

# Ensure Print 1 also has loading="lazy"
chat_stream_html = chat_stream_html.replace(
    'width="400" height="400" decoding="async">',
    'width="400" height="400" loading="lazy" decoding="async">'
)

# ── Extract the 9 testimonials content from Block B ──
# Destaques, Interactive Wrapper, Controls, Modal
# Starts at <!-- ── A) DESTAQUES: 3 DEPOIMENTOS COMPLETOS SEMPRE ABERTOS (9, 2, 4) ── -->
m_test = re.search(r'(<!-- ── A\) DESTAQUES:[\s\S]*?</div>\s*<!-- ── MODAL FLUTUANTE DE LEITURA COMPLETA[\s\S]*?</div>\s*</div>)', orig_b)
if not m_test:
    print("ERROR: could not find testimonials content in Block B")
    sys.exit(1)

testimonials_content_html = m_test.group(1)

# Also extract the script from Block B
m_script_b = re.search(r'(<script>[\s\S]*?SCRIPT: DOBRA 6 — DEPOIMENTOS DA PLATAFORMA[\s\S]*?</script>)', orig_b)
if not m_script_b:
    print("ERROR: could not find script in Block B")
    sys.exit(1)

orig_script_testimonials = m_script_b.group(1)

# ── Build NEW BLOCK B (Antes do Preço) ──
# - Seam line na emenda com o bloco anterior (#bonus)
# - Fundo escuro
# - Título: "VOCÊ NÃO VAI ACREDITAR NO QUE OS ALUNOS ESTÃO DIZENDO" (Barlow 900, uppercase, dourado)
# - Os 6 prints de WhatsApp (com layout aprovado, 1x e 2x webp, lazy loading em todos)
new_block_b = '''  <!-- ══════════════════════════════════════════════════════════════════════════
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

      ''' + chat_stream_html + '''
  </section>

  <script>
    /* ═════════════════════════════════════════════════════════════════════════
       SCRIPT: BLOCO B — PROVA SOCIAL WHATSAPP (P12)
       Linha de transição e entrada escalonada dos prints
       ═════════════════════════════════════════════════════════════════════════ */
    (function () {
      var blockB = document.getElementById('testimonials-block-b');
      if (!blockB) return;

      var isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      var seamLine = document.getElementById('blockBSeamLine');
      var chatStream = document.getElementById('socialChatStream');

      if (isReducedMotion) {
        if (seamLine) seamLine.classList.add('is-drawn');
        return;
      }

      if (chatStream) chatStream.classList.add('js-animate-cards');

      // 1. Linha de transição dourada
      if (seamLine && 'IntersectionObserver' in window) {
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
      }

      // 2. Entrada dos prints como mensagens de chat
      if (chatStream && 'IntersectionObserver' in window) {
        var cards = Array.prototype.slice.call(chatStream.querySelectorAll('.chat-bubble-card'));
        var chatObs = new IntersectionObserver(function (entries, observer) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              cards.forEach(function (c, idx) {
                setTimeout(function () {
                  c.classList.add('is-arrived');
                }, idx * 180);
              });
              observer.unobserve(entry.target);
            }
          });
        }, { threshold: 0.15 });
        chatObs.observe(chatStream);
      } else if (chatStream) {
        var cardsFallback = chatStream.querySelectorAll('.chat-bubble-card');
        for (var j = 0; j < cardsFallback.length; j++) {
          cardsFallback[j].classList.add('is-arrived');
        }
      }
    })();
  </script>
'''

# ── Build NEW BLOCK A (Depois do Preço) ──
# - Seam line na emenda com o cartão de preço
# - Fundo escuro
# - Título: "VOCÊ ESTARÁ A FRENTE DE 95% DAS PESSOAS" (Barlow 900, uppercase, dourado)
# - Subtítulo: "Em 60 minutos você vai entender mais..." + "(e você está a um clique disso)"
# - Os 9 depoimentos em texto (3 destaques, swipe mobile, marquee desktop, modal)
new_block_a = '''  <!-- ══════════════════════════════════════════════════════════════════════════
       BLOCO A: DEPOIMENTOS DA PLATAFORMA DA SÉRIE (P12)
       Título e Subtítulo originais + 9 Depoimentos em texto completos
       ══════════════════════════════════════════════════════════════════════════ -->
  <div class="social-seam-line" id="socialSeamLine" aria-hidden="true">
    <div class="seam-line-draw"></div>
  </div>

  <section id="social-proof" class="testimonials-text-block">
    <div class="social-proof-glow" aria-hidden="true"></div>

    <div class="testimonials-container">
      <div class="social-header-block">
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
      </div>

      ''' + testimonials_content_html + '''
  </section>

  <script>
    /* ═════════════════════════════════════════════════════════════════════════
       SCRIPT: BLOCO A — 9 DEPOIMENTOS DA PLATAFORMA (P12)
       Linha de transição, título palavra por palavra, destaques, faixas e modal
       ═════════════════════════════════════════════════════════════════════════ */
    (function () {
      var MARQUEE_LOOP_DURATION = 75; // 75 segundos por volta completa

      var sec = document.getElementById('social-proof');
      if (!sec) return;

      var isReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      sec.style.setProperty('--marquee-speed', MARQUEE_LOOP_DURATION + 's');

      var seamLine = document.getElementById('socialSeamLine');
      var headline = document.getElementById('socialHeadline');

      // 1. Linha de transição dourada
      if (seamLine && 'IntersectionObserver' in window) {
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
      }

      // 2. Título palavra por palavra
      if (headline && !isReducedMotion && 'IntersectionObserver' in window) {
        var headerBlock = sec.querySelector('.social-header-block');
        if (headerBlock) headerBlock.classList.add('js-animate-title');
        var words = Array.prototype.slice.call(headline.querySelectorAll('.word-split'));
        var headlineObs = new IntersectionObserver(function (entries, observer) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              words.forEach(function (w, idx) {
                setTimeout(function () {
                  w.classList.add('is-visible');
                }, idx * 75);
              });
              observer.unobserve(entry.target);
            }
          });
        }, { threshold: 0.25 });
        headlineObs.observe(headline);
      } else if (headline) {
        var wordsFallback = headline.querySelectorAll('.word-split');
        for (var i = 0; i < wordsFallback.length; i++) {
          wordsFallback[i].classList.add('is-visible');
        }
      }

      // 3. Revelação Suave dos 3 Destaques
      var highlightCards = Array.prototype.slice.call(sec.querySelectorAll('.t-highlight-card'));
      if (isReducedMotion) {
        highlightCards.forEach(function (c) { c.classList.add('is-revealed'); });
      } else if ('IntersectionObserver' in window) {
        var hObserver = new IntersectionObserver(function (entries, observer) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              highlightCards.forEach(function (c, idx) {
                setTimeout(function () { c.classList.add('is-revealed'); }, idx * 140);
              });
              observer.unobserve(entry.target);
            }
          });
        }, { threshold: 0.15 });
        hObserver.observe(sec);
      } else {
        highlightCards.forEach(function (c) { c.classList.add('is-revealed'); });
      }

      // 4. Mobile Swipe: Atualização dos Pontinhos Indicadores
      var swipeTrack = document.getElementById('mobileSwipeTrack');
      var dots = Array.prototype.slice.call(document.querySelectorAll('.swipe-dot'));
      if (swipeTrack && dots.length > 0) {
        var swipeCards = Array.prototype.slice.call(swipeTrack.querySelectorAll('.t-swipe-card'));
        var scrollTimeout = null;
        swipeTrack.addEventListener('scroll', function () {
          if (scrollTimeout) clearTimeout(scrollTimeout);
          scrollTimeout = setTimeout(function () {
            var trackScroll = swipeTrack.scrollLeft;
            var trackWidth = swipeTrack.offsetWidth;
            var bestIdx = 0;
            var bestDiff = Infinity;
            swipeCards.forEach(function (card, idx) {
              var cardCenter = card.offsetLeft + card.offsetWidth / 2;
              var viewCenter = trackScroll + trackWidth / 2;
              var diff = Math.abs(cardCenter - viewCenter);
              if (diff < bestDiff) {
                bestDiff = diff;
                bestIdx = idx;
              }
            });
            dots.forEach(function (d, i) {
              if (i === bestIdx) d.classList.add('is-active');
              else d.classList.remove('is-active');
            });
          }, 40);
        }, { passive: true });
      }

      // 5. Botão de Pausa Desktop (só ícone)
      var pauseBtn = document.getElementById('marqueePauseBtn');
      var isPausedManual = false;
      if (pauseBtn) {
        var pauseIcon = pauseBtn.querySelector('.pause-icon');
        var playIcon = pauseBtn.querySelector('.play-icon');
        function updatePauseState(paused) {
          if (paused) {
            sec.classList.add('is-paused');
            pauseBtn.classList.add('is-paused');
            pauseBtn.setAttribute('aria-label', 'Retomar animação dos depoimentos');
            pauseBtn.setAttribute('title', 'Retomar animação');
            if (pauseIcon) pauseIcon.style.display = 'none';
            if (playIcon) playIcon.style.display = 'block';
          } else {
            sec.classList.remove('is-paused');
            pauseBtn.classList.remove('is-paused');
            pauseBtn.setAttribute('aria-label', 'Pausar animação dos depoimentos');
            pauseBtn.setAttribute('title', 'Pausar animação');
            if (pauseIcon) pauseIcon.style.display = 'block';
            if (playIcon) playIcon.style.display = 'none';
          }
        }
        pauseBtn.addEventListener('click', function () {
          isPausedManual = !isPausedManual;
          updatePauseState(isPausedManual);
        });
      }

      // 6. Pausa Automática quando a seção sai da tela
      if ('IntersectionObserver' in window && !isReducedMotion) {
        var marqueeVisibilityObs = new IntersectionObserver(function (entries) {
          entries.forEach(function (entry) {
            if (!entry.isIntersecting) {
              sec.classList.add('is-offscreen');
            } else {
              sec.classList.remove('is-offscreen');
            }
          });
        }, { threshold: 0.05 });
        marqueeVisibilityObs.observe(sec);
      }

      // 7. Modal de Leitura Completa
      var modal = document.getElementById('testimonialsModal');
      var modalContent = document.getElementById('modalContent');
      var modalClose = document.getElementById('modalCloseBtn');
      var lastFocusedEl = null;

      function openModal(card) {
        if (!modal || !modalContent) return;
        lastFocusedEl = document.activeElement;
        modalContent.innerHTML = '';
        var clone = card.cloneNode(true);
        clone.classList.remove('is-collapsed', 't-highlight-card', 't-swipe-card', 't-marquee-card');
        clone.classList.add('is-expanded');
        var readMoreBtn = clone.querySelector('.t-read-more');
        if (readMoreBtn) readMoreBtn.remove();
        modalContent.appendChild(clone);
        modal.classList.add('is-open');
        modal.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
        if (modalClose) modalClose.focus();
      }

      function closeModal() {
        if (!modal) return;
        modal.classList.remove('is-open');
        modal.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
        if (lastFocusedEl && typeof lastFocusedEl.focus === 'function') {
          lastFocusedEl.focus();
        }
      }

      if (modalClose) {
        modalClose.addEventListener('click', closeModal);
      }
      if (modal) {
        modal.addEventListener('click', function (e) {
          if (e.target === modal) closeModal();
        });
      }
      window.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && modal && modal.classList.contains('is-open')) {
          closeModal();
        }
      });

      // Abre modal ao clicar em cards cortados
      sec.addEventListener('click', function (e) {
        var readMore = e.target.closest('.t-read-more');
        if (readMore) {
          var card = readMore.closest('.t-card');
          if (card) {
            e.preventDefault();
            openModal(card);
          }
        }
      });
    })();
  </script>
'''

# Remove old script at lines 7824-7909 (since script is now self-contained in Block A and Block B)
# Find the old script in content
old_scr8_pattern = r'<script>\s*/\* ═════════════════════════════════════════════════════════════════════════\s*SCRIPT: DOBRA 8 — PROVA SOCIAL WHATSAPP[\s\S]*?</script>'
m_old_scr = re.search(old_scr8_pattern, p12)
if m_old_scr:
    print("Found old Dobra 8 script at the bottom. Will remove to avoid duplicate listeners.")
    p12 = p12[:m_old_scr.start()] + p12[m_old_scr.end():]
else:
    print("WARNING: Could not find old Dobra 8 script pattern.")

# Now replace Block B and Block A in p12
pos6_start = p12.find('<!-- SEÇÃO: Depoimentos Hotmart -->')
pos6_end = p12.find('<!-- ═══════════════════════════════════\n       SEÇÃO: PREÇO / CTA 1', pos6_start)

pos8_start = p12.find('<div class="social-seam-line" id="socialSeamLine"')
pos8_end = p12.find('<!-- ═══════════════════════════════════\n       SEÇÃO: PARA QUEM É / NÃO É', pos8_start)

# Replace Block A first (since it is further down, so indices for Block B remain valid)
p12_updated = p12[:pos8_start] + new_block_a + p12[pos8_end:]

# Now find Block B again in p12_updated
pos6_start = p12_updated.find('<!-- SEÇÃO: Depoimentos Hotmart -->')
pos6_end = p12_updated.find('<!-- ═══════════════════════════════════\n       SEÇÃO: PREÇO / CTA 1', pos6_start)

p12_final = p12_updated[:pos6_start] + new_block_b + p12_updated[pos6_end:]

# Also update CSS for .testimonials-b-seam-line and #testimonials-block-b
css_additions = '''
    /* Bloco B Seam Line e Container */
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

# Insert CSS additions right before </style>
pos_style_close = p12_final.find('</style>')
if pos_style_close != -1:
    p12_final = p12_final[:pos_style_close] + css_additions + p12_final[pos_style_close:]

# Write to test file first
with open('scratch/test_swap.html', 'w', encoding='utf-8') as f:
    f.write(p12_final)

print("Generated scratch/test_swap.html successfully! Length:", len(p12_final))
