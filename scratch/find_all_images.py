import os

for root, dirs, files in os.walk('img'):
    for file in files:
        if any(file.endswith(ext) for ext in ['.png', '.webp', '.jpg', '.jpeg']):
            p = os.path.join(root, file)
            print(p, os.path.getsize(p))
