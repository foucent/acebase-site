#!/usr/bin/env python3
"""Parse ProSettings player HTML and emit JSON for CS2 pages."""
import json
import re
import sys
from html import unescape
from pathlib import Path

MODEL = Path(__file__).resolve().parent.parent / "model"

TRANSLATIONS = {
    "Classic Static": "经典静态",
    "Yes": "是",
    "No": "否",
    "Custom": "自定义",
    "Cyan": "青色",
    "Green": "绿色",
    "Yellow": "黄色",
    "Red": "红色",
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
    "Factory New": "崭新出厂",
    "Minimal Wear": "略有磨损",
    "Field-Tested": "久经沙场",
    "Well-Worn": "破损不堪",
    "Battle-Scarred": "战痕累累",
}

COUNTRY_ZH = {
    "Russia": ("俄罗斯", "🇷🇺"),
    "France": ("法国", "🇫🇷"),
    "Ukraine": ("乌克兰", "🇺🇦"),
    "Estonia": ("爱沙尼亚", "🇪🇪"),
    "Turkey": ("土耳其", "🇹🇷"),
    "Brazil": ("巴西", "🇧🇷"),
    "Mongolia": ("蒙古", "🇲🇳"),
    "Denmark": ("丹麦", "🇩🇰"),
    "Canada": ("加拿大", "🇨🇦"),
    "United States": ("美国", "🇺🇸"),
    "USA": ("美国", "🇺🇸"),
}

WEAR_ZH = {
    "Factory New": "崭新出厂",
    "Minimal Wear": "略有磨损",
    "Field-Tested": "久经沙场",
    "Well-Worn": "破损不堪",
    "Battle-Scarred": "战痕累累",
}

ROLE_ZH = {
    "AWPer": "AWPer（狙击手）",
    "Rifler": "步枪手（Rifler）",
    "Lurker": "自由人（Lurker）",
    "In-game leader": "指挥（IGL）",
    "Support": "辅助（Support）",
}


