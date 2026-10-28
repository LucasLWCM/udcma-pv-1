import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

idx = orig.find('/* ── Para quem é / não é ── */')
if idx != -1:
    print(orig[idx:idx+1500])
else:
    print("Comment not found, searching #for-who in CSS")
    idx2 = orig.find('#for-who {')
    if idx2 != -1:
        print(orig[idx2-50:idx2+1000])
