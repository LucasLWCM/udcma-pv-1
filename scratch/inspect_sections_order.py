import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

# Let's find all section tags and their line numbers
sections = []
for m in re.finditer(r'<section\b[^>]*>', p12):
    line_no = p12[:m.start()].count('\n') + 1
    tag = m.group(0)
    sections.append((line_no, tag, m.start()))

print(f"Total sections found: {len(sections)}")
for s in sections:
    print(f"Line {s[0]}: {s[1]}")
