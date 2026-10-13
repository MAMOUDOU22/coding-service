#!/usr/bin/env bash
# Ajoute la maquette sonore (musique temporaire + SFX + logo sonore) aux MP4 de l'animatique.
# Normalisation : −14 LUFS intégré, crêtes ≤ −1 dBTP (cible réseaux sociaux).
set -e
cd "$(dirname "$0")/.."
python3 render/audio_temp.py
mux(){ v="$1"; a="$2"; tmp="${v%.mp4}.tmp.mp4"
  ffmpeg -y -loglevel error -i "$v" -i "$a" -map 0:v:0 -map 1:a:0 -c:v copy \
    -af "loudnorm=I=-14:TP=-1.5:LRA=11,alimiter=limit=0.84:level=false" -c:a aac -b:a 192k -ar 48000 -shortest "$tmp" && mv "$tmp" "$v"; }
for f in 16x9 9x16; do
  mux out/kambily-animatique-master-$f.mp4 out/audio/kambily-temp-master-mix.wav
  mux out/kambily-animatique-15-$f.mp4     out/audio/kambily-temp-15-mix.wav
done
echo "mux OK"
