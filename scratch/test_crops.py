from PIL import Image
import os

for name, (w, h, x, y) in [
    ("Candidate A (680x980)", (680, 980, 20, 150)),
    ("Candidate B (660x960)", (660, 960, 30, 160)),
    ("Candidate C (680x960)", (680, 960, 20, 160)),
]:
    im_0 = Image.open('scratch/all_frames/f_001.png').crop((x, y, x+w, y+h))
    im_45 = Image.open('scratch/all_frames/f_045.png').crop((x, y, x+w, y+h))
    im_144 = Image.open('scratch/all_frames/f_144.png').crop((x, y, x+w, y+h))
    
    os.makedirs(f'scratch/test_crop_{w}x{h}', exist_ok=True)
    im_0.save(f'scratch/test_crop_{w}x{h}/f1.png')
    im_45.save(f'scratch/test_crop_{w}x{h}/f45.png')
    im_144.save(f'scratch/test_crop_{w}x{h}/f144.png')
    print(f"Saved {name} samples.")
