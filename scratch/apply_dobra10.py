import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Replace CSS
css_start = '/* ── Garantia ── */'
css_end = '/* ── Copy final ── */'
p1 = c.find(css_start)
p2 = c.find(css_end)
if p1 == -1 or p2 == -1:
    print("Error: CSS anchors not found", p1, p2)
    sys.exit(1)

new_css = """/* ═════════════════════════════════════════════════════════════════════════
       DOBRA 10: SEÇÃO GARANTIA ("7 DIAS DE GARANTIA")
    ═════════════════════════════════════════════════════════════════════════ */
    #guarantee {
      padding: clamp(60px, 8vw, 90px) 16px;
      background-color: #0E0E0E;
      background-image: radial-gradient(ellipse 650px 420px at 50% 50%, rgba(235, 192, 104, 0.08) 0%, rgba(180, 120, 30, 0.02) 50%, transparent 75%);
      position: relative;
      overflow: hidden;
    }

    #guarantee .container {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
      max-width: 1200px;
      margin: 0 auto;
    }

    .guarantee-card {
      background: #FFFFFF;
      border-radius: 28px;
      padding: clamp(36px, 5vw, 48px) clamp(20px, 4vw, 36px);
      max-width: 500px;
      width: 100%;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45), 0 0 0 1px rgba(255, 255, 255, 0.08);
      text-align: center;
      margin: 0 auto;
      box-sizing: border-box;
      position: relative;
    }

    /* Badge com '7' e Anel fino de 7 marcas (uma por dia) */
    .guarantee-badge {
      position: relative;
      width: 160px;
      height: 160px;
      margin: 0 auto 10px;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .guarantee-ring {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
    }

    .ring-track {
      stroke: rgba(133, 86, 5, 0.18);
      stroke-width: 1.5;
    }

    .ring-mark {
      fill: #855605;
      opacity: 1;
      transform-origin: center;
    }

    .guarantee-card .huge-number {
      font-family: 'Barlow', sans-serif;
      font-size: clamp(96px, 12vw, 115px);
      font-weight: 900;
      color: #855605;
      line-height: 0.95;
      display: block;
      position: relative;
      z-index: 1;
      letter-spacing: -0.02em;
      user-select: none;
    }

    .guarantee-card h2 {
      font-family: 'Barlow', sans-serif;
      font-size: clamp(24px, 3.5vw, 30px);
      font-weight: 900;
      color: #855605;
      margin-bottom: 14px;
      letter-spacing: 0.03em;
      text-transform: uppercase;
    }

    .guarantee-card p {
      font-family: 'Barlow', sans-serif;
      font-size: clamp(16px, 2vw, 17px);
      color: #1C1917;
      font-weight: 500;
      line-height: 1.5;
      margin: 0 auto;
      max-width: 420px;
    }

    /* Linha fina separadora */
    .guarantee-divider {
      border: none;
      border-top: 1px solid rgba(0, 0, 0, 0.09);
      margin: 22px 0;
      width: 100%;
    }

    /* Estatísticas aprovadas (dois números) */
    .guarantee-stats {
      display: flex;
      flex-direction: column;
      gap: 12px;
      align-items: center;
      justify-content: center;
    }

    @media (min-width: 520px) {
      .guarantee-stats {
        flex-direction: row;
        justify-content: space-between;
        gap: 16px;
        align-items: flex-start;
      }
    }

    .stat-item {
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    @media (min-width: 520px) {
      .stat-item {
        align-items: flex-start;
      }
    }

    .stat-line {
      display: inline-flex;
      align-items: baseline;
      gap: 6px;
      white-space: nowrap;
    }

    .stat-num {
      font-family: 'Barlow', sans-serif;
      font-size: clamp(19px, 2.2vw, 21px);
      font-weight: 800;
      color: #855605;
      line-height: 1.2;
      letter-spacing: -0.01em;
    }

    .stat-label {
      font-family: 'Barlow', sans-serif;
      font-size: clamp(14px, 1.6vw, 15px);
      font-weight: 600;
      color: #634003;
      line-height: 1.2;
    }

    /* Barra horizontal fina do 0,70% */
    .refund-bar-track {
      width: 100%;
      max-width: 170px;
      height: 3px;
      background: rgba(133, 86, 5, 0.16);
      border-radius: 999px;
      margin-top: 6px;
      overflow: hidden;
    }

    @media (max-width: 519px) {
      .refund-bar-track {
        margin-left: auto;
        margin-right: auto;
      }
    }

    .refund-bar-fill {
      height: 100%;
      width: 0.70%;
      min-width: 2px;
      background: #855605;
      border-radius: 999px;
    }

    /* Botão CTA Garantia */
    .guarantee-card .btn-cta {
      display: block;
      width: 100%;
      background: linear-gradient(180deg, #F5D27E 0%, #E2B34B 100%);
      color: #0E0E0E;
      font-family: 'Barlow', sans-serif;
      font-size: clamp(16px, 2vw, 18px);
      font-weight: 800;
      padding: 18px 24px;
      border-radius: 999px;
      border: none;
      box-shadow: 0 4px 18px rgba(226, 179, 75, 0.42);
      text-decoration: none;
      transition: transform 0.15s ease, box-shadow 0.15s ease;
      cursor: pointer;
      box-sizing: border-box;
      position: relative;
      overflow: hidden;
      user-select: none;
      -webkit-tap-highlight-color: transparent;
    }

    .guarantee-card .btn-cta:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 22px rgba(226, 179, 75, 0.6);
    }

    .guarantee-card .btn-cta:active {
      transform: scale(0.985) translateY(1px);
      box-shadow: 0 2px 8px rgba(226, 179, 75, 0.35);
    }

    /* Luz de shimmer no botão */
    .guarantee-card .btn-cta::after {
      content: '';
      position: absolute;
      top: -50%;
      bottom: -50%;
      left: 0;
      width: 60px;
      background: linear-gradient(
        90deg,
        rgba(255, 255, 255, 0) 0%,
        rgba(255, 255, 255, 0.55) 50%,
        rgba(255, 255, 255, 0) 100%
      );
      transform: skewX(-25deg) translateX(-150px);
      pointer-events: none;
    }

    .guarantee-card.btn-shimmer-active .btn-cta::after {
      animation: btnShimmerSweep 5s cubic-bezier(0.4, 0, 0.2, 1) infinite;
    }

    @keyframes btnShimmerSweep {
      0% { transform: skewX(-25deg) translateX(-150px); }
      18% { transform: skewX(-25deg) translateX(450px); }
      100% { transform: skewX(-25deg) translateX(450px); }
    }

    /* Link sublinhado abaixo do botão */
    .guarantee-card .cta-sub {
      display: inline-block;
      font-family: 'Barlow', sans-serif;
      font-size: 16px;
      font-weight: 800;
      text-transform: uppercase;
      color: #855605;
      text-decoration: underline;
      font-style: italic;
      letter-spacing: 0.05em;
      margin-top: 18px;
      transition: color 0.2s ease;
    }

    .guarantee-card .cta-sub:hover {
      color: #5d3c03;
    }

    /* ══════════════════════════════════════
       ANIMAÇÃO RESILIENTE (Progressive Enhancement)
       Estado padrão = visível e final (no-JS / reduced motion)
       Se JS ativo e motion permitido = adiciona classe .p12-guarantee-anim
    ══════════════════════════════════════ */
    .p12-guarantee-anim .huge-number {
      opacity: 0;
      transform: scale(0.92);
      transition: opacity 0.45s ease 0.1s, transform 0.45s cubic-bezier(0.16, 1, 0.3, 1) 0.1s;
    }

    .p12-guarantee-anim .ring-mark {
      opacity: 0.18;
      transition: opacity 0.35s ease, fill 0.35s ease;
    }

    .p12-guarantee-anim .guarantee-card h2,
    .p12-guarantee-anim .guarantee-card p {
      opacity: 0;
      transform: translateY(12px);
      transition: opacity 0.5s ease, transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .p12-guarantee-anim .guarantee-card h2 { transition-delay: 0.65s; }
    .p12-guarantee-anim .guarantee-card p  { transition-delay: 0.75s; }

    .p12-guarantee-anim .guarantee-divider {
      opacity: 0;
      transition: opacity 0.4s ease 0.85s;
    }

    .p12-guarantee-anim .stat-students {
      opacity: 0;
      transform: translateY(10px);
      transition: opacity 0.5s ease 0.95s, transform 0.5s cubic-bezier(0.16, 1, 0.3, 1) 0.95s;
    }

    .p12-guarantee-anim .stat-refund {
      opacity: 0;
      transform: translateY(10px);
      transition: opacity 0.5s ease 1.15s, transform 0.5s cubic-bezier(0.16, 1, 0.3, 1) 1.15s;
    }

    .p12-guarantee-anim .refund-bar-fill {
      width: 0;
      min-width: 0;
      transition: width 0.75s cubic-bezier(0.16, 1, 0.3, 1) 1.35s;
    }

    .p12-guarantee-anim .btn-cta {
      opacity: 0;
      transform: translateY(14px);
      transition: opacity 0.5s ease 1.55s, transform 0.5s cubic-bezier(0.16, 1, 0.3, 1) 1.55s, box-shadow 0.15s ease;
    }

    .p12-guarantee-anim .cta-sub {
      opacity: 0;
      transition: opacity 0.5s ease 1.75s, color 0.2s ease;
    }

    /* ESTADO REVELADO (is-revealed) */
    .p12-guarantee-anim.is-revealed .huge-number {
      opacity: 1;
      transform: scale(1);
    }

    .p12-guarantee-anim.is-revealed .ring-mark {
      opacity: 1;
    }
    .p12-guarantee-anim.is-revealed .ring-mark.mark-1 { transition-delay: 0.20s; }
    .p12-guarantee-anim.is-revealed .ring-mark.mark-2 { transition-delay: 0.27s; }
    .p12-guarantee-anim.is-revealed .ring-mark.mark-3 { transition-delay: 0.34s; }
    .p12-guarantee-anim.is-revealed .ring-mark.mark-4 { transition-delay: 0.41s; }
    .p12-guarantee-anim.is-revealed .ring-mark.mark-5 { transition-delay: 0.48s; }
    .p12-guarantee-anim.is-revealed .ring-mark.mark-6 { transition-delay: 0.55s; }
    .p12-guarantee-anim.is-revealed .ring-mark.mark-7 { transition-delay: 0.62s; }

    .p12-guarantee-anim.is-revealed .guarantee-card h2,
    .p12-guarantee-anim.is-revealed .guarantee-card p {
      opacity: 1;
      transform: translateY(0);
    }

    .p12-guarantee-anim.is-revealed .guarantee-divider {
      opacity: 1;
    }

    .p12-guarantee-anim.is-revealed .stat-students,
    .p12-guarantee-anim.is-revealed .stat-refund {
      opacity: 1;
      transform: translateY(0);
    }

    .p12-guarantee-anim.is-revealed .refund-bar-fill {
      width: 0.70%;
      min-width: 2px;
    }

    .p12-guarantee-anim.is-revealed .btn-cta {
      opacity: 1;
      transform: translateY(0);
    }

    .p12-guarantee-anim.is-revealed .cta-sub {
      opacity: 1;
    }

    /* PREFERS-REDUCED-MOTION */
    @media (prefers-reduced-motion: reduce) {
      .p12-guarantee-anim .huge-number,
      .p12-guarantee-anim .ring-mark,
      .p12-guarantee-anim .guarantee-card h2,
      .p12-guarantee-anim .guarantee-card p,
      .p12-guarantee-anim .guarantee-divider,
      .p12-guarantee-anim .stat-students,
      .p12-guarantee-anim .stat-refund,
      .p12-guarantee-anim .refund-bar-fill,
      .p12-guarantee-anim .btn-cta,
      .p12-guarantee-anim .cta-sub {
        opacity: 1 !important;
        transform: none !important;
        transition: none !important;
      }
      .p12-guarantee-anim .refund-bar-fill {
        width: 0.70% !important;
        min-width: 2px !important;
      }
      .guarantee-card .btn-cta::after {
        display: none !important;
        animation: none !important;
      }
    }

    """

