import sys
sys.stdout.reconfigure(encoding='utf-8')
import os

sys.path.insert(0, 'scratch')
from dobra9_css import DOBRA9_CSS
from dobra9_html import DOBRA9_HTML
from dobra9_js import DOBRA9_JS

css_b = len(DOBRA9_CSS.encode('utf-8'))
html_b = len(DOBRA9_HTML.encode('utf-8'))
js_b = len(DOBRA9_JS.encode('utf-8'))

print(f"Dobra 9 CSS: {css_b} bytes ({css_b/1024:.2f} KB)")
print(f"Dobra 9 HTML: {html_b} bytes ({html_b/1024:.2f} KB)")
print(f"Dobra 9 JS: {js_b} bytes ({js_b/1024:.2f} KB)")
print(f"Total Dobra 9 code: {css_b + html_b + js_b} bytes ({(css_b + html_b + js_b)/1024:.2f} KB)")

# Media files
media_files = [
    ('video/phone_members.webm', 'Vídeo WebM Principal (680p)'),
    ('video/phone_members.mp4', 'Vídeo MP4 Fallback (680p)'),
    ('video/phone_members_mob.webm', 'Vídeo WebM Mobile (540p)'),
    ('video/phone_members_mob.mp4', 'Vídeo MP4 Mobile (540p)'),
    ('video/phone_poster.webp', 'Poster WebP (1º quadro)'),
    ('video/phone_poster.jpg', 'Poster JPG Fallback'),
    ('video/phone_fallback.webp', 'Plano B WebP (Último quadro)'),
    ('video/phone_fallback.jpg', 'Plano B JPG Fallback'),
]

print("\n--- MEDIA FILES REPORT ---")
for p, desc in media_files:
    if os.path.exists(p):
        sz = os.path.getsize(p)
        print(f"{desc:<32} ({p}): {sz} bytes ({sz/1024:.2f} KB)")
