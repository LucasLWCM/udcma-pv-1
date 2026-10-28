import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

s_idx = orig.find('id="guarantee"')
if s_idx == -1:
    s_idx = orig.find('guarantee')
print('s_idx in index.html:', s_idx)
if s_idx != -1:
    sec_start = orig.rfind('<section', 0, s_idx)
    sec_end = orig.find('</section>', s_idx) + len('</section>')
    print("Section bounds in index.html:", sec_start, sec_end)
    print("\n--- CONTENT IN INDEX.HTML ---")
    print(orig[sec_start:sec_end+200])

# Also check CSS in index.html
c_idx = orig.find('/* ── Garantia ── */')
if c_idx == -1:
    c_idx = orig.find('#guarantee')
print('\nCSS in index.html at:', c_idx)
if c_idx != -1:
    print(orig[c_idx-30:c_idx+1200])
