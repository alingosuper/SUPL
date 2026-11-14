# SarakLuk Security Integration Test — النگو ڈویلپرز
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
from security.suraksha import SurakshaEngine, SecurityError

def test_system():
    suraksha = SurakshaEngine()
    
    print("--- 1. محفوظ ان پٹ ٹیسٹ ---")
    safe_text = suraksha.sanitize_input("سلام سرائیکی دنیا!")
    print(f"محفوظ متن: {safe_text}")

    print("\n--- 2. ٹائپ سیفٹی ٹیسٹ ---")
    try:
        suraksha.validate_variable_type("عمر", "عدد", 25)
        print("تصدیق کامیاب: ویری ایبل بالکل محفوظ ہے۔")
    except Exception as e:
        print(e)

    print("\n--- 3. خطرناک کوڈ بلاکنگ ٹیسٹ ---")
    try:
        suraksha.sanitize_input("eval('dangerous_code')")
    except SecurityError as se:
        print(f"کامیابی سے روک لیا گیا: {se}")

if __name__ == "__main__":
    test_system()
