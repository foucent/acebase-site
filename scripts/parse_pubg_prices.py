#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse PUBG Mobile UC prices scraped from bittopup / topuplist / seagm."""
import json
import re
import os

TMP = r"C:\Users\fouce\AppData\Local\Temp"


def parse_bittopup(text):
    # "TIER\n\nPUBG Mobile UC\n\nDiscount: xx% OFF\nHK$ price\nHK$ original"
    pattern = re.compile(
        r"([\d,]+ ?\+ ?[\d,]+ UC|60 UC|120 UC)\s*\n+\s*PUBG Mobile UC\s*\n+\s*Discount:[^\n]*\n+HK\$ ([\d,]+\.\d\d)\s*\n+HK\$ ([\d,]+\.\d\d)"
    )
    return [(t, float(p.replace(",", "")), float(o.replace(",", ""))) for t, p, o in pattern.findall(text)]


def parse_topuplist(text):
    # "-14%\n60 UC\nHK$6.67\nHK$7.77" (no space after HK$)
    pattern = re.compile(
        r"([\d,]+ ?\+ ?[\d,]+ UC|60 UC|120 UC)\nHK\$ ?([\d,]+\.\d\d)\nHK\$ ?([\d,]+\.\d\d)"
    )
    return [(t, float(p.replace(",", "")), float(o.replace(",", ""))) for t, p, o in pattern.findall(text)]


def parse_seagm(text):
    # seagm embedded prodectBuyList: "item_name":"60 UC","price":"6.75"
    pattern = re.compile(r'"item_name":"([^"]+)","price":"([0-9.]+)"')
    return [(t, float(p)) for t, p in pattern.findall(text)]


def main():
    results = {}
    # seagm prices are HKD (from JSON-LD priceCurrency HKD); bittopup/topuplist also HKD
    seagm = parse_seagm(open(os.path.join(TMP, "seagm_pubg.html"), encoding="utf-8", errors="replace").read())
    bt = parse_bittopup(open(os.path.join(TMP, "pubg_bittopup.txt"), encoding="utf-8", errors="replace").read())
    tl = parse_topuplist(open(os.path.join(TMP, "pubg_topuplist.txt"), encoding="utf-8", errors="replace").read())

    print("=== seagm ===")
    for t, p in seagm:
        print(f"  {t}: {p}")
    print("=== bittopup ===")
    for t, p, o in bt:
        print(f"  {t}: {p} (orig {o})")
    print("=== topuplist ===")
    for t, p, o in tl:
        print(f"  {t}: {p} (orig {o})")


if __name__ == "__main__":
    main()
