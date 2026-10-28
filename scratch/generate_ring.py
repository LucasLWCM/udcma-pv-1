import math
import sys

sys.stdout.reconfigure(encoding='utf-8')

cx, cy = 90, 90
r = 72
tick_len = 10

print("<!-- Radial tick marks -->")
for i in range(7):
    deg = -90 + i * (360.0 / 7.0)
    rad = math.radians(deg)
    r1 = r - tick_len / 2
    r2 = r + tick_len / 2
    x1 = round(cx + r1 * math.cos(rad), 2)
    y1 = round(cy + r1 * math.sin(rad), 2)
    x2 = round(cx + r2 * math.cos(rad), 2)
    y2 = round(cy + r2 * math.sin(rad), 2)
    print(f'  <line class="ring-mark mark-{i+1}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#855605" stroke-width="3" stroke-linecap="round" />')

print("\n<!-- Circular dots alternative -->")
for i in range(7):
    deg = -90 + i * (360.0 / 7.0)
    rad = math.radians(deg)
    x = round(cx + r * math.cos(rad), 2)
    y = round(cy + r * math.sin(rad), 2)
    print(f'  <circle class="ring-dot dot-{i+1}" cx="{x}" cy="{y}" r="4" fill="#855605" />')
