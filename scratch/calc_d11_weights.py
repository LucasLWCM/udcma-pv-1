import sys
import os
import re
import gzip

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

css_m = re.search(r'(/\* ═+\s+DOBRA 11: SEÇÃO COPY FINAL PERSUASÃO[\s\S]*?/\* ── FAQ ── \*/)', c)
css_len = len(css_m.group(1).encode('utf-8')) if css_m else 0

html_m = re.search(r'(<!-- ═+\s+SEÇÃO: COPY FINAL PERSUASÃO \(DOBRA 11 P12\)[\s\S]*?</section>)', c)
html_len = len(html_m.group(1).encode('utf-8')) if html_m else 0

js_m = re.search(r'(<!-- ═+\s+SCRIPT: DOBRA 11 — COPY FINAL PERSUASÃO[\s\S]*?</script>)', c)
js_len = len(js_m.group(1).encode('utf-8')) if js_m else 0

total_added = css_len + html_len + js_len
gzipped_block = gzip.compress((css_m.group(1) + html_m.group(1) + js_m.group(1)).encode('utf-8'))

print(f"Dobra 11 CSS size: {css_len} bytes ({css_len/1024:.2f} KB)")
print(f"Dobra 11 HTML size: {html_len} bytes ({html_len/1024:.2f} KB)")
print(f"Dobra 11 JS size: {js_len} bytes ({js_len/1024:.2f} KB)")
print(f"Dobra 11 Total added raw weight: {total_added} bytes ({total_added/1024:.2f} KB)")
print(f"Dobra 11 Gzipped wire weight: {len(gzipped_block)} bytes ({len(gzipped_block)/1024:.2f} KB)")
