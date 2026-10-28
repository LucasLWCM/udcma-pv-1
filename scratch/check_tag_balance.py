import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check open vs close tags in Dobra 7 section
s_idx = content.find('<section id="pricing">')
e_idx = content.find('</section>', s_idx) + len('</section>')
sec_code = content[s_idx:e_idx]

import re
div_opens = len(re.findall(r'<div\b', sec_code))
div_closes = len(re.findall(r'</div\b', sec_code))
p_opens = len(re.findall(r'<p\b', sec_code))
p_closes = len(re.findall(r'</p\b', sec_code))
ul_opens = len(re.findall(r'<ul\b', sec_code))
ul_closes = len(re.findall(r'</ul\b', sec_code))
li_opens = len(re.findall(r'<li\b', sec_code))
li_closes = len(re.findall(r'</li\b', sec_code))
a_opens = len(re.findall(r'<a\b', sec_code))
a_closes = len(re.findall(r'</a\b', sec_code))

print(f"div tags: {div_opens} open, {div_closes} close")
print(f"p tags: {p_opens} open, {p_closes} close")
print(f"ul tags: {ul_opens} open, {ul_closes} close")
print(f"li tags: {li_opens} open, {li_closes} close")
print(f"a tags: {a_opens} open, {a_closes} close")

if div_opens == div_closes and p_opens == p_closes and ul_opens == ul_closes and li_opens == li_closes and a_opens == a_closes:
    print("\nALL HTML TAGS PERFECTLY BALANCED AND CLOSED!")
else:
    print("\nWARNING: Unbalanced tags detected!")
    sys.exit(1)
