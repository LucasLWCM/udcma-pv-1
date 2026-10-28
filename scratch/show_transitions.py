import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

def show_lines(start, end):
    for i in range(start-1, min(end, len(lines))):
        print(f"{i+1}: {lines[i].rstrip()}")

print("--- End of pricing to start of social-proof ---")
show_lines(6865, 6885)

print("\n--- End of social-proof to start of for-who ---")
show_lines(7415, 7435)

print("\n--- End of for-who to start of about ---")
show_lines(7535, 7555)

print("\n--- End of about to start of guarantee ---")
show_lines(7560, 7580)

print("\n--- End of guarantee to start of closing ---")
show_lines(7625, 7645)

print("\n--- End of closing to start of faq ---")
show_lines(7655, 7675)
