#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SUPL دیسی لغت (Dictionary) ماڈیول
"""
import json
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CSV_PATH = DATA_DIR / "dictionary.csv"
JSON_PATH = DATA_DIR / "dictionary.json"

def load_dictionary():
    """JSON اور CSV دونوں سے لغت کے الفاظ لوڈ کرتا ہے"""
    words = {}
    
    if JSON_PATH.exists():
        try:
            with open(JSON_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    words.update(data)
        except Exception:
            pass

    if CSV_PATH.exists():
        try:
            with open(CSV_PATH, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader, None)  # ہیڈر چھوڑیں
                for row in reader:
                    if len(row) >= 2 and row[0].strip():
                        words[row[0].strip()] = row[1].strip()
        except Exception:
            pass

    return words

def search_word(query):
    query = query.strip()
    words = load_dictionary()
    print("=" * 55)
    print(f" تلاش کا نتیجہ برائے: '{query}' (کل الفاظ: {len(words)})")
    print("=" * 55)
    
    found = False
    for k, v in words.items():
        if query in k or query in v:
            print(f"📖 {k}:\n   {v}\n")
            found = True
            
    if not found:
        print(f"❌ معذرت! لغت میں '{query}' سے متعلق کوئی لفظ نہیں ملا۔")
    print("=" * 55)

def add_word(word, meaning):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    file_exists = CSV_PATH.exists()
    try:
        with open(CSV_PATH, "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["لفظ", "معنی"])
            writer.writerow([word, meaning])
        print(f"✅ کامیابی! نیا لفظ '{word}' لغت میں شامل کر دیا گیا ہے۔")
    except Exception as e:
        print(f"❌ خرابی: {e}")

def delete_word(target):
    if not CSV_PATH.exists():
        print("❌ لغت کی فائل موجود نہیں ہے۔")
        return
    rows = []
    found = False
    try:
        with open(CSV_PATH, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0].strip() == target:
                    found = True
                    continue
                rows.append(row)
        if found:
            with open(CSV_PATH, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(rows)
            print(f"🗑️ لفظ '{target}' کو لغت سے ہٹا دیا گیا ہے۔")
        else:
            print(f"❌ لفظ '{target}' لغت میں نہیں ملا۔")
    except Exception as e:
        print(f"❌ خرابی: {e}")

def list_all_words():
    words = load_dictionary()
    print("=" * 60)
    print(f" 📚 SUPL دیسی لغت — کل الفاظ: {len(words)}")
    print("=" * 60)
    for idx, (w, m) in enumerate(sorted(words.items()), 1):
        print(f" {idx}. **{w}** ── {m}")
    print("=" * 60)

def search_cli():
    import sys
    if len(sys.argv) > 1:
        search_word(" ".join(sys.argv[1:]))
    else:
        list_all_words()
