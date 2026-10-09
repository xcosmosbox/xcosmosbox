#!/usr/bin/env python3
"""Regenerate the profile's original SVG artwork. Python standard library only."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

PALETTES = {
    "light": dict(bg="#f5f8fb", panel="#ffffff", ink="#10263b", muted="#506779",
                  line="#d2dee8", accent="#007c70", soft="#e0f2ed", amber="#a05c15"),
    "dark": dict(bg="#101d2c", panel="#17293a", ink="#edf6fa", muted="#b0c3d2",
                 line="#344a5b", accent="#77e2c3", soft="#173e3b", amber="#efbb72"),
}

def text(x, y, content, size=20, fill=None, weight=400, **attrs):
    attrs = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in attrs.items())
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}"'
            f' fill="{fill or "currentColor"}" {attrs}>{escape(content)}</text>')

def line(x1,y1,x2,y2,color,width=2,extra=""):
    return f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}" {extra}/>'

def circle(x,y,r,color,stroke=None):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"'+(f' stroke="{stroke}" stroke-width="2"' if stroke else '')+'/>'

def rect(x,y,w,h,r,fill,stroke=None):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"'+(f' stroke="{stroke}"' if stroke else '')+'/>'

def wrap(h, title, desc, body, p):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{h}" viewBox="0 0 1000 {h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<g font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" fill="{p['ink']}">
{rect(.5,.5,999,h-1,20,p['bg'],p['line'])}{body}
</g></svg>'''

def hero(p):
    b = text(44,49,"SAN_CHECK  /  XCOSMOSBOX",16,p['muted'],600,letter_spacing="2")
    b += text(41,124,"Knowledge into action.",49,p['ink'],700,letter_spacing="-1.5")
    b += text(44,168,"Agent systems · GraphRAG · Infrastructure",22,p['muted'])
    b += line(44,203,622,203,p['line'],1)
    b += circle(50,239,5,p['accent']) + text(66,245,"BUILD",14,p['accent'],700,letter_spacing="1.5")
    b += text(165,245,"SHIP",14,p['muted'],600,letter_spacing="1.5")
    b += text(243,245,"EVALUATE",14,p['muted'],600,letter_spacing="1.5")
    for x in range(684,957,28):
        for y in range(35,262,28): b += circle(x,y,1,p['line'])
    nodes=[(731,83),(875,58),(819,138),(939,160),(733,214),(884,237)]
    for a,z in [(0,1),(0,2),(1,2),(1,3),(2,3),(2,4),(2,5),(3,5),(4,5)]:
        b += line(*nodes[a],*nodes[z],p['line'],2)
    for x,y in nodes:
        b += circle(x,y,9,p['panel'],p['accent'])
        b += circle(x,y,3,p['accent'])
    b += circle(819,138,34,p['soft'],p['accent'])
    b += text(798,146,"SC",22,p['accent'],700)
    b += rect(859,208,109,39,10,p['panel'],p['line'])
    b += text(878,233,"COMMIT",12,p['muted'],600,letter_spacing="1.5")
    return wrap(286,"San_Check — Knowledge into action", "Agent systems, GraphRAG and infrastructure. A connected knowledge graph with an SC monogram.",b,p)

def cairn(p):
    b = rect(28,27,52,6,3,p['accent'])
    b += text(29,62,"01 / KNOWLEDGE SYSTEMS",13,p['muted'],600,letter_spacing="1.6")
    b += text(27,110,"Cairn",42,p['ink'],700,letter_spacing="-1")
    b += text(29,145,"Versioned knowledge for agents.",21,p['muted'])
    b += text(29,183,"BUILD  →  EVOLVE  →  SERVE",13,p['accent'],700,letter_spacing="1.3")
    # A conceptual pipeline, not a product screenshot.
    for x,label in [(533,"DOCS"),(714,"GRAPH"),(890,"MCP")]:
        b += text(x,177,label,13,p['muted'],600,text_anchor="middle",letter_spacing="1")
    b += line(568,99,652,99,p['line'],2) + line(779,99,854,99,p['line'],2)
    b += text(610,104,"›",26,p['accent'],600) + text(816,104,"›",26,p['accent'],600)
    for d in [(511,62),(504,68),(497,74)]:
        b += rect(*d,59,66,7,p['panel'],p['line'])
    for y,w in [(93,31),(103,24),(113,31)]: b += line(510,y,510+w,y,p['accent'],2)
    ns=[(682,70),(747,77),(714,106),(680,129),(751,128)]
    for i,j in [(0,1),(0,2),(1,2),(2,3),(2,4),(3,4)]: b+=line(*ns[i],*ns[j],p['line'],2)
    for x,y in ns: b+=circle(x,y,7,p['soft'],p['accent'])
    b += rect(862,68,58,69,12,p['soft'],p['accent'])
    b += text(873,112,"<>_",19,p['accent'],700)
    return wrap(214,"Cairn — Versioned knowledge for agents", "Conceptual pipeline: skill documents become a knowledge graph, delivered over MCP.",b,p)

def campus(p):
    b = rect(28,27,52,6,3,p['amber'])
    b += text(29,62,"02 / PRODUCT ENGINEERING",13,p['muted'],600,letter_spacing="1.6")
    b += text(27,110,"Campus Jobs 2027",39,p['ink'],700,letter_spacing="-1")
    b += text(29,145,"Find an opportunity. Follow it through.",21,p['muted'])
    b += text(29,183,"FILTER  →  VERIFY  →  TRACK",13,p['amber'],700,letter_spacing="1.3")
    # A conceptual workflow, not a product screenshot.
    for i,(label,color,mark) in enumerate([("DISCOVER",p['muted'],"01"),("VERIFY",p['accent'],"02"),("TRACK",p['amber'],"03")]):
        x=528+i*143
        b += rect(x,60,128,91,10,p['panel'],p['line'])
        b += circle(x+24,84,10,p['bg'])
        b += text(x+17,88,mark,10,color,600)
        b += line(x+17,108,x+109,108,p['line'],3)
        b += line(x+17,122,x+82,122,p['line'],3)
        b += text(x+64,177,label,12,color,600,text_anchor="middle",letter_spacing="1")
        b += rect(x+97,74,15,15,4,p['bg'],color)
        if i>0: b+=f'<path d="M{x+100} 81 l3 3 6-7" fill="none" stroke="{color}" stroke-width="1.5"/>'
    return wrap(214,"Campus Jobs 2027 — A complete job-search workspace", "Conceptual workflow: discover opportunities, verify sources and track applications.",b,p)

for mode,palette in PALETTES.items():
    for name,render in [("hero",hero),("cairn",cairn),("campus",campus)]:
        (ASSETS/f"{name}-{mode}.svg").write_text(render(palette)+"\n",encoding="utf-8")
print("Generated 6 SVG assets.")
