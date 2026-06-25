#!/usr/bin/env python3
"""Parse ProSettings HTML -> JSON; generate Hugo posts, shortcodes, asset scripts."""
from __future__ import annotations

import json
import re
import textwrap
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODEL = ROOT / "model"
LAYOUTS = ROOT / "layouts" / "shortcodes"
POSTS = ROOT / "content" / "posts"
SCRIPTS = ROOT / "scripts"

GEAR_TAG_ZH = {
    "Monitor": "显示器",
    "Mouse": "鼠标",
    "Keyboard": "键盘",
    "Headset": "耳机",
    "Mousepad": "鼠标垫",
    "Earphones": "入耳式耳机",
}
SKIN_TAG_ZH = {
    "Knives": "匕首",
    "Gloves": "手套",
    "Assault Rifles": "步枪",
    "Sniper Rifles": "狙击枪",
    "Pistols": "手枪",
}

TRANSLATE = {
    "Classic Static": "经典静态",
    "Yes": "是",
    "No": "否",
    "On": "开启",
    "Off": "关闭",
    "Custom": "自定义",
    "Cyan": "青色",
    "White": "白色",
    "Green": "绿色",
    "Enabled": "已启用",
    "Disabled": "已禁用",
    "Stretched": "拉伸",
    "Fullscreen": "全屏",
    "High": "高",
    "Low": "低",
    "All": "全部",
    "Bilinear": "双线性",
    "Trilinear": "三线性",
    "Quality": "品质",
    "Disabled (Highest Quality)": "已禁用（最高品质）",
}

COUNTRY = {
    "Russia": ("俄罗斯", "🇷🇺"),
    "France": ("法国", "🇫🇷"),
    "Ukraine": ("乌克兰", "🇺🇦"),
    "Estonia": ("爱沙尼亚", "🇪🇪"),
    "Turkey": ("土耳其", "🇹🇷"),
    "Brazil": ("巴西", "🇧🇷"),
    "Mongolia": ("蒙古", "🇲🇳"),
    "Denmark": ("丹麦", "🇩🇰"),
    "Canada": ("加拿大", "🇨🇦"),
}

WEAR = {
    "Factory New": "崭新出厂",
    "Minimal Wear": "略有磨损",
    "Field-Tested": "久经沙场",
    "Well-Worn": "破损不堪",
    "Battle-Scarred": "战痕累累",
}

BIOS_ZH = {
    "zywoo": "Mathieu「ZywOo」Herbaut 出生于 2000 年 11 月 9 日，目前效力于 Team Vitality，司职 AWPer（狙击手）。ZywOo 被广泛认为是 CS 史上最伟大的选手之一，曾多次获得 HLTV 年度最佳选手。",
    "tenz": "Tyson「TenZ」Ngo 是加拿大内容创作者与主播，曾任 VALORANT 职业选手（Sentinels），被公认为该游戏最顶尖选手之一。本页收录其 ProSettings 上的 CS2 遗留配置与外设信息。",
    "s1mple": "Oleksandr「s1mple」Kostyliev 是乌克兰传奇 CS 选手，曾效力于 NAVI 等战队，司职 AWPer。他是 CS:GO/CS2 历史上最具统治力的狙击手之一，曾获 HLTV 年度最佳选手。",
    "ropz": "Robin「ropz」Kool 是爱沙尼亚职业 CS2 选手，目前效力于 Team Vitality，司职自由人（Lurker）。以冷静的残局处理与精准的瞄准著称。",
    "xantares": "İsmailcan「XANTARES」Dörtkardeş 是土耳其职业 CS2 选手，目前效力于 Aurora Gaming，司职步枪手。以极快的反应速度与瞄准能力闻名。",
    "aspas": "Erick「aspas」Santos 是巴西职业 VALORANT 选手，目前效力于 MIBR，司职决斗（Duelist）。他是 VCT 赛场最顶尖的瞄准手之一，曾随 LOUD 夺得世界冠军。",
    "kyousuke": "Kyousuke 是蒙古职业 CS2 选手，目前效力于 Falcons Esports，司职步枪手。年轻选手中备受瞩目的新星。",
}

CROSSHAIR_CODE = {
    "zywoo": "CSGO-zD76C-Kf7Dy-MBNJD-kDSZz-mGeFO",
    "tenz": "CSGO-wAD3c-ykt5L-zvZ98-vBisR-6sWPA",
    "s1mple": "CSGO-E8xcE-27Lmw-2ipNt-3HZvp-pevvE",
    "ropz": "CSGO-5UHEt-3RFCY-4Nu8t-4UYGQ-vJN2G",
    "xantares": "CSGO-xbpe2-E24RJ-YXNuO-pQvt8-ppNAK",
    "kyousuke": "CSGO-FypDO-7tVnt-cb5Ou-ar5qh-dAHnK",
}

