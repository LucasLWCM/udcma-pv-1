import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

h1 = content.find('<section id="for-who">')
h2 = content.find('</section>', h1) + len('</section>')
print("HTML bounds:", h1, h2)
print("Snippet around h1:")
print(repr(content[h1-50:h1+100]))
print("Snippet around h2:")
print(repr(content[h2-100:h2+50]))
