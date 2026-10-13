"""
MUSIQUE TEMPORAIRE + EFFETS SONORES + LOGO SONORE — synthèse 100 % programmée.

Ce n'est PAS la musique finale : c'est une maquette sonore originale (aucun
échantillon, aucun morceau existant, donc aucun problème de droits) qui sert à
juger le rythme du montage. Elle suit la structure décrite au §7 de la bible :
ambiance → départ sur le pictogramme K → montée → temps fort « un seul panier »
→ redescente sur le plan humain → remontée → respiration → logo sonore.

La voix off n'est pas incluse (à enregistrer par une comédienne).
Pas de ducking ici : sans voix, les creux sonneraient comme des défauts.
Le ducking (−8 à −10 dB sous la voix) se fera au mixage final.

Usage : python3 render/audio_temp.py   → out/audio/*.wav
"""
import os, wave
import numpy as np

SR = 44100
OUT = os.path.join(os.path.dirname(__file__), '..', 'out', 'audio')
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(7)
BPM = 102
BEAT = 60 / BPM
BAR = 4 * BEAT

def nt(n):  # nom de note → Hz
    names = {'C': -9, 'D': -7, 'E': -5, 'F': -4, 'G': -2, 'A': 0, 'B': 2}
    semis = names[n[0]] + (1 if '#' in n else 0) + 12 * (int(n[-1]) - 4)
    return 440 * 2 ** (semis / 12)

def smooth(x, k):
    return np.convolve(x, np.ones(k) / k, mode='same')

# ---------- instruments ----------
def mallet(f, dur=1.2, amp=0.25):
    t = np.arange(int(dur * SR)) / SR
    s = np.sin(2*np.pi*f*t) * np.exp(-t*5) + 0.35*np.sin(2*np.pi*f*3.93*t) * np.exp(-t*22) \
        + 0.12*np.sin(2*np.pi*f*9.2*t) * np.exp(-t*60)
    s *= np.minimum(1, t / 0.002)
    return amp * s

def bass(f, dur, amp=0.32):
    t = np.arange(int(dur * SR)) / SR
    s = np.sin(2*np.pi*f*t) + 0.25*np.sin(2*np.pi*2*f*t)
    env = np.minimum(1, t/0.01) * np.exp(-t*1.6)
    return amp * s * env

def kick(amp=0.55):
    t = np.arange(int(0.35 * SR)) / SR
    f = 45 + 80*np.exp(-t*30)
    return amp * np.sin(2*np.pi*np.cumsum(f)/SR) * np.exp(-t*12)

def shaker(amp=0.05):
    n = int(0.06 * SR); t = np.arange(n) / SR
    x = np.diff(rng.standard_normal(n+1))
    return amp * x * np.exp(-t*60)

def clap(amp=0.12):
    n = int(0.18 * SR); t = np.arange(n) / SR
    x = smooth(np.diff(rng.standard_normal(n+1)), 3)
    return amp * x * (np.exp(-t*28) + 0.4*np.exp(-np.maximum(0, t-0.012)*28)*(t > 0.012))

def pad(freqs, dur, amp=0.05, att=0.6, rel=0.8):
    t = np.arange(int(dur * SR)) / SR
    s = np.zeros_like(t)
    for f in freqs:
        for d in (-0.15, 0, 0.17):
            s += np.sin(2*np.pi*(f*(1+d/100))*t + rng.uniform(0, 6))
    env = np.minimum(1, t/att) * np.minimum(1, (dur - t)/rel).clip(0)
    return amp * s / (3*len(freqs)) * env * 3

# ---------- SFX ----------
def tick(amp=0.12):
    t = np.arange(int(0.04*SR))/SR
    return amp*np.sin(2*np.pi*2400*t)*np.exp(-t*120)

def tap(amp=0.18):
    t = np.arange(int(0.06*SR))/SR
    return amp*(np.sin(2*np.pi*900*t)*np.exp(-t*90) + 0.3*rng.standard_normal(len(t))*np.exp(-t*300))

def pop(amp=0.22):
    t = np.arange(int(0.12*SR))/SR
    f = 300 + 500*np.minimum(1, t/0.06)
    return amp*np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*30)

