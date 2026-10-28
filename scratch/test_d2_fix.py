import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

# 1. Update the CSS for Dobra 2
css_d2_replacement = '''
    /* ── Seção Dor / Ciclo (P12 - Dobra 2) ── */
    #pain {
      position: relative;
      background: #030303;
      padding: clamp(64px, 8vw, 108px) 0;
      overflow: hidden;
      width: 100%;
    }

    /* Brilho bem leve cor de brasa atrás dos cards */
    .pain-glow {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 100%;
      max-width: 900px;
      height: 700px;
      background: radial-gradient(ellipse at center, rgba(212, 114, 28, 0.12) 0%, rgba(180, 70, 10, 0.04) 50%, rgba(3, 3, 3, 0) 75%);
      pointer-events: none;
      z-index: 1;
    }

    .pain-container {
      position: relative;
      z-index: 2;
      width: 100%;
      max-width: 740px;
      margin: 0 auto;
      padding: 0 20px;
    }

    /* Título em fonte forte sem serifa (Barlow) */
    .pain-title {
      font-family: var(--font-heading);
      font-size: clamp(23px, 3.8vw, 36px);
      font-weight: 700;
      color: #FFFFFF;
      text-align: center;
      line-height: 1.28;
      letter-spacing: -0.01em;
      margin: 0 auto clamp(36px, 5vw, 56px);
      max-width: 660px;
      text-wrap: balance;
    }

    /* Wrapper com trilha da timeline e o ciclo infinito */
    .pain-timeline-wrapper {
      position: relative;
      --timeline-pad: 56px;
      --timeline-axis: 34px;
      --node-radius: 11px;
      padding-left: var(--timeline-pad);
    }

    /* Container SVG da timeline e ciclo perfeitamente alinhado */
    .pain-cycle-svg {
      position: absolute;
      left: 0;
      top: 0;
      width: var(--timeline-pad);
      height: 100%;
      overflow: visible;
      pointer-events: none;
      z-index: 1;
    }

    /* Trilha descendente base (dim) */
    .svg-track {
      stroke: rgba(199, 158, 59, 0.22);
      stroke-width: 2;
      stroke-linecap: round;
    }

    /* Preenchimento ativo descendente */
    .svg-fill {
      stroke: #FFC107;
      stroke-width: 2.5;
      stroke-linecap: round;
      filter: drop-shadow(0 0 8px rgba(255, 193, 7, 0.8));
      transition: stroke-dashoffset 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* Linha de retorno do ciclo (curva embaixo do card 6, sobe e conecta no card 1) */
    .svg-loop-line {
      stroke: rgba(199, 158, 59, 0.32);
      stroke-width: 2;
      stroke-linecap: round;
      stroke-linejoin: round;
      transition: stroke 0.6s ease, filter 0.6s ease;
    }

    .svg-loop-arrow {
      fill: rgba(199, 158, 59, 0.45);
      transition: fill 0.6s ease, filter 0.6s ease;
    }

    .pain-timeline-wrapper.cycle-closed .svg-loop-line {
      stroke: #FFC107;
      stroke-dasharray: 6 5;
      filter: drop-shadow(0 0 6px rgba(255, 193, 7, 0.75));
      animation: loopFlow 1.6s linear infinite;
    }

    .pain-timeline-wrapper.cycle-closed .svg-loop-arrow {
      fill: #FFC107;
      filter: drop-shadow(0 0 8px #FFC107);
    }

    @keyframes loopFlow {
      0% {
        stroke-dashoffset: 0;
      }
      100% {
        stroke-dashoffset: -22;
      }
    }

    /* Lista de cards */
    .pain-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 16px;
      margin: 0;
      padding: 0;
    }

    /* Card escuro */
    .pain-card {
      position: relative;
      display: flex;
      align-items: center;
      width: 100%;
    }

    /* ── BOLINHA PERTENCENTE AO PRÓPRIO CARD (CENTRO VERTICAL EXATO) ── */
    .pain-node-anchor {
      position: absolute;
      left: calc(-1 * var(--timeline-pad));
      top: 50%;
      transform: translateY(-50%);
      width: var(--timeline-pad);
      height: 32px;
      pointer-events: none;
      z-index: 3;
    }

    /* O conector horizontal que vai da bolinha até a borda do card */
    .pain-node-connector {
      position: absolute;
      left: var(--timeline-axis);
      right: 0;
      top: 50%;
      height: 2px;
      transform: translateY(-50%);
      background: rgba(199, 158, 59, 0.3);
      transition: background 0.4s ease, box-shadow 0.4s ease;
    }

    .pain-card.is-visible .pain-node-connector {
      background: #FFC107;
      box-shadow: 0 0 6px rgba(255, 193, 7, 0.9);
    }

    /* A bolinha (nó luminoso) perfeitamente centrada no eixo da timeline */
    .pain-node-bullet {
      position: absolute;
      left: var(--timeline-axis);
      top: 50%;
      transform: translate(-50%, -50%);
      width: calc(var(--node-radius) * 2);
      height: calc(var(--node-radius) * 2);
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .bullet-halo {
      position: absolute;
      width: calc(var(--node-radius) * 2 + 8px);
      height: calc(var(--node-radius) * 2 + 8px);
      border-radius: 50%;
      border: 1.5px solid transparent;
      transition: border-color 0.35s ease;
    }

    .pain-card.is-visible .bullet-halo {
      border-color: rgba(255, 193, 7, 0.35);
    }

    .bullet-bg {
      position: absolute;
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background: #12100E;
      border: 1.8px solid rgba(199, 158, 59, 0.45);
      transition: background 0.35s ease, border-color 0.35s ease, box-shadow 0.35s ease;
    }

    .pain-card.is-visible .bullet-bg {
      background: #1A160E;
      border-color: #FFC107;
      box-shadow: 0 0 8px rgba(255, 193, 7, 0.6);
    }

    .bullet-core {
      position: relative;
      z-index: 2;
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: rgba(199, 158, 59, 0.45);
      transition: background 0.35s ease, box-shadow 0.35s ease, transform 0.35s ease;
    }

    .pain-card.is-visible .bullet-core {
      background: #FFC107;
      box-shadow: 0 0 6px #FFC107;
      transform: scale(1.15);
    }

    /* Interior do card escuro com borda fina dourada e cantos pouco arredondados */
    .pain-card-inner {
      display: flex;
      align-items: center;
      gap: 16px;
      width: 100%;
      padding: 20px 22px;
      background: linear-gradient(145deg, #12100E 0%, #0A0908 100%);
      border: 1px solid rgba(199, 158, 59, 0.22);
      border-radius: 8px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
      transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

    .pain-card:hover .pain-card-inner {
      border-color: rgba(235, 192, 104, 0.55);
      box-shadow: 0 6px 24px rgba(0, 0, 0, 0.6), 0 0 16px rgba(212, 114, 28, 0.16);
    }

    .pain-card.is-visible .pain-card-inner {
      border-color: rgba(199, 158, 59, 0.35);
    }

    /* Ícone em SVG linear com traço e tamanho dourado idêntico */
    .pain-icon-wrap {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 40px;
      height: 40px;
      flex-shrink: 0;
      color: #FFC107;
    }

    .pain-icon {
      width: 22px;
      height: 22px;
      display: block;
    }

    /* Texto do card: sem serifa, >= 16px, bom espaçamento entre linhas */
    .pain-text {
      font-family: var(--font-body);
      font-size: 16px;
      font-weight: 400;
      color: #F5F0E8;
      line-height: 1.55;
    }

    /* Destaque dourado com efeito de revelação da esquerda para a direita */
    .pain-highlight {
      color: #FFC107;
      font-weight: 700;
      position: relative;
      display: inline;
      background: linear-gradient(90deg, #FFC107 0%, #FFE082 50%, #FFC107 100%);
      background-size: 200% 100%;
      background-position: 100% 0;
      -webkit-background-clip: text;
      -webkit-text-fill-color: #FFC107;
      transition: background-position 0.9s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* Animações via IntersectionObserver (Progressive Enhancement) */
    .pain-animated .pain-card {
      opacity: 0;
      transform: translateY(22px);
      transition: opacity 0.55s cubic-bezier(0.16, 1, 0.3, 1), transform 0.55s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .pain-animated .pain-card.is-visible {
      opacity: 1;
      transform: translateY(0);
    }

    .pain-animated .pain-card.is-visible .pain-highlight {
      background-position: 0% 0;
      -webkit-text-fill-color: transparent;
      animation: highlightShimmer 1.8s ease-out 1;
    }

    @keyframes highlightShimmer {
      0% {
        filter: drop-shadow(0 0 0px transparent);
      }
      50% {
        filter: drop-shadow(0 0 8px rgba(255, 193, 7, 0.7));
      }
      100% {
        filter: drop-shadow(0 0 0px transparent);
      }
    }

    /* Preferência de redução de movimento */
    @media (prefers-reduced-motion: reduce) {
      .pain-card,
      .pain-animated .pain-card {
        opacity: 1 !important;
        transform: none !important;
        transition: none !important;
      }
      .pain-highlight {
        animation: none !important;
        -webkit-text-fill-color: #FFC107 !important;
      }
    }

    /* Mobile First Breakpoints (360px, 390px, 768px) */
    @media (max-width: 480px) {
      .pain-container {
        padding: 0 14px;
      }

      .pain-timeline-wrapper {
        --timeline-pad: 46px;
        --timeline-axis: 26px;
        --node-radius: 10px;
        padding-left: var(--timeline-pad);
      }

      .pain-card-inner {
        padding: 16px 14px;
        gap: 12px;
      }

      .pain-icon-wrap {
        width: 36px;
        height: 36px;
      }

      .pain-icon {
        width: 20px;
        height: 20px;
      }

      .pain-text {
        font-size: 16px;
        line-height: 1.5;
      }
    }

    @media (max-width: 360px) {
      .pain-container {
        padding: 0 10px;
      }

      .pain-timeline-wrapper {
        --timeline-pad: 40px;
        --timeline-axis: 22px;
        --node-radius: 9px;
        padding-left: var(--timeline-pad);
      }

      .pain-card-inner {
        padding: 14px 12px;
        gap: 10px;
      }
    }
'''

