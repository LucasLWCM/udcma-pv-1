const fs = require('fs');
const content = fs.readFileSync('p12/index.html', 'utf8');

// Check for event listeners or tracking calls
const keywords = ['pricingCtaBtn', 'btn-cta', 'fbq', 'gtag', 'dataLayer', 'pixel', 'hotmart', 'track', 'InitiateCheckout', 'Purchase'];
keywords.forEach(kw => {
  let idx = 0;
  while ((idx = content.indexOf(kw, idx)) !== -1) {
    console.log(`Keyword '${kw}' at ${idx}: ${content.slice(Math.max(0, idx - 40), idx + 100).replace(/\r?\n/g, ' ')}`);
    idx += kw.length + 10;
  }
});
