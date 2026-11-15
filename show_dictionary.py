#!/usr/init/env python3
# -*- coding: utf-8 -*-
"""
SUPL لغت کے تمام الفاظ کی فہرست دکھانے کا انجن
"""
import sys
import json
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

def get_all_words():
    all_words = {}
    
    # 1. JSON سے الفاظ لوڈ کرنا
    json_path = DATA_DIR / "dictionary.json"
    if json_path.exists():
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    all_words.update(data)
        except Exception:
            pass

    # 2. CSV سے الفاظ لوڈ کرنا
    csv_path = DATA_DIR / "dictionary.csv"
    if csv_path.exists():
        try:
            with open(csv_path, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader, None) # ہیڈر لائن چھوڑنا
                for row in reader:
                    if len(row) >= 2 and row[0].strip():
                        all_words[row[0].strip()] = row[1].strip()
        except Exception:
            pass

    return all_words

def display_dictionary():
    words = get_all_words()
    
    print("=" * 65)
    print(f" 📚 SUPL دیسی لغت — کل درج الفاظ: {len(words)}")
    print("=" * 65)
    
    if not words:
        print("❌ لغت میں فی الحال کوئی لفظ موجود نہیں ہے۔")
    else:
        for idx, (word, meaning) in enumerate(sorted(words.items()), 1):
            print(f" {idx}. **{word}**")
            print(f"    └─ {meaning}\n")
            
    print("=" * 65)

if __name__ == "__main__":
    display_dictionary()
