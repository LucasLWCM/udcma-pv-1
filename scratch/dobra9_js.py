DOBRA9_JS = """    /* ═════════════════════════════════════════════════════════════════════════
       SCRIPT: DOBRA 9 — VÍDEO DO CELULAR & CARDS PARA QUEM É / NÃO É (P12)
       Carregamento sob demanda, autoplay inteligente com Plano B e animação dos cards
    ═════════════════════════════════════════════════════════════════════════ */
    (function () {
      var forWhoSec = document.getElementById('for-who');
      if (!forWhoSec) return;

      var video = document.getElementById('phoneMemberVideo');
      var fallback = document.getElementById('phoneFallbackPicture');
      var cardsGrid = document.getElementById('forWhoCardsGrid');
      var cardPositive = document.getElementById('cardPositive');
      var cardNegative = document.getElementById('cardNegative');

      var isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      var isSaveData = navigator.connection && navigator.connection.saveData;

      function activatePlanB() {
        if (video) video.style.display = 'none';
        if (fallback) fallback.style.display = 'block';
      }

      // 1. Caso modo economia de dados ou reduced motion estejam ativos, ativa Plano B imediatamente
      if (isReducedMotion || isSaveData) {
        activatePlanB();
      }

      // 2. Carregamento sob demanda do vídeo (quando estiver a ~1 viewport de distância)
      var sourcesLoaded = false;
      function loadVideoSources() {
        if (sourcesLoaded || !video) return;
        sourcesLoaded = true;

        var isMobile = window.innerWidth <= 768;
        var webmSrc = isMobile ? video.getAttribute('data-src-webm-mob') : video.getAttribute('data-src-webm');
        var mp4Src = isMobile ? video.getAttribute('data-src-mp4-mob') : video.getAttribute('data-src-mp4');

        var sWebm = document.createElement('source');
        sWebm.src = webmSrc;
        sWebm.type = 'video/webm';

        var sMp4 = document.createElement('source');
        sMp4.src = mp4Src;
        sMp4.type = 'video/mp4';

        video.appendChild(sWebm);
        video.appendChild(sMp4);
        video.load();
      }

      if ('IntersectionObserver' in window && !isReducedMotion && !isSaveData) {
        // Preload quando o bloco se aproxima
        var preloadObs = new IntersectionObserver(function (entries, obs) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              loadVideoSources();
              obs.unobserve(entry.target);
            }
          });
        }, { rootMargin: '600px 0px 600px 0px' });
        preloadObs.observe(forWhoSec);

        // Autoplay de 1 vez ao atingir 50% de visibilidade na tela
        var hasPlayed = false;
        var playObs = new IntersectionObserver(function (entries, obs) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting && !hasPlayed) {
              hasPlayed = true;
              obs.unobserve(entry.target);

              // Garante que as fontes foram adicionadas
              loadVideoSources();

              var playPromise = video.play();
              if (playPromise !== undefined) {
                playPromise.catch(function (error) {
                  console.warn('Autoplay bloqueado pelo navegador/sistema. Ativando Plano B:', error);
                  activatePlanB();
                });
              }
            }
          });
        }, { threshold: 0.5 });
        playObs.observe(video);

        // Ao terminar, o vídeo para naturalmente congelado no último quadro
        video.addEventListener('ended', function () {
          video.pause();
        });
      } else if (!isReducedMotion && !isSaveData) {
        loadVideoSources();
      }

      // 3. Animação de entrada dos cards e traçado dos ícones
      if (cardsGrid && !isReducedMotion) {
        cardsGrid.classList.add('js-animate-for-who');

        if ('IntersectionObserver' in window) {
          var cardsObs = new IntersectionObserver(function (entries, obs) {
            entries.forEach(function (entry) {
              if (entry.isIntersecting) {
                // Entrada dos cards
                if (cardPositive) cardPositive.classList.add('is-entered');
                setTimeout(function () {
                  if (cardNegative) cardNegative.classList.add('is-entered');
                }, 160);

                // Brilho suave nos cabeçalhos
                setTimeout(function () {
                  if (cardPositive) {
                    var h1 = cardPositive.querySelector('.for-who-card-header');
                    if (h1) h1.classList.add('header-shimmer-active');
                  }
                  if (cardNegative) {
                    var h2 = cardNegative.querySelector('.for-who-card-header');
                    if (h2) h2.classList.add('header-shimmer-active');
                  }
                }, 350);

                // Traçado dos ícones SVG item a item
                var items = Array.prototype.slice.call(cardsGrid.querySelectorAll('.for-who-item'));
                items.forEach(function (it, idx) {
                  setTimeout(function () {
                    it.classList.add('icon-drawn');
                  }, 400 + idx * 120);
                });

                obs.unobserve(entry.target);
              }
            });
          }, { threshold: 0.18 });
          cardsObs.observe(cardsGrid);
        } else {
          if (cardPositive) cardPositive.classList.add('is-entered');
          if (cardNegative) cardNegative.classList.add('is-entered');
          var allItems = cardsGrid.querySelectorAll('.for-who-item');
          for (var i = 0; i < allItems.length; i++) {
            allItems[i].classList.add('icon-drawn');
          }
        }
      }
    })();
"""