# Find original CSS for pain: from line 409 to before DOBRA 3
pos_css_start = p12.find('/* ── Seção Dor / Ciclo (P12 - Dobra 2) ── */')
pos_css_end = p12.find('/* ══════════════════════════════════════════════════════════════════════════\n   DOBRA 3: ERROS', pos_css_start)

# 2. Update HTML of cards: inject .pain-node-anchor in each .pain-card
node_html = '''            <div class="pain-node-anchor" aria-hidden="true">
              <div class="pain-node-connector"></div>
              <div class="pain-node-bullet">
                <span class="bullet-halo"></span>
                <span class="bullet-bg"></span>
                <span class="bullet-core"></span>
              </div>
            </div>
'''

pos_html_start = p12.find('<section id="pain">')
pos_html_end = p12.find('<!-- ═══════════════════════════════════\n       SEÇÃO: ERROS', pos_html_start)

pain_section_html = p12[pos_html_start:pos_html_end]

# In pain_section_html, clean SVG of branches and nodes groups (now rendered directly on each card)
pain_section_html = re.sub(r'<g id="svg-branches-group"></g>\s*<g id="svg-nodes-group"></g>', '', pain_section_html)

# Add node_html before <div class="pain-card-inner">
def add_anchor_to_card(m):
    return m.group(1) + '\n' + node_html + m.group(2)

