from PIL import Image
import os

images = ['8.2.webp', '5.webp', '6.webp', '9.2.webp', '7.webp']
for img in images:
    path = os.path.join('img', 'testimonials', img)
    if os.path.exists(path):
        im = Image.open(path)
        print(f"{img}: size={im.size}, mode={im.mode}, format={im.format}, bytes={os.path.getsize(path)}")
    else:
        print(f"{img} NOT FOUND")

# Also check social95.webp
if os.path.exists('img/ref/social95.webp'):
    im = Image.open('img/ref/social95.webp')
    print(f"img/ref/social95.webp: size={im.size}")
