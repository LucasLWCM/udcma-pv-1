import sys

sys.stdout.reconfigure(encoding='utf-8')

# Let's write a test script that tests different layouts and inspects bounding rects
html = """<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Barlow:ital,wght@0,400;0,600;0,700;0,800;0,900&display=swap" rel="stylesheet">
<style>
* { box-sizing: border-box; }
body { font-family: 'Barlow', sans-serif; background: #fff; padding: 20px; }
.card { width: 440px; padding: 30px; border: 1px solid #ccc; }
.grid-2col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  align-items: end;
}
.stat-line {
  display: flex;
  align-items: baseline;
  gap: 6px;
  flex-wrap: wrap;
}
.stat-num {
  font-size: 20px;
  font-weight: 800;
  color: #855605;
  white-space: nowrap;
}
.stat-label {
  font-size: 14px;
  font-weight: 600;
  color: #634003;
}
.bar {
  width: 100%;
  height: 3px;
  background: #eee;
  margin-top: 6px;
}
.bar-fill {
  width: 0.7%;
  min-width: 2px;
  height: 100%;
  background: #855605;
}
</style>
</head>
<body>
<div class="card">
  <div class="grid-2col">
    <div>
      <div class="stat-line">
        <span class="stat-num">Mais de 3 mil</span>
        <span class="stat-label">alunos</span>
      </div>
    </div>
    <div>
      <div class="stat-line">
        <span class="stat-num">0,70%</span>
        <span class="stat-label">de reembolso na Hotmart</span>
      </div>
      <div class="bar"><div class="bar-fill"></div></div>
    </div>
  </div>
</div>
</body>
</html>
"""

with open('scratch/measure_layout.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("measure_layout.html written.")
