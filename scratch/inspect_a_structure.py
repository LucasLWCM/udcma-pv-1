import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/current_block_a.html', 'r', encoding='utf-8') as f:
    a = f.read()

pos_h2 = a.find('<h2 class="social-headline"')
print("pos_h2 in A:", pos_h2)

pos_stream = a.find('<div class="social-chat-stream"')
print("pos_stream in A:", pos_stream)

pos_section_close = a.rfind('</section>')
print("pos_section_close in A:", pos_section_close)
print("Content of stream:")
print(a[pos_stream:pos_section_close])
