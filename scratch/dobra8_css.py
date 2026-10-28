DOBRA8_CSS = """/* ══════════════════════════════════════════════════════════════════════════
   DOBRA 8: PROVA SOCIAL WHATSAPP (P12)
   Fundo escuro (#0E0E0E) com brilho de brasa, título serifado palavra por palavra,
   prints estilo balões de conversa com deslizamento suave e alta nitidez.
   ══════════════════════════════════════════════════════════════════════════ */

    /* ── Linha dourada de transição da dobra branca para a escura ── */
    .social-seam-line {
      position: relative;
      width: 100%;
      height: 2px;
      background: rgba(199, 158, 59, 0.15);
      overflow: hidden;
      z-index: 5;
    }

    .social-seam-line .seam-line-draw {
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

    .social-seam-line.is-drawn .seam-line-draw {
      transform: scaleX(1);
    }

    /* ── Seção Prova Social ── */
    #social-proof {
      padding: clamp(64px, 8vw, 110px) 0 clamp(72px, 9vw, 120px);
      background: #0E0E0E;
      position: relative;
      overflow: hidden;
    }

    .social-proof-glow {
      position: absolute;
      top: 25%;
      left: 50%;
      transform: translate(-50%, -25%);
      width: min(850px, 95vw);
      height: min(550px, 75vw);
      background: radial-gradient(circle, rgba(199, 158, 59, 0.08) 0%, rgba(133, 86, 5, 0.03) 45%, transparent 70%);
      filter: blur(60px);
      pointer-events: none;
      z-index: 1;
    }

    #social-proof .container {
      max-width: 1080px;
      margin: 0 auto;
      padding: 0 20px;
      position: relative;
      z-index: 2;
    }

    /* ── Cabeçalho da Seção ── */
    .social-header-block {
      text-align: center;
      max-width: 780px;
      margin: 0 auto clamp(36px, 5vw, 56px);
    }

    .social-headline {
      font-family: var(--font-heading, 'Cormorant Garamond', Georgia, serif);
      font-size: clamp(26px, 4vw, 42px);
      font-weight: 700;
      color: #EBC068;
      text-transform: uppercase;
      letter-spacing: 0.02em;
      line-height: 1.2;
      margin: 0 0 16px;
      text-wrap: balance;
      text-shadow: 0 2px 14px rgba(0, 0, 0, 0.8), 0 0 22px rgba(235, 192, 104, 0.2);
    }

    /* Animação palavra por palavra do título */
    .social-headline .word-split {
      display: inline-block;
      opacity: 1;
      transform: none;
      transition: opacity 0.4s ease, transform 0.4s ease;
    }

    .js-animate-title .social-headline .word-split {
      opacity: 0;
      transform: translateY(8px);
    }

    .js-animate-title .social-headline .word-split.is-visible {
      opacity: 1;
      transform: translateY(0);
    }

    .social-sub {
      font-family: var(--font-body, -apple-system, sans-serif);
      font-size: clamp(16px, 2.2vw, 20px);
      color: #C2BCB0;
      line-height: 1.55;
      margin: 0 auto;
      max-width: 680px;
      text-wrap: pretty;
    }

    .social-sub strong {
      color: #F5F0E8;
      font-weight: 700;
    }

    .social-sub em {
      font-style: italic;
    }

    /* ── Conversational Layout dos Prints ── */
    /* Mobile (< 768px): Coluna única, 88% largura, alternando alinhamento */
    .social-chat-stream {
      display: flex;
      flex-direction: column;
      gap: clamp(18px, 4vw, 26px);
      max-width: 440px;
      margin: 0 auto;
      width: 100%;
    }

    .chat-bubble-card {
      width: 88%;
      max-width: 380px;
      background: #141316;
      border: 1px solid rgba(199, 158, 59, 0.25);
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), 0 2px 8px rgba(199, 158, 59, 0.05);
      opacity: 1;
      transform: none;
      transition: opacity 0.5s ease, transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease;
    }

    .chat-bubble-card:hover {
      border-color: rgba(199, 158, 59, 0.45);
      box-shadow: 0 14px 38px rgba(0, 0, 0, 0.65), 0 4px 12px rgba(199, 158, 59, 0.1);
    }

    /* Alinhamento alternado no mobile */
    .chat-bubble-card.align-left {
      align-self: flex-start;
      margin-left: 2%;
    }

    .chat-bubble-card.align-right {
      align-self: flex-end;
      margin-right: 2%;
    }

    /* Estado inicial para animação de mensagem que chega */
    .js-animate-cards .chat-bubble-card.align-left {
      opacity: 0;
      transform: translateX(-24px);
    }

    .js-animate-cards .chat-bubble-card.align-right {
      opacity: 0;
      transform: translateX(24px);
    }

    .js-animate-cards .chat-bubble-card.is-arrived {
      opacity: 1;
      transform: translateX(0);
    }

    .chat-bubble-card picture,
    .chat-bubble-card img {
      display: block;
      width: 100%;
      height: auto;
      border-radius: 15px;
    }

    /* ── Desktop Layout (>= 768px): 2 Colunas Escalonadas com Ritmo de Conversa ── */
    @media (min-width: 768px) {
      .social-chat-stream {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 28px 32px;
        max-width: 860px;
      }

      .chat-bubble-card {
        width: 100%;
        max-width: 100%;
        margin: 0 !important;
      }

      /* Coluna da esquerda (cards 1, 3, 5) */
      .chat-bubble-card:nth-child(odd) {
        align-self: start;
      }

      /* Coluna da direita escalonada (cards 2, 4) */
      .chat-bubble-card:nth-child(even) {
        align-self: start;
        margin-top: 36px !important;
      }

      .chat-bubble-card:nth-child(5) {
        grid-column: 1 / span 2;
        max-width: 420px;
        justify-self: center;
        margin-top: 10px !important;
      }
    }

    @media (min-width: 1080px) {
      .social-chat-stream {
        max-width: 920px;
        gap: 32px 40px;
      }
    }

    /* ── PREFERS-REDUCED-MOTION ── */
    @media (prefers-reduced-motion: reduce) {
      .seam-line-draw {
        transform: scaleX(1) !important;
        transition: none !important;
      }

      .social-headline .word-split {
        opacity: 1 !important;
        transform: none !important;
        transition: none !important;
      }

      .chat-bubble-card {
        opacity: 1 !important;
        transform: none !important;
        transition: none !important;
      }
    }
"""
