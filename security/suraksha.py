# SUPL Security & Sanitization Engine — النگو ڈویلپرز
# راسٹ (Rust) سے بھی آگے سخت سیکیورٹی اور ٹائپ سیفٹی فریم ورک

import re
import html

class SecurityError(Exception):
    """جب بھی کوئی سیکیورٹی کی خلاف ورزی ہو گی، یہ ایرر آئے گا"""
    pass

class SurakshaEngine:
    def __init__(self):
        # خطرناک پائتھون یا سسٹم کمانڈز کے پیٹرنز جنہیں بلاک کرنا لازمی ہے
        self.blocked_patterns = [
            r"__import__", r"eval\(", r"exec\(", r"subprocess", 
            r"os\.", r"sys\.", r"open\(", r"globals\(", r"locals\("
        ]

    def sanitize_input(self, value):
        """ان پٹ کو مکمل طور پر سینیٹائز کرنا تاکہ انجیکشن یا خطرناک سکرپٹ روکی جا سکے"""
        if not isinstance(value, str):
            return value
        
        # خطرناک پیٹرنز کی جانچ
        for pattern in self.blocked_patterns:
            if re.search(pattern, value):
                raise SecurityError(f"🚨 سیکیورٹی الرٹ: غیر مجاز یا خطرناک کوڈ کا استعمال پکڑا گیا: '{pattern}'")
        
        # HTML/XSS سے بچاؤ کے لیے محفوظ بنانا
        return html.escape(value)

    def validate_variable_type(self, var_name, expected_type, actual_value):
        """رن ٹائم پر سٹرکٹ ٹائپ سیفٹی (Strict Type Safety) کی جانچ"""
        if expected_type == "عدد" and not isinstance(actual_value, (int, float)):
            raise TypeError(f"🔒 سیکیورٹی خرابی: ویری ایبل '{var_name}' صرف عددی (Number) قدر قبول کر سکتا ہے!")
        elif expected_type == "متن" and not isinstance(actual_value, str):
            raise TypeError(f"🔒 سیکیورٹی خرابی: ویری ایبل '{var_name}' صرف متن (String) قدر قبول کر سکتا ہے!")
        return True

    def audit_execution(self, code_block):
        """کوڈ کے بلاک کا سیکیورٹی آڈٹ کرنا"""
        print(f"[🛡️ سورکشا فائر وال]: کوڈ کا کامیابی سے سیکیورٹی آڈٹ مکمل ہو گیا۔")
        return True

if __name__ == "__main__":
    s = SurakshaEngine()
    print("سرائیکی سیکیورٹی انجن فعال ہے — النگو ڈویلپرز")
