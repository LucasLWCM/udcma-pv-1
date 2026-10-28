DOBRA9_CSS = """/* ══════════════════════════════════════════════════════════════════════════
   DOBRA 9: PARA QUEM É / NÃO É + VÍDEO DO CELULAR (P12)
   Fundo escuro (#000000 / #0E0E0E) com brilho de brasa, vídeo recortado em máscara
   suave, cards elevados em verde esmeralda e vinho nobres com ícones finos desenhados.
   ══════════════════════════════════════════════════════════════════════════ */

    #for-who {
      padding: clamp(64px, 8vw, 110px) 0 clamp(72px, 9vw, 120px);
      background: #000000;
      position: relative;
      overflow: hidden;
    }

    /* Brilho suave de brasa atrás do vídeo */
    .for-who-glow {
      position: absolute;
      top: 22%;
      left: 50%;
      transform: translate(-50%, -22%);
      width: min(720px, 90vw);
      height: min(480px, 70vw);
      background: radial-gradient(circle, rgba(235, 192, 104, 0.16) 0%, rgba(199, 158, 59, 0.04) 50%, transparent 75%);
      filter: blur(54px);
      pointer-events: none;
      z-index: 1;
    }

    #for-who .container {
      max-width: 1080px;
      margin: 0 auto;
      padding: 0 20px;
      position: relative;
      z-index: 2;
    }

    /* ── VÍDEO DO CELULAR COM MÁSCARA EM DEGRADÊ ── */
    .phone-video-container {
      position: relative;
      display: flex;
      justify-content: center;
      align-items: center;
      margin: 0 auto clamp(36px, 5vw, 60px);
      width: 100%;
      max-width: 440px;
    }

    .phone-video-mask {
      position: relative;
      width: 100%;
      max-width: 420px;
      aspect-ratio: 680 / 980;
      border-radius: 28px;
      overflow: hidden;
      background: #000000;
      mask-image: radial-gradient(circle at 50% 50%, black 76%, transparent 99%);
      -webkit-mask-image: radial-gradient(circle at 50% 50%, black 76%, transparent 99%);
      box-shadow: 0 14px 44px rgba(0, 0, 0, 0.8);
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .phone-video-player,
    .phone-fallback-img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      display: block;
      border: none;
    }

    /* ── GRID DOS DOIS CARDS (POSITIVO / NEGATIVO) ── */
    .for-who-cards-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: clamp(24px, 4vw, 36px);
      max-width: 1020px;
      margin: 0 auto;
    }

    @media (min-width: 1024px) {
      .for-who-cards-grid {
        grid-template-columns: 1fr 1fr;
        gap: 36px;
      }
    }

    /* ── BASE DOS CARDS ── */
    .for-who-card {
      background: #FFFFFF;
      border-radius: 18px;
      overflow: hidden;
      box-shadow: 0 14px 40px rgba(0, 0, 0, 0.65), 0 2px 8px rgba(255, 255, 255, 0.04);
      display: flex;
      flex-direction: column;
      position: relative;
      opacity: 1;
      transform: none;
      transition: opacity 0.55s ease, transform 0.55s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease;
    }

    .for-who-card:hover {
      box-shadow: 0 18px 48px rgba(0, 0, 0, 0.8), 0 4px 14px rgba(199, 158, 59, 0.1);
    }

    /* Card Positivo: Verde Esmeralda Nobre */
    .for-who-card.card-yes {
      border: 1.5px solid rgba(14, 74, 52, 0.55);
    }

    /* Card Negativo: Vinho Nobre */
    .for-who-card.card-no {
      border: 1.5px solid rgba(94, 23, 30, 0.55);
    }

    /* ── CABEÇALHOS DOS CARDS ── */
    .for-who-card-header {
      padding: clamp(18px, 2.8vw, 24px) 20px;
      position: relative;
      overflow: hidden;
    }

    .for-who-card.card-yes .for-who-card-header {
      background: linear-gradient(135deg, #13533B 0%, #0E4A34 100%);
    }

    .for-who-card.card-no .for-who-card-header {
      background: linear-gradient(135deg, #6B1C24 0%, #54141A 100%);
    }

    .for-who-card-title {
      font-family: var(--font-heading, 'Cinzel', serif);
      font-size: clamp(18px, 2.2vw, 21.5px);
      font-weight: 700;
      color: #FFFFFF;
      text-align: center;
      margin: 0;
      letter-spacing: 0.02em;
      line-height: 1.3;
      text-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
    }

    /* Brilho suave que atravessa o cabeçalho ao entrar na tela */
    .header-shimmer-beam {
      position: absolute;
      top: 0;
      left: -130%;
      width: 60%;
      height: 100%;
      background: linear-gradient(90deg, transparent 0%, rgba(255, 255, 255, 0.3) 50%, transparent 100%);
      transform: skewX(-25deg);
      pointer-events: none;
    }

    .header-shimmer-active .header-shimmer-beam {
      animation: headerShimmerSweep 1.1s ease-in-out;
    }

    @keyframes headerShimmerSweep {
      0%   { left: -130%; }
      100% { left: 160%; }
    }

    /* ── CONTEÚDO DOS CARDS (LISTA DE ITENS) ── */
    .for-who-list {
      list-style: none;
      margin: 0;
      padding: clamp(20px, 3.2vw, 30px) clamp(18px, 3vw, 26px);
      display: flex;
      flex-direction: column;
      background: #FFFFFF;
      flex: 1;
    }

    .for-who-item {
      display: flex;
      align-items: flex-start;
      gap: 14px;
      padding: clamp(14px, 2vw, 18px) 0;
      border-bottom: 1px solid rgba(0, 0, 0, 0.08);
      font-family: var(--font-body, -apple-system, sans-serif);
      font-size: 16px;
      line-height: 1.5;
      color: #1F1C18;
      text-align: left;
    }

    .for-who-item:first-child {
      padding-top: 4px;
    }

    .for-who-item:last-child {
      border-bottom: none;
      padding-bottom: 4px;
    }

    .for-who-item strong {
      font-weight: 700;
      color: #121013;
    }

    .for-who-item em {
      font-style: italic;
      color: #55504A;
      font-size: 15px;
    }

    /* ── ÍCONES SVG FINOS UNIFICADOS (CHECK E X) ── */
    .card-icon-svg {
      width: 22px;
      height: 22px;
      flex-shrink: 0;
      margin-top: 2px;
      display: inline-block;
    }

    /* Traçado dos ícones */
    .icon-check .draw-check {
      stroke-dasharray: 24;
      stroke-dashoffset: 0;
      transition: stroke-dashoffset 0.45s ease;
    }

    .icon-cross .draw-line1,
    .icon-cross .draw-line2 {
      stroke-dasharray: 18;
      stroke-dashoffset: 0;
      transition: stroke-dashoffset 0.4s ease;
    }

    /* ── ESTADOS DE ANIMAÇÃO DINÂMICA (JS ATIVO) ── */
    .js-animate-for-who .for-who-card.card-yes {
      opacity: 0;
      transform: translateY(22px);
    }

    .js-animate-for-who .for-who-card.card-no {
      opacity: 0;
      transform: translateY(22px);
    }

    @media (min-width: 1024px) {
      .js-animate-for-who .for-who-card.card-yes {
        transform: translate(-24px, 12px);
      }
      .js-animate-for-who .for-who-card.card-no {
        transform: translate(24px, 12px);
      }
    }

    .js-animate-for-who .for-who-card.is-entered {
      opacity: 1;
      transform: translate(0, 0);
    }

    .js-animate-for-who .for-who-item:not(.icon-drawn) .draw-check {
      stroke-dashoffset: 24;
    }

    .js-animate-for-who .for-who-item:not(.icon-drawn) .draw-line1,
    .js-animate-for-who .for-who-item:not(.icon-drawn) .draw-line2 {
      stroke-dashoffset: 18;
    }

    /* ── AJUSTES MOBILE FIRST (360px, 390px, 768px) ── */
    @media (max-width: 768px) {
      .phone-video-container {
        max-width: 380px;
        margin-bottom: 32px;
      }

      .for-who-card {
        border-radius: 16px;
      }

      .for-who-item {
        font-size: 15px;
        gap: 12px;
      }

      .for-who-item em {
        font-size: 14px;
      }
    }

    @media (max-width: 380px) {
      .phone-video-container {
        max-width: 320px;
      }

      .for-who-item {
        font-size: 14.5px;
      }
    }

    /* ── PREFERS-REDUCED-MOTION ── */
    @media (prefers-reduced-motion: reduce) {
      .for-who-card {
        opacity: 1 !important;
        transform: none !important;
        transition: none !important;
      }

      .icon-check .draw-check,
      .icon-cross .draw-line1,
      .icon-cross .draw-line2 {
        stroke-dashoffset: 0 !important;
        transition: none !important;
      }

      .header-shimmer-beam {
        display: none !important;
      }
    }
"""
