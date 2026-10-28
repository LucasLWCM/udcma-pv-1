import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

idx_p12 = p12.find('id="pricing"')
print('id="pricing" in p12/index.html:', idx_p12)
if idx_p12 != -1:
    end_p12 = p12.find('</section>', idx_p12)
    print("Pricing section in p12:")
    print(p12[idx_p12-50:end_p12+15])

# Also let's find countdown timer script in index.html and p12/index.html
with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

import re
timer_orig = re.findall(r'<script\b[^>]*>([\s\S]*?countdown-timer[\s\S]*?)</script>', orig, re.IGNORECASE)
print(f"\nCountdown timer script matches in index.html: {len(timer_orig)}")
for i, t in enumerate(timer_orig):
    print(f"--- Timer script #{i+1} in index.html ---")
    print(t.strip())

timer_p12 = re.findall(r'<script\b[^>]*>([\s\S]*?countdown-timer[\s\S]*?)</script>', p12, re.IGNORECASE)
print(f"\nCountdown timer script matches in p12/index.html: {len(timer_p12)}")
for i, t in enumerate(timer_p12):
    print(f"--- Timer script #{i+1} in p12/index.html ---")
    print(t.strip())
