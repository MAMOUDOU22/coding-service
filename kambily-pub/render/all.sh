#!/usr/bin/env bash
# Rend toutes les déclinaisons de l'animatique (MP4 muets, sous-titres incrustés).
set -e
cd "$(dirname "$0")/.."
node render/render.mjs 16x9 master &
node render/render.mjs 9x16 master &
wait
node render/render.mjs 16x9 15 &
node render/render.mjs 9x16 15 &
node render/render.mjs 16x9 master 25 0.6667 "cues=1&end=13" essai-voix-prompteur &
wait
