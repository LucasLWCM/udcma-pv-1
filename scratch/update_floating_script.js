const fs = require('fs');

let p12 = fs.readFileSync('p12/index.html', 'utf8');

// Replace the script for floating CTA
const oldScriptStart = '<!-- Script do Botão Flutuante de Compra (P12) -->';
const oldScriptEnd = '</body>';

const scriptPos = p12.indexOf(oldScriptStart);
if (scriptPos === -1) throw new Error('Old script not found');

const newScript = `<!-- Script do Botão Flutuante de Compra (P12) -->
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

      // Herda os mesmos disparos de clique (Meta Pixel, GTM, onclick)
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

      function updateVisibility() {
        // Verifica se a borda inferior do primeiro CTA já ultrapassou o topo da janela
        var r = firstCta.getBoundingClientRect();
        var isPastFirst = (r.height > 0 && r.bottom <= 0);
        var hasVisibleCta = visibleCtas.size > 0;
        var shouldShow = isPastFirst && !hasVisibleCta;

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

      // 1. Observador de visibilidade de todos os botões de checkout na tela
      // rootMargin com buffer inferior de 75px evita que qualquer CTA e o botão flutuante apareçam visíveis juntos
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

      // 2. Observador para detectar a passagem exata do primeiro botão pelo topo da tela
      var pastFirstObserver = new IntersectionObserver(function () {
        updateVisibility();
      }, {
        rootMargin: '0px 0px 0px 0px',
        threshold: 0
      });

      pastFirstObserver.observe(firstCta);

      // Estado inicial garantido após carregamento do DOM
      requestAnimationFrame(updateVisibility);
    })();
  </script>
`;

p12 = p12.slice(0, scriptPos) + newScript + p12.slice(p12.indexOf('</body>', scriptPos));

fs.writeFileSync('p12/index.html', p12);
console.log('Updated floating CTA script in p12/index.html');
