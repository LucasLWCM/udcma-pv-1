import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print('Is testimonials-hotmart in content?', 'testimonials-hotmart' in content)
print('Is MARQUEE_LOOP_DURATION in content?', 'MARQUEE_LOOP_DURATION' in content)
print('Is hotmart in content?', 'hotmart' in content)
print('Is DEPOIMENTOS RETIRADOS in content?', 'DEPOIMENTOS RETIRADOS' in content)

# Check all script tags at the bottom
scripts = content.split('<script')
print(f'Total script tags: {len(scripts)-1}')
for i, s in enumerate(scripts[1:]):
    s_end = s.find('</script>')
    s_content = s[:s_end] if s_end != -1 else s[:100]
    print(f'Script #{i+1}: length {len(s_content)} chars, preview: {repr(s_content[:60])}')
