import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

s_idx = orig.find('<section id="for-who">')
e_idx = orig.find('</section>', s_idx) + len('</section>')

print("--- ORIGINAL #for-who SECTION ---")
print(orig[s_idx:e_idx])
