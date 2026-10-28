import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

idx = orig.find('id="closing"')
if idx != -1:
    print("--- ORIGINAL #closing HTML ---")
    print(orig[idx-100:idx+2500])

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

idx_p12 = p12.find('id="closing"')
if idx_p12 != -1:
    print("\n--- P12 #closing HTML ---")
    print(p12[idx_p12-100:idx_p12+2500])
