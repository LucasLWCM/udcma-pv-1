const fs = require('fs');

const p12 = fs.readFileSync('p12/index.html', 'utf8');

// 1. New CSS
const newCss = `/* ── Seção Dor / Ciclo (P12 - Dobra 2) ── */
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

    /* Título em fonte serifada (Cormorant Garamond) */
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
      --return-axis: 12px;
      padding-left: var(--timeline-pad);
    }

    /* Linha base CSS estática (fallback sem JavaScript) */
    .pain-timeline-wrapper::before {
      content: '';
      position: absolute;
      left: var(--timeline-axis);
      top: 35px;
      bottom: 35px;
      width: 2px;
      transform: translateX(-50%);
      background: rgba(199, 158, 59, 0.22);
      pointer-events: none;
      z-index: 1;
    }

    .pain-animated .pain-timeline-wrapper::before {
      display: none;
    }

    /* Container SVG da timeline e ciclo desenhado dinamicamente */
    .pain-cycle-svg {
      position: absolute;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      overflow: visible;
      pointer-events: none;
      z-index: 2;
    }

    /* Trilha descendente base (dim) */
    .svg-track {
      stroke: rgba(199, 158, 59, 0.22);
      stroke-width: 2;
      stroke-linecap: round;
    }

    /* Preenchimento ativo descendente (ilumina conforme os cards entram) */
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

    /* Quando o ciclo fecha (último card visível) */
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

    /* Âncora da bolinha: pertence ao card, posicionada a 50% de sua altura exata */
    .pain-node-anchor {
      position: absolute;
      left: calc(-1 * var(--timeline-pad));
      width: var(--timeline-pad);
      top: 50%;
      transform: translateY(-50%);
      height: 32px;
      pointer-events: none;
      z-index: 3;
    }

    /* Ramo horizontal conectando o centro da bolinha à borda esquerda do card */
    .pain-node-connector {
      position: absolute;
      left: var(--timeline-axis);
      right: 0;
      top: 50%;
      height: 2px;
      transform: translateY(-50%);
      background: rgba(199, 158, 59, 0.3);
      border-radius: 1px;
      transition: background-color 0.4s ease, box-shadow 0.4s ease;
    }

    .pain-card.is-visible .pain-node-connector {
      background: #FFC107;
      box-shadow: 0 0 6px rgba(255, 193, 7, 0.9);
    }

    /* Bolinha luminosa pertencente ao próprio card */
    .pain-node-bullet {
      position: absolute;
      left: var(--timeline-axis);
      top: 50%;
      transform: translate(-50%, -50%);
      width: 32px;
      height: 32px;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .pain-bullet-svg {
      width: 100%;
      height: 100%;
      overflow: visible;
    }

    /* Camadas da bolinha: halo, fundo e núcleo */
    .svg-node-halo {
      fill: none;
      stroke: transparent;
      stroke-width: 1.5;
      transition: stroke 0.35s ease;
    }

    .svg-node-bg {
      fill: #12100E;
      stroke: rgba(199, 158, 59, 0.45);
      stroke-width: 1.8;
      transition: fill 0.35s ease, stroke 0.35s ease, filter 0.35s ease;
    }

    .svg-node-core {
      fill: rgba(199, 158, 59, 0.45);
      transition: fill 0.35s ease, filter 0.35s ease, r 0.35s ease;
    }

    .pain-card.is-visible .svg-node-bg {
      fill: #1A160E;
      stroke: #FFC107;
      filter: drop-shadow(0 0 6px rgba(255, 193, 7, 0.6));
    }

    .pain-card.is-visible .svg-node-core {
      fill: #FFC107;
      filter: drop-shadow(0 0 6px #FFC107);
      r: 4.5;
    }

    .pain-card.is-visible .svg-node-halo {
      stroke: rgba(255, 193, 7, 0.35);
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
      border-radius: 6px;
      background: rgba(235, 192, 104, 0.08);
      border: 1px solid rgba(235, 192, 104, 0.2);
      color: #EBC068;
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
    /* Por padrão (se JS falhar), tudo já está 100% visível! */
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
      .pain-line-fill {
        transform: scaleY(1) !important;
        transition: none !important;
      }
      .pain-highlight {
        animation: none !important;
        -webkit-text-fill-color: #FFC107 !important;
      }
      .pain-timeline-wrapper.cycle-closed .svg-loop-line {
        animation: none !important;
      }
    }

    /* Mobile First Breakpoints (360px, 390px, 768px) */
    @media (max-width: 480px) {
      .pain-container {
        padding: 0 14px;
      }

      .pain-timeline-wrapper {
        --timeline-pad: 42px;
        --timeline-axis: 26px;
        --node-radius: 10px;
        --return-axis: 8px;
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
        --timeline-pad: 36px;
        --timeline-axis: 22px;
        --node-radius: 9px;
        --return-axis: 6px;
        padding-left: var(--timeline-pad);
      }

      .pain-card-inner {
        padding: 14px 12px;
        gap: 10px;
      }

      .pain-text {
        font-size: 16px;
      }
    }

    `;

