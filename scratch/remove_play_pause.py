import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove button from HTML
button_html_target = '''        <!-- Botão de controle de animação (somente ícone, acessível) -->
        <button type="button" class="marquee-toggle-btn" id="marqueeToggleBtn" aria-label="Pausar animação das faixas de depoimentos">
          <svg class="icon-pause" viewBox="0 0 24 24" aria-hidden="true">
            <rect x="6" y="4" width="4" height="16" rx="1"/>
            <rect x="14" y="4" width="4" height="16" rx="1"/>
          </svg>
          <svg class="icon-play" viewBox="0 0 24 24" style="display:none;" aria-hidden="true">
            <polygon points="6,4 20,12 6,20"/>
          </svg>
        </button>'''

if button_html_target in content:
    content = content.replace(button_html_target, '')
    print('1. Button HTML removed successfully!')
else:
    print('1. Button HTML target NOT found exactly, checking variant')

# 2. Remove CSS for .marquee-toggle-btn
css_target_1 = '''    /* Botão de Pausar/Tocar as faixas (somente ícone, acessível) */
    .marquee-toggle-btn {
      position: absolute;
      right: 0;
      bottom: -6px;
      background: rgba(22, 20, 24, 0.75);
      border: 1px solid rgba(199, 158, 59, 0.35);
      border-radius: 50%;
      width: 36px;
      height: 36px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      color: #EBC068;
      cursor: pointer;
      transition: all 0.25s ease;
      backdrop-filter: blur(8px);
    }

    .marquee-toggle-btn:hover {
      background: rgba(235, 192, 104, 0.15);
      border-color: #EBC068;
      transform: scale(1.06);
    }

    .marquee-toggle-btn svg {
      width: 16px;
      height: 16px;
      fill: currentColor;
    }'''

if css_target_1 in content:
    content = content.replace(css_target_1, '')
    print('2. CSS rules for marquee-toggle-btn removed successfully!')
else:
    print('2. CSS rules target 1 NOT found')

css_target_2 = '''      .marquee-toggle-btn {
        display: inline-flex;
      }'''
if css_target_2 in content:
    content = content.replace(css_target_2, '')
    print('3. CSS media query 1024px toggle btn removed!')
else:
    print('3. CSS target 2 NOT found')

css_target_3 = '''      .marquee-toggle-btn {
        display: none !important;
      }'''
if css_target_3 in content:
    content = content.replace(css_target_3, '')
    print('4. CSS media query reduced-motion toggle btn removed!')
else:
    print('4. CSS target 3 NOT found')

# 3. Clean up JS
js_target = '''      /* 4. Desktop Marquee: Botão de Pausar/Tocar e Auto-Pausa Fora do Viewport */
      var toggleBtn = document.getElementById('marqueeToggleBtn');
      var isManuallyPaused = false;

      if (toggleBtn) {
        var iconPause = toggleBtn.querySelector('.icon-pause');
        var iconPlay = toggleBtn.querySelector('.icon-play');

        toggleBtn.addEventListener('click', function () {
          isManuallyPaused = !isManuallyPaused;
          if (isManuallyPaused) {
            sec.classList.add('testimonials-paused');
            if (iconPause) iconPause.style.display = 'none';
            if (iconPlay) iconPlay.style.display = 'block';
            toggleBtn.setAttribute('aria-label', 'Retomar animação das faixas de depoimentos');
          } else {
            sec.classList.remove('testimonials-paused');
            if (iconPause) iconPause.style.display = 'block';
            if (iconPlay) iconPlay.style.display = 'none';
            toggleBtn.setAttribute('aria-label', 'Pausar animação das faixas de depoimentos');
          }
        });
      }

      /* Pausa automática quando sai do viewport para economizar CPU/bateria */
      if ('IntersectionObserver' in window && !isReducedMotion) {
        var marqueeViewObs = new IntersectionObserver(function (entries) {
          entries.forEach(function (entry) {
            if (!entry.isIntersecting && !isManuallyPaused) {
              sec.classList.add('testimonials-paused');
            } else if (entry.isIntersecting && !isManuallyPaused) {
              sec.classList.remove('testimonials-paused');
            }
          });
        }, { threshold: 0.05 });
        marqueeViewObs.observe(sec);
      }'''

js_replacement = '''      /* 4. Desktop Marquee: Auto-Pausa Fora do Viewport para economizar CPU/bateria */
      if ('IntersectionObserver' in window && !isReducedMotion) {
        var marqueeViewObs = new IntersectionObserver(function (entries) {
          entries.forEach(function (entry) {
            if (!entry.isIntersecting) {
              sec.classList.add('testimonials-paused');
            } else {
              sec.classList.remove('testimonials-paused');
            }
          });
        }, { threshold: 0.05 });
        marqueeViewObs.observe(sec);
      }'''

if js_target in content:
    content = content.replace(js_target, js_replacement)
    print('5. JS toggle logic replaced with clean viewport observer!')
else:
    print('5. JS target NOT found')

with open('p12/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated p12/index.html successfully.')
