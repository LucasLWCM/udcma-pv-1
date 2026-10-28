import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

def print_range(start, count):
    for i in range(start-1, min(len(lines), start-1+count)):
        print(f"{i+1}: {lines[i].rstrip()}")

print("=== START OF DOBRA 6 (#testimonials-hotmart) ===")
print_range(6535, 45)

print("\n=== END OF DOBRA 6 (#testimonials-hotmart) ===")
print_range(7065, 30)

print("\n=== START OF DOBRA 8 (#social-proof) ===")
print_range(7225, 45)

print("\n=== END OF DOBRA 8 (#social-proof) ===")
print_range(7335, 30)
