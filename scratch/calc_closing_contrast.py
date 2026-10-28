import sys

sys.stdout.reconfigure(encoding='utf-8')

def rel_lum(r, g, b):
    def ch(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)

def contrast(c1, c2):
    l1 = rel_lum(*c1)
    l2 = rel_lum(*c2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)

bg_pure = (14, 14, 14) # #0E0E0E
# Background at peak glow: blend of #0E0E0E with ~20% of #EBC068 (approx rgb(45, 34, 18))
bg_glow = (45, 34, 18)

colors = {
    'Heading Gold (#EBC068)': (235, 192, 104),
    'Light Gold (#F5D27E)': (245, 210, 126),
    'Warm White (#F5F0E8)': (245, 240, 232),
    'Soft White (#E2DDD5)': (226, 221, 213),
    'Muted Secondary (#C2BCB0)': (194, 188, 176),
    'Pure White (#FFFFFF)': (255, 255, 255),
}

print("=== CONTRAST ON BASE BACKGROUND (#0E0E0E) ===")
for name, rgb in colors.items():
    cr = contrast(rgb, bg_pure)
    print(f"{name}: {cr:.2f}:1 (Normal text >= 4.5: {cr >= 4.5}, Large text >= 3.0: {cr >= 3.0})")

print("\n=== CONTRAST ON PEAK SUNRISE GLOW (#2D2212) ===")
for name, rgb in colors.items():
    cr = contrast(rgb, bg_glow)
    print(f"{name}: {cr:.2f}:1 (Normal text >= 4.5: {cr >= 4.5}, Large text >= 3.0: {cr >= 3.0})")
