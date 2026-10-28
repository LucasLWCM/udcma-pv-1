import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('id="testimonials-hotmart"')
print("Surroundings of id=testimonials-hotmart:")
print(repr(content[idx-60:idx+200]))

c_idx = content.find('DOBRA 6')
print("\nFirst mention of DOBRA 6 at:", c_idx)
if c_idx != -1:
    print(repr(content[c_idx-30:c_idx+150]))
