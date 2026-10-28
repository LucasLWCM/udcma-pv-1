import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/current_block_b.html', 'r', encoding='utf-8') as f:
    b = f.read()

# Let's find headings and major tags in b
pos_h2 = b.find('<h2 class="testimonials-title">')
print("pos_h2:", pos_h2)
print("After h2:")
print(b[pos_h2:pos_h2+500])

pos_script = b.find('<script>')
print("\npos_script:", pos_script)
print("Before script:")
print(b[pos_script-500:pos_script])
