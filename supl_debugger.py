import sys
import subprocess

def check_supl_file(filename):
    print(f"\n🔍 [ڈیبگ جاری ہے] فائل '{filename}' کا معائنہ کیا جا رہا ہے...")
    try:
        # پائتھون کے ذریعے فائل رن کریں اور ایرر کیپچر کریں
        result = subprocess.run(["python3", "cli.py", filename], capture_output=True, text=True, check=True)
        print("✅ ماشاء اللہ! سکرپٹ میں کوئی غلطی نہیں ملی۔ آؤٹ پٹ یہ ہے:\n")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("\n❌ خبردار! آپ کے SUPL کوڈ میں خرابی (غلطی) پائی گئی ہے:\n")
        print("-" * 40)
        print(e.stderr)
        print("-" * 40)
        print("💡 مشورہ: اپنے کی ورڈز (جیسے شروع، ختم، عدد، اگر) کی درستی چیک کریں۔\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        check_supl_file(sys.argv[1])
    else:
        print("⚠️ براہ کرم فائل کا نام دیں۔ مثال: python3 supl_debugger.py test_urdu.supl")
