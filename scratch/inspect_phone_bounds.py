from PIL import Image
import os
import glob
import numpy as np

# Let's check thresholds 20, 30, 40 to distinguish ember glow / background noise from the phone device
for thresh in [15, 25, 35, 50]:
    print(f"\n--- THRESHOLD = {thresh} ---")
    g_min_x, g_min_y, g_max_x, g_max_y = 9999, 9999, 0, 0
    for f in sorted(glob.glob('scratch/frames/*.png')):
        im = Image.open(f)
        arr = np.array(im)
        bright = arr.max(axis=2)
        y_indices, x_indices = np.where(bright > thresh)
        if len(y_indices) > 0:
            min_y, max_y = y_indices.min(), y_indices.max()
            min_x, max_x = x_indices.min(), x_indices.max()
            g_min_x = min(g_min_x, min_x)
            g_min_y = min(g_min_y, min_y)
            g_max_x = max(g_max_x, max_x)
            g_max_y = max(g_max_y, max_y)
    print(f"Global bounds: X [{g_min_x}, {g_max_x}] (w={g_max_x - g_min_x}), Y [{g_min_y}, {g_max_y}] (h={g_max_y - g_min_y})")
    print(f"Crop suggestion: in_w={g_max_x - g_min_x}, in_h={g_max_y - g_min_y}, x={g_min_x}, y={g_min_y}")
