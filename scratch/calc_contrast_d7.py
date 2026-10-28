def get_luminance(r, g, b):
    def channel_lum(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * channel_lum(r) + 0.7152 * channel_lum(g) + 0.0722 * channel_lum(b)

def contrast_ratio(hex1, hex2):
    def hex_to_rgb(h):
        h = h.lstrip('#')
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    l1 = get_luminance(*hex_to_rgb(hex1))
    l2 = get_luminance(*hex_to_rgb(hex2))
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)

bg = '#FFFFFF'
card_bg = '#FFFFFF'
section_bg = '#FBF8F1'

tests = [
    ('Section title (#121013 on #FBF8F1)', '#121013', section_bg),
    ('Section title (#121013 on #FFFFFF)', '#121013', bg),
    ('Item text (#1F1C18 on #FFFFFF)', '#1F1C18', bg),
    ('Item note (#55504A on #FFFFFF)', '#55504A', bg),
    ('Item price (#121013 on #FFFFFF)', '#121013', bg),
    ('Item price priceless (#855605 on #FFFFFF)', '#855605', bg),
    ('Bonus subtitle/em-dash (#55504A on #FFFFFF)', '#55504A', bg),
    ('Total value label (#44403C on #FFFFFF)', '#44403C', bg),
    ('Total old value (#D9383A on #FFFFFF)', '#D9383A', bg),
    ('Timer subtext (#55504A on #FFFFFF)', '#55504A', bg),
    ('Timer digits (#F3CA68 on #141316)', '#F3CA68', '#141316'),
    ('Callout text (#1F1C18 on #FFFFFF)', '#1F1C18', bg),
    ('Original price label (#55504A on #FFFFFF)', '#55504A', bg),
    ('Price R$29,90 (#855605 on #FFFFFF)', '#855605', bg),
    ('CTA button text (#121013 on #E2B755)', '#121013', '#E2B755'),
    ('Guarantee link (#855605 on #FFFFFF)', '#855605', bg),
]

for label, fg, background in tests:
    cr = contrast_ratio(fg, background)
    print(f'{label}: {cr:.2f}:1 ({"PASS" if cr >= 4.5 or ("digits" in label and cr >= 4.5) or ("Price R$29,90" in label and cr >= 3.0) else "CHECK"})')
