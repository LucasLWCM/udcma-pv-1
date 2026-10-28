import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Replace CSS for Copy Final (#closing)
css_start = '/* ── Copy final ── */'
css_end = '/* ── FAQ ── */'
p1 = c.find(css_start)
p2 = c.find(css_end)

if p1 == -1 or p2 == -1:
    print(f"Error: CSS anchors not found (p1={p1}, p2={p2})")
    sys.exit(1)

new_css = """/* ═════════════════════════════════════════════════════════════════════════
       DOBRA 11: SEÇÃO COPY FINAL PERSUASÃO (#closing)
    ═════════════════════════════════════════════════════════════════════════ */
    /* Linha divisória de emenda com a dobra anterior */
    .closing-divider-wrap {
      width: 100%;
      max-width: 720px;
      margin: 0 auto;
      padding: 0 24px;
      box-sizing: border-box;
    }

    .closing-divider-line {
      height: 1px;
      width: 100%;
      background: linear-gradient(90deg, transparent 0%, #EBC068 25%, #C79E3B 75%, transparent 100%);
      transform-origin: left center;
      transform: scaleX(0);
      transition: transform 1s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .closing-divider-wrap.is-inview .closing-divider-line {
      transform: scaleX(1);
    }

    #closing {
      position: relative;
      padding: clamp(70px, 10vw, 120px) 20px clamp(80px, 12vw, 140px);
      background-color: #0E0E0E;
      overflow: hidden;
      text-align: center;
    }

    /* Luz de Amanhecer (Degradê Radial Dourado Quente que sobe com o scroll) */
    .closing-dawn-glow {
      position: absolute;
      bottom: -4%;
      left: 50%;
      width: clamp(550px, 90vw, 950px);
      height: clamp(500px, 80vw, 850px);
      background: radial-gradient(
        ellipse 60% 50% at 50% 65%,
        rgba(235, 192, 104, 0.22) 0%,
        rgba(199, 158, 59, 0.11) 40%,
        rgba(140, 70, 10, 0.04) 70%,
        transparent 100%
      );
      transform: translate3d(-50%, 60px, 0);
      opacity: 0.45;
      pointer-events: none;
      z-index: 0;
      transition: transform 0.2s ease-out, opacity 0.2s ease-out;
      will-change: transform, opacity;
    }

    #closing .container {
      position: relative;
      z-index: 1;
      width: 100%;
      max-width: 720px;
      margin: 0 auto;
      padding: 0 clamp(8px, 2vw, 16px);
      box-sizing: border-box;
    }

    /* Caixa com borda removida: bloco amplo, limpo e centralizado */
    .closing-box {
      width: 100%;
      margin: 0 auto;
      text-align: center;
      border: none;
      box-shadow: none;
      background: transparent;
      padding: 0;
    }

    /* Título em fonte serifada dourada */
    .closing-question {
      font-family: var(--font-heading, 'Cormorant Garamond', Georgia, serif);
      font-size: clamp(26px, 4.4vw, 40px);
      font-weight: 700;
      line-height: 1.25;
      color: var(--cta-primary, #EBC068);
      text-align: center;
      margin-bottom: clamp(40px, 6vw, 56px);
      text-wrap: balance;
      letter-spacing: -0.01em;
      text-shadow: 0 2px 14px rgba(235, 192, 104, 0.15);
    }

    .closing-body {
      display: flex;
      flex-direction: column;
      gap: clamp(26px, 4vw, 38px);
      align-items: center;
      max-width: 680px;
      margin: 0 auto;
    }

    /* Frases de apoio em branco suave, peso normal, tamanho de leitura (>= 16px) */
    .closing-item {
      font-family: var(--font-body, 'Barlow', sans-serif);
      font-size: clamp(16px, 2vw, 18px);
      line-height: 1.65;
      color: #E2DDD5;
      font-weight: 400;
      max-width: 640px;
      margin: 0 auto;
      text-align: center;
    }

    /* Destaque 1: "A real?" */
    .closing-item-areal {
      margin: clamp(10px, 1.8vw, 16px) auto;
    }

    .closing-item-areal strong {
      font-family: var(--font-heading, 'Cormorant Garamond', Georgia, serif);
      font-size: clamp(24px, 3.5vw, 30px);
      font-weight: 700;
      color: #FFFFFF;
      letter-spacing: 0.01em;
      text-shadow: 0 0 20px rgba(235, 192, 104, 0.2);
      display: inline-block;
    }

    /* Destaque 2: "É quem tem o plano certo." com traço dourado desenhado */
    .closing-highlight-draw {
      position: relative;
      display: inline-block;
      color: #FFFFFF;
      font-weight: 700;
      font-size: clamp(18px, 2.3vw, 21px);
    }

    .closing-highlight-draw::after {
      content: '';
      position: absolute;
      bottom: -3px;
      left: 0;
      width: 100%;
      height: 1.5px;
      background: linear-gradient(90deg, #EBC068, #C79E3B);
      transform-origin: left center;
      transform: scaleX(0);
      transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.3s;
      border-radius: 1px;
    }

    .closing-item.is-inview .closing-highlight-draw::after {
      transform: scaleX(1);
    }

    /* Destaque 3: "E o plano tá aqui. / Um Dia com Marco Aurélio." */
    .closing-item-plan-here {
      font-size: clamp(18px, 2.3vw, 20px);
      color: #EDE8DF;
    }

    .closing-plan-name {
      font-family: var(--font-heading, 'Cormorant Garamond', Georgia, serif);
      font-size: clamp(24px, 3.5vw, 31px);
      font-weight: 700;
      font-style: italic;
      color: var(--cta-primary, #EBC068);
      display: inline-block;
      margin-top: 6px;
      text-shadow: 0 0 16px rgba(235, 192, 104, 0.25);
    }

    /* Destaque 4: Pergunta Final com bastante espaço antes */
    .closing-item-final {
      margin-top: clamp(40px, 6vw, 62px);
      max-width: 680px;
    }

    .closing-final-lead {
      display: inline-block;
      font-size: clamp(15px, 1.8vw, 17px);
      font-weight: 600;
      color: var(--text-secondary, #C2BCB0);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 12px;
    }

    .closing-final-ask {
      font-family: var(--font-heading, 'Cormorant Garamond', Georgia, serif);
      font-size: clamp(28px, 4.6vw, 42px);
      font-weight: 700;
      line-height: 1.25;
      color: #FFFFFF;
      text-wrap: balance;
      display: block;
      text-shadow: 0 2px 24px rgba(235, 192, 104, 0.28);
    }

    /* ══════════════════════════════════════
       ANIMAÇÃO RESILIENTE (Progressive Enhancement)
       Padrão = visível no estado final (no-JS e reduced motion)
       Classe .closing-anim-ready adicionada apenas se JS ativo e sem reduced-motion
    ══════════════════════════════════════ */
    .closing-anim-ready .closing-question,
    .closing-anim-ready .closing-item {
      opacity: 0;
      transform: translateY(14px);
      transition: opacity 0.6s ease, transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .closing-anim-ready .closing-question.is-inview,
    .closing-anim-ready .closing-item.is-inview {
      opacity: 1;
      transform: translateY(0);
    }

    /* PREFERS-REDUCED-MOTION */
    @media (prefers-reduced-motion: reduce) {
      .closing-anim-ready .closing-question,
      .closing-anim-ready .closing-item,
      .closing-divider-line {
        opacity: 1 !important;
        transform: none !important;
        transition: none !important;
      }
      .closing-highlight-draw::after {
        transform: scaleX(1) !important;
        transition: none !important;
      }
      .closing-dawn-glow {
        opacity: 0.65 !important;
        transform: translate3d(-50%, 0, 0) !important;
        transition: none !important;
      }
    }

    """

c = c[:p1] + new_css + c[p2:]

# 2. Replace HTML for Closing section
html_start = '<!-- ═══════════════════════════════════\n       SEÇÃO: COPY FINAL PERSUASÃO'
html_end = '<!-- ═══════════════════════════════════\n       SEÇÃO: FAQ + CTA 3'

h1 = c.find(html_start)
h2 = c.find(html_end)

if h1 == -1 or h2 == -1:
    print(f"Error: HTML anchors not found (h1={h1}, h2={h2})")
    sys.exit(1)

new_html = """<!-- ═══════════════════════════════════
       SEÇÃO: COPY FINAL PERSUASÃO (DOBRA 11 P12)
  ════════════════════════════════════ -->
  <div class="closing-divider-wrap">
    <div class="closing-divider-line"></div>
  </div>

  <section id="closing">
    <div class="closing-dawn-glow" aria-hidden="true"></div>
    <div class="container">
      <div class="closing-box">
        <h2 class="closing-question">Você ainda vai ficar assistindo os outros aprofundando e vivendo o estoicismo
          enquanto você só coleciona frases?</h2>
        <div class="closing-body">
          <p class="closing-item">Todo mundo fala que estoicismo muda vidas.<br>Mas ninguém mostra o que fazer quando ele não funciona pra
            você.</p>
          <p class="closing-item">Você já comprou livros. Já assistiu vídeos. Já salvou dezenas de posts.<br>Mas se ainda não mudou, é porque
            tá faltando a peça certa.</p>
          <p class="closing-item closing-item-areal"><strong>A real?</strong></p>
          <p class="closing-item">Quem entende estoicismo de verdade não é quem consome mais.<br><span class="closing-highlight-draw">É quem tem o plano certo.</span></p>
          <p class="closing-item closing-item-plan-here">E o plano tá aqui.<br><em class="closing-plan-name closing-highlight-draw">Um Dia com Marco Aurélio.</em></p>
          <p class="closing-item closing-item-final">
            <span class="closing-final-lead">Agora é contigo.</span><br>
            <span class="closing-final-ask">Vai continuar só acumulando... ou vai viver esse dia?</span>
          </p>
        </div>
      </div>
    </div>
  </section>

  <div class="section-divider"></div>

  """

c = c[:h1] + new_html + c[h2:]

# 3. Add Dobra 11 Script right after Dobra 10 script
d10_script_anchor = 'SCRIPT: DOBRA 10 — GARANTIA 7 DIAS'
sp10 = c.find(d10_script_anchor)
if sp10 == -1:
    print("Error: Dobra 10 script anchor not found")
    sys.exit(1)

# Find the end of dobra 10's </script>
end_d10_script = c.find('</script>', sp10)
if end_d10_script == -1:
    print("Error: </script> after Dobra 10 not found")
    sys.exit(1)

end_d10_script += len('</script>')

new_script = """

  <!-- ═════════════════════════════════════════════════════════════════════════
       SCRIPT: DOBRA 11 — COPY FINAL PERSUASÃO & LUZ DE AMANHECER
  ═════════════════════════════════════════════════════════════════════════ -->
  <script>
  (function () {
    'use strict';
    var section = document.getElementById('closing');
    if (!section) return;

    var dividerWrap = document.querySelector('.closing-divider-wrap');
    var glow = section.querySelector('.closing-dawn-glow');
    var prefersReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // Se preferir movimento reduzido, mantém tudo estático
    if (prefersReduced) return;

    // Ativa animações progressivas
    section.classList.add('closing-anim-ready');

    // Observador de entrada dos parágrafos e título
    var elementsToAnimate = section.querySelectorAll('.closing-question, .closing-item');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-inview');
          io.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.15,
      rootMargin: '0px 0px -30px 0px'
    });

    elementsToAnimate.forEach(function (el) {
      io.observe(el);
    });

    // Linha divisória de emenda
    if (dividerWrap) {
      var lineIo = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            dividerWrap.classList.add('is-inview');
            lineIo.unobserve(dividerWrap);
          }
        });
      }, { threshold: 0.2 });
      lineIo.observe(dividerWrap);
    }

    // Luz de amanhecer que sobe e intensifica com o scroll
    var ticking = false;
    function updateDawn() {
      var rect = section.getBoundingClientRect();
      var winH = window.innerHeight;
      var totalRange = rect.height + winH * 0.4;
      var progress = Math.max(0, Math.min(1, (winH - rect.top) / totalRange));
      if (glow) {
        var yOffset = (1 - progress) * 80;
        var opacity = 0.35 + (progress * 0.65);
        glow.style.transform = 'translate3d(-50%, ' + yOffset.toFixed(1) + 'px, 0)';
        glow.style.opacity = opacity.toFixed(2);
      }
      ticking = false;
    }

    window.addEventListener('scroll', function () {
      if (!ticking) {
        window.requestAnimationFrame(updateDawn);
        ticking = true;
      }
    }, { passive: true });

    updateDawn();
  })();
  </script>"""

c = c[:end_d10_script] + new_script + c[end_d10_script:]

with open('p12/index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Dobra 11 successfully applied to p12/index.html!")