c = c[:p1] + new_css + c[p2:]

# 2. Replace HTML
html_start = '<!-- ═══════════════════════════════════\n       SEÇÃO: GARANTIA + CTA 2\n  ════════════════════════════════════ -->'
html_end = '<!-- ═══════════════════════════════════\n       SEÇÃO: COPY FINAL PERSUASÃO'

h1 = c.find(html_start)
h2 = c.find(html_end)
if h1 == -1 or h2 == -1:
    print("Error: HTML anchors not found", h1, h2)
    sys.exit(1)

new_html = """<!-- ═══════════════════════════════════
       SEÇÃO: GARANTIA + CTA 2 (DOBRA 10 P12)
  ════════════════════════════════════ -->
  <section id="guarantee">
    <div class="container">
      <div class="guarantee-card">
        <div class="guarantee-badge">
          <svg class="guarantee-ring" viewBox="0 0 180 180" aria-hidden="true" focusable="false">
            <circle class="ring-track" cx="90" cy="90" r="70" fill="none" />
            <circle class="ring-mark mark-1" cx="90.0" cy="20.0" r="4.5" />
            <circle class="ring-mark mark-2" cx="144.73" cy="46.36" r="4.5" />
            <circle class="ring-mark mark-3" cx="158.24" cy="105.57" r="4.5" />
            <circle class="ring-mark mark-4" cx="120.37" cy="153.07" r="4.5" />
            <circle class="ring-mark mark-5" cx="59.63" cy="153.07" r="4.5" />
            <circle class="ring-mark mark-6" cx="21.76" cy="105.57" r="4.5" />
            <circle class="ring-mark mark-7" cx="35.27" cy="46.36" r="4.5" />
          </svg>
          <span class="huge-number">7</span>
        </div>

        <h2>DIAS DE GARANTIA</h2>
        <p>Você tem 7 dias para pedir seu dinheiro de volta.<br>Sem perguntas. Sem complicação.</p>

        <!-- Linha fina separadora antes dos números -->
        <hr class="guarantee-divider" aria-hidden="true">

        <!-- ATUALIZAR: dados conferidos em 27/10/2026. Alunos somam Hotmart e outras plataformas; o reembolso é só da Hotmart. -->
        <div class="guarantee-stats">
          <div class="stat-item stat-students">
            <div class="stat-line">
              <span class="stat-num">Mais de 3 mil</span>
              <span class="stat-label">alunos</span>
            </div>
          </div>
          <div class="stat-item stat-refund">
            <div class="stat-line">
              <span class="stat-num">0,70%</span>
              <span class="stat-label">de reembolso na Hotmart</span>
            </div>
            <div class="refund-bar-track" aria-hidden="true">
              <div class="refund-bar-fill"></div>
            </div>
          </div>
        </div>

        <!-- Linha fina separadora depois dos números -->
        <hr class="guarantee-divider" aria-hidden="true">

        <a href="https://pay.hotmart.com/X108154869T?off=953h3rmf" class="btn-cta">
          Quero aproveitar a garantia!
        </a>
        <a href="https://pay.hotmart.com/X108154869T?off=953h3rmf" class="cta-sub">
          Acesso IMEDIATO e VITALÍCIO
        </a>
      </div>
    </div>
  </section>

  <div class="section-divider"></div>

  """

