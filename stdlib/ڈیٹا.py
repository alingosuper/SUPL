#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ڈیٹا — JSON، CSV (تینوں زبانیں)"""

import json
import csv
from pathlib import Path


# ═══════════════════════════════════════════════════════
# JSON
# ═══════════════════════════════════════════════════════

def json_پڑھو(راستہ: str) -> dict:
    """JSON فائل پڑھیں"""
    with open(راستہ, "r", encoding="utf-8") as f:
        return json.load(f)


def json_لکھو(راستہ: str, ڈیٹا):
    """JSON فائل میں لکھیں"""
    with open(راستہ, "w", encoding="utf-8") as f:
        json.dump(ڈیٹا, f, ensure_ascii=False, indent=2)


def json_سے(متن: str):
    """JSON متن سے ڈیٹا"""
    return json.loads(متن)


def json_میں(ڈیٹا) -> str:
    """ڈیٹا کو JSON متن میں"""
    return json.dumps(ڈیٹا, ensure_ascii=False, indent=2)


# ═══════════════════════════════════════════════════════
# CSV
# ═══════════════════════════════════════════════════════

def csv_پڑھو(راستہ: str) -> list:
    """CSV فائل پڑھیں — dicts کی list واپس"""
    with open(راستہ, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def csv_لکھو(راستہ: str, قطاریں: list, عنوانات: list = None):
    """CSV فائل میں لکھیں"""
    if not قطاریں:
        return
    
    if عنوانات is None:
        عنوانات = list(قطاریں[0].keys()) if isinstance(قطاریں[0], dict) else None
    
    with open(راستہ, "w", encoding="utf-8", newline="") as f:
        if isinstance(قطاریں[0], dict):
            writer = csv.DictWriter(f, fieldnames=عنوانات)
            writer.writeheader()
            writer.writerows(قطاریں)
        else:
            writer = csv.writer(f)
            if عنوانات:
                writer.writerow(عنوانات)
            writer.writerows(قطاریں)