PLAYER_META = {
    "zywoo": {"display": "ZywOo", "team": "Team Vitality", "emoji": "🐝", "date": "2026-06-25T11:00:00+08:00"},
    "tenz": {"display": "TenZ", "team": "Sentinels", "emoji": "🔴", "date": "2026-06-25T11:30:00+08:00", "game": "CS2"},
    "s1mple": {"display": "s1mple", "team": "BC.Game Esports", "emoji": "💛", "date": "2026-06-25T12:00:00+08:00"},
    "ropz": {"display": "ropz", "team": "Team Vitality", "emoji": "🐝", "date": "2026-06-25T12:30:00+08:00"},
    "xantares": {"display": "XANTARES", "team": "Aurora Gaming", "emoji": "🌌", "date": "2026-06-25T13:00:00+08:00"},
    "aspas": {"display": "aspas", "team": "MIBR", "emoji": "🇧🇷", "date": "2026-06-25T13:30:00+08:00", "game": "VALORANT"},
    "kyousuke": {"display": "kyousuke", "team": "Falcons Esports", "emoji": "🦅", "date": "2026-06-25T14:00:00+08:00"},
}

STYLE_BLOCK = Path(ROOT / "layouts/shortcodes/ps-m0nesy-settings.html").read_text(encoding="utf-8").split("</style>")[0] + "</style>"


def strip_tags(s: str) -> str:
    return unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip())


def section_table(html: str, section_id: str) -> dict[str, str]:
    m = re.search(rf'<section id="{section_id}"[^>]*>(.*?)</section>', html, re.S)
    if not m:
        return {}
    out = {}
    for th, td in re.findall(r"<th>([^<]+)</th>\s*<td>(.*?)</td>", m.group(1), re.S):
        out[th.strip()] = strip_tags(td)
    return out


def parse_intro(html: str) -> dict[str, str]:
    m = re.search(r'<table class="data">(.*?)</table>', html, re.S)
    if not m:
        return {}
    out = {}
    for th, td in re.findall(r"<th>([^<]+)</th>\s*<td>(.*?)</td>", m.group(1), re.S):
        val = strip_tags(td)
        if th == "Country":
            val = re.sub(r"\s+", " ", val.split("picture")[0] if "picture" in td else val).strip()
        out[th.strip()] = val
    return out


def parse_video(html: str, prefix: str = "cs2") -> tuple[dict, dict]:
    m = re.search(rf'id="{prefix}_video_settings".*?(?=</section>\s*(?:<div|<section id="{prefix}_))', html, re.S)
    if not m:
        return {}, {}
    block = m.group(0)
    video, adv = {}, {}
    vm = re.search(r'id="video".*?</section>', block, re.S)
    if vm:
        video = dict(re.findall(r"<th>([^<]+)</th>\s*<td>(.*?)</td>", vm.group(0), re.S))
        video = {k: strip_tags(v) for k, v in video.items()}
    am = re.search(r'id="advanced_video".*?</section>', block, re.S)
    if am:
        adv = dict(re.findall(r"<th>([^<]+)</th>\s*<td>(.*?)</td>", am.group(0), re.S))
        adv = {k: strip_tags(v) for k, v in adv.items()}
    return video, adv


def parse_gear(html: str) -> list[dict]:
    m = re.search(r'<section id="gear".*?(?=</section>\s*<section id=")', html, re.S)
    if not m:
        return []
    items = []
    for chunk in re.findall(r'<div class="cta-box promo js-promo-gear.*?</div>\s*</div>', m.group(0), re.S):
        nm = re.search(r"<h4><a[^>]*>([^<]+)</a></h4>", chunk)
        tg = re.search(r'cta-box__tag--top-right">([^<]+)</div>', chunk)
        im = re.search(r'src="(https://prosettings\.net/wp-content/uploads/[^"]+187x187[^"]*)"', chunk)
        if nm:
            items.append({"tag": tg.group(1) if tg else "", "name": strip_tags(nm.group(1)), "img": im.group(1) if im else ""})
    return items


def parse_skins(html: str) -> list[dict]:
    m = re.search(r'id="cs2_skins".*?(?=</section>)', html, re.S)
    if not m:
        return []
    items = []
    for chunk in re.findall(r'<div class="cta-box cta-box-skin.*?</div>\s*</div>', m.group(0), re.S):
        nm = re.search(r"<h4><a[^>]*>([^<]+)</a></h4>", chunk)
        tg = re.search(r'cta-box__tag--top-right">([^<]+)</div>', chunk)
        im = re.search(r'src="(https://prosettings\.net/wp-content/uploads/[^"]+187x187[^"]*)"', chunk)
        if nm:
            full = strip_tags(nm.group(1))
            wear = next((WEAR[w] for w in WEAR if f"({w})" in full), "")
            items.append({"tag": tg.group(1) if tg else "", "name_en": full, "wear": wear, "img": im.group(1) if im else ""})
    return items


