DOBRA8_JS = """    /* ═════════════════════════════════════════════════════════════════════════
       SCRIPT: DOBRA 8 — PROVA SOCIAL WHATSAPP (P12)
       Linha de transição, título palavra por palavra e entrada escalonada dos prints
    ═════════════════════════════════════════════════════════════════════════ */
    (function () {
      var socialSec = document.getElementById('social-proof');
      if (!socialSec) return;

      var isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      var seamLine = document.getElementById('socialSeamLine');
      var headline = document.getElementById('socialHeadline');
      var chatStream = document.getElementById('socialChatStream');

      if (isReducedMotion) {
        if (seamLine) seamLine.classList.add('is-drawn');
        return;
      }

      // Habilita animação dinâmica somente com JS ativo
      var headerBlock = socialSec.querySelector('.social-header-block');
      if (headerBlock) headerBlock.classList.add('js-animate-title');
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

      // 2. Título palavra por palavra
      if (headline && 'IntersectionObserver' in window) {
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

      // 3. Entrada dos prints como mensagens de chat
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
"""
