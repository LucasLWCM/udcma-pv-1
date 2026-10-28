import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

m_orig = re.search(r'// Timer Evergreen de 24h[\s\S]*?startTimer\(\);\s*\}\);', orig)
m_p12 = re.search(r'// Timer Evergreen de 24h[\s\S]*?startTimer\(\);\s*\}\);', p12)

if m_orig and m_p12:
    code_orig = m_orig.group(0).strip()
    code_p12 = m_p12.group(0).strip()
    if code_orig == code_p12:
        print("[SUCCESS] The countdown timer code in p12 is 100% IDENTICAL character-by-character to the original!")
        print("\n--- CODE ---")
        print(code_p12)
    else:
        print("[FAIL] Timer code diverges!")
        print("Diff:")
        import difflib
        print('\n'.join(difflib.unified_diff(code_orig.splitlines(), code_p12.splitlines())))
else:
    print(f"Match error: orig={bool(m_orig)}, p12={bool(m_p12)}")