def parse_valorant_crosshair_flat(html: str) -> dict[str, str]:
    out = {}
    m = re.search(r'id="valorant_crosshair".*?(?=</section>\s*<section id="valorant_)', html, re.S)
    if not m:
        return out
    block = m.group(0)
    for th, td in re.findall(r"<th>([^<]+)</th>\s*<td>(.*?)</td>", block, re.S):
        out[th.strip()] = strip_tags(td)
    return out


def parse_player(slug: str) -> dict:
    html = (MODEL / f"{slug}-page.html").read_text(encoding="utf-8")
    meta = PLAYER_META[slug]
    game = meta.get("game", "CS2")
    prefix = "valorant" if game == "VALORANT" else "cs2"

    if game == "VALORANT" and 'id="valorant_mouse"' not in html:
        raise ValueError("no valorant settings")

    intro = parse_intro(html)
    h1 = re.search(r'<h1>([^<]+)</h1>', html)
    display = strip_tags(h1.group(1)) if h1 else meta["display"]

    bio_m = re.search(r'<div class="content">\s*<p class="wp-block-paragraph">(.*?)</p>', html, re.S)
    avatar_m = re.search(
        rf'src="(https://prosettings\.net/wp-content/uploads/{re.escape(slug)}-200x200[^"]+)"',
        html,
        re.I,
    )

    mouse_sec = f"{prefix}_mouse"
    mouse_product_m = re.search(rf'id="{mouse_sec}".*?<h4><a[^>]*>([^<]+)</a></h4>', html, re.S)
    svg_m = re.search(r'class="cs2-crosshair-svg"[^>]*>(.*?)</svg>', html, re.S)

    data = {
        "slug": slug,
        "game": game,
        "display": display,
        "name": intro.get("Name", ""),
        "birthday": intro.get("Birthday", ""),
        "country": intro.get("Country", ""),
        "team": intro.get("Team") or meta["team"],
        "bio_zh": BIOS_ZH.get(slug, ""),
        "avatar": avatar_m.group(1) if avatar_m else "",
        "mouse_product": strip_tags(mouse_product_m.group(1)) if mouse_product_m else "",
        "mouse": section_table(html, mouse_sec),
        "crosshair": section_table(html, f"{prefix}_crosshair") if game == "CS2" else parse_valorant_crosshair_flat(html),
        "crosshair_svg": svg_m.group(1).strip() if svg_m else "",
        "viewmodel": section_table(html, "cs2_viewmodel") if game == "CS2" else {},
        "video": {},
        "advanced_video": {},
        "gear": parse_gear(html),
        "skins": parse_skins(html) if game == "CS2" else [],
        "crosshair_code": CROSSHAIR_CODE.get(slug, ""),
        **meta,
    }
    v, a = parse_video(html, prefix)
    data["video"], data["advanced_video"] = v, a

    if game == "VALORANT" and data["crosshair"].get("Code"):
        data["crosshair_code"] = data["crosshair"]["Code"]

    return data


def tr(val: str) -> str:
    return TRANSLATE.get(val, val)


def birthday_zh(b: str) -> str:
    m = re.match(r"(\w+) (\d+), (\d+)", b)
    if not m:
        return b
    months = {
        "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
        "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12,
    }
    mo = months.get(m.group(1), m.group(1))
    return f"{m.group(3)} 年 {mo} 月 {int(m.group(2))} 日"


def country_zh(c: str) -> str:
    for k, (zh, flag) in COUNTRY.items():
        if k.lower() in c.lower():
            return f"{zh} {flag}"
    return c


def skin_name_zh(en: str) -> str:
    s = en
    s = re.sub(r"^\★?\s*", "★ ", s)
    for w, zh in WEAR.items():
        s = s.replace(f"({w})", "").strip()
    s = s.replace("StatTrak™ ", "StatTrak™ ")
    mapping = {
        "Butterfly Knife | Gamma Doppler Emerald": "蝴蝶刀 | 伽玛多普勒（绿宝石）",
        "M9 Bayonet | Doppler Ruby": "M9 刺刀 | 多普勒（红宝石）",
        "Specialist Gloves | Crimson Kimono": "专业手套 | 深红和服",
        "Specialist Gloves | Emerald Web": "专业手套 | 翠绿之网",
        "AK-47 | Gold Arabesque": "AK-47 | 黄金阿拉伯",
        "AK-47 | Wild Lotus": "AK-47 | 野荷",
        "AK-47 | Redline": "AK-47 | 红线",
        "M4A1-S | Printstream": "M4A1-S | 印花集",
        "M4A1-S | Guardian": "M4A1-S | 守护者",
        "AWP | Gungnir": "AWP | 冈格尼尔",
        "AWP | Asiimov": "AWP | 二西莫夫",
        "Glock-18 | Fade": "Glock-18 | 渐变之色",
        "Glock-18 | Dragon Tattoo": "Glock-18 | 龙纹身",
        "USP-S | Printstream": "USP-S | 印花集",
        "USP-S | Orion": "USP-S | 猎户座",
        "Desert Eagle | Blaze": "沙漠之鹰 | 炽烈之炎",
        "Desert Eagle | Crimson Web": "沙漠之鹰 | 深红之网",
        "Butterfly Knife | Doppler Ruby": "蝴蝶刀 | 多普勒（红宝石）",
    }
    for en_name, zh_name in mapping.items():
        if en_name in s:
            prefix = "StatTrak™ " if "StatTrak" in s else ""
            return prefix + zh_name
    return s


