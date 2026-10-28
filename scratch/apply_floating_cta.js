const fs = require('fs');

let p12 = fs.readFileSync('p12/index.html', 'utf8');

// 1. Mark the 5 CTAs with data-cta
// CTA 1: pricingCtaBtn
const cta1Old = '<a href="https://pay.hotmart.com/X108154869T?off=953h3rmf" class="btn-cta" id="pricingCtaBtn">';
const cta1New = '<a href="https://pay.hotmart.com/X108154869T?off=953h3rmf" class="btn-cta" id="pricingCtaBtn" data-cta="pricing">';

if (!p12.includes(cta1Old)) throw new Error('CTA 1 not found');
p12 = p12.replace(cta1Old, cta1New);

// CTA 2: pricing sub
const cta2Old = '<a href="https://pay.hotmart.com/X108154869T?off=953h3rmf" class="cta-sub">Acesso VITALÍCIO · 7 dias de garantia</a>';
const cta2New = '<a href="https://pay.hotmart.com/X108154869T?off=953h3rmf" class="cta-sub" data-cta="pricing-sub">Acesso VITALÍCIO · 7 dias de garantia</a>';

if (!p12.includes(cta2Old)) throw new Error('CTA 2 not found');
p12 = p12.replace(cta2Old, cta2New);

// CTA 3: guarantee btn
const cta3Old = `<div class="guarantee-cta" aria-hidden="true">
          <a href="https://pay.hotmart.com/X108154869T?off=953h3rmf" class="btn-cta">
            Quero aproveitar a garantia!
          </a>`;

const cta3New = `<div class="guarantee-cta" aria-hidden="true">
          <a href="https://pay.hotmart.com/X108154869T?off=953h3rmf" class="btn-cta" data-cta="guarantee">
            Quero aproveitar a garantia!
          </a>`;

// Use regex or indexOf to replace cleanly
const gIdx = p12.indexOf('Quero aproveitar a garantia!');
const gBtnStart = p12.lastIndexOf('<a href="https://pay.hotmart.com/X108154869T?off=953h3rmf" class="btn-cta"', gIdx);
p12 = p12.slice(0, gBtnStart) + '<a href="https://pay.hotmart.com/X108154869T?off=953h3rmf" class="btn-cta" data-cta="guarantee"' + p12.slice(gBtnStart + 74);

// CTA 4: guarantee sub
const gSubIdx = p12.indexOf('Acesso IMEDIATO e VITALÍCIO');
const gSubStart = p12.lastIndexOf('<a href="https://pay.hotmart.com/X108154869T?off=953h3rmf" class="cta-sub"', gSubIdx);
p12 = p12.slice(0, gSubStart) + '<a href="https://pay.hotmart.com/X108154869T?off=953h3rmf" class="cta-sub" data-cta="guarantee-sub"' + p12.slice(gSubStart + 74);

// CTA 5: final btn (in #faq)
const finalIdx = p12.indexOf('Quero acesso imediato e vitalício');
const finalStart = p12.lastIndexOf('<a href="https://pay.hotmart.com/X108154869T?off=953h3rmf" class="btn-cta"', finalIdx);
p12 = p12.slice(0, finalStart) + '<a href="https://pay.hotmart.com/X108154869T?off=953h3rmf" class="btn-cta" data-cta="final"' + p12.slice(finalStart + 74);

console.log('All 5 CTAs marked with data-cta successfully.');

