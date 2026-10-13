"""
VOIX OFF — Gemini TTS (Google AI Studio, clé gratuite SANS carte bancaire).

Clé : https://aistudio.google.com/apikey  (ou bouton « Créer une clé API Gemini »
dans la console Google Cloud). Gratuit, aucun moyen de paiement requis.

    export GEMINI_API_KEY="AIza..."
    python3 render/vo_gemini.py --voices        # repères sur les voix (doc)
    VO_VOICE=Aoede ./render/mix.sh              # génère la voix + remixe les vidéos

Voix (24 kHz PCM) interprétées en français ; le ton est dirigé phrase par phrase
via une consigne de jeu (§4.2 de la bible). Même minutage et mêmes fichiers de
sortie que vo_gen.py : l'image ne change pas.

Voix de synthèse (Gemini) : plus naturelle qu'une TTS classique, mais ce n'est
pas une voix humaine enregistrée. À déclarer comme telle.
"""
import os, re, sys, json, time, base64
import numpy as np
import soundfile as sf
import urllib.request, urllib.error

HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, "..", "out", "audio")
os.makedirs(OUT, exist_ok=True)
SR = 48000
KEY = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY", "")
VOICE = os.environ.get("VO_VOICE", "Aoede")          # voix féminine chaleureuse par défaut
MODEL = os.environ.get("VO_MODEL", "gemini-2.5-flash-preview-tts")
BASE = "https://generativelanguage.googleapis.com/v1beta/models"

VOICES = {  # repères (doc Google) — voix adaptées à une pub chaleureuse
  "Aoede": "légère, aérée (féminine) — défaut",
  "Leda": "jeune, fraîche (féminine)",
  "Callirrhoe": "décontractée (féminine)",
  "Vindemiatrix": "douce (féminine)",
  "Sulafat": "chaleureuse (féminine)",
  "Achernar": "douce, posée (féminine)",
  "Kore": "assurée, ferme (féminine)",
  "Autonoe": "lumineuse (féminine)",
  "Despina": "fluide (féminine)",
}

if "--voices" in sys.argv:
    print("Voix conseillées (VO_VOICE=…) :")
    for k, v in VOICES.items(): print(f"  {k:14s} {v}")
    print("\nCatalogue complet : https://ai.google.dev/gemini-api/docs/speech-generation")
    sys.exit(0)

if not KEY:
    sys.exit("GEMINI_API_KEY manquante — rien n'est généré (la voix de travail Kokoro reste en place).")

# --- minutage + consignes de jeu (alignées §4.2) ---
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

# Ton par phrase (index → consigne de jeu). Court, pour ne pas être lu à voix haute.
def style_for(i, n, cut):
    if cut == "15":
        return ["intriguant et posé", "assuré et chaleureux", "rassurant et confiant",
                "clair", "chaleureux, en souriant"][min(i, 4)]
    tones = {
        0: "intriguant, à voix basse", 1: "intriguant, à voix basse",
        2: "curieux, une idée qui naît", 3: "chaleureux et assuré, en présentant la marque",
        4: "doux et complice", 5: "lumineux et curieux", 6: "léger et complice",
        7: "clair et simple", 8: "rassurant et protecteur, sans dramatiser",
        9: "posé, un ton plus bas", 10: "posé et conclusif",
        11: "rassurant", 12: "précis et confiant", 13: "léger et souriant",
        14: "léger et souriant", 15: "satisfait, en souriant", 16: "calme et continu",
        17: "confiant, comme une promesse donnée doucement", 18: "direct, vers les commerçants",
        19: "direct et affirmé", 20: "la marque qui se pose, avec intention",
        21: "chaleureux et conclusif",
    }
    return tones.get(i, "chaleureux et naturel")

def req(url, body, tries=6):
    data = json.dumps(body).encode()
    for k in range(tries):
        try:
            r = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(r, timeout=120) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            msg = e.read().decode(errors="replace")[:200]
            if e.code in (429, 500, 503) and k < tries - 1:
                wait = min(60, 2 ** (k + 2))            # backoff : 4,8,16,32,60 s
                print(f"  …{e.code}, nouvelle tentative dans {wait}s ({msg[:80]})"); time.sleep(wait); continue
            raise SystemExit(f"Gemini {e.code} : {msg}")
    raise SystemExit("échec après plusieurs tentatives")

def synth(text, style):
    prompt = f"Lis ce texte en français avec une voix féminine, d'un ton {style}. Dis uniquement le texte, sans le reformuler : {text}"
    body = {"contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"responseModalities": ["AUDIO"],
                "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": VOICE}}}}}
    res = req(f"{BASE}/{MODEL}:generateContent?key={KEY}", body)
    part = res["candidates"][0]["content"]["parts"][0]["inlineData"]
    rate = 24000
    m = re.search(r"rate=(\d+)", part.get("mimeType", ""))
    if m: rate = int(m.group(1))
    pcm = np.frombuffer(base64.b64decode(part["data"]), dtype="<i2").astype(np.float32) / 32768.0
    if rate != SR:
        x = np.arange(len(pcm)); xi = np.linspace(0, len(pcm) - 1, int(len(pcm) * SR / rate))
        pcm = np.interp(xi, x, pcm).astype(np.float32)
    thr = 10 ** (-45 / 20); idx = np.where(np.abs(pcm) > thr)[0]
    if len(idx): pcm = pcm[max(0, idx[0] - int(0.02 * SR)): idx[-1] + int(0.06 * SR)]
    f = int(0.012 * SR);
    if len(pcm) > 2 * f: pcm[:f] *= np.linspace(0, 1, f); pcm[-f:] *= np.linspace(1, 0, f)
    return pcm * (10 ** (-3 / 20)) / (np.max(np.abs(pcm)) or 1)

def build(k, total, name):
    cues = parse(k); track = np.zeros(int(total * SR) + SR, np.float32)
    print(f"== {name} (voix Gemini : {VOICE}) ==")
    for i, (a, t) in enumerate(cues):
        clip = synth(t, style_for(i, len(cues), k))
        s = int(a * SR); j = min(len(track), s + len(clip)); track[s:j] += clip[:j - s]
        print(f"  [{a:5.2f}→{a + len(clip)/SR:5.2f}] « {t} »")
        time.sleep(1.0)                                 # ménage le quota gratuit
    sf.write(os.path.join(OUT, name), np.stack([track[:int(total*SR)]]*2, 1), SR)

build("master", 90, "kambily-voix-master.wav")
build("15", 15, "kambily-voix-15.wav")
print("VO Gemini OK")
