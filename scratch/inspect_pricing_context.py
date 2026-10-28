import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('p12/index.html', 'r', encoding='utf-8') as f:
    p12 = f.read()

idx_pricing = p12.find('id="pricing"')
print('id="pricing" found at index:', idx_pricing)

# Show 300 chars before
print('\n--- 300 chars BEFORE #pricing ---')
print(p12[idx_pricing-300:idx_pricing])

# Find closing of section #pricing
end_pricing = p12.find('</section>', idx_pricing)
print('\n--- End of #pricing tag at index:', end_pricing)
print(p12[end_pricing-100:end_pricing+300])