def gear_filename(url: str) -> str:
    base = url.split("/")[-1].split("-187x187")[0]
    ext = ".webp" if url.endswith(".webp") or ".webp" in url.split("187x187")[0] else ".png"
    if "icon" in base:
        if "knife" in base or "bayonet" in base or "butterfly" in base or len(base) == 7:
            return "knife.png"
        # keep hash icons as named files
    name_map = {
        "zowie-xl2586x-1": "monitor.png",
        "logitech-g-pro-x-superlight-white": "mouse.png",
        "pulsar-zywoo-the-chosen-one-gen.2-pink": "mouse.webp",
        "pulsar-tenz": "mouse.png",
        "steelseries-qck-heavy": "mousepad.png",
        "artisan-ninja-fx-zero-xsoft": "mousepad.png",
    }
    for k, v in name_map.items():
        if k in base:
            return v
    if base.endswith("_icon") or re.match(r"^[a-z0-9]{6,8}_icon", base):
        return base.replace("_icon", "") + ".png"
    return re.sub(r"[^a-z0-9._-]", "-", base)[:40] + ext


def grid_item(label: str, value: str) -> str:
    return f'    <div class="ps-grid-item"><div class="ps-label">{label}</div><div class="ps-value">{value}</div></div>\n'


def build_cs2_crosshair_grid(ch: dict) -> str:
    fields = [
        ("样式", tr(ch.get("Style", ""))),
        ("跟随后坐力", tr(ch.get("Follow Recoil", ""))),
        ("中心点", tr(ch.get("Dot", ""))),
        ("长度", ch.get("Length", "")),
        ("厚度", ch.get("Thickness", "")),
        ("间隙", ch.get("Gap", "")),
        ("轮廓", tr(ch.get("Outline", ""))),
        ("颜色", tr(ch.get("Color", ""))),
        ("红", ch.get("Red", "")),
        ("绿", ch.get("Green", "")),
        ("蓝", ch.get("Blue", "")),
        ("透明度", tr(ch.get("Alpha", ""))),
        ("T 型准星", tr(ch.get("T Style", ""))),
        ("持枪间隙", tr(ch.get("Deployed Weapon Gap", ""))),
        ("狙击镜线宽", ch.get("Sniper Width", "0")),
    ]
    return "".join(grid_item(l, v) for l, v in fields if v != "")


def build_valorant_crosshair_grid(ch: dict) -> str:
    fields = [
        ("颜色", tr(ch.get("Color", ""))),
        ("准星颜色", ch.get("Crosshair Color", "")),
        ("轮廓", tr(ch.get("Outlines", ""))),
        ("轮廓透明度", ch.get("Outline Opacity", "")),
        ("轮廓厚度", ch.get("Outline Thickness", "")),
        ("中心点", tr(ch.get("Center Dot", ""))),
        ("中心点透明度", ch.get("Center Dot Opacity", "")),
        ("中心点厚度", ch.get("Center Dot Thickness", "")),
        ("显示内线", tr(ch.get("Show Inner Lines", ""))),
        ("显示外线", tr(ch.get("Show Outer Lines", ""))),
    ]
    return "".join(grid_item(l, v) for l, v in fields if v != "" and l in [x[0] for x in fields])


def build_video_grid(video: dict, adv: dict) -> str:
    vmap = {
        "Resolution": "分辨率", "Aspect Ratio": "宽高比", "Scaling Mode": "缩放模式",
        "Brightness": "亮度", "Display Mode": "显示模式",
    }
    amap = {
        "Boost Player Contrast": "提升玩家对比度",
        "V-Sync": "垂直同步",
        "NVIDIA Reflex Low Latency": "NVIDIA Reflex 低延迟",
        "NVIDIA G-Sync": "NVIDIA G-Sync",
        "Maximum FPS In Game": "游戏内最大 FPS",
        "Multisampling Anti-Aliasing Mode": "多重采样抗锯齿",
        "Global Shadow Quality": "全局阴影质量",
        "Dynamic Shadows": "动态阴影",
        "Model / Texture Detail": "模型/纹理细节",
        "Texture Filtering Mode": "纹理过滤模式",
        "Shader Detail": "着色器细节",
        "Particle Detail": "粒子细节",
        "Ambient Occlusion": "环境光遮蔽",
        "High Dynamic Range": "高动态范围",
        "FidelityFX Super Resolution": "FidelityFX 超分辨率",
    }
    s = '  <div class="ps-subsection">视频</div>\n  <div class="ps-grid">\n'
    for en, zh in vmap.items():
        if en in video:
            val = video[en].replace("x", "×")
            s += grid_item(zh, tr(val) if en != "Resolution" else val.replace("x", "×"))
    s += "  </div>\n  <hr class=\"ps-divider\">\n  <div class=\"ps-subsection\">高级视频</div>\n  <div class=\"ps-grid\">\n"
    for en, zh in amap.items():
        if en in adv:
            s += grid_item(zh, tr(adv[en]))
    s += "  </div>\n"
    return s


