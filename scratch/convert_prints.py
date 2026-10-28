from PIL import Image
import os

images = [
    ('8.2.webp', 'sp_1'),
    ('5.webp', 'sp_2'),
    ('6.webp', 'sp_3'),
    ('9.2.webp', 'sp_4'),
    ('7.webp', 'sp_5')
]

out_dir = 'img/testimonials'
report = []

for orig_name, base_name in images:
    src_path = os.path.join(out_dir, orig_name)
    im = Image.open(src_path)
    orig_size = os.path.getsize(src_path)
    
    # 1x version: 400x400 (display is ~340-360px), high quality q=90
    im_1x = im.resize((400, 400), Image.Resampling.LANCZOS)
    path_1x = os.path.join(out_dir, f"{base_name}.webp")
    im_1x.save(path_1x, 'WEBP', quality=90, method=6)
    size_1x = os.path.getsize(path_1x)

    # 2x version: 800x800 (for retina/high-dpi displays), high quality q=92
    im_2x = im.resize((800, 800), Image.Resampling.LANCZOS)
    path_2x = os.path.join(out_dir, f"{base_name}_2x.webp")
    im_2x.save(path_2x, 'WEBP', quality=92, method=6)
    size_2x = os.path.getsize(path_2x)

    report.append({
        'orig': orig_name,
        'orig_size': orig_size,
        'base': base_name,
        'size_1x': size_1x,
        'size_2x': size_2x,
    })

print(f"{'Original':<12} | {'Orig Size':<10} | {'1x WebP':<10} | {'2x WebP':<10} | {'Economia 1x'}")
print("-" * 65)
tot_orig = 0
tot_1x = 0
tot_2x = 0
for r in report:
    tot_orig += r['orig_size']
    tot_1x += r['size_1x']
    tot_2x += r['size_2x']
    diff = (1 - r['size_1x'] / r['orig_size']) * 100
    print(f"{r['orig']:<12} | {r['orig_size']/1024:7.2f} KB | {r['size_1x']/1024:7.2f} KB | {r['size_2x']/1024:7.2f} KB | {diff:5.1f}%")

print("-" * 65)
print(f"TOTAL:       | {tot_orig/1024:7.2f} KB | {tot_1x/1024:7.2f} KB | {tot_2x/1024:7.2f} KB | {(1 - tot_1x/tot_orig)*100:5.1f}%")
