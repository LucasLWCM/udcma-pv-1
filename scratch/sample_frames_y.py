from PIL import Image
import numpy as np
import glob
from scipy.ndimage import binary_opening

all_f = sorted(glob.glob('scratch/all_frames/*.png'))
struct = np.ones((15, 15), dtype=bool)

for idx in range(0, len(all_f), 10):
    im = Image.open(all_f[idx])
    arr = np.array(im)
    clean = binary_opening(arr.max(axis=2) > 40, structure=struct)
    y_idx, x_idx = np.where(clean)
    if len(y_idx) > 0:
        print(f"Frame {idx:03d}: Y=[{y_idx.min():4d}, {y_idx.max():4d}], X=[{x_idx.min():4d}, {x_idx.max():4d}]")