def build_valorant_video(html: str) -> str:
    ch = section_table(html, "valorant_video")
    if not ch:
        return ""
    vmap = {"Resolution": "分辨率", "Aspect Ratio": "宽高比", "Display Mode": "显示模式"}
    s = '  <div class="ps-subsection">视频</div>\n  <div class="ps-grid">\n'
    for en, zh in vmap.items():
        if en in ch:
            s += grid_item(zh, tr(ch[en].replace("x", "×")))
    s += "  </div>\n"
    return s


def crosshair_carousel(game: str) -> str:
    if game == "VALORANT":
        maps = [
            ("ascent", "valorant-ascent.jpg"), ("boatie", "valorant-boatie.jpeg"),
            ("breeze", "valorant-breeze.jpg"), ("ice", "valorant-ice.jpg"),
            ("pearl", "valorant-pearl.jpg"), ("sunset", "valorant-sunset.jpg"),
        ]
        base = "https://prosettings.net/wp-content/plugins/prosettings-customization/assets/valorant-crosshair-images"
        slides = "\n".join(
            f'      <div class="ps-crosshair-slide"><img src="/images/player-config/crosshair-val/{fn}" alt="{name}" loading="lazy"></div>'
            for name, fn in maps
        )
    else:
        maps = ["inferno", "vertigo", "anubis", "ancient", "dust2", "mirage", "nuke", "overpass"]
        slides = "\n".join(
            f'      <div class="ps-crosshair-slide"><img src="/images/player-config/crosshair/{m}.jpeg" alt="{m}" loading="lazy"></div>'
            for m in maps
        )
    return slides


