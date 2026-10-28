import subprocess
import os
import sys

os.makedirs('video/variants', exist_ok=True)
os.makedirs('video/frames_eval', exist_ok=True)

crop_filter = "crop=680:980:20:150"

variants = []

# MP4 variants (H.264)
for crf in [23, 26, 29]:
    variants.append({
        'name': f'mp4_680p_crf{crf}',
        'file': f'video/variants/phone_680p_crf{crf}.mp4',
        'vf': crop_filter,
        'format': 'MP4 (H.264)',
        'crf': crf,
        'width': 680,
        'height': 980,
        'args': ['-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-crf', str(crf), '-preset', 'slow', '-an']
    })
    variants.append({
        'name': f'mp4_540p_crf{crf}',
        'file': f'video/variants/phone_540p_crf{crf}.mp4',
        'vf': f"{crop_filter},scale=540:778",
        'format': 'MP4 (H.264)',
        'crf': crf,
        'width': 540,
        'height': 778,
        'args': ['-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-crf', str(crf), '-preset', 'slow', '-an']
    })

# WebM variants (VP9)
for crf in [33, 38, 42]:
    variants.append({
        'name': f'webm_680p_crf{crf}',
        'file': f'video/variants/phone_680p_crf{crf}.webm',
        'vf': crop_filter,
        'format': 'WebM (VP9)',
        'crf': crf,
        'width': 680,
        'height': 980,
        'args': ['-c:v', 'libvpx-vp9', '-b:v', '0', '-crf', str(crf), '-deadline', 'good', '-cpu-used', '2', '-an']
    })
    variants.append({
        'name': f'webm_540p_crf{crf}',
        'file': f'video/variants/phone_540p_crf{crf}.webm',
        'vf': f"{crop_filter},scale=540:778",
        'format': 'WebM (VP9)',
        'crf': crf,
        'width': 540,
        'height': 778,
        'args': ['-c:v', 'libvpx-vp9', '-b:v', '0', '-crf', str(crf), '-deadline', 'good', '-cpu-used', '2', '-an']
    })

# AV1 variant (comparison)
variants.append({
    'name': 'av1_680p_crf32',
    'file': 'video/variants/phone_680p_crf32.mp4',
    'vf': crop_filter,
    'format': 'MP4 (AV1)',
    'crf': 32,
    'width': 680,
    'height': 980,
    'args': ['-c:v', 'libsvtav1', '-crf', '32', '-preset', '6', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-an']
})

print(f"Starting encoding of {len(variants)} variants...")

results = []

for v in variants:
    out_file = v['file']
    print(f"\n--- Encoding {v['name']} -> {out_file} ---")
    cmd = ['ffmpeg', '-y', '-i', 'img/ref/video_ref.mp4', '-vf', v['vf']] + v['args'] + [out_file]
    res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print(f"Error encoding {v['name']}: {res.stderr[:200]}")
        continue
    
    size_bytes = os.path.getsize(out_file)
    size_kb = size_bytes / 1024
    print(f"Done! Size: {size_bytes} bytes ({size_kb:.2f} KB)")
    
    # Export 3 evaluation frames:
    # 1. Celular deitado: t=0.5s
    # 2. Celular em pé com a lista: t=2.5s
    # 3. Aula tocando: t=5.5s
    eval_dir = f"video/frames_eval/{v['name']}"
    os.makedirs(eval_dir, exist_ok=True)
    for tag, t in [('horiz', '0.5'), ('list', '2.5'), ('playing', '5.5')]:
        f_cmd = ['ffmpeg', '-y', '-ss', t, '-i', out_file, '-vframes', '1', f"{eval_dir}/{tag}.png"]
        subprocess.run(f_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    results.append({
        'name': v['name'],
        'format': v['format'],
        'crf': v['crf'],
        'width': v['width'],
        'height': v['height'],
        'size_bytes': size_bytes,
        'size_kb': size_kb,
        'file': out_file
    })

print("\nEncoding complete! Results count:", len(results))
