import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('SEÇÃO: GARANTIA')
if idx != -1:
    print('Found SEÇÃO: GARANTIA at', idx)
    print(c[idx-50:idx+600])

scripts = [m.start() for m in re.finditer(r'<script', c)] if 're' in globals() else []
import re
scripts = [m.start() for m in re.finditer(r'<script', c)]
print('Total <script> tags in p12:', len(scripts))
for s in scripts[-3:]:
    print('Script at', s, c[s:s+150])
