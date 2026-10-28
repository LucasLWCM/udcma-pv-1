from PIL import Image
import numpy as np
import glob

# Let's inspect frames 30 to 60 (the rotation phase)
# specifically check where the phone corners are!
for idx in range(30, 65, 3):
    im = Image.open(f'scratch/all_frames/f_{idx:03d}.png')
    arr = np.array(im)
    # Brightness of phone rim is high (> 60)
    # Let's check where the large body is
    # Phone screen has pixels > 40
    # Let's find rows that have at least 50 pixels > 40 (definitely the phone, not a spark)
    row_counts = (arr.max(axis=2) > 40).sum(axis=1)
    col_counts = (arr.max(axis=2) > 40).sum(axis=0)
    
    valid_rows = np.where(row_counts > 40)[0]
    valid_cols = np.where(col_counts > 40)[0]
    if len(valid_rows) > 0:
        print(f"Frame {idx:03d}: Y=[{valid_rows.min()}, {valid_rows.max()}], X=[{valid_cols.min()}, {valid_cols.max()}]")
