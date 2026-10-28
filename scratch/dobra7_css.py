DOBRA7_CSS = """/* ══════════════════════════════════════════════════════════════════════════
   DOBRA 7: SEÇÃO DE PREÇO / CTA (P12)
   Fundo branco/creme (#FBF8F1), cartões brancos elevados, ícones dourados finos,
   contador de soma gradual, risco vermelho suave e cronômetro idêntico.
   ══════════════════════════════════════════════════════════════════════════ */

    /* ── Linha dourada de transição da dobra escura para a clara ── */
    .pricing-seam-line {
      height: 2px;
      width: 100%;
      background: linear-gradient(90deg, transparent 0%, #C79E3B 20%, #F5DE9C 50%, #C79E3B 80%, transparent 100%);
      box-shadow: 0 0 14px rgba(199, 158, 59, 0.45);
      position: relative;
      z-index: 5;
    }

    #pricing {
      padding: clamp(52px, 7vw, 96px) 0 clamp(64px, 8vw, 110px);
      background-color: #FBF8F1;
      background-image: radial-gradient(circle at 50% 20%, #FFFFFF 0%, #FBF8F1 80%);
      color: #1F1C18;
      position: relative;
      overflow: hidden;
    }

    /* ── Grid e Container ── */
    #pricing .container {
      max-width: 1120px;
      margin: 0 auto;
      padding: 0 20px;
      position: relative;
      z-index: 2;
    }

    /* ── Mockup do Produto no Topo ── */
    .pricing-mockup-wrapper {
      position: relative;
      display: flex;
      justify-content: center;
      align-items: center;
      margin: 0 auto clamp(36px, 5vw, 54px);
      max-width: 580px;
    }

    .pricing-mockup-glow {
      position: absolute;
      width: min(520px, 92%);
      height: min(340px, 75%);
      background: radial-gradient(circle, rgba(235, 192, 104, 0.22) 0%, rgba(212, 168, 67, 0.08) 50%, transparent 75%);
      filter: blur(40px);
      pointer-events: none;
      z-index: 1;
    }

    .pricing-mockup-img {
      position: relative;
      z-index: 2;
      width: 100%;
      max-width: min(520px, 94%);
      height: auto;
      filter: drop-shadow(0 18px 40px rgba(70, 50, 15, 0.16));
      animation: floatPricingMockup 7s ease-in-out infinite alternate;
      will-change: transform;
    }

    @keyframes floatPricingMockup {
      0%   { transform: translateY(0); }
      100% { transform: translateY(-7px); }
    }

    /* ── Disposição dos Cartões (Desktop 2 colunas / Mobile 1 coluna) ── */
    .pricing-cards-layout {
      display: grid;
      grid-template-columns: 1fr;
      gap: clamp(28px, 4vw, 36px);
      align-items: start;
      max-width: 1080px;
      margin: 0 auto;
    }

    @media (min-width: 960px) {
      .pricing-cards-layout {
        grid-template-columns: 1.15fr 0.95fr;
        gap: 36px;
      }
    }

    /* ── Estilo Base dos Cartões Brancos Elevados ── */
    .pricing-card-white {
      background: #FFFFFF;
      border: 1px solid rgba(199, 158, 59, 0.32);
      border-radius: 20px;
      box-shadow: 0 14px 40px rgba(120, 95, 45, 0.08), 0 2px 8px rgba(0, 0, 0, 0.02);
      transition: box-shadow 0.3s ease;
    }

    .pricing-card-white:hover {
      box-shadow: 0 18px 48px rgba(120, 95, 45, 0.12), 0 4px 12px rgba(0, 0, 0, 0.03);
    }

    /* ── Cartão Checklist (Esquerda no Desktop) ── */
    .checklist-card {
      padding: clamp(28px, 4vw, 40px) clamp(20px, 3.5vw, 36px);
      text-align: left;
    }

    .pricing-title {
      font-family: 'Barlow', sans-serif;
      font-size: clamp(20px, 2.5vw, 24px);
      font-weight: 800;
      color: #121013;
      margin-bottom: clamp(22px, 3vw, 30px);
      text-align: center;
      text-transform: uppercase;
      letter-spacing: 0.02em;
      line-height: 1.3;
    }

    .includes-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0;
      margin: 0 0 24px;
      padding: 0;
    }

    .checklist-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: var(--font-body, -apple-system, sans-serif);
      font-size: 16px;
      padding: 14px 0;
      border-bottom: 1px solid rgba(199, 158, 59, 0.14);
      gap: 16px;
      opacity: 1;
      transform: none;
      transition: opacity 0.4s ease, transform 0.4s ease;
    }

    /* Estado inicial para animação JS */
    .js-animate-items .checklist-item {
      opacity: 0;
      transform: translateX(-12px);
    }

    .js-animate-items .checklist-item.is-revealed {
      opacity: 1;
      transform: translateX(0);
    }

    .checklist-item.item-main {
      padding: 16px 0;
    }

    .checklist-item.item-main .item-name strong {
      font-size: 16.5px;
    }

    .item-left {
      display: flex;
      align-items: center;
      gap: 12px;
      line-height: 1.35;
      color: #1F1C18;
      flex: 1;
    }

    .item-text-group {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }

    .item-name {
      color: #1F1C18;
      line-height: 1.35;
    }

    .item-name strong {
      font-weight: 700;
      color: #121013;
    }

    .item-note {
      font-style: italic;
      color: #55504A;
      font-size: 14px;
      line-height: 1.3;
    }

    /* Ícone SVG fino dourado unificado */
    .item-check-svg {
      width: 20px;
      height: 20px;
      flex-shrink: 0;
      display: inline-block;
      vertical-align: middle;
    }

    .item-check-svg circle {
      stroke: #C79E3B;
      stroke-width: 1.5;
    }

    .item-check-svg .check-path {
      stroke: #855605;
      stroke-width: 2;
      stroke-linecap: round;
      stroke-linejoin: round;
      stroke-dasharray: 20;
      stroke-dashoffset: 0;
      transition: stroke-dashoffset 0.45s ease;
    }

    .js-animate-items .checklist-item:not(.is-revealed) .check-path {
      stroke-dashoffset: 20;
    }

    /* Agrupamento elegante dos 4 bônus com filete vertical dourado */
    .bonus-group-wrapper {
      border-left: 2px solid rgba(199, 158, 59, 0.45);
      padding-left: 14px;
      margin: 4px 0 4px 6px;
    }

    .bonus-item {
      padding: 12px 0;
      font-size: 15.5px;
    }

    .bonus-item:last-child {
      border-bottom: none;
    }

    .item-price {
      color: #121013;
      font-weight: 800;
      font-size: 15.5px;
      white-space: nowrap;
      text-align: right;
      font-variant-numeric: tabular-nums;
    }

    /* R$ INESTIMÁVEL em dourado nobre com leve brilho */
    .item-price-inestimavel {
      color: #855605;
      font-weight: 800;
      letter-spacing: 0.04em;
      text-shadow: 0 0 10px rgba(199, 158, 59, 0.28);
    }

    /* ── Valor Total ── */
    .total-value {
      font-family: var(--font-body, -apple-system, sans-serif);
      font-size: 18px;
      font-weight: 700;
      color: #44403C;
      text-align: center;
      margin: 22px 0 0;
      padding-top: 18px;
      border-top: 1px dashed rgba(199, 158, 59, 0.25);
    }

    /* Risco vermelho discreto animado da esquerda para a direita */
    .animated-strike {
      position: relative;
      display: inline-block;
      font-variant-numeric: tabular-nums;
      font-weight: 800;
      color: #121013;
      padding: 0 2px;
    }

    .animated-strike::after {
      content: '';
      position: absolute;
      left: 0;
      top: 50%;
      width: 100%;
      height: 2px;
      background: #D9383A;
      transform-origin: left center;
      transform: scaleX(0);
      transition: transform 0.45s cubic-bezier(0.22, 1, 0.36, 1);
    }

    .animated-strike.is-struck::after {
      transform: scaleX(1);
    }

    .total-value .old-total {
      font-size: 21px;
      margin-left: 6px;
    }

    /* ── Cartão de Preço (Direita no Desktop / Embaixo no Mobile) ── */
    .pricing-box {
      padding: clamp(32px, 4.5vw, 44px) clamp(22px, 3.8vw, 36px);
      text-align: center;
      position: relative;
    }

    /* ── Cronômetro Pílula Escura com Dígitos Dourados ── */
    .pricing-timer-wrap {
      margin-bottom: 26px;
      padding-bottom: 22px;
      border-bottom: 1px solid rgba(199, 158, 59, 0.22);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }

    .pricing-timer-pill {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: #141316;
      border: 1px solid rgba(199, 158, 59, 0.42);
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.16), inset 0 1px 1px rgba(255, 255, 255, 0.08);
      border-radius: 999px;
      padding: 8px 24px;
      transition: transform 0.2s ease;
    }

    .timer-digits {
      font-family: var(--font-body, -apple-system, sans-serif);
      font-size: clamp(22px, 3.8vw, 26px);
      font-weight: 800;
      color: #F3CA68;
      letter-spacing: 0.08em;
      line-height: 1;
      font-variant-numeric: tabular-nums;
      text-shadow: 0 0 12px rgba(243, 202, 104, 0.35);
    }

    .timer-subtext {
      font-family: var(--font-body, -apple-system, sans-serif);
      font-size: 13.5px;
      font-weight: 600;
      color: #55504A;
      margin: 10px auto 0;
      max-width: 270px;
      line-height: 1.35;
      text-align: center;
    }

    /* ── Preço e Chamada ── */
    .pricing-box .callout {
      font-family: var(--font-body, -apple-system, sans-serif);
      font-size: clamp(20px, 2.5vw, 24px);
      font-weight: 800;
      line-height: 1.25;
      letter-spacing: -0.01em;
      color: #1F1C18;
      margin: 0 0 12px;
    }

    .pricing-box .original {
      font-family: var(--font-body, -apple-system, sans-serif);
      font-size: 16px;
      font-weight: 600;
      color: #55504A;
      margin: 0 0 6px;
    }

    .pricing-box .price {
      font-family: 'Barlow', sans-serif;
      font-size: clamp(66px, 9vw, 86px);
      font-weight: 900;
      color: #855605;
      background: linear-gradient(135deg, #A7740B 0%, #855605 50%, #6E4603 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      line-height: 1;
      margin: 6px 0 22px;
      letter-spacing: -2px;
      text-shadow: 0 4px 20px rgba(199, 158, 59, 0.22);
      position: relative;
      display: inline-block;
    }

    /* Brilho suave passageiro sobre o R$29,90 */
    .price-shimmer-active {
      animation: priceShimmerEffect 1s ease-in-out;
    }

    @keyframes priceShimmerEffect {
      0%   { filter: brightness(1); }
      50%  { filter: brightness(1.35) drop-shadow(0 0 16px rgba(243, 202, 104, 0.6)); }
      100% { filter: brightness(1); }
    }

    /* ── Botão Dourado Premium ── */
    .pricing-box .btn-cta {
      display: block;
      width: 100%;
      padding: 18px 24px;
      font-family: var(--font-heading, sans-serif);
      font-size: clamp(16.5px, 2.2vw, 19.5px);
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.03em;
      color: #121013;
      background: linear-gradient(135deg, #F5DE9C 0%, #E2B755 45%, #C79E3B 100%);
      border: 1px solid rgba(255, 255, 255, 0.5);
      border-radius: 999px;
      box-shadow: 0 10px 28px rgba(199, 158, 59, 0.38), 0 2px 6px rgba(0, 0, 0, 0.06);
      text-align: center;
      text-decoration: none;
      cursor: pointer;
      position: relative;
      overflow: hidden;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .pricing-box .btn-cta:hover {
      transform: translateY(-2px);
      box-shadow: 0 14px 36px rgba(199, 158, 59, 0.48);
    }

    .pricing-box .btn-cta:active {
      transform: scale(0.98);
      box-shadow: 0 6px 18px rgba(199, 158, 59, 0.3);
    }

    /* Feixe de luz suave que atravessa o botão a cada ~5s */
    .btn-shimmer-beam {
      position: absolute;
      top: 0;
      left: -130%;
      width: 60%;
      height: 100%;
      background: linear-gradient(90deg, transparent 0%, rgba(255, 255, 255, 0.55) 50%, transparent 100%);
      transform: skewX(-25deg);
      pointer-events: none;
    }

    .btn-sweep-active .btn-shimmer-beam {
      animation: btnBeamSweep 1.2s ease-in-out;
    }

    @keyframes btnBeamSweep {
      0%   { left: -130%; }
      100% { left: 160%; }
    }

    /* ── Garantia e Selos ── */
    .cta-sub {
      display: inline-block;
      font-family: var(--font-body, -apple-system, sans-serif);
      font-size: 14px;
      font-weight: 700;
      text-transform: uppercase;
      color: #855605;
      text-decoration: underline;
      margin-top: 18px;
      letter-spacing: 0.04em;
      transition: color 0.2s ease;
    }

    .cta-sub:hover {
      color: #5d3c03;
    }

    .pricing-seals {
      display: block;
      width: 100%;
      max-width: 250px;
      height: auto;
      margin: 22px auto 0;
    }

    /* ── Mobile First Ajustes (360px, 390px, 768px) ── */
    @media (max-width: 768px) {
      .checklist-card {
        padding: 26px 18px;
        border-radius: 16px;
      }

      .pricing-box {
        padding: 28px 18px;
        border-radius: 16px;
      }

      .checklist-item {
        font-size: 15px;
        padding: 12px 0;
      }

      .bonus-item {
        font-size: 14.5px;
      }

      .bonus-group-wrapper {
        padding-left: 10px;
        margin-left: 2px;
      }

      .item-price {
        font-size: 14.5px;
      }

      .pricing-box .callout {
        font-size: 21px;
      }

      .pricing-box .price {
        font-size: 68px;
      }

      .pricing-box .btn-cta {
        padding: 16px 20px;
        font-size: 16px;
      }
    }

    @media (max-width: 380px) {
      .checklist-card {
        padding: 22px 14px;
      }

      .pricing-box {
        padding: 24px 14px;
      }

      .checklist-item {
        font-size: 14px;
        gap: 10px;
      }

      .item-price {
        font-size: 13.5px;
      }

      .pricing-box .price {
        font-size: 60px;
      }
    }

    /* ── PREFERS-REDUCED-MOTION ── */
    @media (prefers-reduced-motion: reduce) {
      .pricing-mockup-img {
        animation: none !important;
        transform: none !important;
      }

      .checklist-item {
        opacity: 1 !important;
        transform: none !important;
        transition: none !important;
      }

      .item-check-svg .check-path {
        stroke-dashoffset: 0 !important;
        transition: none !important;
      }

      .animated-strike::after {
        transform: scaleX(1) !important;
        transition: none !important;
      }

      .price-shimmer-active {
        animation: none !important;
      }

      .btn-sweep-active .btn-shimmer-beam {
        animation: none !important;
      }
    }
"""
