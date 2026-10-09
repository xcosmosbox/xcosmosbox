#!/usr/bin/env python3
"""Build the three linked investigator skill slots. Standard library only."""
from html import escape
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"
FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans SC','Microsoft YaHei',sans-serif"
MONO = "ui-monospace,SFMono-Regular,Consolas,monospace"
SKILLS = [
    ("graphrag", "GraphRAG", "侦查线索", "把知识碎片连成图", "图谱 · 检索", "Connect clues", "Turn scattered clues into a map.", "Graph · Retrieval"),
    ("agent", "Agent", "召唤队友", "工具在手，记忆随身", "工具 · 记忆", "Call the party", "Tools ready. Memories packed.", "Tools · Memory"),
    ("rl", "RL", "试错升级", "再试一把，经验 +1", "探索 · 奖励", "Try. Learn. Repeat.", "One more try. Experience +1.", "Explore · Reward"),
]
ICONS = {
    "graphrag": '<path d="M6 6h13M6 6v14m0-14 13 14M6 20h13M19 6v14"/><path d="M3 3h6v6H3zm13 0h6v6h-6zM3 17h6v6H3zm13 0h6v6h-6z" fill="currentColor" stroke="none"/>',
    "agent": '<path d="M5 7h16v15H5zM9 12h1m6 0h1M9 17h8M13 2v5M1 12h4m16 0h4"/><path d="M11 1h4v3h-4" fill="currentColor" stroke="none"/>',
    "rl": '<path d="M3 21h20M5 18v-5h5V9h6V4h6M18 4h4v4"/><path d="M2 2h5m-2.5-2.5v5"/>',
}
THEMES = {
    "light": dict(bg="#fafbf9", border="#dce3df", ink="#283633", sub="#52645e", accents=("#21826a", "#386f9c", "#966823"), tiles=("#eaf2ed", "#ebf1f8", "#f5efe1")),
    "dark": dict(bg="#161e22", border="#34423e", ink="#e4eee7", sub="#bacbc2", accents=("#8ed6b5", "#91bff1", "#e2c282"), tiles=("#253a31", "#233545", "#3a3325")),
}


def build(skill, index, theme, lang, compact=False):
    slug, name, zh_role, zh_desc, zh_short, en_role, en_desc, en_short = skill
    role, desc, short = (zh_role, zh_desc, zh_short) if lang == "zh" else (en_role, en_desc, en_short)
    p = THEMES[theme]
    accent, tile = p["accents"][index], p["tiles"][index]
    width, height = (240, 142) if compact else (280, 82)
    title = escape(f"{name} · {role} — {desc}")
    if compact:
        content = f'''<path d="M14 16h16m-16 0v16M210 116h16m0-16v16" fill="none" stroke="{accent}" stroke-width="3"/>
<text x="120" y="49" text-anchor="middle" font-family="{MONO}" font-size="33" font-weight="700" fill="{accent}">{name}</text>
<text x="120" y="84" text-anchor="middle" font-size="{26 if lang == 'zh' else 19}" font-weight="600" fill="{p['ink']}">{escape(role)}</text>
<text x="120" y="115" text-anchor="middle" font-size="{21 if lang == 'zh' else 17}" fill="{p['sub']}">{escape(short)}</text>'''
    else:
        content = f'''<rect x="13" y="16" width="32" height="34" rx="6" fill="{tile}"/>
<g transform="translate(17 20) scale(.9)" color="{accent}" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="square" stroke-linejoin="miter">{ICONS[slug]}</g>
<text x="55" y="34" font-family="{MONO}" font-size="22" font-weight="700" fill="{accent}">{name}</text>
<text x="264" y="31" text-anchor="end" font-size="{11.5 if lang == 'zh' else 9}" font-weight="600" fill="{p['sub']}">{escape(role)}</text>
<text x="55" y="59" font-size="{12.5 if lang == 'zh' else 11}" fill="{p['ink']}">{escape(desc)}</text>
<path d="M254 61l9-9m-7 0h7v7" fill="none" stroke="{accent}" stroke-width="1.4"/>
<path d="M1 19V9a8 8 0 0 1 8-8h12" fill="none" stroke="{accent}" stroke-width="2"/>'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title">
<title id="title">{title}</title>
<rect x=".5" y=".5" width="{width-1}" height="{height-6}" rx="8" fill="{p['bg']}" stroke="{p['border']}"/>
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
print("Built 3 skill slots × 2 languages × 2 themes × 2 sizes.")
