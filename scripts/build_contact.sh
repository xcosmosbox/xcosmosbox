#!/usr/bin/env bash
# The frame is imagegen artwork. The QR is the user's original, copied 1:1.
# No generated pixels, filters, colors or perspective are applied to the QR.
set -euo pipefail
project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
if command -v magick >/dev/null 2>&1; then
  converter=magick
else
  converter=convert
fi
"$converter" -size 1403x1753 canvas:none \
  -fill white -draw 'rectangle 205,425 1200,1405' \
  \( "$project_dir/assets/source/investigator-contact-frame.png" -filter point -resize '1403x1753!' \) \
  -compose Over -composite \
  "$project_dir/assets/source/wechat-qr-original.png" -geometry +257+472 -composite \
  -define png:compression-level=9 "$project_dir/assets/investigator-contact.png"
printf 'Built investigator contact pass; original QR occupies 890 × 882 pixels at +257+472.\n'
