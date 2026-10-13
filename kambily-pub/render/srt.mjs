// Génère les sous-titres .srt (voix off complète) depuis animatic/vo-cues.js.
import fs from 'node:fs'; import path from 'node:path'; import { fileURLToPath } from 'node:url';
const here = path.dirname(fileURLToPath(import.meta.url));
const window = {}; eval(fs.readFileSync(path.join(here,'..','animatic','vo-cues.js'),'utf8'));
const ts = s => { const ms=Math.round(s*1000); const h=String(Math.floor(ms/3600000)).padStart(2,'0'), m=String(Math.floor(ms/60000)%60).padStart(2,'0'),
  sec=String(Math.floor(ms/1000)%60).padStart(2,'0'), r=String(ms%1000).padStart(3,'0'); return `${h}:${m}:${sec},${r}`; };
for (const [k,name] of [['master','90s'],['15','15s']]) {
  const L = window.VO[k]; const srt = L.map((c,i)=>`${i+1}\n${ts(c.a-0.1)} --> ${ts(Math.min(c.b+0.4, L[i+1] ? L[i+1].a-0.15 : 1e9))}\n${c.text}\n`).join('\n');
  fs.writeFileSync(path.join(here,'..','out',`kambily-voix-off-${name}.srt`), srt); }
console.log('SRT OK');