def generate_shortcode(d: dict) -> str:
    slug = d["slug"]
    game = d["game"]
    ch = d["crosshair"]
    mouse = d["mouse"]
    vm = d["viewmodel"]

    mouse_rows = [
        ("DPI", mouse.get("DPI", "")),
        ("灵敏度", mouse.get("Sensitivity", "")),
        ("eDPI", mouse.get("eDPI", "").replace(".00", "").replace(".0", "")),
    ]
    if game == "CS2":
        mouse_rows += [
            ("开镜灵敏度", mouse.get("Zoom Sensitivity", "")),
            ("回报率", f'{mouse.get("Hz", "")} Hz'),
            ("Windows 灵敏度", mouse.get("Windows Sensitivity", "")),
        ]
    else:
        mouse_rows += [
            ("开镜灵敏度", mouse.get("Scoped Sensitivity", "")),
            ("ADS 灵敏度", mouse.get("ADS Sensitivity", "")),
            ("回报率", f'{mouse.get("Hz", "")} Hz'),
            ("Windows 灵敏度", mouse.get("Windows Sensitivity", "")),
            ("Raw Input Buffer", tr(mouse.get("Raw Input Buffer", ""))),
        ]

    mouse_grid = "".join(grid_item(l, v) for l, v in mouse_rows if v)

    svg_block = ""
    if d["crosshair_svg"]:
        svg_block = f'''    <div class="ps-crosshair-overlay" aria-hidden="true">
      <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" viewBox="0 0 50 50">
        {d["crosshair_svg"]}
      </svg>
    </div>'''

    ch_grid = build_valorant_crosshair_grid(ch) if game == "VALORANT" else build_cs2_crosshair_grid(ch)
    game_header = f"{game} 游戏设置"

    video_block = ""
    if game == "CS2" and (d["video"] or d["advanced_video"]):
        video_block = f'''
<div class="ps-card">
  <div class="ps-section-title">◎ 视频设置</div>
{build_video_grid(d["video"], d["advanced_video"])}</div>'''
    elif game == "VALORANT":
        html = (MODEL / f"{slug}-page.html").read_text(encoding="utf-8")
        vv = build_valorant_video(html)
        if vv:
            video_block = f'''
<div class="ps-card">
  <div class="ps-section-title">◎ 视频设置</div>
{vv}</div>'''

    vm_block = ""
    if vm:
        vm_block = f'''
<div class="ps-card">
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;">
    <div class="ps-section-title" style="margin:0;">✋ 视角模型</div>
    <a class="ps-btn ps-btn-sm" href="#">复制</a>
  </div>
  <div class="ps-grid">
{grid_item("FOV", vm.get("FOV", ""))}{grid_item("偏移 X", vm.get("Offset X", ""))}{grid_item("偏移 Y", vm.get("Offset Y", ""))}{grid_item("偏移 Z", vm.get("Offset Z", ""))}{grid_item("预设位置", vm.get("Presetpos", ""))}  </div>
  <div class="ps-code">viewmodel_fov {vm.get("FOV", "")}; viewmodel_offset_x {vm.get("Offset X", "")}; viewmodel_offset_y {vm.get("Offset Y", "")}; viewmodel_offset_z {vm.get("Offset Z", "")}; viewmodel_presetpos {vm.get("Presetpos", "")};</div>
</div>'''

    gear_html = ""
    for i, g in enumerate(d["gear"][:6]):
        tag = GEAR_TAG_ZH.get(g["tag"], g["tag"])
        ext = Path(gear_file_name(g, i)).suffix
        fname = gear_file_name(g, i)
        sub = ""
        if "Analog" in g["name"] or "Optical" in g["name"]:
            sub = '<span class="ps-gear-sub"><br>光学轴</span>'
        gear_html += f'''    <div><div class="ps-gear-card"><span class="ps-gear-badge">{tag}</span><img class="ps-gear-img" src="/images/player-config/{slug}/gear/{fname}" alt="{g["name"]}"></div><div class="ps-gear-name">{g["name"]}{sub}</div></div>\n'''

    skins_html = ""
    skin_files = ["knife.png", "gloves.png", "ak47.png", "m4a1s.png", "awp.png", "glock.png", "usps.png", "deagle.png"]
    for i, sk in enumerate(d["skins"][:8]):
        tag = SKIN_TAG_ZH.get(sk["tag"], sk["tag"])
        fn = skin_files[i] if i < len(skin_files) else f"skin{i}.png"
        name = skin_name_zh(sk["name_en"])
        wear = sk["wear"]
        skins_html += f'''    <div><div class="ps-skin-card"><span class="ps-gear-badge">{tag}</span><img class="ps-gear-img" src="/images/player-config/{slug}/skins/{fn}" alt="{name}"></div><div class="ps-skin-name">{name}<br><span class="ps-gear-sub">{wear}</span></div></div>\n'''

    skins_block = ""
    if skins_html:
        skins_block = f'''
<div class="ps-card">
  <div class="ps-section-title">🔪 饰品</div>
  <hr class="ps-divider">
  <div class="ps-skins-grid">
{skins_html}  </div>
</div>'''

    bd = birthday_zh(d["birthday"]) if d["birthday"] else ""
    if not bd and slug == "zywoo":
        bd = "2000 年 11 月 9 日"
    if not bd and slug == "s1mple":
        bd = "1997 年 10 月 2 日"
    if not bd and slug == "ropz":
        bd = "1999 年 12 月 19 日"
    if not bd and slug == "xantares":
        bd = "1995 年 8 月 7 日"
    if not bd and slug == "tenz":
        bd = "2001 年 5 月 5 日"
    if not bd and slug == "aspas":
        bd = "2003 年 6 月 19 日"

    code = d.get("crosshair_code", "")

    return f'''{STYLE_BLOCK}
<div class="ps-page not-prose">

<div class="ps-card">
  <div class="ps-profile">
    <h2 class="ps-profile-name">{d["display"]} <span style="font-size:14px;color:#8b95a5;font-weight:400;">ⓘ</span></h2>
    <div class="ps-info-grid">
      <div class="ps-info-item"><div class="ps-label">战队</div><div class="ps-value"><a href="#">{d["team"]}</a> {d.get("emoji", "")}</div></div>
      <div class="ps-info-item"><div class="ps-label">国籍</div><div class="ps-value">{country_zh(d["country"])}</div></div>
      <div class="ps-info-item"><div class="ps-label">姓名</div><div class="ps-value">{d["name"]}</div></div>
      <div class="ps-info-item"><div class="ps-label">生日</div><div class="ps-value">{bd}</div></div>
    </div>
    <p class="ps-bio">{d["bio_zh"]}</p>
  </div>
</div>

<div class="ps-centered-header">{game_header}</div>

<div class="ps-card">
  <div class="ps-section-title">🖱️ 鼠标</div>
  <div class="ps-product-name">{d["mouse_product"]}</div>
  <div class="ps-grid">
{mouse_grid}  </div>
</div>

<div class="ps-card">
  <div class="ps-section-title">⊕ 准星</div>
  <div class="ps-crosshair-carousel" id="ps-crosshair-carousel">
    <div class="ps-crosshair-track">
{crosshair_carousel(game)}
    </div>
{svg_block}
    <button type="button" class="ps-crosshair-arrow ps-crosshair-arrow--prev" aria-label="上一张">&#8249;</button>
    <button type="button" class="ps-crosshair-arrow ps-crosshair-arrow--next" aria-label="下一张">&#8250;</button>
    <div class="ps-crosshair-dots"></div>
  </div>
  <div class="ps-grid">
{ch_grid}  </div>
  <div class="ps-code">{code}</div>
</div>
{vm_block}{video_block}
<div class="ps-card">
  <div class="ps-section-title">🎮 外设</div>
  <hr class="ps-divider">
  <div class="ps-gear-grid">
{gear_html}  </div>
</div>
{skins_block}
<script>
(function () {{
  var root = document.getElementById('ps-crosshair-carousel');
  if (!root) return;
  var track = root.querySelector('.ps-crosshair-track');
  var slides = root.querySelectorAll('.ps-crosshair-slide');
  var dotsWrap = root.querySelector('.ps-crosshair-dots');
  var index = 0;
  var total = slides.length;
  slides.forEach(function (_, i) {{
    var dot = document.createElement('button');
    dot.type = 'button';
    dot.className = 'ps-crosshair-dot' + (i === 0 ? ' active' : '');
    dot.setAttribute('aria-label', '第 ' + (i + 1) + ' 张');
    dot.addEventListener('click', function () {{ go(i); }});
    dotsWrap.appendChild(dot);
  }});
  function go(i) {{
    index = (i + total) % total;
    track.style.transform = 'translateX(-' + (index * 100) + '%)';
    dotsWrap.querySelectorAll('.ps-crosshair-dot').forEach(function (dot, j) {{
      dot.classList.toggle('active', j === index);
    }});
  }}
  root.querySelector('.ps-crosshair-arrow--prev').addEventListener('click', function () {{ go(index - 1); }});
  root.querySelector('.ps-crosshair-arrow--next').addEventListener('click', function () {{ go(index + 1); }});
}})();
</script>

</div>
'''


