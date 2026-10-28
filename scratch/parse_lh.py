import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/lighthouse_report.json', 'r', encoding='utf-8') as f:
    report = json.load(f)

perf_score = report['categories']['performance']['score'] * 100
audits = report['audits']

fcp = audits.get('first-contentful-paint', {}).get('displayValue', 'N/A')
lcp = audits.get('largest-contentful-paint', {}).get('displayValue', 'N/A')
tbt = audits.get('total-blocking-time', {}).get('displayValue', 'N/A')
cls = audits.get('cumulative-layout-shift', {}).get('displayValue', 'N/A')
speed_index = audits.get('speed-index', {}).get('displayValue', 'N/A')

print(f"Lighthouse Mobile Performance Score: {perf_score:.0f}/100")
print(f" - First Contentful Paint (FCP): {fcp}")
print(f" - Largest Contentful Paint (LCP): {lcp}")
print(f" - Total Blocking Time (TBT): {tbt}")
print(f" - Cumulative Layout Shift (CLS): {cls}")
print(f" - Speed Index: {speed_index}")
