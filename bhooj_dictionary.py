#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SUPL دیسی لغت (Dictionary) انجن — JSON اور CSV سپورٹ کے ساتھ
"""
import sys
import json
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

# بنیادی بلٹ ان لغت
DEFAULT_DICTIONARY = {
    "پروگرامنگ": "کمپیوٹر کو ہدایات دینے کا عمل تاکہ وہ خاص کام انجام دے۔",
    "سڑک_لک": "SarakLuk ایک کثیر اللسانی پروگرامنگ زبان ہے جو اردو، پنجابی اور سرائیکی کو سپورٹ کرتی ہے۔",
    "انٹرپریٹر": "ایک ایسا سافٹ ویئر جو کوڈ کو لائن بہ لائن پڑھ کر فوراً چلاتا ہے۔",
    "پندھ": "سفر یا راستے کا آغاز/فاصلہ (سرائیکی)۔",
    "ڳالھ": "بات یا گفتگو (سرائیکی)۔"
}

def load_all_dictionaries():
    """بلٹ ان، JSON اور CSV فائلوں سے تمام الفاظ لوڈ کرتا ہے"""
    combined = dict(DEFAULT_DICTIONARY)

    # 1. JSON فائل لوڈ کرنا
    json_path = DATA_DIR / "dictionary.json"
    if json_path.exists():
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    combined.update(data)
        except Exception as e:
            print(f"[انتباہ] JSON فائل پڑھنے میں خرابی: {e}")

    # 2. CSV فائل لوڈ کرنا
    csv_path = DATA_DIR / "dictionary.csv"
    if csv_path.exists():
        try:
            with open(csv_path, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader, None)  # ہیڈر لائن (لفظ,معنی) چھوڑنے کے لیے
                for row in reader:
                    if len(row) >= 2 and row[0].strip():
                        combined[row[0].strip()] = row[1].strip()
        except Exception as e:
            print(f"[انتباہ] CSV فائل پڑھنے میں خرابی: {e}")

    return combined

def search_word(word):
    word = word.strip()
    dictionary = load_all_dictionaries()
    
    print("=" * 55)
    print(f" تلاش کا نتیجہ برائے: '{word}' (کل الفاظ: {len(dictionary)})")
    print("=" * 55)
    
    found = False
    for k, v in dictionary.items():
        if word in k or word in v:
            print(f"📖 {k}:\n   {v}\n")
            found = True
            
    if not found:
        print(f"❌ معذرت! لغت میں '{word}' سے متعلق کوئی لفظ نہیں ملا۔")
    print("=" * 55)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_word(" ".join(sys.argv[1:]))
    else:
        print("استعمال کا طریقہ: تلاش_لفظ <کوئی_بھی_لفظ>")