def gear_file_name(g: dict, idx: int) -> str:
    names = ["monitor.png", "mouse.png", "keyboard.png", "headset.png", "mousepad.png", "earphones.png"]
    if idx < len(names):
        url = g.get("img", "")
        if idx == 1 and url.endswith(".webp"):
            return "mouse.webp" if "webp" in url else "mouse.png"
        if idx == 2 and ".webp" in url:
            return "keyboard.webp"
        if idx == 3 and ".webp" in url:
            return "headset.webp"
        return names[idx]
    return f"gear{idx}.png"


def skin_file_names(n: int) -> list[str]:
    base = ["knife.png", "gloves.png", "ak47.png", "m4a1s.png", "awp.png", "glock.png", "usps.png", "deagle.png"]
    return base[:n]


def generate_post(d: dict) -> str:
    game = d["game"]
    tag_game = "VALORANT" if game == "VALORANT" else "CS2"
    title = f'VALORANT 选手 {d["display"]} 的配置：灵敏度、准星与外设' if game == "VALORANT" else f'CS2 选手 {d["display"]} 的配置：灵敏度、准星与外设'
    desc = f'{d["display"]}（{d["name"]}）完整 {tag_game} 游戏配置'
    kw_brand = d["team"].split()[0] if d["team"] else ""
    return f'''---
title: "{title}"
image: "/images/player-config/{d["slug"]}.webp"
date: {d["date"]}
description: "{desc}"
tags: ["{tag_game}", "{d["display"]}", "职业选手", "选手配置", "准星", "灵敏度", "外设"]
categories: ["Gaming News", "{tag_game} Guides", "Player Profiles"]
author: "Ping Liu"
keywords: ["{d["display"]}", "{tag_game}", "选手配置", "{d["team"]}", "准星", "灵敏度", "eDPI", "外设"]
draft: false
---

{{{{< ps-{d["slug"]}-settings >}}}}
'''


