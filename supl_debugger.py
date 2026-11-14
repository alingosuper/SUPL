import sys
import os

# عام غلط یا ملتے جلتے الفاظ کی درستگی کی لغت (Auto-Correction Dictionary)
KEYWORD_CORRECTIONS = {
    # اردو اصلاحات
    "لکھ": "لکھو",
    "شروع_کرو_پروگرام": "شروع",
    "ورنہ_نہیں": "ورنہ",
    "جبکہ": "جب_تک",
    
    # سرائیکی اصلاحات
    "چھاپو": "چھاپ",
    "تاں_جے": "جے",
    
    # پنجابی اصلاحات
    "دسو": "دسّو",
    "مکاؤ": "مک_گیا"
}

def auto_correct_and_check(filename):
    print(f"\n🔍 [خودکار ڈیبگنگ اور اصلاح] فائل '{filename}' کا معائنہ جاری ہے...")
    
    if not os.path.exists(filename):
        print(f"❌ خرابی: فائل '{filename}' نہیں ملی۔")
        return

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    corrected_lines = []
    changes_made = False

    for line_no, line in enumerate(lines, 1):
        original_line = line
        for wrong, correct in KEYWORD_CORRECTIONS.items():
            if wrong in line:
                line = line.replace(wrong, correct)
                print(f"💡 [لائن {line_no}] اصلاح کی گئی: '{wrong}' ➔ '{correct}'")
                changes_made = True
        corrected_lines.append(line)

    # اگر تبدیلیاں کی گئی ہیں تو فائل کو خود بخود اپ ڈیٹ کر دیں
    if changes_made:
        backup_name = filename + ".bak"
        with open(backup_name, "w", encoding="utf-8") as f:
            f.writelines(lines)
        
        with open(filename, "w", encoding="utf-8") as f:
            f.writelines(corrected_lines)
        
        print(f"✨ کامیابی: کوڈ کی خودکار اصلاح کر دی گئی ہے! (پرانی فائل کا بیک اپ '{backup_name}' کے نام سے محفوظ ہے)")
    else:
        print("✅ ماشاء اللہ! کوڈ میں کوئی غلط کی ورڈ نہیں پایا گیا۔")

    # اب سکرپٹ کو رن کر کے چیک کریں
    print("\n🚀 سکرپٹ کا ایگزیکیوشن نتیجہ:")
    print("-" * 40)
    os.system(f"python3 cli.py {filename}")
    print("-" * 40)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        auto_correct_and_check(sys.argv[1])
    else:
        print("⚠️ براہ کرم فائل کا نام دیں۔ مثال: چیک_فائل test_urdu.supl")
