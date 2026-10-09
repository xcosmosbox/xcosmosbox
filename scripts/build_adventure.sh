#!/usr/bin/env bash
# Package the imagegen-authored 2 × 7 atlas as a full-width pixel theatre.
# Requires ImageMagick 6/7. All poses come from the supplied artwork.
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

# Delivered atlas: 1340 × 1174. Exclude each shared panel-edge scanline.
# The generator's seven rows vary slightly in height.
row_y=(1 169 338 506 675 843 1008)
row_h=(165 165 165 166 165 162 165)
for frame in {0..13}; do
  col=$((frame % 2))
  row=$((frame / 2))
  "$converter" "$atlas" -crop "668x${row_h[$row]}+$((col*670+1))+${row_y[$row]}" +repage \
    -filter point -resize '960x240!' "$frame_dir/$frame.png"
done

# Arrival → investigation → die → Old One → debugging → tea → distant-eye gag.
# Centiseconds. Slow enough to follow; the friendly ending gets breathing room.
delays=(160 80 180 100 160 120 100 140 200 180 180 220 260 180)
args=()
for frame in {0..13}; do
  args+=( -delay "${delays[$frame]}" "$frame_dir/$frame.png" )
done
"$converter" "${args[@]}" -alpha off +dither -colors 128 -loop 0 \
  -layers Optimize "$project_dir/assets/quantum-pier.gif"
cp "$frame_dir/11.png" "$project_dir/assets/quantum-pier-still.png"
printf 'Built 14 story poses / 22.6-second loop at 960 × 240 (4:1).\n'
