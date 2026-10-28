import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

c_start = content.find('DOBRA 6: DEPOIMENTOS')
# Go back to the comment start
comm_start = content.rfind('/*', 0, c_start)

# Where does Dobra 6 CSS end?
# Let's find the next major section in CSS or </style>
style_end = content.find('</style>')
# Let's check what comes after Dobra 6 CSS
print('comm_start:', comm_start)
css_block = content[comm_start:style_end]
print('Length of CSS block until </style>:', len(css_block.encode('utf-8')), 'bytes')
print('First 150 chars:', repr(css_block[:150]))
print('Last 150 chars:', repr(css_block[-150:]))
