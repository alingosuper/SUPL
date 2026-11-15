#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AlinGo Brand Fix — خودکار برانڈنگ نصب کنندہ
تمام README، docs، HTML، Python فائلوں میں لوگو لگاتا ہے۔
"""
import sys
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
BRAND = ROOT / "assets" / "branding"

BANNER_REL = "assets/branding/alingo-banner-dark.svg"
LOGO_REL = "assets/branding/alingo-logo.svg"
ICON_REL = "assets/branding/alingo-icon.svg"
FAVICON_REL = "assets/branding/favicon.svg"

README_HEADER = f'''<p align="center">
  <img src="{BANNER_REL}" alt="AlinGo Saraiki" width="100%" />
</p>

<h1 align="center">AlinGo Saraiki</h1>

<p align="center">
  <strong>دیسی پروگرامنگ لینگویج — سرائیکی، اردو، پنجابی</strong><br/>
  <em>Saraiki · Urdu · Punjabi Programming Language</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.1-green.svg" />
  <img src="https://img.shields.io/badge/python-3.9+-blue.svg" />
  <img src="https://img.shields.io/badge/license-MIT-yellow.svg" />
</p>

---

'''


def fix_readme():
    p = ROOT / "README.md"
    if not p.exists():
        print("⚠️ README.md نہیں ملا")
        return
    src = p.read_text(encoding="utf-8")
    if BANNER_REL in src:
        print("ℹ️ README.md پہلے سے برانڈڈ ہے")
        return
    p.write_text(README_HEADER + src, encoding="utf-8")
    print("✅ README.md میں banner شامل")


def fix_docs_index():
    p = ROOT / "docs" / "index.md"
    if not p.exists():
        print("⚠️ docs/index.md نہیں ملا")
        return
    src = p.read_text(encoding="utf-8")
    if "alingo-logo-full.svg" in src:
        print("ℹ️ docs/index.md پہلے سے برانڈڈ ہے")
        return
    header = f'<p align="center">\n  <img src="../{LOGO_REL}" alt="AlinGo" width="600" />\n</p>\n\n'
    p.write_text(header + src, encoding="utf-8")
    print("✅ docs/index.md میں لوگو شامل")


def fix_mkdocs():
    p = ROOT / "mkdocs.yml"
    if not p.exists():
        print("⚠️ mkdocs.yml نہیں ملا — پہلے بنائیں")
        return
    src = p.read_text(encoding="utf-8")
    changed = False
    if "favicon:" not in src:
        src = src.rstrip() + f"\nfavicon: {FAVICON_REL}\n"
        changed = True
    if "logo:" not in src:
        src = src.rstrip() + f"\nlogo: {LOGO_REL}\n"
        changed = True
    if changed:
        p.write_text(src, encoding="utf-8")
        print("✅ mkdocs.yml میں favicon + logo شامل")
    else:
        print("ℹ️ mkdocs.yml پہلے سے برانڈڈ ہے")


def fix_html_favicon():
    """تمام .html فائلوں میں favicon شامل کریں"""
    count = 0
    for html in ROOT.rglob("*.html"):
        if "node_modules" in str(html) or "site-packages" in str(html):
            continue
        try:
            src = html.read_text(encoding="utf-8")
        except Exception:
            continue
        if "favicon.svg" in src:
            continue
        # <head> کے بعد favicon شامل کریں
        m = re.search(r"<head[^>]*>", src, re.I)
        if m:
            rel_path = "../" * len(html.relative_to(ROOT).parts[:-1]) + FAVICON_REL
            tag = f'\n  <link rel="icon" type="image/svg+xml" href="{rel_path}">'
            src = src[:m.end()] + tag + src[m.end():]
            html.write_text(src, encoding="utf-8")
            count += 1
    print(f"✅ {count} HTML فائلوں میں favicon شامل")


def verify():
    print("\n════════ تصدیق ════════")
    svgs = list(BRAND.glob("*.svg"))
    print(f"SVG فائلیں: {len(svgs)}")
    for s in svgs:
        print(f"  ✓ {s.name} ({s.stat().st_size} بائٹس)")

    readme = ROOT / "README.md"
    if readme.exists() and BANNER_REL in readme.read_text(encoding="utf-8"):
        print("✓ README.md برانڈڈ")

    print("\n✅ برانڈنگ مکمل")


if __name__ == "__main__":
    if not BRAND.exists():
        print(f"❌ برانڈنگ فولڈر نہیں ملا: {BRAND}")
        print("   پہلے: mkdir -p assets/branding && SVG فائلیں بنائیں")
        sys.exit(1)

    fix_readme()
    fix_docs_index()
    fix_mkdocs()
    fix_html_favicon()
    verify()