pain_section_html = re.sub(
    r'(<li class="pain-card"[^>]*>)\s*(<div class="pain-card-inner">)',
    add_anchor_to_card,
    pain_section_html
)

# 3. Update the script of Dobra 2
script_d2_replacement = '''  <!-- Script da Dobra 2: Conexão Geométrica Exata da Timeline e Ciclo -->
  <script>
    (function () {
      var painSection = document.getElementById('pain');
      if (!painSection) return;

      var wrapper = painSection.querySelector('.pain-timeline-wrapper');
      var svg = painSection.querySelector('.pain-cycle-svg');
      var trackPath = document.getElementById('svg-descent-track');
      var fillPath = document.getElementById('svg-descent-fill');
      var loopPath = document.getElementById('svg-loop-path');
      var loopArrow = document.getElementById('svg-loop-arrow');
      var cards = Array.prototype.slice.call(painSection.querySelectorAll('.pain-card'));
      if (!cards.length || !wrapper || !svg) return;

      painSection.classList.add('pain-animated');

      var visibleIndexes = new Set();
      var cachedYCoords = [];
      var currentXMain = 34;
      var currentNodeRadius = 11;

      // Mede a posição vertical exata (estática) do centro de cada card/bolinha
      function getCardCenterY(card) {
        return card.offsetTop + (card.offsetHeight / 2);
      }

      function updateLayoutGeometry() {
        var isSmallMobile = window.innerWidth <= 360;
        var isMobile = window.innerWidth <= 480;

        currentXMain = isSmallMobile ? 22 : (isMobile ? 26 : 34);
        var xReturn = isSmallMobile ? 6 : (isMobile ? 8 : 12);
        currentNodeRadius = isSmallMobile ? 9 : (isMobile ? 10 : 11);
        var rArc = (currentXMain - xReturn) / 2;
        var totalH = wrapper.offsetHeight;

        svg.setAttribute('viewBox', '0 0 ' + (currentXMain + 10) + ' ' + totalH);
        svg.style.height = totalH + 'px';

        // 1. Calcula o centro Y exato de cada bolinha/card relativo ao wrapper
        cachedYCoords = cards.map(function (card) {
          return getCardCenterY(card);
        });

        if (cachedYCoords.length < 2) return;

        var y1 = cachedYCoords[0];
        var y6 = cachedYCoords[cachedYCoords.length - 1];
        var loopPad = isMobile ? 14 : 18;

        // 2. Trilha descendente base (passa exatamente pelo centro da bolinha 1 até a bolinha 6)
        if (trackPath) {
          trackPath.setAttribute('d', 'M ' + currentXMain + ',' + y1 + ' L ' + currentXMain + ',' + y6);
        }

        // 3. Linha do Ciclo (Loop de Retorno fechando da última bolinha à primeira)
        if (loopPath) {
          var bottomCurveY = y6 + currentNodeRadius + loopPad;
          var topCurveY = y1 - currentNodeRadius - loopPad;
          var arrowStopY = y1 - currentNodeRadius - 7;

          var dLoop = 'M ' + currentXMain + ',' + (y6 + currentNodeRadius) + ' ' +
                      'L ' + currentXMain + ',' + bottomCurveY + ' ' +
                      'A ' + rArc + ' ' + rArc + ' 0 0 1 ' + xReturn + ',' + bottomCurveY + ' ' +
                      'L ' + xReturn + ',' + topCurveY + ' ' +
                      'A ' + rArc + ' ' + rArc + ' 0 0 1 ' + currentXMain + ',' + topCurveY + ' ' +
                      'L ' + currentXMain + ',' + arrowStopY;
          loopPath.setAttribute('d', dLoop);
        }

        // 4. Seta conectando perfeitamente a descida no topo da Bolinha 1
        if (loopArrow) {
          var tipY = y1 - currentNodeRadius - 1;
          var baseY = y1 - currentNodeRadius - 7;
          var pts = currentXMain + ',' + tipY + ' ' +
                    (currentXMain - 4.5) + ',' + baseY + ' ' +
                    (currentXMain + 4.5) + ',' + baseY;
          loopArrow.setAttribute('points', pts);
        }

        updateFillTrack();
      }

      function updateFillTrack() {
        if (!fillPath || !cachedYCoords.length) return;
        var y1 = cachedYCoords[0];
        var maxVisibleIdx = -1;
        visibleIndexes.forEach(function (idx) {
          if (idx > maxVisibleIdx) maxVisibleIdx = idx;
        });

        if (maxVisibleIdx >= 0) {
          var targetY = cachedYCoords[maxVisibleIdx];
          fillPath.setAttribute('d', 'M ' + currentXMain + ',' + y1 + ' L ' + currentXMain + ',' + targetY);
        } else {
          fillPath.setAttribute('d', '');
        }

        if (visibleIndexes.size === cards.length) {
          wrapper.classList.add('cycle-closed');
        }
      }

      // Eventos de recalculo: fonts.ready, resize, orientationchange e ResizeObserver nos cards
      if (document.fonts && document.fonts.ready) {
        document.fonts.ready.then(updateLayoutGeometry);
      }
      window.addEventListener('load', updateLayoutGeometry);
      window.addEventListener('orientationchange', function () {
        setTimeout(updateLayoutGeometry, 100);
      });

      var resizeTimer;
      window.addEventListener('resize', function () {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function () {
          requestAnimationFrame(updateLayoutGeometry);
        }, 60);
      });

      // ResizeObserver monitora mudanças de altura nos cards sem recalcular em frames de scroll
      if ('ResizeObserver' in window) {
        var ro = new ResizeObserver(function () {
          updateLayoutGeometry();
        });
        cards.forEach(function (card) { ro.observe(card); });
      }

      requestAnimationFrame(updateLayoutGeometry);

      // Redução de movimento
      if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        cards.forEach(function (card, i) {
          card.classList.add('is-visible');
          visibleIndexes.add(i);
        });
        wrapper.classList.add('cycle-closed');
        requestAnimationFrame(updateLayoutGeometry);
        return;
      }

      // IntersectionObserver para ativar cada card e preencher a trilha
      if ('IntersectionObserver' in window) {
        var observer = new IntersectionObserver(function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              var card = entry.target;
              var index = parseInt(card.getAttribute('data-index'), 10);
              card.classList.add('is-visible');
              visibleIndexes.add(index);
              updateFillTrack();
              observer.unobserve(card);
            }
          });
        }, {
          threshold: 0.15,
          rootMargin: '0px 0px -40px 0px'
        });

        cards.forEach(function (card) {
          observer.observe(card);
        });
      } else {
        cards.forEach(function (card, i) {
          card.classList.add('is-visible');
          visibleIndexes.add(i);
        });
        updateFillTrack();
      }
    })();
  </script>
'''

# Find original script of Dobra 2 in pain_section_html
pos_scr_start = pain_section_html.find('<!-- Script da Dobra 2: Conexão Geométrica Exata da Timeline e Ciclo -->')
if pos_scr_start != -1:
    pain_section_html = pain_section_html[:pos_scr_start] + script_d2_replacement

# Replace in p12
# First replace section HTML
p12_step1 = p12[:pos_html_start] + pain_section_html + p12[pos_html_end:]

# Then replace CSS
pos_css_start = p12_step1.find('/* ── Seção Dor / Ciclo (P12 - Dobra 2) ── */')
pos_css_end = p12_step1.find('/* ══════════════════════════════════════════════════════════════════════════\n   DOBRA 3: ERROS', pos_css_start)

p12_final = p12_step1[:pos_css_start] + css_d2_replacement + p12_step1[pos_css_end:]

with open('scratch/test_d2_fix.html', 'w', encoding='utf-8') as f:
    f.write(p12_final)

print("Saved scratch/test_d2_fix.html successfully! Length:", len(p12_final))