def chime(amp=0.16, dur=1.4):
    t = np.arange(int(dur*SR))/SR
    return amp*(np.sin(2*np.pi*nt('E6')*t) + 0.7*np.sin(2*np.pi*nt('B6')*t)*np.exp(-t*1.5)) * np.exp(-t*3) * np.minimum(1, t/0.003)

def ambience(dur, amp=0.05):
    n = int(dur*SR)
    x = smooth(rng.standard_normal(n), 40) * 4          # rumeur de rue, très filtrée
    lfo = 0.7 + 0.3*np.sin(2*np.pi*0.23*np.arange(n)/SR)
    return amp * x * lfo

def put(buf, sig, at, gain=1.0):
    i = int(at * SR)
    if i >= len(buf): return
    j = min(len(buf), i + len(sig))
    buf[i:j] += gain * sig[:j-i]

# ---------- partition ----------
CHORDS = [('D', ['D3', 'F#3', 'A3'], 'D2', ['D5', 'A4', 'F#4', 'A4', 'D5', 'E5', 'F#5', 'E5']),
          ('Bm', ['B2', 'D3', 'F#3'], 'B1', ['B4', 'F#4', 'D5', 'F#4', 'B4', 'D5', 'E5', 'D5']),
          ('G', ['G2', 'B2', 'D3'], 'G1', ['G4', 'D5', 'B4', 'D5', 'G5', 'F#5', 'D5', 'B4']),
          ('A', ['A2', 'C#3', 'E3'], 'A1', ['A4', 'E5', 'C#5', 'E5', 'A5', 'E5', 'C#5', 'E5'])]

def music(total, t0, stop, sections):
    """sections : liste (début, fin, {couches}) ; couches ∈ mar, mar_hi, pad, bass, kick, shk, clap"""
    buf = np.zeros(int(total * SR) + SR)
    def layers(t):
        for a, b, L in sections:
            if a <= t < b: return L
        return {}
    bar = 0
    t = t0
    while t < stop - 1e-6:
        name, chord, root, arp = CHORDS[bar % 4]
        L = layers(t + 0.01)
        if 'pad' in L:
            put(buf, pad([nt(n) for n in chord] + [nt(chord[0])*2], BAR + 0.6, amp=L['pad']), t)
        if 'bass' in L:
            put(buf, bass(nt(root), BEAT*1.5, L['bass']), t)
            put(buf, bass(nt(root), BEAT*0.9, L['bass']*0.8), t + 2.5*BEAT)
            put(buf, bass(nt(root)*1.5, BEAT*0.9, L['bass']*0.7), t + 3.5*BEAT)
        for k in range(8):                              # croches
            tt = t + k * BEAT / 2
            if tt >= stop: break
            L = layers(tt + 0.01)
            if 'mar' in L and (k % 2 == 0 or k in (3, 7)):
                put(buf, mallet(nt(arp[k]), 1.0, L['mar']), tt)
            if 'mar_hi' in L and k in (1, 5, 6):
                put(buf, mallet(nt(arp[k])*2, 0.8, L['mar_hi']), tt)
            if 'kick' in L and k in (0, 3, 4):
                put(buf, kick(L['kick']), tt)
            if 'clap' in L and k in (2, 6):
                put(buf, clap(L['clap']), tt)
            if 'shk' in L:
                put(buf, shaker(L['shk']), tt); put(buf, shaker(L['shk']*0.6), tt + BEAT/4)
        t += BAR; bar += 1
    # coupure propre à « stop » (laisse résonner 0,25 s)
    i = int(stop * SR); fade = int(0.25 * SR)
    buf[i:i+fade] *= np.linspace(1, 0, fade); buf[i+fade:] = 0
    return buf

def logo(buf, at):
    """Logo sonore : deux notes (grand puis petit quart de cercle) + accord ouvert."""
    put(buf, mallet(nt('D4'), 2.5, 0.34), at)
    put(buf, mallet(nt('A4'), 2.5, 0.30), at + 0.18)
    put(buf, pad([nt('D3'), nt('A3'), nt('E4'), nt('F#4')], 4.2, amp=0.09, att=0.25, rel=2.2), at + 0.18)
    put(buf, mallet(nt('F#5'), 2.0, 0.10), at + 0.36)

