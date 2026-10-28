import os
import glob

files = glob.glob('img/testimonials/*.*')
for f in sorted(files):
    print(f, os.path.getsize(f), 'bytes')
