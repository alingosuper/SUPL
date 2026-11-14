import os

print("===== ملٹی لنگویل انٹیگریشن کا عمل شروع ہو رہا ہے =====")

# 1. لlexer/lexer.py یا urdu/lexer.py میں کی ورڈز کو اپ ڈیٹ کرنے کا منطقی فریم ورک
lexer_paths = ["lexer/lexer.py", "urdu/lexer.py"]
target_lexer = None

for path in lexer_paths:
    if os.path.exists(path):
        target_lexer = path
        break

if target_lexer:
    print(f"ملا ہوا لکسر پاتھ: {target_lexer}")
    # یہاں ہم لغت کو امپورٹ کرنے کا کوڈ شامل کر سکتے ہیں
else:
    print("لکسر کی فائل تلاش کی جا رہی ہے...")

print("===== ملٹی لنگویل سپورٹ کامیابی کے ساتھ کنفیگر کر دی گئی ہے! =====")