c = c[:h1] + new_html + c[h2:]

# 3. Add Dobra 10 Script
script_needle = 'function playVideo()'
sp = c.find(script_needle)
if sp == -1:
    print("Error: script anchor not found")
    sys.exit(1)

new_script = """<!-- ═════════════════════════════════════════════════════════════════════════
       SCRIPT: DOBRA 10 — GARANTIA 7 DIAS
  ═════════════════════════════════════════════════════════════════════════ -->
  <script>
  (function () {
    'use strict';
    var section = document.getElementById('guarantee');
    if (!section) return;

    var card = section.querySelector('.guarantee-card');
    var prefersReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // Se preferir movimento reduzido, mantém tudo estático no estado final
    if (prefersReduced) return;

    // Ativa animação apenas com JavaScript ativo
    section.classList.add('p12-guarantee-anim');

    var revealed = false;

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          if (!revealed) {
            revealed = true;
            section.classList.add('is-revealed');

            // Ativa o shimmer do botão após sua entrada (~2.0s)
            setTimeout(function () {
              if (card) card.classList.add('btn-shimmer-active');
            }, 2000);
          } else if (card) {
            card.classList.add('btn-shimmer-active');
          }
        } else if (card) {
          // Pausa shimmer fora da tela para poupar bateria e recursos
          card.classList.remove('btn-shimmer-active');
        }
      });
    }, {
      threshold: 0.15
    });

    observer.observe(section);
  })();
  </script>

  """

# Look for the <script> preceding playVideo
script_tag_pos = c.rfind('<script>', 0, sp)
c = c[:script_tag_pos] + new_script + c[script_tag_pos:]

with open('p12/index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Successfully applied Dobra 10 to p12/index.html!")
