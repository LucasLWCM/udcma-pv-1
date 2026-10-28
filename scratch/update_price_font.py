with open('p12/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = """    .pricing-box .price {
      font-family: var(--font-heading, 'Cinzel', serif);
      font-size: clamp(66px, 9vw, 86px);
      font-weight: 900;
      color: #855605;
      background: linear-gradient(135deg, #A7740B 0%, #855605 50%, #6E4603 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      line-height: 1;
      margin: 6px 0 22px;
      letter-spacing: -0.02em;
      text-shadow: 0 4px 20px rgba(199, 158, 59, 0.22);
      position: relative;
      display: inline-block;
    }"""

replacement = """    .pricing-box .price {
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
    }"""

if target in content:
    content = content.replace(target, replacement)
    print("Found exact target and replaced with Barlow font!")
else:
    print("Exact target not found, checking with partial find")
    idx = content.find('.pricing-box .price {')
    print("Snippet at .pricing-box .price {:")
    print(repr(content[idx:idx+250]))

with open('p12/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Also update scratch/dobra7_css.py
with open('scratch/dobra7_css.py', 'r', encoding='utf-8') as f:
    css_file = f.read()

css_file = css_file.replace("font-family: var(--font-heading, 'Cinzel', serif);", "font-family: 'Barlow', sans-serif;")
css_file = css_file.replace("letter-spacing: -0.02em;", "letter-spacing: -2px;")

with open('scratch/dobra7_css.py', 'w', encoding='utf-8') as f:
    f.write(css_file)

print("Updated scratch/dobra7_css.py as well.")
