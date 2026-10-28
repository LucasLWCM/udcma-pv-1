const fs = require('fs');
const path = require('path');

function getFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const filePath = path.join(dir, file);
    try {
      const stat = fs.statSync(filePath);
      if (stat.isDirectory()) {
        getFiles(filePath, fileList);
      } else {
        fileList.push({ path: filePath.replace(/\\/g, '/'), size: stat.size });
      }
    } catch (e) {}
  }
  return fileList;
}

// Untracked directories from git status:
const untrackedDirs = ['p12', 'scratch', 'video'];
const untrackedIndividual = [
  'img/bonus/Capa_plano_roteiro_estoico.png',
  'img/bonus/Foto_perfil.jpg',
  'img/bonus/Fundo_noites_portico.png',
  'img/bonus/Roteiro_estoico.png',
  'img/bonus/estoico_campo.jpg',
  'img/bonus/estoico_campo.webp',
  'img/bonus/estoico_campo_2x.webp',
  'img/bonus/img2_arte_estoico_em_campo.png',
  'img/bonus/noites_portico.jpg',
  'img/bonus/noites_portico.webp',
  'img/bonus/noites_portico_2x.webp',
  'img/bonus/rafa_avatar.jpg',
  'img/bonus/rafa_avatar.webp',
  'img/bonus/rafa_avatar_2x.webp',
  'img/bonus/roteiro_capa.jpg',
  'img/bonus/roteiro_capa.webp',
  'img/bonus/roteiro_capa_2x.webp',
  'img/hero/Aniamacao_h1.mp4',
  'img/ref/video_ref.mp4',
  'img/testimonials/fabio_alencar.jpg',
  'img/testimonials/fabio_alencar.webp',
  'img/testimonials/fabio_alencar_2x.webp',
  'img/testimonials/sp_1.webp',
  'img/testimonials/sp_1_2x.webp',
  'img/testimonials/sp_2.webp',
  'img/testimonials/sp_2_2x.webp',
  'img/testimonials/sp_3.webp',
  'img/testimonials/sp_3_2x.webp',
  'img/testimonials/sp_4.webp',
  'img/testimonials/sp_4_2x.webp',
  'img/testimonials/sp_5.webp',
  'img/testimonials/sp_5_2x.webp'
];

let allNewFiles = [];

for (const dir of untrackedDirs) {
  if (fs.existsSync(dir)) {
    getFiles(dir, allNewFiles);
  }
}

for (const f of untrackedIndividual) {
  if (fs.existsSync(f)) {
    allNewFiles.push({ path: f, size: fs.statSync(f).size });
  }
}

console.log('Total untracked files:', allNewFiles.length);

const over50MB = allNewFiles.filter(f => f.size > 50 * 1024 * 1024);
console.log('Files > 50MB:', over50MB);

const totalBytes = allNewFiles.reduce((acc, f) => acc + f.size, 0);
console.log(`Total untracked size: ${(totalBytes / (1024 * 1024)).toFixed(2)} MB`);

fs.writeFileSync('scratch/untracked_list.json', JSON.stringify(allNewFiles, null, 2));
