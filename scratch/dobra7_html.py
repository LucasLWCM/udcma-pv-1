DOBRA7_HTML = """  <!-- ═══════════════════════════════════════════════════════════════════════
       DOBRA 7: SEÇÃO DE PREÇO / CTA (P12)
       Mockup no topo, checklist com soma interativa, cronômetro idêntico e preço
  ══════════════════════════════════════════════════════════════════════════ -->
  <div class="pricing-seam-line" aria-hidden="true"></div>

  <section id="pricing">
    <div class="container">

      <!-- 1. Imagem do produto (Mockup) no topo com brilho suave e flutuação sutil -->
      <div class="pricing-mockup-wrapper">
        <div class="pricing-mockup-glow" aria-hidden="true"></div>
        <img class="deco-img pricing-mockup-img" src="../img/ref/mckp6.webp" alt="Série Um Dia Com Marco Aurélio Mockup" width="1024"
          height="898" loading="lazy" decoding="async">
      </div>

      <!-- Layout dos dois cartões elevados (Desktop 2 colunas / Mobile 1 coluna) -->
      <div class="pricing-cards-layout">

        <!-- ── CARTÃO 1: CHECKLIST DE BENEFÍCIOS E BÔNUS ── -->
        <div class="checklist-card pricing-card-white" id="checklistCard">
          <h2 class="pricing-title">VEJA TUDO QUE VOCÊ VAI RECEBER:</h2>

          <ul class="includes-list" id="includesList">
            <!-- Item 1: Episódios Cinematográficos -->
            <li class="checklist-item item-main" data-sum-step="97">
              <div class="item-left">
                <svg class="item-check-svg" viewBox="0 0 20 20" fill="none" aria-hidden="true">
                  <circle cx="10" cy="10" r="8" />
                  <path class="check-path" d="M6 10.2l2.6 2.6L14 7.5" />
                </svg>
                <div class="item-text-group">
                  <span class="item-name"><strong>3 episódios cinematográficos</strong></span>
                  <em class="item-note">(sem aula chata em slide)</em>
                </div>
              </div>
              <span class="item-price">R$ 97,00</span>
            </li>

            <!-- Item 2: Acesso Vitalício -->
            <li class="checklist-item item-main" data-sum-step="97">
              <div class="item-left">
                <svg class="item-check-svg" viewBox="0 0 20 20" fill="none" aria-hidden="true">
                  <circle cx="10" cy="10" r="8" />
                  <path class="check-path" d="M6 10.2l2.6 2.6L14 7.5" />
                </svg>
                <div class="item-text-group">
                  <span class="item-name"><strong>Acesso VITALÍCIO ao conteúdo</strong></span>
                  <em class="item-note">(só para quem comprar esse mês)</em>
                </div>
              </div>
              <span class="item-price item-price-inestimavel">R$ INESTIMÁVEL</span>
            </li>

            <!-- Grupo dos 4 Bônus com filete vertical dourado ao lado -->
            <div class="bonus-group-wrapper">
              <!-- Bônus 1 -->
              <li class="checklist-item bonus-item" data-sum-step="144">
                <div class="item-left">
                  <svg class="item-check-svg" viewBox="0 0 20 20" fill="none" aria-hidden="true">
                    <circle cx="10" cy="10" r="8" />
                    <path class="check-path" d="M6 10.2l2.6 2.6L14 7.5" />
                  </svg>
                  <span class="item-name"><strong>Bônus 1 —</strong> O Roteiro Estoico</span>
                </div>
                <span class="item-price">R$ 47,00</span>
              </li>

              <!-- Bônus 2 -->
              <li class="checklist-item bonus-item" data-sum-step="211">
                <div class="item-left">
                  <svg class="item-check-svg" viewBox="0 0 20 20" fill="none" aria-hidden="true">
                    <circle cx="10" cy="10" r="8" />
                    <path class="check-path" d="M6 10.2l2.6 2.6L14 7.5" />
                  </svg>
                  <span class="item-name"><strong>Bônus 2 —</strong> O Estoico em Campo</span>
                </div>
                <span class="item-price">R$ 67,00</span>
              </li>

              <!-- Bônus 3 -->
              <li class="checklist-item bonus-item" data-sum-step="230">
                <div class="item-left">
                  <svg class="item-check-svg" viewBox="0 0 20 20" fill="none" aria-hidden="true">
                    <circle cx="10" cy="10" r="8" />
                    <path class="check-path" d="M6 10.2l2.6 2.6L14 7.5" />
                  </svg>
                  <span class="item-name"><strong>Bônus 3 —</strong> Sementes Matinais (12 meses)</span>
                </div>
                <span class="item-price">R$ 19,00</span>
              </li>

              <!-- Bônus 4 -->
              <li class="checklist-item bonus-item" data-sum-step="297">
                <div class="item-left">
                  <svg class="item-check-svg" viewBox="0 0 20 20" fill="none" aria-hidden="true">
                    <circle cx="10" cy="10" r="8" />
                    <path class="check-path" d="M6 10.2l2.6 2.6L14 7.5" />
                  </svg>
                  <span class="item-name"><strong>Bônus 4 —</strong> Noites de Pórtico</span>
                </div>
                <span class="item-price">R$ 67,00</span>
              </li>
            </div>
          </ul>

          <!-- Valor total com contagem de soma e risco vermelho -->
          <p class="total-value">Valor total: <span class="old-total animated-strike is-struck" id="totalValueDisplay">R$ 297,00</span></p>
        </div>

        <!-- ── CARTÃO 2: CRONÔMETRO, PREÇO, BOTÃO E GARANTIA ── -->
        <div class="pricing-box pricing-card-white" id="pricingBox">

          <!-- Bloco do Cronômetro (lógica original intacta) -->
          <div class="pricing-timer-wrap">
            <div id="scarcity-timer-wrap" class="pricing-timer-pill">
              <div id="countdown-timer" class="timer-digits">24:00:00</div>
            </div>
            <p class="timer-subtext">Após o cronômetro zerar, o valor vai para R$ 97,00</p>
          </div>

          <!-- Oferta e Valores -->
          <p class="callout">Hoje você garante tudo isso por apenas:</p>
          <p class="original">de <span class="strike-price animated-strike is-struck" id="strikeOriginalPrice">R$ 297,00</span> por:</p>
          <div class="price" id="mainPriceDisplay">R$29,90</div>

          <!-- Botão CTA Principal (mesmo destino e comportamento) -->
          <a href="https://pay.hotmart.com/X108154869T?off=953h3rmf" class="btn-cta" id="pricingCtaBtn">
            Quero dominar o estoicismo
            <span class="btn-shimmer-beam" aria-hidden="true"></span>
          </a>

          <!-- Linha de Garantia -->
          <a href="https://pay.hotmart.com/X108154869T?off=953h3rmf" class="cta-sub">Acesso VITALÍCIO · 7 dias de garantia</a>

          <!-- Selos de Segurança Compra Segura / Hotmart (originais sem alteração) -->
          <img class="pricing-seals" src="../img/ref/tqbbyxdw.png" alt="Compra Segura Hotmart" width="300" height="75"
            loading="lazy" decoding="async">
        </div>

      </div>
    </div>
  </section>"""
