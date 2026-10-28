import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

for query in ['VOCÊ ESTARÁ A FRENTE', 'DEPOIMENTOS RETIRADOS']:
    matches = [m.start() for m in re.finditer(re.escape(query), c)]
    print(f"Matches for '{query}': {len(matches)}")
    for m in matches:
        # Check if in <style>
        is_in_style = m < c.find('</style>')
        print(f"  Pos {m} (in style: {is_in_style})")
        print("  Snippet:", repr(c[m-60:m+80]))
