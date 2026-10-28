from PIL import Image
import numpy as np
import glob
from scipy.ndimage import binary_opening, binary_closing

all_f = sorted(glob.glob('scratch/all_frames/*.png'))

phone_min_x = 720
phone_max_x = 0
phone_min_y = 1280
phone_max_y = 0

for idx, f in enumerate(all_f):
    im = Image.open(f)
    arr = np.array(im)
    # Phone body has strong brightness
    mask = arr.max(axis=2) > 40
    # Remove small sparks: open with a 15x15 structure
    struct = np.ones((15, 15), dtype=bool)
    clean_mask = binary_opening(mask, structure=struct)
    
    y_idx, x_idx = np.where(clean_mask)
    if len(y_idx) > 0:
        f_min_y, f_max_y = y_idx.min(), y_idx.max()
        f_min_x, f_max_x = x_idx.min(), x_idx.max()
        phone_min_x = min(phone_min_x, f_min_x)
        phone_max_x = max(phone_max_x, f_max_x)
        phone_min_y = min(phone_min_y, f_min_y)
        phone_max_y = max(phone_max_y, f_max_y)

print(f"PHONE BODY (without isolated sparks) across ALL frames:")
print(f"X: [{phone_min_x}, {phone_max_x}] (width={phone_max_x - phone_min_x + 1})")
print(f"Y: [{phone_min_y}, {phone_max_y}] (height={phone_max_y - phone_min_y + 1})")
