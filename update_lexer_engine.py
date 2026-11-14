import os

lexer_path = "lexer/lexer.py"
if os.path.exists(lexer_path):
    with open(lexer_path, "r", encoding="utf-8") as f:
        content = f.read()

    # اگر multilingual_keywords امپورٹ نہیں ہے تو اسے شامل کریں
    if "multilingual_keywords" not in content:
        import_line = "from multilingual_keywords import MULTILINGUAL_KEYWORDS\n"
        content = import_line + content
        with open(lexer_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("===== lexer.py میں ملٹی لنگویل لغت کامیابی سے جوڑ دی گئی ہے! =====")
    else:
        print("لکسر میں ملٹی لنگویل لغت پہلے سے موجود ہے۔")
else:
    print("لکسر کی فائل نہیں ملی۔")
