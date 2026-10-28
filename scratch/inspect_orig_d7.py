import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

idx_lower = orig.lower().find('veja tudo que você')

# Let's find the enclosing section or container before this mockup image
start_search = orig.rfind('<section', 0, idx_lower)
if start_search == -1:
    start_search = orig.rfind('<div', 0, idx_lower - 500)

# Let's find "Compra Segura" or Hotmart seal after idx_lower
end_search = orig.find('Compra Segura', idx_lower)
if end_search != -1:
    end_tag = orig.find('</section>', end_search)
    if end_tag == -1:
        end_tag = orig.find('</div>', end_search + 500)
    print("Found section bounds in index.html:")
    print(f"Start: {start_search}, End: {end_tag}")
    print("\n--- CONTENT IN INDEX.HTML ---")
    print(orig[start_search:end_tag+10])
else:
    print("Compra Segura not found after index!")
