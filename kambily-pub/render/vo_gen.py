"""
VOIX OFF — SCRATCH NEURONALE (provisoire, à remplacer par une comédienne).

Modèle Kokoro (open-source, licence Apache-2.0), voix française ff_siwis.
Ce n'est PAS la voix finale : c'est une voix neuronale de travail, pour
entendre le film monté. La bible (§4) garde la recommandation d'enregistrer
une comédienne ; le remplacement se fait en reposant le stem voix.

Entrée  : ../animatic/vo-cues.js (minutage)
Sortie  : ../out/audio/kambily-voix-<cut>.wav (stem voix seul, 48 kHz stéréo)
          + report des collisions éventuelles.

Prononciation : « Kambily » est écrit « Kambili » POUR LA SYNTHÈSE seulement
(espeak lit « Kambily » en anglais). À valider avec la marque.
"""
import os, re, json, wave
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

HERE = os.path.dirname(__file__)
TTS = os.environ.get("KOKORO_DIR", "/tmp/claude-0/-home-user-coding-service/36cbe431-abf4-5a64-bdb4-db1edc5e822b/scratchpad/tts")
OUT = os.path.join(HERE, "..", "out", "audio")
os.makedirs(OUT, exist_ok=True)
SR = 48000
VOICE = "ff_siwis"

k = Kokoro(os.path.join(TTS, "kokoro-v1.0.onnx"), os.path.join(TTS, "voices-v1.0.bin"))

# --- lire vo-cues.js (a, b, text) ---
js = open(os.path.join(HERE, "..", "animatic", "vo-cues.js")).read()
def parse(cutkey):
    pat = {"master:": r"master:\s*\[(.*?)\n\s*\],\s*\n\s*\"15\"",
           '"15":': r'"15":\s*\[(.*?)\n\s*\],\s*\n\s*\};'}[cutkey]
    block = re.search(pat, js, re.S)
    body = block.group(1)
    rows = re.findall(r"\{([^}]*)\}", body)
    out = []
    for r in rows:
        a = float(re.search(r"a:\s*([\d.]+)", r).group(1))
        b = float(re.search(r"b:\s*([\d.]+)", r).group(1))
        raw = re.search(r'text:\s*"((?:[^"\\]|\\.)*)"', r).group(1)
        t = raw.replace('\\"', '"').replace("\\'", "'")
        out.append((a, b, t))
    return out

# intention → vitesse (débit) par phrase ; plus bas = plus posé
def speed_for(text, i, n):
    s = 0.92
    if i < 2: s = 0.86            # accroche, lent
    if "?" in text: s = 0.9
    if "panier" in text.lower(): s = 0.88
    if text.strip() in ("Kambily.", "Et c'est confirmé."): s = 0.85
    return s

def synth(text):
    audio_text = re.sub(r"\bKambily\b", "Kambili", text)
    a, sr = k.create(audio_text, voice=VOICE, speed=speed_for(text, 0, 1), lang="fr-fr")
    a = np.asarray(a, dtype=np.float32)
    # resample 24k -> 48k (linéaire, suffisant pour une voix de travail)
    if sr != SR:
        x = np.arange(len(a)); xi = np.linspace(0, len(a) - 1, int(len(a) * SR / sr))
        a = np.interp(xi, x, a).astype(np.float32)
    # trim silences (seuil -45 dBFS)
    thr = 10 ** (-45 / 20)
    idx = np.where(np.abs(a) > thr)[0]
    if len(idx):
        a = a[max(0, idx[0] - int(0.02 * SR)): idx[-1] + int(0.06 * SR)]
    # HPF ~90 Hz (one-pole) + de-click fade
    b = np.copy(a); alpha = 0.98
    hp = np.empty_like(b); prev_x = prev_y = 0.0
    for n2 in range(len(b)):
        hp[n2] = alpha * (prev_y + b[n2] - prev_x); prev_x = b[n2]; prev_y = hp[n2]
    a = hp
    f = int(0.012 * SR); a[:f] *= np.linspace(0, 1, f); a[-f:] *= np.linspace(1, 0, f)
    # normalise la phrase à -3 dBFS crête
    pk = np.max(np.abs(a)) or 1.0
    a *= (10 ** (-3 / 20)) / pk
    return a

def build(cutkey, total, outname):
    cues = parse(cutkey)
    track = np.zeros(int(total * SR) + SR, dtype=np.float32)
    report = []
    ends = []
    for i, (a, b, t) in enumerate(cues):
        clip = synth(t)
        start = int(a * SR)
        end_t = a + len(clip) / SR
        nxt = cues[i + 1][0] if i + 1 < len(cues) else total
        flag = "OK"
        if end_t > nxt - 0.05:
            # trop long : ré-essaie plus vite pour tenir avant la phrase suivante
            avail = max(0.4, nxt - a - 0.12)
            sp = min(1.15, max(0.8, (len(clip) / SR) / avail * 0.92))
            at = re.sub(r"\bKambily\b", "Kambili", t)
            c2, sr2 = k.create(at, voice=VOICE, speed=sp, lang="fr-fr")
            c2 = np.asarray(c2, np.float32)
            x = np.arange(len(c2)); xi = np.linspace(0, len(c2) - 1, int(len(c2) * SR / sr2))
            clip = np.interp(xi, x, c2).astype(np.float32)
            thr = 10 ** (-45 / 20); idx = np.where(np.abs(clip) > thr)[0]
            if len(idx): clip = clip[idx[0]: idx[-1] + int(0.05 * SR)]
            ff = int(0.012 * SR); clip[:ff] *= np.linspace(0, 1, ff); clip[-ff:] *= np.linspace(1, 0, ff)
            pk = np.max(np.abs(clip)) or 1.0; clip *= (10 ** (-3 / 20)) / pk
            end_t = a + len(clip) / SR
            flag = f"RESERRÉ x{sp:.2f}" + ("" if end_t <= nxt - 0.02 else " ⚠ENCORE LONG")
        j = min(len(track), start + len(clip))
        track[start:j] += clip[:j - start]
        ends.append(end_t)
        report.append(f"  [{a:5.2f}→{end_t:5.2f}] (cible fin {b:4.1f}, suiv {nxt:4.1f}) {flag}  « {t} »")
    track = track[:int(total * SR)]
    st = np.stack([track, track], 1)
    (sf.write(os.path.join(OUT, outname), st, SR))
    print(f"== {outname} ==")
    print("\n".join(report))
    return ends

build("master:", 90, "kambily-voix-master.wav")
build(r'"15":', 15, "kambily-voix-15.wav")
print("VO OK")
