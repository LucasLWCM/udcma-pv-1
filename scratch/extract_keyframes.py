import subprocess
import os

os.makedirs('scratch/frames', exist_ok=True)

# Extract key timestamps: 0.0s (first frame), 1.0s (horizontal), 1.8s (rotating), 2.5s (vertical list), 4.2s (lesson playing), 5.95s (last frame)
times = [
    ('frame_00_first.png', '0.0'),
    ('frame_01_horiz.png', '0.8'),
    ('frame_02_rotating.png', '1.6'),
    ('frame_03_list.png', '2.5'),
    ('frame_04_playing.png', '4.5'),
    ('frame_05_last.png', '5.95'),
]

for name, t in times:
    out = os.path.join('scratch/frames', name)
    cmd = ['ffmpeg', '-y', '-ss', t, '-i', 'img/ref/video_ref.mp4', '-vframes', '1', out]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("Frames extracted:", sorted(os.listdir('scratch/frames')))
