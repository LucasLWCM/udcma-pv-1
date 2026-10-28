import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'(/\* [^\n]*Garantia[^\n]*\*/[\s\S]*?)(/\* ── [^\n]+ ── \*/|</style>)', c)
if m:
    print('CSS for guarantee in p12:')
    print(m.group(1))

m_html = re.search(r'(<section id="guarantee"[\s\S]*?</section>)', c)
if m_html:
    print('\nHTML for guarantee in p12:')
    print(m_html.group(1))

with open('index.html', 'r', encoding='utf-8') as f:
    orig_c = f.read()

m_orig_html = re.search(r'(<section id="guarantee"[\s\S]*?</section>)', orig_c)
if m_orig_html:
    print('\nHTML for guarantee in index.html:')
    print(m_orig_html.group(1))
