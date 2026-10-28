import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

classes = ['social-headline', 'bonus-title', 'for-who-col']
for c in classes:
    print(f"\n==================== CSS for .{c} in index.html ====================")
    matches = re.findall(rf'([^{{}}]*{c}[^{{}}]*\{{[^}}]+\}})', orig)
    for m in matches:
        print(m.strip())
        print("-" * 30)
