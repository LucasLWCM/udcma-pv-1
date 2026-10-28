import subprocess
import os
import glob
from PIL import Image
import numpy as np

# Let's extract all 144 frames of the video to scratch/all_frames
os.makedirs('scratch/all_frames', exist_ok=True)
cmd = ['ffmpeg', '-y', '-i', 'img/ref/video_ref.mp4', 'scratch/all_frames/f_%03d.png']
subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

all_f = sorted(glob.glob('scratch/all_frames/*.png'))
print(f"Extracted {len(all_f)} frames.")

# Let's find the absolute maximum extent of the phone body across ALL 144 frames
# To avoid embers/sparks, let's look at contiguous bright regions or threshold 45
min_top = 1280
max_bottom = 0
min_left = 720
max_right = 0

for f in all_f:
    im = Image.open(f)
    arr = np.array(im)
    # Phone rim has bright golden pixels (> 60)
    # Check pixels > 55
    y_idx, x_idx = np.where(arr.max(axis=2) > 55)
    if len(y_idx) > 0:
        min_top = min(min_top, y_idx.min())
        max_bottom = max(max_bottom, y_idx.max())
        min_left = min(min_left, x_idx.min())
        max_right = max(max_right, x_idx.max())

print(f"Absolute extent across ALL 144 frames with threshold > 55:")
print(f"X: [{min_left}, {max_right}] (width={max_right - min_left + 1})")
print(f"Y: [{min_top}, {max_bottom}] (height={max_bottom - min_top + 1})")