// 2. Add Floating CTA CSS
const cssBlock = `
    /* ══════════════════════════════════════════════════════════════════════════
       BOTÃO FLUTUANTE DE COMPRA (P12)
       ══════════════════════════════════════════════════════════════════════════ */
    .floating-cta-wrap {
      position: fixed;
      left: 50%;
      bottom: calc(12px + env(safe-area-inset-bottom, 0px));
      transform: translate(-50%, calc(100% + 32px));
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
      z-index: 9990;
      width: min(92%, 420px);
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.2s ease, visibility 0.2s;
      will-change: transform, opacity;
    }

    .floating-cta-wrap.is-visible {
      transform: translate(-50%, 0);
      opacity: 1;
      visibility: visible;
      pointer-events: auto;
    }

    .floating-cta-btn {
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      height: 54px;
      padding: 0 24px;
      background: linear-gradient(135deg, #EBC068 0%, #C79E3B 100%);
      color: #070707;
      font-family: var(--font-body, 'DM Sans', sans-serif);
      font-size: 18px;
      font-weight: 700;
      text-align: center;
      text-decoration: none;
      border-radius: 999px;
      border: 1.5px solid rgba(80, 50, 10, 0.45);
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35), 0 2px 6px rgba(0, 0, 0, 0.2), 0 0 16px rgba(235, 192, 104, 0.2);
      cursor: pointer;
      user-select: none;
      -webkit-tap-highlight-color: transparent;
      outline: none;
      transition: transform 0.15s ease, box-shadow 0.15s ease;
    }

    .floating-cta-btn:focus-visible {
      outline: 3px solid #FFFFFF;
      outline-offset: 3px;
    }

    .floating-cta-btn:active {
      transform: scale(0.98);
    }

    /* Brilho dourado suave expansivo no pulso */
    .floating-cta-glow {
      position: absolute;
      inset: -4px;
      border-radius: 999px;
      background: rgba(235, 192, 104, 0.55);
      filter: blur(8px);
      opacity: 0;
      pointer-events: none;
      z-index: -1;
    }

    /* Animação de pulso: 3 pulsos suaves de 1.2s seguidos, depois repouso de ~8.4s */
    .floating-cta-wrap.is-visible .floating-cta-btn {
      animation: ctaPulseCycle 12s ease-in-out infinite;
    }

    .floating-cta-wrap.is-visible .floating-cta-glow {
      animation: ctaGlowCycle 12s ease-in-out infinite;
    }

    /* Pausa o pulso quando passar o mouse ou tocar */
    .floating-cta-wrap.is-visible .floating-cta-btn:hover,
    .floating-cta-wrap.is-visible .floating-cta-btn:active,
    .floating-cta-wrap.is-visible .floating-cta-btn:hover .floating-cta-glow,
    .floating-cta-wrap.is-visible .floating-cta-btn:active .floating-cta-glow {
      animation-play-state: paused;
    }

    @keyframes ctaPulseCycle {
      /* Pulso 1 (0s a 1.2s -> 0% a 10%) */
      0%   { transform: scale(1); }
      5%   { transform: scale(1.03); }
      10%  { transform: scale(1); }
      /* Pulso 2 (1.2s a 2.4s -> 10% a 20%) */
      15%  { transform: scale(1.03); }
      20%  { transform: scale(1); }
      /* Pulso 3 (2.4s a 3.6s -> 20% a 30%) */
      25%  { transform: scale(1.03); }
      30%  { transform: scale(1); }
      /* Repouso (3.6s a 12.0s -> 30% a 100%) */
      100% { transform: scale(1); }
    }

    @keyframes ctaGlowCycle {
      /* Pulso 1 */
      0%   { opacity: 0; transform: scale(0.98); }
      5%   { opacity: 0.8; transform: scale(1.08); }
      10%  { opacity: 0; transform: scale(1.15); }
      /* Pulso 2 */
      15%  { opacity: 0.8; transform: scale(1.08); }
      20%  { opacity: 0; transform: scale(1.15); }
      /* Pulso 3 */
      25%  { opacity: 0.8; transform: scale(1.08); }
      30%  { opacity: 0; transform: scale(1.15); }
      /* Repouso */
      100% { opacity: 0; transform: scale(1); }
    }

    /* Desktop (1024px ou mais): pílula centralizada embaixo, largura de 420px, a 20px da borda */
    @media (min-width: 1024px) {
      .floating-cta-wrap {
        width: 420px;
        bottom: 20px;
      }
    }

    /* Respiro para o botão flutuante no final da página */
    footer {
      padding-bottom: calc(84px + env(safe-area-inset-bottom, 0px)) !important;
    }

    /* Ajuste para evitar sobreposição do sales-toast no mobile */
    .floating-cta-active .sales-toast {
      bottom: calc(78px + env(safe-area-inset-bottom, 0px));
    }
    @media (min-width: 1024px) {
      .floating-cta-active .sales-toast {
        bottom: 24px;
        left: 24px;
      }
    }

    /* Preferência de redução de movimento */
    @media (prefers-reduced-motion: reduce) {
      .floating-cta-wrap {
        transition: opacity 0.15s ease !important;
        transform: translate(-50%, 0) !important;
      }
      .floating-cta-wrap:not(.is-visible) {
        opacity: 0 !important;
        visibility: hidden !important;
      }
      .floating-cta-wrap.is-visible .floating-cta-btn,
      .floating-cta-wrap.is-visible .floating-cta-glow {
        animation: none !important;
        transform: none !important;
      }
    }
`;

