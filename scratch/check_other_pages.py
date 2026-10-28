import os
import glob
import re

for d in ['p11', 'p10', 'p7', 'p8', 'p9', 'p6', 'p5', 'principal']:
    p = os.path.join(d, 'index.html')
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
        m = re.findall(r'<img\b[^>]*src=[\'"]([^\'"]*testimonials[^\'"]*)[\'"][^>]*>', html, re.IGNORECASE)
        print(f"{p}: {len(m)} testimonial images found:")
        for img in m:
            print("  ", img)
