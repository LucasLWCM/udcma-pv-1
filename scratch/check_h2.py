import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

s_idx = p12.find('<section id="social-proof">')
e_idx = p12.find('</section>', s_idx) + len('</section>')
sec_code = p12[s_idx:e_idx]

h2_match = re.search(r'<h2 class="social-headline"[^>]*>([\s\S]*?)</h2>', sec_code)
if h2_match:
    raw_h2 = h2_match.group(1)
    clean_h2 = ' '.join(re.sub(r'<[^>]+>', ' ', raw_h2).split())
    print("Clean H2 text:", repr(clean_h2))
    assert clean_h2 == "VOCÊ ESTARÁ A FRENTE DE 95% DAS PESSOAS"
    print("[OK] Title matches 100% exactly without tags!")
else:
    print("[FAIL] H2 not found")
