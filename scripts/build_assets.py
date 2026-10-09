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

# The illustrated board remains a night scene in either GitHub theme.
# Full-bleed tile backgrounds make adjacent images one surface, while each
# project remains a separate ordinary GitHub link.
THEMES = {
    "light": dict(canvas="#0b1730", bg="#10233e", border="#2b4562", ink="#ecf2fa", sub="#b7cbdc", dim="#94b0c5", accent="#72d9cc", tile="#16394b", gold="#efc474"),
    "dark": dict(canvas="#0b1730", bg="#10233e", border="#34536f", ink="#ecf2fa", sub="#b7cbdc", dim="#94b0c5", accent="#80e0d2", tile="#16394b", gold="#efc474"),
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
<rect width="360" height="88" fill="{p['canvas']}"/>
<path d="M8 4h338l6 6v65l-6 6H8z" fill="{p['bg']}" stroke="{p['border']}"/>
<path d="M8 22V4h23" fill="none" stroke="{p['accent']}" stroke-width="1.5"/>
<path d="M332 81h14l6-6" fill="none" stroke="{p['gold']}" stroke-opacity=".55"/>
<rect x="15" y="19" width="38" height="42" rx="5" fill="{p['tile']}"/>
<g transform="translate(20 26)" fill="none" stroke="{p['accent']}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{ICONS[icon]}</g>
<g font-family="-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans CJK SC','Microsoft YaHei',sans-serif">
<text x="65" y="27" font-size="15.5" font-weight="650" fill="{p['ink']}">{escape(name)}</text>
<text x="337" y="26" text-anchor="end" font-size="9" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" letter-spacing=".5" fill="{p['gold']}">{label}</text>
<text x="65" y="48" font-size="13" fill="{p['sub']}">{escape(desc)}</text>
<text x="65" y="68" font-size="11" fill="{p['dim']}">{escape(sub)}</text>
</g>
<path d="M329 65h8m-3-3 3 3-3 3" fill="none" stroke="{p['accent']}" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''


def build_intro(lang):
    name = "San_Check 的存档点" if lang == "zh" else "San_Check’s save point"
    desc = "写点 Agent，连点知识，偶尔跟 bug 对线。" if lang == "zh" else "Agents, knowledge, and the occasional bug."
    prompt = "挑个副本，随便逛逛" if lang == "zh" else "Pick a quest. Have a look around."
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="360" height="101" viewBox="0 0 360 101" role="img" aria-labelledby="title desc">
<title id="title">{escape(name)}</title><desc id="desc">{escape(desc)} GraphRAG · Agent · RL. {escape(prompt)}</desc>
<rect width="360" height="101" fill="#0b1730"/>
<path d="M0 0h360" stroke="#234360"/>
<rect x="16" y="18" width="3" height="17" fill="#72d9cc"/>
<g font-family="-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans CJK SC','Microsoft YaHei',sans-serif">
<text x="28" y="32" font-size="19" font-weight="650" fill="#ecf2fa">{escape(name)}</text>
<text x="17" y="54" font-size="13" fill="#b7cbdc">{escape(desc)}</text>
<text x="17" y="75" font-size="11" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" fill="#efc474">GraphRAG  /  Agent  /  RL</text>
<text x="17" y="93" font-size="10" fill="#72d9cc">$ ls ~/playground</text>
<text x="128" y="93" font-size="10" fill="#94b0c5">{escape(prompt)}</text>
</g>
</svg>'''


for card in CARDS:
    for theme in THEMES:
        for lang in ("zh", "en"):
            (ASSETS / f"{card[0]}-{lang}-{theme}.svg").write_text(build(card, theme, lang) + "\n", encoding="utf-8")
for lang in ("zh", "en"):
    (ASSETS / f"savepoint-{lang}.svg").write_text(build_intro(lang) + "\n", encoding="utf-8")
print("Built 24 project cards and 2 intro panels on one coherent night-scene canvas.")
