// Rendu image par image de l'animatique → MP4 (H.264), via Playwright + ffmpeg.
// Usage : node render/render.mjs <16x9|9x16> <master|15> [fps] [scale] [query-extra] [nom]
//   ex. essai voix : node render/render.mjs 16x9 master 25 0.6667 "cues=1&end=13" essai-voix
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { spawn } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const [fmt='16x9', cut='master', fpsArg='25', scaleArg='0.6667', extra='', name=''] = process.argv.slice(2);
const fps = +fpsArg, scale = +scaleArg;
const here = path.dirname(fileURLToPath(import.meta.url));
const W = Math.round((fmt==='9x16'?1080:1920)*scale/2)*2, H = Math.round((fmt==='9x16'?1920:1080)*scale/2)*2;
const out = path.join(here, '..', 'out', name ? `kambily-${name}-${fmt}.mp4` : `kambily-animatique-${cut}-${fmt}.mp4`);
const url = 'file://' + path.join(here, '..', 'animatic', 'index.html') + `?format=${fmt}&cut=${cut}&t=0${extra?'&'+extra:''}`;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: W, height: H } });
await page.goto(url); await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(300);
const dur = await page.evaluate(() => window.__dur);
const n = Math.round(dur * fps);
const ff = spawn('ffmpeg', ['-y','-loglevel','error','-f','image2pipe','-framerate',String(fps),'-i','-',
  '-c:v','libx264','-pix_fmt','yuv420p','-crf','20','-preset','medium','-movflags','+faststart', out], { stdio: ['pipe','inherit','inherit'] });
for (let i = 0; i < n; i++) {
  await page.evaluate(t => window.__render(t), i / fps);
  const buf = await page.screenshot({ type: 'jpeg', quality: 92 });
  if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  if (i % 125 === 0) process.stdout.write(`${fmt}/${cut} ${i}/${n}\n`);
}
ff.stdin.end(); await new Promise(r => ff.on('close', r));
await browser.close();
console.log('OK', out);
