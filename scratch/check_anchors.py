import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

print('links to testimonials:', re.findall(r'href=[\'"][^\'"]*testimonials[^\'"]*[\'"]', p12))
print('links to social:', re.findall(r'href=[\'"][^\'"]*social[^\'"]*[\'"]', p12))
