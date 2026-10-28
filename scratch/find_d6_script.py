import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

scripts = content.split('<script')
for i, s in enumerate(scripts[1:]):
    if 'MARQUEE_LOOP_DURATION' in s:
        s_end = s.find('</script>')
        s_code = s[:s_end]
        print(f'Script #{i+1} has MARQUEE_LOOP_DURATION!')
        print(f'Length in bytes: {len(s_code.encode("utf-8"))} ({len(s_code.encode("utf-8"))/1024:.2f} KB)')
        print('First 200 chars:')
        print(s_code[:200])
