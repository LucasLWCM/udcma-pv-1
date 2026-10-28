from PIL import Image
import os
import glob
import numpy as np

for f in sorted(glob.glob('scratch/frames/*.png')):
    im = Image.open(f)
    arr = np.array(im)
    bright = arr.max(axis=2)
    y_indices, x_indices = np.where(bright > 35)
    if len(y_indices) > 0:
        min_y, max_y = y_indices.min(), y_indices.max()
        min_x, max_x = x_indices.min(), x_indices.max()
        print(f"{os.path.basename(f)}: X [{min_x}, {max_x}] (w={max_x-min_x+1}), Y [{min_y}, {max_y}] (h={max_y-min_y+1})")
