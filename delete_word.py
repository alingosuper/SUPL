#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SUPL لغت سے لفظ حذف کرنے (Delete) کا انجن
"""
import sys
import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"
CSV_PATH = DATA_DIR / "dictionary.csv"

def delete_word(target_word):
    target_word = target_word.strip()
    
    if not CSV_PATH.exists():
        print("❌ خرابی: لغت کی CSV فائل موجود نہیں ہے۔")
        return
        
    rows = []
    found = False
    
    # فائل پڑھ کر ہدف والے لفظ کے علاوہ باقی تمام الفاظ محفوظ کرنا
    try:
        with open(CSV_PATH, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0].strip() == target_word:
                    found = True
                    continue
                rows.append(row)
                
        if found:
            with open(CSV_PATH, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(rows)
            print("=" * 50)
            print(f" کامیابی! لغت سے لفظ '{target_word}' کو حذف کر دیا گیا ہے۔")
            print("=" * 50)
        else:
            print(f"❌ معذرت! لغت میں '{target_word}' نام کا کوئی لفظ نہیں ملا۔")
            
    except Exception as e:
        print(f"❌ خرابی: لفظ حذف کرنے میں مسئلہ پیش آیا: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = " ".join(sys.argv[1:])
        delete_word(target)
    else:
        print("استعمال کا طریقہ: لفظ_مٹاؤ <لفظ_کا_نام>")
        print("مثال: لفظ_مٹاؤ پرانی_اصطلاح")
