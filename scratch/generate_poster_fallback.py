import subprocess
import os

os.makedirs('video', exist_ok=True)

crop = "crop=680:980:20:150"

# 1. Poster: frame 0 (t=0.0)
# Export high-res PNG first
subprocess.run(['ffmpeg', '-y', '-ss', '0.0', '-i', 'img/ref/video_ref.mp4', '-vf', crop, '-vframes', '1', 'scratch/poster_raw.png'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
# Convert to WebP (q=90) and JPG (q=88)
subprocess.run(['ffmpeg', '-y', '-i', 'scratch/poster_raw.png', '-c:v', 'libwebp', '-quality', '90', 'video/phone_poster.webp'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.run(['ffmpeg', '-y', '-i', 'scratch/poster_raw.png', '-q:v', '3', 'video/phone_poster.jpg'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# 2. Plano B (Fallback): last frame (t=5.95)
subprocess.run(['ffmpeg', '-y', '-ss', '5.95', '-i', 'img/ref/video_ref.mp4', '-vf', crop, '-vframes', '1', 'scratch/fallback_raw.png'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.run(['ffmpeg', '-y', '-i', 'scratch/fallback_raw.png', '-c:v', 'libwebp', '-quality', '90', 'video/phone_fallback.webp'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.run(['ffmpeg', '-y', '-i', 'scratch/fallback_raw.png', '-q:v', '3', 'video/phone_fallback.jpg'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

p_webp = os.path.getsize('video/phone_poster.webp')
p_jpg = os.path.getsize('video/phone_poster.jpg')
f_webp = os.path.getsize('video/phone_fallback.webp')
f_jpg = os.path.getsize('video/phone_fallback.jpg')

print(f"Poster WebP: {p_webp} bytes ({p_webp/1024:.2f} KB)")
print(f"Poster JPG:  {p_jpg} bytes ({p_jpg/1024:.2f} KB)")
print(f"Plano B WebP: {f_webp} bytes ({f_webp/1024:.2f} KB)")
print(f"Plano B JPG:  {f_jpg} bytes ({f_jpg/1024:.2f} KB)")
