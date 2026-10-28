import sys
sys.stdout.reconfigure(encoding='utf-8')
import os

sys.path.insert(0, 'scratch')
from dobra8_css import DOBRA8_CSS
from dobra8_html import DOBRA8_HTML
from dobra8_js import DOBRA8_JS

css_b = len(DOBRA8_CSS.encode('utf-8'))
html_b = len(DOBRA8_HTML.encode('utf-8'))
js_b = len(DOBRA8_JS.encode('utf-8'))

print(f"Dobra 8 CSS: {css_b} bytes ({css_b/1024:.2f} KB)")
print(f"Dobra 8 HTML: {html_b} bytes ({html_b/1024:.2f} KB)")
print(f"Dobra 8 JS: {js_b} bytes ({js_b/1024:.2f} KB)")
print(f"Total Dobra 8 code: {css_b + html_b + js_b} bytes ({(css_b + html_b + js_b)/1024:.2f} KB)")

# Images comparison
images = [
    ('8.2.webp', 'sp_1'),
    ('5.webp', 'sp_2'),
    ('6.webp', 'sp_3'),
    ('9.2.webp', 'sp_4'),
    ('7.webp', 'sp_5')
]
out_dir = 'img/testimonials'
tot_orig = 0
tot_1x = 0
tot_2x = 0

print("\n--- IMAGES WEIGHT REPORT ---")
for orig, base in images:
    orig_p = os.path.join(out_dir, orig)
    p_1x = os.path.join(out_dir, f"{base}.webp")
    p_2x = os.path.join(out_dir, f"{base}_2x.webp")
    s_orig = os.path.getsize(orig_p)
    s_1x = os.path.getsize(p_1x)
    s_2x = os.path.getsize(p_2x)
    tot_orig += s_orig
    tot_1x += s_1x
    tot_2x += s_2x
    print(f"{orig} ({s_orig/1024:.2f} KB) -> 1x: {s_1x/1024:.2f} KB, 2x: {s_2x/1024:.2f} KB")

print(f"\nTotal Imagens Originais: {tot_orig} bytes ({tot_orig/1024:.2f} KB)")
print(f"Total Imagens 1x Otimizadas: {tot_1x} bytes ({tot_1x/1024:.2f} KB)")
print(f"Total Imagens 2x Retina: {tot_2x} bytes ({tot_2x/1024:.2f} KB)")
