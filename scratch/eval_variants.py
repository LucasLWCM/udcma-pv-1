import os
from PIL import Image
import numpy as np

for tag, t in [('horiz', '0.5'), ('list', '2.5'), ('playing', '5.5')]:
    cmd = f'ffmpeg -y -ss {t} -i img/ref/video_ref.mp4 -vf "crop=680:980:20:150" -vframes 1 scratch/ref_{tag}.png'
    os.system(cmd)

ref_list = Image.open('scratch/ref_list.png')
ref_arr = np.array(ref_list)
ui_ref = ref_arr[450:900, 180:500]

variants_dirs = sorted(os.listdir('video/frames_eval'))

evaluations = []

for v in variants_dirs:
    dir_p = os.path.join('video/frames_eval', v)
    im_p = os.path.join(dir_p, 'list.png')
    if not os.path.exists(im_p):
        continue
    im_l = Image.open(im_p)
    if im_l.size != (680, 980):
        im_l = im_l.resize((680, 980), Image.Resampling.LANCZOS)
    arr_l = np.array(im_l)
    ui_eval = arr_l[450:900, 180:500]
    
    mse = np.mean((ui_ref.astype(np.float64) - ui_eval.astype(np.float64)) ** 2)
    psnr = 10 * np.log10(255.0 ** 2 / mse) if mse > 0 else 99.0
    evaluations.append((v, psnr, mse))

print(f"{'Variant':<22} | {'PSNR (UI)':<10} | {'MSE'}")
print("-" * 45)
for v, psnr, mse in evaluations:
    print(f"{v:<22} | {psnr:6.2f} dB   | {mse:6.2f}")
