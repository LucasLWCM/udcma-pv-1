DOBRA9_HTML = """  <!-- ═══════════════════════════════════════════════════════════════════════
       DOBRA 9: PARA QUEM É / NÃO É + VÍDEO DO CELULAR (P12)
       Vídeo da área de membros em mockup recortado + Cards Positivo e Negativo
  ══════════════════════════════════════════════════════════════════════════ -->
  <section id="for-who">
    <div class="for-who-glow" aria-hidden="true"></div>

    <div class="container">

      <!-- 1. VÍDEO DO CELULAR NO TOPO CENTRALIZADO -->
      <div class="phone-video-container">
        <div class="phone-video-mask" id="phoneVideoWrapper">

          <!-- Vídeo do celular (carregamento sob demanda, toca uma vez ao atingir 50% de visibilidade) -->
          <video id="phoneMemberVideo"
                 class="phone-video-player"
                 muted
                 playsinline
                 preload="none"
                 poster="../video/phone_poster.webp"
                 width="680"
                 height="980"
                 data-src-webm="../video/phone_members.webm"
                 data-src-mp4="../video/phone_members.mp4"
                 data-src-webm-mob="../video/phone_members_mob.webm"
                 data-src-mp4-mob="../video/phone_members_mob.mp4"
                 aria-label="Celular exibindo a experiência imersiva da área de membros da série">
          </video>

          <!-- Imagem estática do Plano B (último quadro com aula tocando) -->
          <picture id="phoneFallbackPicture" style="display: none;">
            <source srcset="../video/phone_fallback.webp" type="image/webp">
            <img class="phone-fallback-img" src="../video/phone_fallback.jpg" alt="Celular exibindo a aula tocando na área de membros da série" width="680" height="980">
          </picture>

          <!-- Fallback absoluto sem JavaScript -->
          <noscript>
            <picture>
              <source srcset="../video/phone_fallback.webp" type="image/webp">
              <img class="phone-fallback-img" src="../video/phone_fallback.jpg" alt="Celular exibindo a aula tocando na área de membros da série" width="680" height="980">
            </picture>
          </noscript>
        </div>
      </div>

      <!-- 2. GRID DOS DOIS CARDS (POSITIVO / NEGATIVO) -->
      <div class="for-who-cards-grid" id="forWhoCardsGrid">

        <!-- CARD 1: POSITIVO (Verde Esmeralda Nobre) -->
        <div class="for-who-card card-yes" id="cardPositive">
          <div class="for-who-card-header">
            <div class="header-shimmer-beam" aria-hidden="true"></div>
            <h3 class="for-who-card-title">Essa série é para quem quer:</h3>
          </div>
          <ul class="for-who-list">
            <li class="for-who-item">
              <svg class="card-icon-svg icon-check" viewBox="0 0 20 20" fill="none" aria-hidden="true">
                <circle cx="10" cy="10" r="8" stroke="#0E4A34" stroke-width="1.8" />
                <polyline class="draw-check" points="6 10.5 8.5 13 14 7.5" stroke="#0E4A34" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
              </svg>
              <span><strong>Dominar o Pensamento Estoico</strong> <em>(fixando o conhecimento, sem esquecimento)</em></span>
            </li>
            <li class="for-who-item">
              <svg class="card-icon-svg icon-check" viewBox="0 0 20 20" fill="none" aria-hidden="true">
                <circle cx="10" cy="10" r="8" stroke="#0E4A34" stroke-width="1.8" />
                <polyline class="draw-check" points="6 10.5 8.5 13 14 7.5" stroke="#0E4A34" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
              </svg>
              <span><strong>Aprender as principais ideias de Marco Aurélio</strong> <em>(mesmo que nunca tenha estudado filosofia antes)</em></span>
            </li>
            <li class="for-who-item">
              <svg class="card-icon-svg icon-check" viewBox="0 0 20 20" fill="none" aria-hidden="true">
                <circle cx="10" cy="10" r="8" stroke="#0E4A34" stroke-width="1.8" />
                <polyline class="draw-check" points="6 10.5 8.5 13 14 7.5" stroke="#0E4A34" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
              </svg>
              <span><strong>Viver o Estoicismo</strong> <em>(de maneira natural e consistente)</em><strong>em seus hábitos e conversas</strong></span>
            </li>
          </ul>
        </div>

        <!-- CARD 2: NEGATIVO (Vinho Nobre) -->
        <div class="for-who-card card-no" id="cardNegative">
          <div class="for-who-card-header">
            <div class="header-shimmer-beam" aria-hidden="true"></div>
            <h3 class="for-who-card-title">Essa série NÃO é para você que:</h3>
          </div>
          <ul class="for-who-list">
            <li class="for-who-item">
              <svg class="card-icon-svg icon-cross" viewBox="0 0 20 20" fill="none" aria-hidden="true">
                <circle cx="10" cy="10" r="8" stroke="#5E171E" stroke-width="1.8" />
                <line class="draw-line1" x1="7" y1="7" x2="13" y2="13" stroke="#5E171E" stroke-width="2" stroke-linecap="round" />
                <line class="draw-line2" x1="13" y1="7" x2="7" y2="13" stroke="#5E171E" stroke-width="2" stroke-linecap="round" />
              </svg>
              <span><strong>Quer um curso acadêmico</strong> <em>(longo e complexo)</em> <strong>em filosofia clássica</strong></span>
            </li>
            <li class="for-who-item">
              <svg class="card-icon-svg icon-cross" viewBox="0 0 20 20" fill="none" aria-hidden="true">
                <circle cx="10" cy="10" r="8" stroke="#5E171E" stroke-width="1.8" />
                <line class="draw-line1" x1="7" y1="7" x2="13" y2="13" stroke="#5E171E" stroke-width="2" stroke-linecap="round" />
                <line class="draw-line2" x1="13" y1="7" x2="7" y2="13" stroke="#5E171E" stroke-width="2" stroke-linecap="round" />
              </svg>
              <span><strong>Acha que "filosofia de verdade" precisa ser chata e incompreensível</strong></span>
            </li>
            <li class="for-who-item">
              <svg class="card-icon-svg icon-cross" viewBox="0 0 20 20" fill="none" aria-hidden="true">
                <circle cx="10" cy="10" r="8" stroke="#5E171E" stroke-width="1.8" />
                <line class="draw-line1" x1="7" y1="7" x2="13" y2="13" stroke="#5E171E" stroke-width="2" stroke-linecap="round" />
                <line class="draw-line2" x1="13" y1="7" x2="7" y2="13" stroke="#5E171E" stroke-width="2" stroke-linecap="round" />
              </svg>
              <span><strong>Prefere só colecionar frases motivacionais</strong> <em>(que muitas vezes nem são dos Estoicos)</em></span>
            </li>
          </ul>
        </div>

      </div>

    </div>
  </section>"""
