import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/lh_d11.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

perf = d.get('categories', {}).get('performance', {})
print('Performance Score:', round(perf.get('score', 0) * 100))
audits = d.get('audits', {})
for k in ['first-contentful-paint', 'largest-contentful-paint', 'total-blocking-time', 'cumulative-layout-shift', 'speed-index']:
    a = audits.get(k, {})
    print(f"{a.get('title')}: {a.get('displayValue', 'N/A')}")