const styleClose = '</style>';
const stylePos = p12.indexOf(styleClose);
p12 = p12.slice(0, stylePos) + cssBlock + p12.slice(stylePos);

// 3. Add Floating CTA HTML right before </body>
const htmlBlock = `
  <!-- Botão Flutuante de Compra (P12) -->
  <aside id="floatingCtaWrap" class="floating-cta-wrap" aria-hidden="true">
    <a href="https://pay.hotmart.com/X108154869T?off=953h3rmf"
       id="floatingCtaBtn"
       class="floating-cta-btn"
       data-cta="floating">
      <span class="floating-cta-glow" aria-hidden="true"></span>
      <span class="floating-cta-text">Quero dominar o estoicismo</span>
    </a>
  </aside>
`;

// 4. Add Floating CTA Script right before </body>
const scriptBlock = `
  <!-- Script do Botão Flutuante de Compra (P12) -->
  <script>
    (function () {
      var floatingWrap = document.getElementById('floatingCtaWrap');
      var floatingBtn = document.getElementById('floatingCtaBtn');
      var firstCta = document.getElementById('pricingCtaBtn');

      if (!floatingWrap || !floatingBtn) return;
      if (!firstCta) {
        console.warn('Botão flutuante: primeiro botão de checkout (pricingCtaBtn) não encontrado.');
        return;
      }

      // Sincroniza href e parâmetros dinâmicos (UTMs) com o botão de preço original
      function syncHref() {
        if (firstCta && firstCta.href) {
          floatingBtn.href = firstCta.href;
        }
      }
      syncHref();

      // Dispara os mesmos eventos caso o botão original possua onclick ou evento customizado
      floatingBtn.addEventListener('click', function (e) {
        syncHref();
        if (typeof firstCta.onclick === 'function') {
          firstCta.onclick.call(firstCta, e);
        }
      });

      // Se IntersectionObserver não for suportado, mantém o botão oculto (fail-safe)
      if (!('IntersectionObserver' in window)) return;

      var allCtas = Array.prototype.slice.call(document.querySelectorAll('[data-cta]'))
        .filter(function (el) { return el !== floatingBtn; });

      var visibleCtas = new Set();
      var isPastFirst = false;

      function updateVisibility() {
        var shouldShow = isPastFirst && (visibleCtas.size === 0);
        if (shouldShow) {
          floatingWrap.classList.add('is-visible');
          floatingWrap.setAttribute('aria-hidden', 'false');
          document.body.classList.add('floating-cta-active');
        } else {
          floatingWrap.classList.remove('is-visible');
          floatingWrap.setAttribute('aria-hidden', 'true');
          document.body.classList.remove('floating-cta-active');
        }
      }

      // 1. Observador de visibilidade dos botões CTA na tela
      // rootMargin com buffer inferior de 75px evita que qualquer CTA e o botão flutuante fiquem visíveis juntos
      var visibilityObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            visibleCtas.add(entry.target);
          } else {
            visibleCtas.delete(entry.target);
          }
        });
        updateVisibility();
      }, {
        rootMargin: '20px 0px 75px 0px',
        threshold: 0
      });

      allCtas.forEach(function (el) {
        visibilityObserver.observe(el);
      });

      // 2. Observador para detectar se a pessoa já passou do primeiro botão (pricingCtaBtn)
      // Dispara assim que a borda inferior do primeiro botão ultrapassa o topo da tela
      var pastFirstObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.target === firstCta) {
            if (entry.boundingClientRect.bottom <= 0) {
              isPastFirst = true;
            } else {
              isPastFirst = false;
            }
          }
        });
        updateVisibility();
      }, {
        rootMargin: '0px 0px 0px 0px',
        threshold: 0
      });

      pastFirstObserver.observe(firstCta);
    })();
  </script>
`;

const bodyClose = '</body>';
const bodyPos = p12.indexOf(bodyClose);
p12 = p12.slice(0, bodyPos) + htmlBlock + scriptBlock + p12.slice(bodyPos);

fs.writeFileSync('p12/index.html', p12);
console.log('Successfully updated p12/index.html with Floating CTA!');
