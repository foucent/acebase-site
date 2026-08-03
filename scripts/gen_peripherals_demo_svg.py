#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate demo SVG product images (keyboards + mice) for the acebase.cc
peripherals (/peripherals/) page.

Placeholder product renders so the shop grid can be previewed before real
product photos are sourced. All artwork is generated code, no copyright.
"""
import os

OUT = r"C:/1Work/acebase.cc/docs/assets/peripherals"
TH = os.path.join(OUT, "thumbs")
HE = os.path.join(OUT, "hero")

os.makedirs(TH, exist_ok=True)
os.makedirs(HE, exist_ok=True)

GAP = 3
UNIT = 26
KEY_H = 26
BODY_PAD = 20


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def row_width(row, unit=UNIT, gap=GAP):
    return sum(w * unit for w in row) + gap * (len(row) - 1)


def keycap_grad(key_top, key_bot):
    return f'<linearGradient id="kc" x1="0" y1="0" x2="0" y2="1">' \
           f'<stop offset="0" stop-color="{key_top}"/>' \
           f'<stop offset="1" stop-color="{key_bot}"/></linearGradient>'


def kbd_group(rows, colors, unit=UNIT, gap=GAP, scale=1.0, tx=0, ty=0,
              glow_keys=(), labels=None, brand=""):
    """Rows: list of rows; each row a list of key widths (units)."""
    labels = labels or {}
    key_top, key_bot = colors["keycap"]
    body_top, body_bot = colors["body"]
    accent = colors["accent"]
    key_stroke = colors.get("key_stroke", "rgba(15,23,42,0.45)")
    glow = colors.get("glow", accent)

    max_w = max(row_width(r, unit, gap) for r in rows)
    body_w = max_w + 2 * BODY_PAD
    body_h = len(rows) * KEY_H + (len(rows) - 1) * gap + 2 * BODY_PAD + 26

    x0 = -body_w / 2.0
    y0 = -body_h / 2.0

    parts = []
    parts.append(
        f'<rect x="{x0 + 6}" y="{y0 + body_h - 4}" width="{body_w}" height="14" '
        f'rx="10" fill="rgba(2,6,17,0.5)" filter="url(#shadow)"/>'
    )
    # front edge (depth)
    parts.append(
        f'<rect x="{x0}" y="{y0 + body_h - 26}" width="{body_w}" height="26" '
        f'rx="9" fill="url(#bodybot)" stroke="{key_stroke}" stroke-width="1"/>'
    )
    # body top
    parts.append(
        f'<rect x="{x0}" y="{y0}" width="{body_w}" height="{body_h - 8}" '
        f'rx="9" fill="url(#bodytop)" stroke="{key_stroke}" stroke-width="1.4"/>'
    )
    # keys
    for r, row in enumerate(rows):
        rw = row_width(row, unit, gap)
        kx = -rw / 2.0
        for k, w in enumerate(row):
            kw = w * unit
            fill = "url(#kc)"
            if (r, k) in glow_keys:
                fill = f"url(#kcglow)"
            parts.append(
                f'<rect x="{kx:.2f}" y="{y0 + BODY_PAD + r * (KEY_H + gap):.2f}" '
                f'width="{kw:.2f}" height="{KEY_H}" rx="5" fill="{fill}" '
                f'stroke="{key_stroke}" stroke-width="1"/>'
            )
            if (r, k) in labels:
                lab = labels[(r, k)]
                lw = 8.6
                lh = 10
                parts.append(
                    f'<text x="{kx + kw / 2:.2f}" y="{y0 + BODY_PAD + r * (KEY_H + gap) + KEY_H / 2 + 3.5:.2f}" '
                    f'text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" '
                    f'font-size="9" font-weight="700" fill="{colors.get("label", "#475569")}">{esc(lab)}</text>'
                )
            kx += kw + gap
    if brand:
        parts.append(
            f'<text x="{x0 + BODY_PAD}" y="{y0 + body_h - 4}" '
            f'font-family="Segoe UI, Arial, sans-serif" font-size="11" '
            f'font-weight="800" letter-spacing="2.5" fill="{colors.get("brand", "#64748b")}">{esc(brand)}</text>'
        )

    inner = "".join(parts)
    inner = inner.replace("url(#bodytop)", f"url(#bodytop)").replace("url(#bodybot)", f"url(#bodybot)")
    defs = (
        f'<linearGradient id="bodytop" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{body_top}"/><stop offset="1" stop-color="{body_bot}"/></linearGradient>'
        f'<linearGradient id="bodybot" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{body_bot}"/><stop offset="1" stop-color="{body_top}"/></linearGradient>'
        + keycap_grad(key_top, key_bot)
        + f'<linearGradient id="kcglow" x1="0" y1="0" x2="1" y2="1">'
          f'<stop offset="0" stop-color="{glow}" stop-opacity="0.85"/>'
          f'<stop offset="1" stop-color="{accent}"/></linearGradient>'
        + '<filter id="shadow" x="-30%" y="-60%" width="160%" height="220%">'
          '<feGaussianBlur stdDeviation="4"/></filter>'
    )
    return f'<g transform="translate({tx} {ty}) scale({scale})">' \
           f'<defs>{defs}</defs>{inner}</g>'


def mouse_group(colors, scale=1.0, tx=0, ty=0, dpi=True):
    body_top, body_bot = colors["body"]
    accent = colors["accent"]
    edge = colors.get("edge", "rgba(255,255,255,0.35)")
    body_stroke = colors.get("stroke", "rgba(15,23,42,0.35)")
    # body path (top view, front toward bottom)
    body = ("M0 -150 "
            "C 88 -150, 140 -78, 148 8 "
            "C 156 96, 110 158, 0 158 "
            "C -110 158, -156 96, -148 8 "
            "C -140 -78, -88 -150, 0 -150 Z")
    parts = []
    parts.append(f'<ellipse cx="0" cy="172" rx="118" ry="20" fill="rgba(2,6,17,0.5)" filter="url(#shad)"/>')
    parts.append(
        f'<clipPath id="mclip"><path d="{body}"/></clipPath>'
    )
    parts.append(
        f'<g clip-path="url(#mclip)">'
        f'<path d="{body}" fill="url(#mbody)" stroke="{body_stroke}" stroke-width="2"/>'
        f'<path d="M0 -152 L0 40 L-156 40 Z" fill="{colors.get("btn", "rgba(255,255,255,0.05)")}"/>'
        f'<path d="M0 -152 L0 40 L156 40 Z" fill="{colors.get("btn", "rgba(255,255,255,0.05)")}"/>'
        f'<rect x="-2" y="-150" width="4" height="200" fill="{colors.get("seam", "rgba(15,23,42,0.28)")}"/>'
        f'</g>'
    )
    # buttons seam line across middle
    parts.append(f'<line x1="-128" y1="30" x2="128" y2="30" stroke="{colors.get("seam", "rgba(15,23,42,0.3)")}" stroke-width="2"/>')
    # scroll wheel
    parts.append(
        f'<rect x="-20" y="46" width="40" height="16" rx="8" fill="url(#wheel)"/>'
        f'<line x1="-20" y1="54" x2="20" y2="54" stroke="rgba(15,23,42,0.3)" stroke-width="1.5"/>'
    )
    # dpi button
    if dpi:
        parts.append(f'<rect x="-9" y="72" width="18" height="8" rx="4" fill="{colors.get("dpi", "#94a3b8")}"/>')
    # logo
    parts.append(f'<circle cx="0" cy="-78" r="15" fill="{accent}" opacity="0.95"/>')
    parts.append(f'<circle cx="0" cy="-78" r="7" fill="rgba(255,255,255,0.85)"/>')
    # top edge highlight
    parts.append(
        f'<path d="M0 -148 C 80 -148, 128 -80, 136 2" fill="none" stroke="{edge}" stroke-width="2.5" stroke-linecap="round"/>'
    )
    defs = (
        f'<linearGradient id="mbody" x1="0" y1="-1" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{body_top}"/><stop offset="1" stop-color="{body_bot}"/></linearGradient>'
        f'<linearGradient id="wheel" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{colors.get("wheel_top", "#e2e8f0")}"/>'
        f'<stop offset="1" stop-color="{colors.get("wheel_bot", "#94a3b8")}"/></linearGradient>'
        + '<filter id="shad" x="-40%" y="-80%" width="180%" height="260%">'
          '<feGaussianBlur stdDeviation="5"/></filter>'
    )
    return f'<g transform="translate({tx} {ty}) scale({scale})">' \
           f'<defs>{defs}</defs>{"".join(parts)}</g>'


def wrap_square(group, glow="#14b8a6", cx=300, cy=300):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600" viewBox="0 0 600 600">' \
           f'<defs><radialGradient id="bg" cx="0.5" cy="0.32" r="0.95">' \
           f'<stop offset="0" stop-color="{glow}" stop-opacity="0.28"/>' \
           f'<stop offset="0.55" stop-color="#0f172a"/>' \
           f'<stop offset="1" stop-color="#070b14"/></radialGradient></defs>' \
           f'<rect width="600" height="600" fill="url(#bg)"/>' \
           f'<g transform="translate({cx} {cy})">{group}</g></svg>'


def wrap_hero(group, glow="#14b8a6", cx=700, cy=470):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="900" viewBox="0 0 1400 900">' \
           f'<defs><radialGradient id="bg" cx="0.5" cy="0.35" r="0.95">' \
           f'<stop offset="0" stop-color="{glow}" stop-opacity="0.34"/>' \
           f'<stop offset="0.55" stop-color="#0f172a"/>' \
           f'<stop offset="1" stop-color="#070b14"/></radialGradient></defs>' \
           f'<rect width="1400" height="900" fill="url(#bg)"/>' \
           f'<g transform="translate({cx} {cy})">{group}</g></svg>'


def write(name, content, subdir=TH):
    path = os.path.join(subdir, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)


# ---------------- layouts ----------------
ROWS_75 = [
    [1.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.5],
    [1.75, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2.0],
    [2.25, 1, 1, 1, 1, 1, 1, 1, 1, 2.25],
    [1.25, 1.25, 1.25, 6.25, 1.25, 1.25, 1.25],
]
ROWS_60 = [
    [1.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.5],
    [1.75, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2.0],
    [2.25, 1, 1, 1, 1, 1, 1, 1, 1, 2.25],
    [1.25, 1.25, 1.25, 6.25, 1.25, 1.25, 1.25],
]

LABELS_75 = {(0, 0): "ESC", (4, 3): ""}
GLOW_WASD = {(3, 2), (3, 3), (3, 4), (3, 5)}  # row3 indices: [2.25,1,1,1,1,...] => W,A,S,D at 1..4
GLOW_TKL = {(0, 0), (1, 11), (2, 10), (3, 1), (3, 2), (3, 3), (3, 4)}

# ---------------- products ----------------
def product_svg(fname, group, glow):
    write(fname, wrap_square(group, glow=glow))


# Keyboards
keychron = kbd_group(ROWS_75, {
    "keycap": ("#f8fafc", "#c2ccda"), "body": ("#e9eef5", "#aab6c6"),
    "accent": "#14b8a6", "glow": "#5eead4", "brand": "#5b6b7d", "label": "#7d8b9c",
}, glow_keys={(0, 0)}, labels={(0, 0): "ESC"}, brand="KEYCHRON", scale=1.0)
product_svg("kbd-keychron-k2-pro.svg", keychron, "#14b8a6")

mx = kbd_group(ROWS_75, {
    "keycap": ("#3c465c", "#232b3e"), "body": ("#2b3348", "#151b2b"),
    "accent": "#38bdf8", "glow": "#7dd3fc", "brand": "#94a3b8", "label": "#64748b",
}, glow_keys=set(), labels={(0, 0): "ESC"}, brand="Logitech MX", scale=1.0)
product_svg("kbd-logitech-mx-keys.svg", mx, "#38bdf8")

ducky = kbd_group(ROWS_75, {
    "keycap": ("#ffffff", "#d7dee8"), "body": ("#f1f5f9", "#c3cdda"),
    "accent": "#a78bfa", "glow": "#22d3ee", "brand": "#64748b", "label": "#94a3b8",
    "key_stroke": "rgba(15,23,42,0.3)",
}, glow_keys=GLOW_TKL, labels={(0, 0): "ESC"}, brand="Ducky", scale=1.0)
product_svg("kbd-ducky-one-3.svg", ducky, "#22d3ee")

vgn = kbd_group(ROWS_60, {
    "keycap": ("#1d2942", "#0e1424"), "body": ("#15203a", "#0b1120"),
    "accent": "#22d3ee", "glow": "#38bdf8", "brand": "#64748b", "label": "#94a3b8",
    "key_stroke": "rgba(0,0,0,0.4)",
}, glow_keys=GLOW_WASD, labels={(0, 0): "ESC"}, brand="VGN", scale=1.0)
product_svg("kbd-vgn-v98-pro.svg", vgn, "#22d3ee")

# Mice
g502 = mouse_group({
    "body": ("#303a55", "#141a2e"), "accent": "#14b8a6", "dpi": "#0f766e",
    "btn": "rgba(255,255,255,0.04)", "edge": "rgba(94,234,212,0.35)",
    "stroke": "rgba(0,0,0,0.5)", "wheel_top": "#3d4964", "wheel_bot": "#1a2236",
}, scale=1.3)
product_svg("mouse-logitech-g502x.svg", g502, "#14b8a6")

da3 = mouse_group({
    "body": ("#ffffff", "#cdd5e0"), "accent": "#10b981", "dpi": "#94a3b8",
    "btn": "rgba(15,23,42,0.05)", "edge": "rgba(255,255,255,0.95)",
    "stroke": "rgba(15,23,42,0.3)", "wheel_top": "#f1f5f9", "wheel_bot": "#b6c0cc",
}, scale=1.3)
product_svg("mouse-razer-deathadder-v3.svg", da3, "#10b981")

gpx = mouse_group({
    "body": ("#f8fafc", "#b8c2d0"), "accent": "#0ea5e9", "dpi": "#cbd5e1",
    "btn": "rgba(15,23,42,0.04)", "edge": "rgba(255,255,255,0.9)",
    "stroke": "rgba(15,23,42,0.25)", "wheel_top": "#e9eef5", "wheel_bot": "#aab6c6",
}, scale=1.3, dpi=False)
product_svg("mouse-logitech-gpx-superlight.svg", gpx, "#0ea5e9")

vxe = mouse_group({
    "body": ("#28324c", "#111728"), "accent": "#22d3ee", "dpi": "#0e7490",
    "btn": "rgba(255,255,255,0.04)", "edge": "rgba(34,211,238,0.4)",
    "stroke": "rgba(0,0,0,0.5)", "wheel_top": "#37405c", "wheel_bot": "#161e32",
}, scale=1.3)
product_svg("mouse-vxe-r1-se.svg", vxe, "#22d3ee")

# ---------------- heroes ----------------
write("hero-keyboard.svg", wrap_hero(kbd_group(ROWS_75, {
    "keycap": ("#f8fafc", "#c2ccda"), "body": ("#e9eef5", "#aab6c6"),
    "accent": "#14b8a6", "glow": "#5eead4", "brand": "#5b6b7d", "label": "#7d8b9c",
}, glow_keys={(0, 0)}, labels={(0, 0): "ESC"}, brand="KEYCHRON", scale=1.45), glow="#14b8a6", cx=700, cy=470), HE)

write("hero-mouse.svg", wrap_hero(mouse_group({
    "body": ("#303a55", "#141a2e"), "accent": "#14b8a6", "dpi": "#0f766e",
    "btn": "rgba(255,255,255,0.04)", "edge": "rgba(94,234,212,0.35)",
    "stroke": "rgba(0,0,0,0.5)", "wheel_top": "#3d4964", "wheel_bot": "#1a2236",
}, scale=1.7), glow="#14b8a6", cx=700, cy=470), HE)

write("hero-setup.svg", wrap_hero(
    kbd_group(ROWS_60, {
        "keycap": ("#1d2942", "#0e1424"), "body": ("#15203a", "#0b1120"),
        "accent": "#22d3ee", "glow": "#38bdf8", "brand": "#64748b", "label": "#94a3b8",
        "key_stroke": "rgba(0,0,0,0.4)",
    }, glow_keys=GLOW_WASD, labels={(0, 0): "ESC"}, brand="VGN", scale=1.05, tx=-230, ty=30)
    + mouse_group({
        "body": ("#f8fafc", "#b8c2d0"), "accent": "#0ea5e9", "dpi": "#cbd5e1",
        "btn": "rgba(15,23,42,0.04)", "edge": "rgba(255,255,255,0.9)",
        "stroke": "rgba(15,23,42,0.25)", "wheel_top": "#e9eef5", "wheel_bot": "#aab6c6",
    }, scale=1.35, tx=330, ty=20, dpi=False),
    glow="#22d3ee", cx=700, cy=470), HE)

print("done")
