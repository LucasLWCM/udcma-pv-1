import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

anchors = re.findall(r'href=[\'"](#[^\'"]+)[\'"]', p12)
print("All anchor links in p12/index.html:")
for a in set(anchors):
    # Check if target ID exists
    target_id = a[1:]
    exists = f'id="{target_id}"' in p12 or f"id='{target_id}'" in p12
    count = anchors.count(a)
    print(f" - {a} (used {count} times) -> Target exists: {exists}")
