#!/usr/bin/env bash
# Mixe voix off (scratch neuronale) + musique temporaire + SFX dans les MP4.
# - Musique/SFX atténués sous la voix (sidechain ducking).
# - Sortie normalisée −14 LUFS / crêtes ≤ −1 dBFS.
set -e
cd "$(dirname "$0")/.."
python3 render/audio_temp.py
# Voix : Google TTS si une clé est fournie (GOOGLE_TTS_API_KEY), sinon voix de travail Kokoro.
if [ -n "${GOOGLE_TTS_API_KEY:-}" ]; then python3 render/vo_google.py; else python3 render/vo_gen.py; fi
mix(){ v="$1"; bed="$2"; vo="$3"; tmp="${v%.mp4}.tmp.mp4"
  ffmpeg -y -loglevel error -i "$v" -i "$bed" -i "$vo" -map 0:v:0 \
    -filter_complex "\
[1:a]aresample=48000[bed];[2:a]aresample=48000[vo1];\
[vo1]asplit=2[vosc][vomix];\
[bed][vosc]sidechaincompress=threshold=0.05:ratio=10:attack=15:release=320:makeup=2[duck];\
[duck]volume=0.95[duckv];\
[vomix]volume=1.12[vov];\
[duckv][vov]amix=inputs=2:normalize=0[m];\
[m]loudnorm=I=-14:TP=-1.5:LRA=11,alimiter=limit=0.85:level=false[a]" \
    -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 -shortest "$tmp" && mv "$tmp" "$v"; }
for f in 16x9 9x16; do
  mix out/kambily-animatique-master-$f.mp4 out/audio/kambily-temp-master-mix.wav out/audio/kambily-voix-master.wav
  mix out/kambily-animatique-15-$f.mp4     out/audio/kambily-temp-15-mix.wav     out/audio/kambily-voix-15.wav
done
echo "mix OK"
