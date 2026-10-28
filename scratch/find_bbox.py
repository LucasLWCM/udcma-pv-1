from PIL import Image
import os
import glob
import numpy as np

frames = glob.glob('scratch/frames/*.png')

global_min_x = 9999
global_min_y = 9999
global_max_x = 0
global_max_y = 0

print("Analyzing bounding boxes (threshold > 10 brightness):")

for f in sorted(frames):
    im = Image.open(f)
    arr = np.array(im)
    # Brightness = max(r, g, b)
    bright = arr.max(axis=2)
    # find where bright > 8 (anything not pure black)
    y_indices, x_indices = np.where(bright > 8)
    if len(y_indices) > 0:
        min_y, max_y = y_indices.min(), y_indices.max()
        min_x, max_x = x_indices.min(), x_indices.max()
        print(f"{os.path.basename(f)}: X [{min_x}, {max_x}] width={max_x-min_x}, Y [{min_y}, {max_y}] height={max_y-min_y}")
        global_min_x = min(global_min_x, min_x)
        global_min_y = min(global_min_y, min_y)
        global_max_x = max(global_max_x, max_x)
        global_max_y = max(global_max_y, max_y)

print("\n--- GLOBAL NON-BLACK BOUNDS ---")
print(f"X: {global_min_x} to {global_max_x} (width={global_max_x - global_min_x})")
print(f"Y: {global_min_y} to {global_max_y} (height={global_max_y - global_min_y})")
print(f"Original video size: 720 x 1280")
print(f"Top margin: {global_min_y}px")
print(f"Bottom margin: {1280 - global_max_y}px")
print(f"Left margin: {global_min_x}px")
print(f"Right margin: {720 - global_max_x}px")
