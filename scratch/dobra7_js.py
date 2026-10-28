DOBRA7_JS = """    /* ═════════════════════════════════════════════════════════════════════════
       SCRIPT: DOBRA 7 — CHECKLIST SOMA, RISCO VERMELHO E PREÇO (P12)
       Animação progressiva de itens, contador somatório e varredura do botão
    ═════════════════════════════════════════════════════════════════════════ */
    (function () {
      var pricingSec = document.getElementById('pricing');
      if (!pricingSec) return;

      var isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      var totalDisplay = document.getElementById('totalValueDisplay');
      var strikeOriginal = document.getElementById('strikeOriginalPrice');
      var priceDisplay = document.getElementById('mainPriceDisplay');
      var ctaBtn = document.getElementById('pricingCtaBtn');
      var checklistCard = document.getElementById('checklistCard');
      var items = Array.prototype.slice.call(pricingSec.querySelectorAll('.checklist-item'));

      // Se o usuário preferir movimento reduzido, mantém estado final estático
      if (isReducedMotion) {
        if (totalDisplay) {
          totalDisplay.textContent = 'R$ 297,00';
          totalDisplay.classList.add('is-struck');
        }
        if (strikeOriginal) {
          strikeOriginal.classList.add('is-struck');
        }
        return;
      }

      // Prepara estado inicial apenas se JS estiver ativo
      checklistCard.classList.add('js-animate-items');
      if (totalDisplay) {
        totalDisplay.classList.remove('is-struck');
        totalDisplay.textContent = 'R$ 0,00';
      }
      if (strikeOriginal) {
        strikeOriginal.classList.remove('is-struck');
      }

      var hasAnimated = false;

      function runChecklistSequence() {
        if (hasAnimated) return;
        hasAnimated = true;

        var stepDelay = 320; // intervalo suave entre cada item
        var sumValues = [97, 97, 144, 211, 230, 297];

        items.forEach(function (item, index) {
          setTimeout(function () {
            // Revela item e desenha checkmark
            item.classList.add('is-revealed');

            // Atualiza somatório do total correspondente
            if (totalDisplay && sumValues[index] !== undefined) {
              totalDisplay.textContent = 'R$ ' + sumValues[index] + ',00';
            }

            // Quando o último item é revelado
            if (index === items.length - 1) {
              // Pausa curta antes de riscar o valor total
              setTimeout(function () {
                if (totalDisplay) {
                  totalDisplay.classList.add('is-struck');
                }

                // Em seguida risca o valor original e aciona o brilho do R$29,90
                setTimeout(function () {
                  if (strikeOriginal) {
                    strikeOriginal.classList.add('is-struck');
                  }
                  if (priceDisplay) {
                    priceDisplay.classList.add('price-shimmer-active');
                    setTimeout(function () {
                      priceDisplay.classList.remove('price-shimmer-active');
                    }, 1100);
                  }
                }, 380);

              }, 400);
            }
          }, index * stepDelay);
        });
      }

      // Observador de entrada na tela para disparar a sequência
      if ('IntersectionObserver' in window) {
        var checklistObserver = new IntersectionObserver(function (entries, observer) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              runChecklistSequence();
              observer.unobserve(entry.target);
            }
          });
        }, { threshold: 0.2 });

        checklistObserver.observe(checklistCard);
      } else {
        // Fallback imediato se não suportar IntersectionObserver
        runChecklistSequence();
      }

      // Varredura suave de luz no botão a cada ~5s enquanto visível na tela
      if (ctaBtn && 'IntersectionObserver' in window) {
        var btnInterval = null;

        var btnObserver = new IntersectionObserver(function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              if (!btnInterval) {
                btnInterval = setInterval(function () {
                  ctaBtn.classList.add('btn-sweep-active');
                  setTimeout(function () {
                    ctaBtn.classList.remove('btn-sweep-active');
                  }, 1250);
                }, 5000);
              }
            } else {
              if (btnInterval) {
                clearInterval(btnInterval);
                btnInterval = null;
              }
            }
          });
        }, { threshold: 0.1 });

        btnObserver.observe(ctaBtn);
      }
    })();
"""
