#!/usr/bin/env python3
"""Draw the profile's tiny pixel cat. Standard library only; no remote assets."""
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"
ASSETS.mkdir(exist_ok=True)

THEMES = {
    "light": {"fur":"#b4a2ef", "shade":"#8b78ca", "edge":"#393456", "ear":"#f3bddb", "screen":"#e3f5f0", "mint":"#167c6b", "shine":"#efe7ff"},
    "dark": {"fur":"#c1b2f5", "shade":"#9783d8", "edge":"#302c47", "ear":"#fac9df", "screen":"#243c3a", "mint":"#91e4ce", "shine":"#f2ebff"},
}

def rect(x,y,w,h,c):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/>'

def draw(p):
    b = ''
    # Pixel ears, head, shoulders and a curled tail.
    for a in [(25,15,12,22),(58,15,12,22),(21,29,53,29),(25,54,46,24),(67,62,12,8),(75,53,7,14)]:
        b += rect(*a,p['edge'])
    for a in [(29,19,4,13),(62,19,4,13),(25,33,45,21),(29,54,38,20),(70,63,9,4),(78,54,4,10)]:
        b += rect(*a,p['fur'])
    b += rect(29,27,4,7,p['ear']) + rect(62,27,4,7,p['ear'])
    b += rect(25,50,45,4,p['shade']) + rect(34,57,24,13,p['shine'])
    b += '<g class="eyes">' + rect(33,38,5,6,p['edge']) + rect(57,38,5,6,p['edge']) + '</g>'
    b += rect(27,44,6,3,p['ear']) + rect(63,44,6,3,p['ear'])
    b += '<path d="M44 45h3v3h4v-3h3" fill="none" stroke="'+p['edge']+'" stroke-width="2"/>'
    # The terminal is an illustration, not a simulated status panel.
    b += rect(18,62,52,24,p['edge']) + rect(22,66,44,15,p['screen'])
    b += '<path d="m29 70 4 3-4 3" fill="none" stroke="'+p['mint']+'" stroke-width="2"/>'
    b += rect(38,75,8,2,p['mint']) + rect(14,84,60,4,p['shade'])
    b += '<g class="spark" fill="'+p['mint']+'"><path d="M80 23h3v4h4v3h-4v4h-3v-4h-4v-3h4z"/></g>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="96" height="96" viewBox="0 0 96 96" role="img" aria-labelledby="title desc" shape-rendering="crispEdges">
<title id="title">Pixel cat at a terminal</title>
<desc id="desc">A small lavender cat with a mint terminal, blinking gently.</desc>
<style>
.eyes {{ transform-origin: 48px 41px; animation: blink 7s steps(1,end) infinite; }}
.spark {{ animation: sparkle 5s ease-in-out infinite; }}
@keyframes blink {{ 0%,94%,98%,100% {{ transform:scaleY(1); }} 95%,97% {{ transform:scaleY(.2); }} }}
@keyframes sparkle {{ 0%,100% {{ opacity:.5; }} 50% {{ opacity:1; }} }}
@media (prefers-reduced-motion:reduce) {{ .eyes,.spark {{ animation:none; }} }}
</style>
{b}
</svg>'''

for theme,palette in THEMES.items():
    (ASSETS/f'pixel-cat-{theme}.svg').write_text(draw(palette)+'\n')
print('Generated two 96 × 96 pixel cats; displayed at 76 × 76.')
