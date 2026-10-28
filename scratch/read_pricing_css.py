import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

idx = orig.find('.pricing-box .callout')
print(orig[idx:idx+1500])
