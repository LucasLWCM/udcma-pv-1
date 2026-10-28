import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

terms = ['social-chat-stream', 'chat-bubble-card', 'testimonials-title', 't-highlight-card', 'mobileSwipeTrack', 'marqueePauseBtn']
for t in terms:
    print(f"=== CSS referencing {t} ===")
    matches = re.findall(r'([^\n}]*' + re.escape(t) + r'[^{]*\{[^}]+\})', p12)
    for m in matches:
        print(m.strip()[:140] + '...')
    print()
