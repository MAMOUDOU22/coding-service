// Planches du storyboard : une image clé par plan (PNG).
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import path from 'node:path'; import { fileURLToPath } from 'node:url';
const here = path.dirname(fileURLToPath(import.meta.url));
const [fmt='16x9', times='3.5,10.6,16.2,24.0,32.6,42.9,51.6,58.2,63.0,71.0,77.2,83.8,88.6'] = process.argv.slice(2);
const W = fmt==='9x16'?540:960, H = fmt==='9x16'?960:540;
const b = await chromium.launch(); const p = await b.newPage({ viewport:{width:W,height:H} });
await p.goto('file://'+path.join(here,'..','animatic','index.html')+`?format=${fmt}&t=0${process.argv[4]?'&'+process.argv[4]:''}`); await p.evaluate(()=>document.fonts.ready);
let i=1; for (const t of times.split(',').map(Number)) { await p.evaluate(t=>window.__render(t), t);
  await p.screenshot({ path: path.join(here,'..','out','planches',`${fmt}-plan${String(i++).padStart(2,'0')}-${t}s.png`) }); }
await b.close();
