from PIL import Image
import numpy as np

# In frame_05_last.png, let's find the phone's top, bottom, left, right:
im_v = Image.open('scratch/frames/frame_05_last.png')
arr_v = np.array(im_v)

# The phone has a visible screen and gold rim.
# Let's inspect rows from top to bottom
for y in range(0, 1280, 20):
    row = arr_v[y, :, :]
    # look at center columns (200 to 520)
    center_bright = row[250:470].max(axis=1)
    # print if significantly brighter than 20
    avg = center_bright.mean()
    if avg > 30:
        pass

# Let's crop tightly to the phone's extent:
# In vertical (frame 5):
# Phone left rim is around x=160, right rim around x=560.
# Phone top rim is around y=210, bottom rim around y=1070.
# Let's verify by checking slices:
print("Inspecting vertical phone in frame 5:")
for y in range(180, 250, 5):
    line = arr_v[y, 300:420, :]
    print(f"y={y}: center brightness max = {line.max()}")

for y in range(1030, 1100, 5):
    line = arr_v[y, 300:420, :]
    print(f"y={y}: center brightness max = {line.max()}")

print("\nInspecting horizontal phone in frame 0:")
im_h = Image.open('scratch/frames/frame_00_first.png')
arr_h = np.array(im_h)
for x in range(40, 100, 5):
    line = arr_h[600:680, x, :]
    print(f"x={x}: center brightness max = {line.max()}")

for x in range(620, 680, 5):
    line = arr_h[600:680, x, :]
    print(f"x={x}: center brightness max = {line.max()}")
