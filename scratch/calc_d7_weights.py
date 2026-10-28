import sys
sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, 'scratch')
from dobra7_css import DOBRA7_CSS
from dobra7_html import DOBRA7_HTML
from dobra7_js import DOBRA7_JS

css_b = len(DOBRA7_CSS.encode('utf-8'))
html_b = len(DOBRA7_HTML.encode('utf-8'))
js_b = len(DOBRA7_JS.encode('utf-8'))

print(f"Dobra 7 CSS: {css_b} bytes ({css_b/1024:.2f} KB)")
print(f"Dobra 7 HTML: {html_b} bytes ({html_b/1024:.2f} KB)")
print(f"Dobra 7 JS: {js_b} bytes ({js_b/1024:.2f} KB)")
print(f"Total Dobra 7 code: {css_b + html_b + js_b} bytes ({(css_b + html_b + js_b)/1024:.2f} KB)")
print(f"New image files: 0 bytes (uses existing mckp6.webp and tqbbyxdw.png)")
