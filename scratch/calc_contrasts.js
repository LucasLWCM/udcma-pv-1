function getLuminance(r, g, b) {
  const [rs, gs, bs] = [r, g, b].map(c => {
    c = c / 255;
    return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
  });
  return 0.2126 * rs + 0.7152 * gs + 0.0722 * bs;
}

function getRatio(l1, l2) {
  const lighter = Math.max(l1, l2);
  const darker = Math.min(l1, l2);
  return (lighter + 0.05) / (darker + 0.05);
}

const colors = {
  text: [7, 7, 7],            // #070707
  goldLight: [235, 192, 104], // #EBC068
  goldDark: [199, 158, 59],   // #C79E3B
  bgDark: [14, 14, 14],       // #0E0E0E
  bgDeepDark: [3, 3, 3],      // #030303
  bgWhite: [255, 255, 255],   // #FFFFFF
  bgCream: [251, 248, 241]    // #FBF8F1
};

const l = {};
for (const [k, [r, g, b]] of Object.entries(colors)) {
  l[k] = getLuminance(r, g, b);
}

console.log('Luminances:', l);
console.log('1. Text (#070707) on Gold Light (#EBC068):', getRatio(l.text, l.goldLight).toFixed(2) + ':1');
console.log('2. Text (#070707) on Gold Mid (#C79E3B):', getRatio(l.text, l.goldDark).toFixed(2) + ':1');
console.log('3. Gold Button (#EBC068) on Dark Page (#0E0E0E):', getRatio(l.goldLight, l.bgDark).toFixed(2) + ':1');
console.log('4. Gold Button (#EBC068) on Deep Dark Page (#030303):', getRatio(l.goldLight, l.bgDeepDark).toFixed(2) + ':1');
console.log('5. White Background on Dark Contour/Shadow border (blended):', getRatio(l.bgWhite, getLuminance(80, 50, 10)).toFixed(2) + ':1');
