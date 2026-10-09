#!/usr/bin/env bash
# Package the imagegen-authored 2 × 4 frame atlas as a compact looping GIF.
# Requires ImageMagick 6/7. No network calls; no hand-painted/generated replacement art.
set -euo pipefail
project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
atlas="$project_dir/assets/source/quantum-pier-atlas.webp"
frame_dir="$(mktemp -d)"
trap 'rm -rf -- "$frame_dir"' EXIT
if command -v magick >/dev/null 2>&1; then
  converter=magick
else
  converter=convert
fi

# The delivered atlas is 1672 × 941; each panel is 836 × 235.
# The final extra scanline is outside the eight equal frame tiles.
for frame in {0..7}; do
  col=$((frame % 2))
  row=$((frame / 2))
  "$converter" "$atlas" -crop "836x235+$((col*836))+$((row*235))" +repage \
    -filter point -resize '720x202!' "$frame_dir/$frame.png"
done

# Story beats in centiseconds: discover, wake, debug, sparkle, relax, offer tea, cheers, reset.
delays=(90 45 25 30 60 70 150 60)
args=()
for frame in {0..7}; do
  args+=( -delay "${delays[$frame]}" "$frame_dir/$frame.png" )
done
"$converter" "${args[@]}" -alpha off +dither -colors 128 -loop 0 \
  -layers Optimize "$project_dir/assets/quantum-pier.gif"
cp "$frame_dir/6.png" "$project_dir/assets/quantum-pier-still.png"
printf 'Built 8-frame / 5.3-second loop at 720 × 202, displayed at 360 × 101.\n'