def finish(name, mus, sfx, total):
    n = int(total * SR)
    mus, sfx = mus[:n], sfx[:n]
    fo = int(0.8 * SR)                                  # fin propre
    mix = mus + sfx
    mix[-fo:] *= np.linspace(1, 0, fo) ** 2
    peak = np.max(np.abs(mix)) or 1
    g = 0.89 / peak                                      # ≈ −1 dBFS (loudnorm ensuite)
    for suffix, sig in (('musique', mus), ('sfx', sfx), ('mix', mix)):
        st = np.stack([sig*g, sig*g], 1)
        st[:, 0] *= 0.97                                 # micro-élargissement stéréo
        data = (np.clip(st, -1, 1) * 32767).astype('<i2')
        with wave.open(os.path.join(OUT, f'kambily-temp-{name}-{suffix}.wav'), 'wb') as w:
            w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(data.tobytes())

# ================= FILM MAÎTRE (52 s) =================
T = 52
mus = np.zeros(int(T*SR) + SR); sfx = np.zeros_like(mus)
amb = ambience(5.6); amb[-int(0.5*SR):] *= np.linspace(1, 0, int(0.5*SR))
put(mus, amb, 0)
put(mus, mallet(nt('A4'), 1.4, 0.16), 0.8)              # repère « Abdalah »
put(mus, mallet(nt('E5'), 1.4, 0.16), 1.6)              # repère « Tombon (Electro) »
put(mus, pad([nt('D3'), nt('A3'), nt('D4')], 2.2, amp=0.05, att=1.6, rel=0.3), 3.4)  # convergence
mus += music(T, 5.4, 46.8, [
    (5.4, 9.4,   {'mar': .16, 'pad': .05}),                                   # le K, la question
    (9.4, 17.4,  {'mar': .17, 'pad': .05, 'bass': .26, 'kick': .40, 'shk': .035}),  # vitrines
    (17.4, 26.4, {'mar': .17, 'pad': .05, 'bass': .28, 'kick': .45, 'shk': .04, 'clap': .09}),
    (26.4, 29.7, {'mar': .19, 'mar_hi': .09, 'pad': .07, 'bass': .30, 'kick': .50, 'shk': .05, 'clap': .11}),  # temps fort
    (29.7, 35.2, {'mar': .17, 'pad': .05, 'bass': .28, 'kick': .45, 'shk': .04, 'clap': .09}),
    (35.2, 41.2, {'mar': .13, 'pad': .06}),                                   # plan humain
    (41.2, 46.8, {'mar': .18, 'mar_hi': .07, 'pad': .06, 'bass': .30, 'kick': .48, 'shk': .045, 'clap': .10}),
])[:len(mus)]
logo(mus, 47.5)
for t in (12.6, 13.7, 14.7, 30.3): put(sfx, tick(), t)                 # vitrines, créneau
for t in (19.2, 28.4, 31.2, 32.9): put(sfx, tap(), t)                  # taps
put(sfx, pop(), 20.6)                                                   # arrivée dans le panier
put(sfx, chime(), 34.0)                                                 # « confirmé »
for i in range(7): put(sfx, tick(0.07), 36.6 + i*0.35)                 # étapes du suivi
put(sfx, chime(0.08, 1.0), 39.2)                                        # « Livrée »
finish('master', mus, sfx, T)

# ================= SPOT 15 s =================
T = 15
mus = np.zeros(int(T*SR) + SR); sfx = np.zeros_like(mus)
amb = ambience(2.8); amb[-int(0.4*SR):] *= np.linspace(1, 0, int(0.4*SR))
put(mus, amb, 0)
put(mus, mallet(nt('A4'), 1.2, 0.16), 0.1); put(mus, mallet(nt('E5'), 1.2, 0.16), 0.6)
mus += music(T, 2.6, 11.9, [
    (2.6, 6.6,  {'mar': .19, 'mar_hi': .08, 'pad': .07, 'bass': .30, 'kick': .50, 'shk': .05, 'clap': .11}),
    (6.6, 9.6,  {'mar': .17, 'pad': .05, 'bass': .28, 'kick': .45, 'shk': .04, 'clap': .09}),
    (9.6, 11.9, {'mar': .14, 'pad': .06}),
])[:len(mus)]
logo(mus, 12.5)
put(sfx, chime(), 7.4)
for t in (9.9, 10.25, 10.6, 10.95): put(sfx, tick(0.07), t)
finish('15', mus, sfx, T)
print('audio OK')
