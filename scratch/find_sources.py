import os

for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for f in files:
        if any(term in f for term in ['8.2', '9.2', 'Captura', 'whatsapp', 'social']):
            print(os.path.join(root, f))