// 2. New HTML
// Read current HTML and inject pain-node-anchor into each pain-card
let currentHtml = p12.slice(152999, 159058);

// Remove branches-group and nodes-group from SVG
currentHtml = currentHtml.replace(/<g id="svg-branches-group"><\/g>[\s\r\n]*/, '');
currentHtml = currentHtml.replace(/<g id="svg-nodes-group"><\/g>[\s\r\n]*/, '');

const nodeAnchorHtml = `<div class="pain-node-anchor" aria-hidden="true">
              <div class="pain-node-connector"></div>
              <div class="pain-node-bullet">
                <svg class="pain-bullet-svg" viewBox="0 0 32 32" width="32" height="32" aria-hidden="true">
                  <circle cx="16" cy="16" r="15" class="svg-node-halo"></circle>
                  <circle cx="16" cy="16" r="11" class="svg-node-bg"></circle>
                  <circle cx="16" cy="16" r="3.5" class="svg-node-core"></circle>
                </svg>
              </div>
            </div>
            `;

// Replace each '<div class="pain-card-inner">' with nodeAnchorHtml + '<div class="pain-card-inner">'
currentHtml = currentHtml.replaceAll('<div class="pain-card-inner">', nodeAnchorHtml + '<div class="pain-card-inner">');

// 3. New JS
const newJs = `<!-- Script da Dobra 2: Conexão Geométrica Exata da Timeline e Ciclo -->
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
      var cards = painSection.querySelectorAll('.pain-card');
      if (!cards.length || !wrapper || !svg) return;

      painSection.classList.add('pain-animated');

      var visibleIndexes = new Set();
      var cachedYCoords = [];
      var currentAxisX = 34;

      function getBulletCenterInWrapper(card) {
        var wrapperRect = wrapper.getBoundingClientRect();
        var bullet = card.querySelector('.pain-node-bullet');
        
        // Coordenada horizontal X: medida real do navegador relativa ao wrapper
        var bulletRect = bullet ? bullet.getBoundingClientRect() : null;
        var bX = bulletRect ? ((bulletRect.left - wrapperRect.left) + (bulletRect.width / 2)) : 34;
        
        // Coordenada vertical Y de repouso: offsetTop do card relativo ao wrapper + metade da altura do card
        // top: 50% garante matematicamente o alinhamento com a altura real medida do card
        var cTop = 0;
        var el = card;
        while (el && el !== wrapper) {
          cTop += el.offsetTop;
          el = el.offsetParent;
        }
        var bY = cTop + (card.offsetHeight / 2);
        
        return { x: bX, y: bY };
      }

      function updateLayoutGeometry() {
        if (!cards.length || !wrapper) return;
        var totalH = wrapper.offsetHeight;
        var totalW = wrapper.offsetWidth;
        svg.setAttribute('viewBox', '0 0 ' + totalW + ' ' + totalH);
        svg.style.height = totalH + 'px';

        // 1. Coordenadas medidas reais no navegador para cada card / bolinha
        cachedYCoords = [];
        var pFirst = getBulletCenterInWrapper(cards[0]);
        currentAxisX = pFirst.x;

        cards.forEach(function (card) {
          var p = getBulletCenterInWrapper(card);
          cachedYCoords.push(p.y);
        });

        if (cachedYCoords.length < 2) return;

        var y1 = cachedYCoords[0];
        var y6 = cachedYCoords[cachedYCoords.length - 1];
        
        var isSmallMobile = window.innerWidth <= 360;
        var isMobile = window.innerWidth <= 480;
        var xReturn = isSmallMobile ? 6 : (isMobile ? 8 : 12);
        var nodeRadius = isSmallMobile ? 9 : (isMobile ? 10 : 11);
        var rArc = (currentAxisX - xReturn) / 2;
        var loopPad = isMobile ? 14 : 18;

        // 2. Trilha descendente base (passa exatamente pelo centro de todas as bolinhas)
        if (trackPath) {
          trackPath.setAttribute('d', 'M ' + currentAxisX + ',' + y1 + ' L ' + currentAxisX + ',' + y6);
        }

        // 3. Linha do Ciclo (Loop de Retorno fechando do último ao primeiro card)
        if (loopPath) {
          var bottomCurveY = y6 + nodeRadius + loopPad;
          var topCurveY = y1 - nodeRadius - loopPad;
          var arrowStopY = y1 - nodeRadius - 7;

          var dLoop = 'M ' + currentAxisX + ',' + (y6 + nodeRadius) + ' ' +
                      'L ' + currentAxisX + ',' + bottomCurveY + ' ' +
                      'A ' + rArc + ' ' + rArc + ' 0 0 1 ' + xReturn + ',' + bottomCurveY + ' ' +
                      'L ' + xReturn + ',' + topCurveY + ' ' +
                      'A ' + rArc + ' ' + rArc + ' 0 0 1 ' + currentAxisX + ',' + topCurveY + ' ' +
                      'L ' + currentAxisX + ',' + arrowStopY;
          loopPath.setAttribute('d', dLoop);
        }

        // 4. Seta conectando perfeitamente a descida no topo da Bolinha 1
        if (loopArrow) {
          var tipY = y1 - nodeRadius - 1;
          var baseY = y1 - nodeRadius - 7;
          var pts = currentAxisX + ',' + tipY + ' ' +
                    (currentAxisX - 4.5) + ',' + baseY + ' ' +
                    (currentAxisX + 4.5) + ',' + baseY;
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
          fillPath.setAttribute('d', 'M ' + currentAxisX + ',' + y1 + ' L ' + currentAxisX + ',' + targetY);
        } else {
          fillPath.setAttribute('d', '');
        }

        if (visibleIndexes.size === cards.length) {
          wrapper.classList.add('cycle-closed');
        }
      }

      // 1. Recalcula quando as fontes terminarem de carregar
      if (document.fonts && document.fonts.ready) {
        document.fonts.ready.then(function () {
          requestAnimationFrame(updateLayoutGeometry);
        });
      }

      // 2. Recalcula quando a altura de qualquer card mudar (ResizeObserver)
      if ('ResizeObserver' in window) {
        var ro = new ResizeObserver(function () {
          updateLayoutGeometry();
        });
        cards.forEach(function (card) {
          ro.observe(card);
        });
        ro.observe(wrapper);
      }

      // 3. Recalcula em resize de tela e mudança de orientação (debounced)
      var resizeTimer;
      function onViewportChange() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function () {
          requestAnimationFrame(updateLayoutGeometry);
        }, 50);
      }
      window.addEventListener('resize', onViewportChange);
      window.addEventListener('orientationchange', onViewportChange);
      window.addEventListener('load', updateLayoutGeometry);
      requestAnimationFrame(updateLayoutGeometry);

      // 4. Preferência de redução de movimento
      if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        cards.forEach(function (card, i) {
          card.classList.add('is-visible');
          visibleIndexes.add(i);
        });
        wrapper.classList.add('cycle-closed');
        requestAnimationFrame(updateLayoutGeometry);
        return;
      }

      // 5. IntersectionObserver para animar os cards e a trilha conforme a rolagem
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
        wrapper.classList.add('cycle-closed');
        requestAnimationFrame(updateLayoutGeometry);
      }
    })();
  </script>`;

// Assemble the final file
const cssStart = p12.indexOf('/* ── Seção Dor / Ciclo (P12 - Dobra 2) ── */');
const cssEnd = p12.indexOf('/* ── Seção Erros (P12 - Dobra 3) ── */');
const htmlStart = p12.indexOf('<section id="pain">');
const htmlEnd = p12.indexOf('</section>', htmlStart) + 10;
const jsStart = p12.indexOf('<!-- Script da Dobra 2:', htmlEnd);
const jsEnd = p12.indexOf('</script>', jsStart) + 9;

const part1 = p12.slice(0, cssStart);
const part2 = p12.slice(cssEnd, htmlStart);
const part3 = p12.slice(htmlEnd, jsStart);
const part4 = p12.slice(jsEnd);

const finalContent = part1 + newCss + part2 + currentHtml + part3 + newJs + part4;

fs.writeFileSync('p12/index.html', finalContent);
console.log('Successfully updated p12/index.html! New file size:', finalContent.length);
