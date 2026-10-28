import sys
sys.stdout.reconfigure(encoding='utf-8')

import os
sys.path.insert(0, 'scratch')
from dobra7_css import DOBRA7_CSS
from dobra7_html import DOBRA7_HTML
from dobra7_js import DOBRA7_JS

with open('p12/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace CSS
css_start = content.find('/* ── Seção Preço ── */')
css_end = content.find('/* ── Prova Social ── */', css_start)
if css_start == -1 or css_end == -1:
    print(f'ERROR: CSS bounds not found! css_start={css_start}, css_end={css_end}')
    sys.exit(1)

content = content[:css_start] + DOBRA7_CSS + '\n\n    ' + content[css_end:]
print('1. CSS replaced successfully!')

# 2. Replace HTML
html_start = content.find('<section id="pricing">')
html_end = content.find('</section>', html_start) + len('</section>')
if html_start == -1 or html_end == -1:
    print(f'ERROR: HTML bounds not found! html_start={html_start}, html_end={html_end}')
    sys.exit(1)

content = content[:html_start] + DOBRA7_HTML + content[html_end:]
print('2. HTML replaced successfully!')

# 3. Add Dobra 7 Script
# Put it right before timer script or after Dobra 6 script
timer_idx = content.find('// Timer Evergreen de 24h')
if timer_idx != -1:
    script_tag = content.rfind('<script', 0, timer_idx)
    js_block = '<script>\n' + DOBRA7_JS.strip() + '\n  </script>\n\n  '
    content = content[:script_tag] + js_block + content[script_tag:]
    print('3. JS script inserted before timer script successfully!')
else:
    print('ERROR: Could not find timer script to insert Dobra 7 JS!')
    sys.exit(1)

with open('p12/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('\nSuccessfully updated p12/index.html with Dobra 7!')
