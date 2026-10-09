#!/usr/bin/env python3
"""Build the compact project-launcher cards. Python standard library only."""
from html import escape
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"
ASSETS.mkdir(exist_ok=True)

# All projects use the same dimensions and typography. No live counters or services.
CARDS = [
    ("relax", "Relax", "RL", "train", "让大模型学会更好的下一步。", "强化学习 · 训练引擎", "A training ground for better next moves.", "Reinforcement learning · Training engine"),
    ("nanobot", "nanobot", "AGENT", "bot", "轻装上阵的 Agent 小伙伴。", "工具调用 · 长期记忆", "A lightweight Agent companion.", "Tool use · Long-term memory"),
    ("codex-manager", "Codex-Manager", "TOOLS", "terminal", "给模型请求安排个好管家。", "账号管理 · 请求路由", "A little order for your model requests.", "Account management · Request routing"),
    ("knowhere", "Knowhere", "KNOWLEDGE", "book", "把文档拆开，给知识找个家。", "文档解析 · 知识提取", "Give the knowledge in your docs a home.", "Document parsing · Knowledge extraction"),
    ("cairn", "Cairn", "GRAPHRAG", "graph", "给 Agent 一张知识地图。", "图谱检索 · 版本化知识", "A knowledge map for your Agent.", "Graph retrieval · Versioned knowledge"),
    ("party", "邀请一位新队友", "CO-OP", "chat", "带个脑洞来，或者就打个招呼。", "聊个想法 · 留个脚印", "Bring an idea, or simply say hello.", "Swap ideas · Leave a little note"),
]

THEMES = {
    "light": dict(bg="#fafbf9", border="#dce3df", ink="#283633", sub="#52645e", dim="#67776f", accent="#21826a", tile="#eaf2ed", gold="#9a711e"),
    "dark": dict(bg="#161e22", border="#34423e", ink="#e4eee7", sub="#bacbc2", dim="#93a99d", accent="#8ed6b5", tile="#253a31", gold="#dfc17e"),
}

ICONS = {
    "train": '<path d="M2 21h22M4 16l5-5 4 2 8-10M16 3h5v5"/>',
    "bot": '<rect x="3" y="7" width="20" height="15" rx="4"/><path d="M13 3v4M0 13h3m20 0h3M9 17h8"/><path d="M8 12h2m6 0h2"/>',
    "terminal": '<rect x="2" y="3" width="23" height="20" rx="3"/><path d="m7 9 4 4-4 4m8 0h5"/>',
    "book": '<path d="M13 6C8 3 3 4 2 5v17c4-2 8-1 11 1 3-2 7-3 11-1V5c-3-2-7-1-11 1v17M6 9l4 1m-4 4 4 1m7-5 4-1m-4 6 4-1"/>',
    "graph": '<path d="m7 8 11-3M7 8l-2 13m2-13 13 11M5 21l15-2M18 5l2 14"/><circle cx="7" cy="8" r="3"/><circle cx="18" cy="5" r="3"/><circle cx="5" cy="21" r="3"/><circle cx="20" cy="19" r="3"/>',
    "chat": '<path d="M4 4h20v14H13l-7 5v-5H4zM8 9h12M8 13h8"/>',
}


def build(card, theme, lang):
    slug, name, label, icon, zh, zh_sub, en, en_sub = card
    p = THEMES[theme]
    if lang == "en" and slug == "party":
        name = "Find a new party member"
    desc, sub = (zh, zh_sub) if lang == "zh" else (en, en_sub)
    title = f"{name} — {desc} {sub}"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="360" height="88" viewBox="0 0 360 88" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">{escape('打开项目' if slug != 'party' else '打开留言入口')}</desc>
<rect x=".5" y=".5" width="359" height="81" rx="9" fill="{p['bg']}" stroke="{p['border']}"/>
<path d="M1 23V10a9 9 0 0 1 9-9h16" fill="none" stroke="{p['accent']}" stroke-width="2"/>
<rect x="13" y="17" width="40" height="44" rx="8" fill="{p['tile']}"/>
<g transform="translate(20 26)" fill="none" stroke="{p['accent']}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{ICONS[icon]}</g>
<g font-family="-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans CJK SC','Microsoft YaHei',sans-serif">
<text x="65" y="25" font-size="15.5" font-weight="650" fill="{p['ink']}">{escape(name)}</text>
<text x="339" y="24" text-anchor="end" font-size="10" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" letter-spacing=".5" fill="{p['gold']}">{label}</text>
<text x="65" y="46" font-size="13" fill="{p['sub']}">{escape(desc)}</text>
<text x="65" y="66" font-size="11" fill="{p['dim']}">{escape(sub)}</text>
</g>
<path d="M331 63h8m-3-3 3 3-3 3" fill="none" stroke="{p['accent']}" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''


def build_compact(card, theme, lang):
    """Keep project names readable when two columns share a phone screen."""
    slug, name, label, icon, zh, zh_sub, en, en_sub = card
    p = THEMES[theme]
    if lang == "en" and slug == "party":
        name = "Say hello"
    topic = zh_sub if lang == "zh" else en_sub.split(" · ")[0]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="360" height="160" viewBox="0 0 360 160" role="img" aria-labelledby="title">
<title id="title">{escape(name)} — {escape(topic)}</title>
<rect x=".5" y=".5" width="359" height="151" rx="12" fill="{p['bg']}" stroke="{p['border']}"/>
<path d="M1 26V13A12 12 0 0 1 13 1h22" fill="none" stroke="{p['accent']}" stroke-width="3"/>
<g font-family="-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans CJK SC','Microsoft YaHei',sans-serif">
<text x="22" y="55" font-size="29" font-weight="650" fill="{p['ink']}">{escape(name)}</text>
<text x="22" y="102" font-size="23" fill="{p['sub']}">{escape(topic)}</text>
</g>
<path d="M319 130h17m-6-6 6 6-6 6" fill="none" stroke="{p['accent']}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''


for card in CARDS:
    for theme in THEMES:
        for lang in ("zh", "en"):
            (ASSETS / f"{card[0]}-{lang}-{theme}.svg").write_text(build(card, theme, lang) + "\n", encoding="utf-8")
            (ASSETS / f"{card[0]}-{lang}-{theme}-compact.svg").write_text(build_compact(card, theme, lang) + "\n", encoding="utf-8")
print("Built desktop and narrow-screen cards: 6 destinations × 2 languages × 2 themes.")
