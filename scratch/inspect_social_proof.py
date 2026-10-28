import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

idx = orig.find('VOCÊ ESTARÁ A FRENTE')
print('Index in index.html:', idx)
if idx != -1:
    # Find enclosing section
    sec_start = orig.rfind('<section', 0, idx)
    sec_end = orig.find('</section>', idx) + len('</section>')
    print("Section bounds in index.html:", sec_start, sec_end)
    print("\n--- CONTENT IN INDEX.HTML ---")
    print(orig[sec_start:sec_end+200])
else:
    print("Not found by exact string, searching case-insensitive")
    idx2 = orig.lower().find('você estará a frente')
    print('idx2:', idx2)
    if idx2 != -1:
        sec_start = orig.rfind('<section', 0, idx2)
        sec_end = orig.find('</section>', idx2) + len('</section>')
        print(orig[sec_start:sec_end+200])
