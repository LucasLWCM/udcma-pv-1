import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# Size of p12/index.html
p12_size = os.path.getsize('p12/index.html')
orig_size = os.path.getsize('index.html')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
css_m = re.search(r'(/\* ═+\s+DOBRA 10: SEÇÃO GARANTIA[\s\S]*?/\* ── Copy final ── \*/)', c)
css_len = len(css_m.group(1).encode('utf-8')) if css_m else 0

html_m = re.search(r'(<!-- ═+\s+SEÇÃO: GARANTIA \+ CTA 2 \(DOBRA 10 P12\)[\s\S]*?</section>)', c)
html_len = len(html_m.group(1).encode('utf-8')) if html_m else 0

js_m = re.search(r'(<!-- ═+\s+SCRIPT: DOBRA 10 — GARANTIA 7 DIAS[\s\S]*?</script>)', c)
js_len = len(js_m.group(1).encode('utf-8')) if js_m else 0

print(f"Total size of p12/index.html: {p12_size} bytes ({p12_size/1024:.2f} KB)")
print(f"Dobra 10 CSS size: {css_len} bytes ({css_len/1024:.2f} KB)")
print(f"Dobra 10 HTML size: {html_len} bytes ({html_len/1024:.2f} KB)")
print(f"Dobra 10 JS size: {js_len} bytes ({js_len/1024:.2f} KB)")
print(f"Dobra 10 Total added code weight: {css_len + html_len + js_len} bytes ({(css_len + html_len + js_len)/1024:.2f} KB)")

# Let's also check gzip estimation
import gzip
gzipped_block = gzip.compress((css_m.group(1) + html_m.group(1) + js_m.group(1)).encode('utf-8'))
print(f"Gzipped Dobra 10 weight on wire: {len(gzipped_block)} bytes ({len(gzipped_block)/1024:.2f} KB)")