def strip_tags(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    s = unescape(re.sub(r"\s+", " ", s).strip())
    return s


def section_table(html: str, section_id: str) -> dict[str, str]:
    m = re.search(rf'<section id="{section_id}"[^>]*>(.*?)</section>', html, re.S)
    if not m:
        return {}
    block = m.group(1)
    out = {}
    for th, td in re.findall(r"<tr[^>]*>\s*<th>([^<]+)</th>\s*<td>(.*?)</td>", block, re.S):
        out[th.strip()] = strip_tags(td)
    return out


def nested_video(html: str) -> tuple[dict, dict]:
    m = re.search(r'id="cs2_video_settings".*?(?=</section>\s*(?:<div|<section id="cs2_))', html, re.S)
    if not m:
        return {}, {}
    block = m.group(0)
    video = {}
    advanced = {}
    vm = re.search(r'id="video".*?</section>', block, re.S)
    if vm:
        for th, td in re.findall(r"<th>([^<]+)</th><td>(.*?)</td>", vm.group(0), re.S):
            video[th.strip()] = strip_tags(td)
    am = re.search(r'id="advanced_video".*?</section>', block, re.S)
    if am:
        for th, td in re.findall(r"<th>([^<]+)</th><td>(.*?)</td>", am.group(0), re.S):
            advanced[th.strip()] = strip_tags(td)
    return video, advanced


def parse_gear(html: str) -> list[dict]:
    m = re.search(r'<section id="gear".*?(?=</section>\s*<section id=")', html, re.S)
    if not m:
        return []
    block = m.group(0)
    items = []
    for chunk in re.findall(r'<div class="cta-box promo js-promo-gear.*?</div>\s*</div>', block, re.S):
        name_m = re.search(r"<h4><a[^>]*>([^<]+)</a></h4>", chunk)
        tag_m = re.search(r'cta-box__tag--top-right">([^<]+)</div>', chunk)
        img_m = re.search(r'src="(https://prosettings\.net/wp-content/uploads/[^"]+187x187[^"]*)"', chunk)
        if name_m:
            items.append({
                "tag": tag_m.group(1) if tag_m else "",
                "name": strip_tags(name_m.group(1)),
                "img": img_m.group(1) if img_m else "",
            })
    return items


def parse_skins(html: str) -> list[dict]:
    m = re.search(r'id="cs2_skins".*?(?=</section>)', html, re.S)
    if not m:
        return []
    block = m.group(0)
    items = []
    for chunk in re.findall(r'<div class="cta-box cta-box-skin.*?</div>\s*</div>', block, re.S):
        name_m = re.search(r"<h4><a[^>]*>([^<]+)</a></h4>", chunk)
        tag_m = re.search(r'cta-box__tag--top-right">([^<]+)</div>', chunk)
        img_m = re.search(r'src="(https://prosettings\.net/wp-content/uploads/[^"]+187x187[^"]*)"', chunk)
        if name_m:
            full = strip_tags(name_m.group(1))
            wear = ""
            for w in WEAR_ZH:
                if f"({w})" in full:
                    wear = WEAR_ZH[w]
                    break
            items.append({
                "tag": tag_m.group(1) if tag_m else "",
                "name_en": full,
                "wear": wear,
                "img": img_m.group(1) if img_m else "",
            })
    return items


def parse_player(slug: str) -> dict:
    html = (MODEL / f"{slug}-page.html").read_text(encoding="utf-8")
    if 'id="cs2-settings"' not in html and 'id="cs2_mouse"' not in html:
        has_val = 'id="valorant-settings"' in html or 'id="valorant_mouse"' in html
        return {"slug": slug, "error": "no_cs2", "has_valorant": has_val}

    intro = section_table(html, "bio")  # might not exist
    name = ""
    birthday = ""
    country = ""
    team = ""
    for th, td in re.findall(
        r'<table class="data">.*?<th>([^<]+)</th><td>(.*?)</td>', html, re.S
    ):
        th, val = th.strip(), strip_tags(td)
        if th == "Name":
            name = val
        elif th == "Birthday":
            birthday = val
        elif th == "Country":
            country = re.sub(r"\s+", " ", val).strip()
        elif th == "Team":
            team = val

    bio_m = re.search(r'<div class="content">\s*<p class="wp-block-paragraph">(.*?)</p>', html, re.S)
    bio = strip_tags(bio_m.group(1)) if bio_m else ""

    avatar_m = re.search(
        r'class="avatar".*?src="(https://prosettings\.net/wp-content/uploads/[^"]+200x200[^"]*\.(?:png|webp))"',
        html,
        re.S,
    )
    if not avatar_m:
        avatar_m = re.search(
            r'src="(https://prosettings\.net/wp-content/uploads/' + re.escape(slug) + r'-200x200[^"]+)"',
            html,
            re.I,
        )
    avatar = avatar_m.group(1) if avatar_m else ""

    mouse_product_m = re.search(r'id="cs2_mouse".*?<h4><a[^>]*>([^<]+)</a></h4>', html, re.S)
    mouse_product = strip_tags(mouse_product_m.group(1)) if mouse_product_m else ""

    svg_m = re.search(
        r'class="cs2-crosshair-svg"[^>]*>(.*?)</svg>', html, re.S
    )
    crosshair_svg = svg_m.group(1).strip() if svg_m else ""

    mouse = section_table(html, "cs2_mouse")
    crosshair = section_table(html, "cs2_crosshair")
    viewmodel = section_table(html, "cs2_viewmodel")
    video, advanced = nested_video(html)
    gear = parse_gear(html)
    skins = parse_skins(html)

    display = slug
    h1_m = re.search(r'<h1>([^<]+)</h1>', html)
    if h1_m:
        display = strip_tags(h1_m.group(1))

    return {
        "slug": slug,
        "display": display,
        "name": name,
        "birthday": birthday,
        "country": country,
        "team": team,
        "bio_en": bio,
        "avatar": avatar,
        "mouse_product": mouse_product,
        "mouse": mouse,
        "crosshair": crosshair,
        "crosshair_svg": crosshair_svg,
        "viewmodel": viewmodel,
        "video": video,
        "advanced_video": advanced,
        "gear": gear,
        "skins": skins,
    }


def main():
    slugs = sys.argv[1:] or [
        "zywoo", "tenz", "s1mple", "ropz", "xantares", "aspas", "kyousuke"
    ]
    for slug in slugs:
        data = parse_player(slug)
        out = MODEL / f"{slug}-data.json"
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        if data.get("error"):
            print(f"{slug}: ERROR {data['error']} valorant={data.get('has_valorant')}")
        else:
            print(
                f"{slug}: OK team={data['team']} mouse={data['mouse'].get('DPI')} "
                f"gear={len(data['gear'])} skins={len(data['skins'])}"
            )


if __name__ == "__main__":
    main()