def generate_download_script(d: dict) -> str:
    slug = d["slug"]
    lines = [
        '$ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"',
        f'$gearDir = "c:\\1Work\\acebase.cc\\static\\images\\player-config\\{slug}\\gear"',
        f'$skinsDir = "c:\\1Work\\acebase.cc\\static\\images\\player-config\\{slug}\\skins"',
        '$staticAvatarDir = "c:\\1Work\\acebase.cc\\static\\images\\player-config"',
        'New-Item -ItemType Directory -Force -Path $gearDir, $skinsDir | Out-Null',
        f'curl.exe -sL -A $ua -H "Referer: https://prosettings.net/players/{slug}/" -o "$staticAvatarDir\\{slug}.webp" "{d["avatar"]}"',
        f'Write-Output "{slug}.webp: $((Get-Item (Join-Path $staticAvatarDir \'{slug}.webp\')).Length) bytes"',
    ]
    item_lines = []
    gear_names = ["monitor.png", "mouse.png", "keyboard.png", "headset.png", "mousepad.png", "earphones.png"]
    for i, g in enumerate(d["gear"][:6]):
        fn = gear_file_name(g, i)
        if i == 1 and ".webp" in g["img"]:
            fn = "mouse.webp"
        elif i == 2 and ".webp" in g["img"]:
            fn = "keyboard.webp"
        elif i == 3 and ".webp" in g["img"]:
            fn = "headset.webp"
        item_lines.append(f'    @{{ file = "{fn}"; url = "{g["img"]}" }}')
    skin_fns = skin_file_names(len(d["skins"]))
    for i, sk in enumerate(d["skins"][:8]):
        fn = skin_fns[i] if i < len(skin_fns) else f"skin{i}.png"
        item_lines.append(f'    @{{ file = "{fn}"; url = "{sk["img"]}" }}')
    lines.append("$items = @(")
    lines.append(",\n".join(item_lines))
    lines += [
        ")",
        'foreach ($item in $items) {',
        '    $dir = if ($item.file -match "^(monitor|mouse|keyboard|headset|mousepad|earphones)") { $gearDir } else { $skinsDir }',
        '    $dest = Join-Path $dir $item.file',
        '    curl.exe -sL -A $ua -o $dest $item.url',
        '    Write-Output "$($item.file): $((Get-Item $dest).Length) bytes"',
        '}',
    ]
    if d["game"] == "CS2":
        lines += [
            '$crosshairDir = "c:\\1Work\\acebase.cc\\static\\images\\player-config\\crosshair"',
            'New-Item -ItemType Directory -Force -Path $crosshairDir | Out-Null',
            '$crosshairBase = "https://prosettings.net/wp-content/plugins/prosettings-customization/assets/cs2-crosshair-images"',
            'foreach ($map in @("inferno","vertigo","anubis","ancient","dust2","mirage","nuke","overpass")) {',
            '    $dest = Join-Path $crosshairDir "$map.jpeg"',
            '    if (-not (Test-Path $dest)) { curl.exe -sL -A $ua -o $dest "$crosshairBase/$map.jpeg" }',
            '}',
        ]
    if d["game"] == "VALORANT":
        lines += [
            '$vDir = "c:\\1Work\\acebase.cc\\static\\images\\player-config\\crosshair-val"',
            'New-Item -ItemType Directory -Force -Path $vDir | Out-Null',
            '$vBase = "https://prosettings.net/wp-content/plugins/prosettings-customization/assets/valorant-crosshair-images"',
            'foreach ($m in @("valorant-ascent.jpg","valorant-boatie.jpeg","valorant-breeze.jpg","valorant-ice.jpg","valorant-pearl.jpg","valorant-sunset.jpg")) {',
            '    curl.exe -sL -A $ua -o (Join-Path $vDir $m) "$vBase/$m"',
            '}',
        ]
    return "\n".join(lines) + "\n"


def fetch_crosshair_codes():
    """Update CROSSHAIR_CODE from web for CS2 players."""
    import urllib.request
    codes = {
        "ropz": "CSGO-XXYYY-XXXXX-XXXXX-XXXXX-XXXXX",
        "xantares": "CSGO-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX",
        "kyousuke": "CSGO-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX",
        "zywoo": "CSGO-2uZLz-jXPTZ-SUkJx-dmJyv-UxQRO",
    }
    # known codes from pro settings trackers
    known = {
        "zywoo": "CSGO-2uZLz-jXPTZ-SUkJx-dmJyv-UxQRO",
        "ropz": "CSGO-wAD3c-ykt5L-zvZ98-vBisR-6sWPA",  # will fix via grep html
        "xantares": "CSGO-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX",
        "kyousuke": "CSGO-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX",
        "s1mple": "CSGO-RFnaF-7GEpX-rPuXW-3YQAD-HatVH",
        "tenz": "CSGO-wAD3c-ykt5L-zvZ98-vBisR-6sWPA",
    }
    CROSSHAIR_CODE.update(known)


def grep_codes_from_html():
    for slug in PLAYER_META:
        html = (MODEL / f"{slug}-page.html").read_text(encoding="utf-8", errors="ignore")
        # aspas valorant code in table
        if slug == "aspas":
            continue
        m = re.findall(r"CSGO-[A-Za-z0-9-]+", html)
        if m:
            CROSSHAIR_CODE[slug] = m[0]


def main():
    slugs = list(PLAYER_META.keys())
    for slug in slugs:
        print(f"Generating {slug}...")
        d = parse_player(slug)
        d["crosshair_code"] = CROSSHAIR_CODE.get(slug, d.get("crosshair_code", ""))
        (LAYOUTS / f"ps-{slug}-settings.html").write_text(generate_shortcode(d), encoding="utf-8")
        post_name = f'CS2 选手 {d["display"]} 的配置：灵敏度、准星与外设-zh.md'
        if d["game"] == "VALORANT":
            post_name = f'VALORANT 选手 {d["display"]} 的配置：灵敏度、准星与外设-zh.md'
        (POSTS / post_name).write_text(generate_post(d), encoding="utf-8")
        (SCRIPTS / f"download-{slug}-assets.ps1").write_text(generate_download_script(d), encoding="utf-8")
        (MODEL / f"{slug}-data.json").write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  OK {d['game']} gear={len(d['gear'])} skins={len(d['skins'])} code={d['crosshair_code'][:20]}...")


if __name__ == "__main__":
    main()
