#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""فائلاں — فائل پڑھنا/لکھنا (تینوں زبانیں)"""

import os
from pathlib import Path


def کھولو(راستہ: str, موڈ: str = "پڑھو"):
    """فائل کھولیں
    
    موڈ: 'پڑھو' / 'لکھو' / 'شامل' / 'بائنری'
    """
    موڈ_میپ = {
        "پڑھو": "r",
        "لکھو": "w",
        "شامل": "a",
        "بائنری": "rb",
        "پڑھو_بائنری": "rb",
        "لکھو_بائنری": "wb",
    }
    actual_mode = موڈ_میپ.get(موڈ, "r")
    
    if actual_mode.startswith("r"):
        return open(راستہ, actual_mode, encoding="utf-8")
    return open(راستہ, actual_mode, encoding="utf-8" if "b" not in actual_mode else None)


def پڑھو(راستہ: str) -> str:
    """پوری فائل پڑھیں"""
    with open(راستہ, "r", encoding="utf-8") as f:
        return f.read()


def لکھو(راستہ: str, مواد: str):
    """فائل میں لکھیں (پچھلا مواد مٹا کر)"""
    with open(راستہ, "w", encoding="utf-8") as f:
        f.write(مواد)


def شامل_کرو(راستہ: str, مواد: str):
    """فائل کے آخر میں شامل کریں"""
    with open(راستہ, "a", encoding="utf-8") as f:
        f.write(مواد)


def موجود_ہے(راستہ: str) -> bool:
    """کیا فائل موجود ہے؟"""
    return os.path.exists(راستہ)


def حذف_کرو(راستہ: str):
    """فائل حذف کریں"""
    os.remove(راستہ)


def فہرست(فولڈر: str = ".") -> list:
    """فولڈر کی فائلیں"""
    return os.listdir(فولڈر)


def بناؤ(راستہ: str):
    """فولڈر بنائیں"""
    os.makedirs(راستہ, exist_ok=True)


def سائز(راستہ: str) -> int:
    """فائل کا سائز (bytes)"""
    return os.path.getsize(راستہ)


def لائنیں(راستہ: str) -> list:
    """فائل کی لائنیں"""
    with open(راستہ, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]
