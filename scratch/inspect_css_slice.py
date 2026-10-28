import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

start_needle = '/* ── Garantia ── */'
end_needle = '/* ── Copy final ── */'

idx_start = c.find(start_needle)
idx_end = c.find(end_needle)

print(f"Garantia CSS from {idx_start} to {idx_end}:")
print(c[idx_start:idx_end])
