import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

def print_section_info(name, start_line, end_line):
    print(f"=== {name} (lines {start_line}-{end_line}) ===")
    for i in range(start_line-1, min(start_line+6, len(lines))):
        print(f"{i+1}: {lines[i].rstrip()}")
    print("...")
    for i in range(max(start_line, end_line-6), end_line):
        print(f"{i+1}: {lines[i].rstrip()}")
    print()

# Locate each section
text = "".join(lines)
sec_names = ['pricing', 'social-proof', 'for-who', 'about', 'guarantee', 'closing', 'faq']
for s in sec_names:
    pos = text.find(f'id="{s}"')
    if pos != -1:
        line_no = text[:pos].count('\n') + 1
        print(f"Section #{s} around line {line_no}")
