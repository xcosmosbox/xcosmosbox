#!/usr/bin/env python3
"""Build three non-interactive investigator equipment slots. Standard library only."""
from html import escape
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"
FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans SC','Microsoft YaHei',sans-serif"
MONO = "ui-monospace,SFMono-Regular,Consolas,monospace"
SKILLS = [
    ("graphrag", "GraphRAG", "侦查线索", "把知识碎片连成图", "Connect clues", "Turn scattered clues into a map."),
    ("agent", "Agent", "召唤队友", "工具在手，记忆随身", "Call the party", "Tools ready. Memories packed."),
    ("rl", "RL", "试错升级", "再试一把，经验 +1", "Try. Learn. Repeat.", "One more try. Experience +1."),
]
# Original pixel glyphs: a constellation, a summoned familiar, and a die.
# These are equipped abilities, not buttons, hotkeys or proficiency scores.
GLYPHS = {
    "graphrag": '''
<path d="M4 4h11v2H6v8h9v2H4zm5 3h2v6H9zm7 1h2v7h-2z" fill="{shade}"/>
<path d="M2 2h5v5H2zm11 0h5v5h-5zM7 8h6v6H7zm-5 7h5v5H2zm12 0h5v5h-5z" fill="{bright}"/>
<path d="M3 3h2v2H3zm11 0h2v2h-2zM8 9h2v2H8zm-5 7h2v2H3zm12 0h2v2h-2z" fill="{shine}"/>''',
    "agent": '''
<path d="M8 1h5v2h3v3h2v10h-2v3h-3v-2h-3v3H7v-3H4v-2H2V7h2V4h4z" fill="{shade}"/>
<path d="M8 3h5v2h3v9h-3v2h-3v-2H7v2H4V8h2V5h2z" fill="{bright}"/>
<path d="M8 4h4v2H8zm-3 3h2v3H5z" fill="{shine}"/>
<path d="M7 8h2v3H7zm5 0h2v3h-2z" fill="#132429"/>
<path d="M17 2h2v2h-2zM1 17h2v2H1z" fill="{shine}"/>''',
    "rl": '''
<path d="M7 1h7v2h3v3h3v9h-3v3h-3v3H7v-3H4v-3H1V6h3V3h3z" fill="{shade}"/>
<path d="M7 3h7v2h3v10h-3v3H7v-3H4V6h3z" fill="{bright}"/>
<path d="M7 4h7v2H7zM5 6h2v7H5z" fill="{shine}"/>
<path d="M9 8h3v5H9zm-2 7h8v2H7z" fill="#47341f"/>
<path d="M17 0h2v2h2v2h-2v2h-2V4h-2V2h2z" fill="{shine}"/>''',
}
THEMES = {
    "light": dict(ink="#283633", sub="#52645e", accents=("#21826a", "#386f9c", "#966823")),
    "dark": dict(ink="#e4eee7", sub="#bacbc2", accents=("#8ed6b5", "#91bff1", "#e2c282")),
}
GEMS = [
    dict(bright="#86d6ad", shade="#366f5d", shine="#d6f9de", bed="#18312b"),
    dict(bright="#91c8ed", shade="#466886", shine="#d9f3ff", bed="#1a2b3b"),
    dict(bright="#e5bb6c", shade="#946a36", shine="#fff0b3", bed="#342c22"),
]


def socket(slug, index, lang):
    gem = GEMS[index]
    status = "已装备" if lang == "zh" else "EQUIPPED"
    return f'''<g shape-rendering="crispEdges">
<path d="M14 4h56v5h7v7h5v56h-5v7h-7v5H14v-5H7v-7H2V16h5V9h7z" fill="#182526"/>
<path d="M13 2h56v5h7v7h5v56h-5v7h-7v5H13v-5H6v-7H1V14h5V7h7z" fill="#52635f"/>
<path d="M14 6h54v5h5v5h4v52h-4v5h-5v5H14v-5H9v-5H5V16h4v-5h5z" fill="#263633"/>
<path d="M17 11h48v4h5v50h-5v5H17v-5h-5V15h5z" fill="{gem['bed']}"/>
<path d="M17 11h48v2H17zm-5 4h2v50h-2z" fill="{gem['shade']}"/>
<path d="M8 8h9v3h-6v6H8zm57 0h9v9h-3v-6h-6zM8 65h3v6h6v3H8zm63 0h3v9h-9v-3h6z" fill="#b5aa7e"/>
<rect x="17" y="69" width="48" height="10" fill="#1b2927"/>
<rect x="21" y="73" width="3" height="3" fill="{gem['bright']}"/>
<g transform="translate(20 22) scale(2)">{GLYPHS[slug].format(**gem)}</g>
</g>
<text x="16" y="21" font-family="{MONO}" font-size="7" fill="#becabe">{index+1:02d}</text>
<text x="43" y="76.5" text-anchor="middle" font-size="{7.5 if lang == 'zh' else 5.5}" letter-spacing=".7" fill="#d4e3d8">{status}</text>'''


def build(skill, index, theme, lang, compact=False):
    slug, name, zh_role, zh_desc, en_role, en_desc = skill
    role, desc = (zh_role, zh_desc) if lang == "zh" else (en_role, en_desc)
    p = THEMES[theme]
    accent = p["accents"][index]
    width, height = (240, 188) if compact else (280, 92)
    title = escape(f"{name} · {role} — {desc}")
    if compact:
        content = f'''<g transform="translate(76 0) scale(1.08)">{socket(slug, index, lang)}</g>
<text x="120" y="132" text-anchor="middle" font-family="{MONO}" font-size="33" font-weight="700" fill="{accent}">{name}</text>
<text x="120" y="172" text-anchor="middle" font-size="{26 if lang == 'zh' else 20}" font-weight="600" fill="{p['ink']}">{escape(role)}</text>'''
    else:
        content = f'''{socket(slug, index, lang)}
<text x="97" y="28" font-family="{MONO}" font-size="22" font-weight="700" fill="{accent}">{name}</text>
<text x="97" y="52" font-size="{13 if lang == 'zh' else 11}" font-weight="600" fill="{p['ink']}">{escape(role)}</text>
<text x="97" y="73" font-size="{11.5 if lang == 'zh' else 10}" fill="{p['sub']}">{escape(desc)}</text>'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title">
<title id="title">{title}</title>
<g font-family="{FONT}">{content}</g>
</svg>
'''


for i, skill in enumerate(SKILLS):
    for theme in THEMES:
        for lang in ("zh", "en"):
            for compact in (False, True):
                suffix = "-compact" if compact else ""
                path = ASSETS / f"skill-{skill[0]}-{lang}-{theme}{suffix}.svg"
                path.write_text(build(skill, i, theme, lang, compact), encoding="utf-8")
print("Built 3 equipped skills × 2 languages × 2 themes × 2 sizes.")
