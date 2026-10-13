"""
VOIX OFF — Google Cloud Text-to-Speech (voix françaises haut de gamme).

Remplace la voix de travail Kokoro dès qu'une clé est disponible :
    export GOOGLE_TTS_API_KEY="…"            # clé API Google Cloud (Text-to-Speech activé)
    python3 render/vo_google.py --list       # liste les voix fr-FR disponibles
    VO_VOICE=fr-FR-Chirp3-HD-Aoede ./render/mix.sh

Même minutage que vo_gen.py (animatic/vo-cues.js), mêmes fichiers de sortie :
out/audio/kambily-voix-master.wav et kambily-voix-15.wav — le mixage et
l'image ne changent pas.

Remarques :
- Chirp 3 HD = voix les plus naturelles de Google ; choisir une voix féminine
  (ex. Aoede, Kore, Leda, Zephyr — vérifier avec --list, le catalogue évolue).
- Voix de synthèse : à déclarer comme telle ; une comédienne reste préférable
  pour la version officielle (bible §4).
"""
import os, re, sys, json, base64, io, wave, urllib.request
import numpy as np
import soundfile as sf

HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, "..", "out", "audio")
os.makedirs(OUT, exist_ok=True)
SR = 48000
KEY = os.environ.get("GOOGLE_TTS_API_KEY", "")
VOICE = os.environ.get("VO_VOICE", "fr-FR-Chirp3-HD-Aoede")
API = "https://texttospeech.googleapis.com/v1"

def call(path, body=None):
    url = f"{API}/{path}{'&' if '?' in path else '?'}key={KEY}"
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())

if not KEY:
    sys.exit("GOOGLE_TTS_API_KEY manquante — rien n'est généré (la voix Kokoro reste en place).")

if "--list" in sys.argv:
    for v in call("voices?languageCode=fr-FR")["voices"]:
        print(v["name"], v.get("ssmlGender"), v.get("naturalSampleRateHertz"))
    sys.exit(0)

js = open(os.path.join(HERE, "..", "animatic", "vo-cues.js")).read()
PAT = {"master": r"master:\s*\[(.*?)\n\s*\],\s*\n\s*\"15\"", "15": r'"15":\s*\[(.*?)\n\s*\],\s*\n\s*\};'}
def parse(k):
    body = re.search(PAT[k], js, re.S).group(1)
    out = []
    for r in re.findall(r"\{([^}]*)\}", body):
        a = float(re.search(r"a:\s*([\d.]+)", r).group(1))
        t = re.search(r'text:\s*"((?:[^"\\]|\\.)*)"', r).group(1).replace('\\"', '"')
        out.append((a, t))
    return out

def synth(text, rate=0.95):
    lang = "-".join(VOICE.split("-")[:2])
    body = {"input": {"text": text},
            "voice": {"languageCode": lang, "name": VOICE},
            "audioConfig": {"audioEncoding": "LINEAR16", "sampleRateHertz": SR, "speakingRate": rate}}
    data = base64.b64decode(call("text:synthesize", body)["audioContent"])
    a, sr = sf.read(io.BytesIO(data), dtype="float32")
    if a.ndim > 1: a = a.mean(1)
    thr = 10 ** (-45 / 20); idx = np.where(np.abs(a) > thr)[0]
    if len(idx): a = a[max(0, idx[0] - int(0.02 * SR)): idx[-1] + int(0.06 * SR)]
    f = int(0.012 * SR); a[:f] *= np.linspace(0, 1, f); a[-f:] *= np.linspace(1, 0, f)
    return a * (10 ** (-3 / 20)) / (np.max(np.abs(a)) or 1)

def build(k, total, name):
    cues = parse(k); track = np.zeros(int(total * SR) + SR, np.float32)
    for i, (a, t) in enumerate(cues):
        nxt = cues[i + 1][0] if i + 1 < len(cues) else total
        clip = synth(t)
        if a + len(clip) / SR > nxt - 0.05:            # trop long : on accélère légèrement
            clip = synth(t, rate=min(1.2, 0.95 * (len(clip) / SR) / max(0.4, nxt - a - 0.12)))
        s = int(a * SR); j = min(len(track), s + len(clip)); track[s:j] += clip[:j - s]
        print(f"  [{a:5.2f}→{a + len(clip) / SR:5.2f}] (suiv {nxt:4.1f}) « {t} »")
    sf.write(os.path.join(OUT, name), np.stack([track[:int(total * SR)]] * 2, 1), SR)

print("voix :", VOICE)
build("master", 90, "kambily-voix-master.wav")
build("15", 15, "kambily-voix-15.wav")
print("VO Google OK")
