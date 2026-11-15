#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SUPL نیا لفظ شامل کرنے کا انجن (CSV میں محفوظ کرتا ہے)
"""
import sys
import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"
CSV_PATH = DATA_DIR / "dictionary.csv"

def add_new_word(word, meaning):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    # اگر فائل موجود نہیں تو ہیڈر بنائیں
    file_exists = CSV_PATH.exists()
    
    try:
        with open(CSV_PATH, "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["لفظ", "معنی"])
            writer.writerow([word, meaning])
            
        print("=" * 50)
        print(f" کامیابی! نیا لفظ لغت میں شامل کر دیا گیا ہے:")
        print(f" 📖 لفظ: {word}")
        print(f" 📝 معنی: {meaning}")
        print("=" * 50)
    except Exception as e:
        print(f"❌ خرابی: لفظ محفوظ کرنے میں مسئلہ پیش آیا: {e}")

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        word = sys.argv[1]
        meaning = " ".join(sys.argv[2:])
        add_new_word(word, meaning)
    else:
        print("استعمال کا طریقہ: لفظ_شامل_کرو <لفظ> <معنی>")
        print("مثال: لفظ_شامل_کرو 'سافٹ ویئر' 'کمپیوٹر کو چلانے والے پروگرام'")
