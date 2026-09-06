#!/usr/bin/env python3
"""Generates this profile's SVG assets in the AZEKTRA brand palette.

Palette and type are lifted directly from azektra.com's own CSS custom
properties, so the profile and the company site stay in sync:
  --bg #0c0414 / --surface #160a28 / --ink #f0e8f8 / --ink-muted #a899b8
  --primary #d47370 / --accent-peach #eba27f / --border #2a1645
  paper #faf4ec / deep purple ink #2f0e5a
  headings Sora, body Manrope

Run:  python3 assets/build_assets.py
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

FONT = "'Sora','Manrope',system-ui,-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"

DARK = dict(
    name="dark",
    bg="#0c0414", surface="#160a28", tint="#1e0e36",
    ink="#f0e8f8", muted="#a899b8", border="#2a1645",
    primary="#d47370", peach="#eba27f", rose="#da9787",
    glow_a="#d47370", glow_b="#6b3fa0", dot="#3a1a5e",
    tile="#160a28", tileborder="#2a1645",
)
LIGHT = dict(
    name="light",
    bg="#faf4ec", surface="#f3e8da", tint="#efe2d2",
    ink="#2f0e5a", muted="#6b5a7d", border="#e0d2c3",
    primary="#c05f5c", peach="#d4805a", rose="#c07a68",
    glow_a="#d47370", glow_b="#a490c2", dot="#e0d2c3",
    tile="#ffffff", tileborder="#e6dbcc",
)


def hero(t):
    d = t["name"] == "dark"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="320" viewBox="0 0 1200 320" role="img" aria-label="Azam Ali Afzal - AI and GenAI Engineer">
  <defs>
    <radialGradient id="g1" cx="82%" cy="18%" r="58%">
      <stop offset="0%" stop-color="{t['glow_a']}" stop-opacity="{0.30 if d else 0.16}"/>
      <stop offset="100%" stop-color="{t['glow_a']}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="g2" cx="8%" cy="88%" r="55%">
      <stop offset="0%" stop-color="{t['glow_b']}" stop-opacity="{0.28 if d else 0.14}"/>
      <stop offset="100%" stop-color="{t['glow_b']}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="name" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{t['ink']}"/>
      <stop offset="62%" stop-color="{t['ink']}"/>
      <stop offset="100%" stop-color="{t['peach']}"/>
    </linearGradient>
    <linearGradient id="wire" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{t['primary']}" stop-opacity="0.15"/>
      <stop offset="50%" stop-color="{t['peach']}" stop-opacity="0.75"/>
      <stop offset="100%" stop-color="{t['primary']}" stop-opacity="0.15"/>
    </linearGradient>
  </defs>

  <rect width="1200" height="320" rx="18" fill="{t['bg']}"/>
  <rect width="1200" height="320" rx="18" fill="url(#g1)"/>
  <rect width="1200" height="320" rx="18" fill="url(#g2)"/>
  <rect x="0.6" y="0.6" width="1198.8" height="318.8" rx="18" fill="none" stroke="{t['border']}" stroke-width="1.2"/>

  <g fill="{t['dot']}" opacity="{0.85 if d else 0.6}">
    {''.join(f'<circle cx="{60+((i*97)%1080)}" cy="{34+((i*53)%250)}" r="{1.5 if i%5 else 2.2}"/>' for i in range(34))}
  </g>

  <g fill="{t['peach']}">
    <circle cx="905" cy="62" r="2.4" opacity="0.9">
      <animate attributeName="opacity" values="0.25;0.95;0.25" dur="4.2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="1042" cy="104" r="1.9" opacity="0.7">
      <animate attributeName="opacity" values="0.7;0.2;0.7" dur="5.6s" repeatCount="indefinite"/>
    </circle>
    <circle cx="978" cy="46" r="1.5" opacity="0.55">
      <animate attributeName="opacity" values="0.2;0.8;0.2" dur="6.8s" repeatCount="indefinite"/>
    </circle>
    <circle cx="1116" cy="70" r="2.1" opacity="0.5">
      <animate attributeName="opacity" values="0.55;0.15;0.55" dur="3.9s" repeatCount="indefinite"/>
    </circle>
  </g>

  <text x="64" y="92" font-family={FONT!r} font-size="13" font-weight="700"
        letter-spacing="4.2" fill="{t['peach']}">AI &#183; GENAI &#183; MLOPS ENGINEER</text>

  <text x="62" y="164" font-family={FONT!r} font-size="60" font-weight="800"
        letter-spacing="-1.4" fill="url(#name)">Azam Ali Afzal</text>

  <rect x="64" y="186" width="86" height="3" rx="1.5" fill="{t['primary']}"/>

  <text x="64" y="222" font-family={FONT!r} font-size="17.5" fill="{t['ink']}" opacity="{0.92 if d else 0.86}">
    Agentic systems, RAG and MLOps &#8212; built to survive production.
  </text>
  <text x="64" y="252" font-family={FONT!r} font-size="14" fill="{t['muted']}">
    MS Artificial Intelligence @ LUMS &#183; Co-founder @ AZEKTRA &#183; Automation consultant
  </text>

  <g transform="translate(830,196)">
    <line x1="0" y1="0" x2="300" y2="0" stroke="url(#wire)" stroke-width="2"/>
    {''.join(f'<circle cx="{i*75}" cy="0" r="7" fill="{t["surface"] if d else t["tile"]}" stroke="{t["primary"]}" stroke-width="1.8"/>' for i in range(5))}
    <circle r="4.5" fill="{t['peach']}">
      <animate attributeName="cx" values="0;300" dur="3.6s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.08;0.9;1" dur="3.6s" repeatCount="indefinite"/>
    </circle>
    <text x="0" y="30" text-anchor="middle" font-family={FONT!r} font-size="10" letter-spacing="1.8" fill="{t['muted']}">INGEST</text>
    <text x="150" y="30" text-anchor="middle" font-family={FONT!r} font-size="10" letter-spacing="1.8" fill="{t['muted']}">GATE</text>
    <text x="300" y="30" text-anchor="middle" font-family={FONT!r} font-size="10" letter-spacing="1.8" fill="{t['muted']}">SHIP</text>
  </g>
</svg>
'''


STATS = [
    ("99.42%", "precision on auto-filed pages", "production doc pipeline"),
    ("~1,470", "documents/year recovered", "from silent loss"),
    ("0.917", "quadratic weighted kappa", "diabetic retinopathy grading"),
    ("11.3&#8594;51%", "auto-file rate lift", "same archive, measured"),
]


def impact(t):
    d = t["name"] == "dark"
    tiles = []
    for i, (big, label, sub) in enumerate(STATS):
        x = 24 + i * 288
        tiles.append(f'''
    <g transform="translate({x},70)">
      <rect width="264" height="126" rx="12" fill="{t['tile']}" stroke="{t['tileborder']}" stroke-width="1.2"/>
      <rect x="18" y="20" width="26" height="2.5" rx="1.25" fill="{t['primary']}"/>
      <text x="18" y="70" font-family={FONT!r} font-size="{30 if len(big) < 9 else 25}" font-weight="800"
            letter-spacing="-0.8" fill="{t['ink']}">{big}</text>
      <text x="18" y="92" font-family={FONT!r} font-size="12.5" fill="{t['ink']}" opacity="0.82">{label}</text>
      <text x="18" y="110" font-family={FONT!r} font-size="10.5" fill="{t['muted']}">{sub}</text>
    </g>''')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="228" viewBox="0 0 1200 228" role="img" aria-label="Measured outcomes">
  <defs>
    <radialGradient id="ig" cx="50%" cy="0%" r="80%">
      <stop offset="0%" stop-color="{t['glow_a']}" stop-opacity="{0.16 if d else 0.10}"/>
      <stop offset="100%" stop-color="{t['glow_a']}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="1200" height="228" rx="18" fill="{t['bg']}"/>
  <rect width="1200" height="228" rx="18" fill="url(#ig)"/>
  <rect x="0.6" y="0.6" width="1198.8" height="226.8" rx="18" fill="none" stroke="{t['border']}" stroke-width="1.2"/>

  <text x="24" y="40" font-family={FONT!r} font-size="12.5" font-weight="700"
        letter-spacing="3.6" fill="{t['peach']}">MEASURED OUTCOMES</text>
  <text x="24" y="58" font-family={FONT!r} font-size="11.5" fill="{t['muted']}">
    Every figure below is measured on committed code or a real production run &#8212; not estimated.
  </text>
  {''.join(tiles)}
</svg>
'''


for theme in (DARK, LIGHT):
    for nm, fn in (("hero", hero), ("impact", impact)):
        path = os.path.join(OUT, f"{nm}-{theme['name']}.svg")
        open(path, "w", encoding="utf-8").write(fn(theme))
        print("wrote", os.path.basename(path))
