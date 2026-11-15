# SUPL Tokens & Keywords — النگو ڈویلپرز

TOKEN_EOF = "EOF"
TOKEN_IDENTIFIER = "IDENTIFIER"
TOKEN_NUMBER = "NUMBER"
TOKEN_STRING = "STRING"

# آسان سرائیکی کی ورڈز کی لغت
KEYWORDS = {
    "عدد": "VAR",
    "جے": "IF",
    "اگر": "IF",
    "نہیں_تاں": "ELSE",
    "ورنہ": "ELSE",
    "جئیں_ویلے_تئیں": "WHILE",
    "ہر": "FOR",
    "کم": "FUNCTION",
    "فنکشن": "FUNCTION",
    "واپس": "RETURN",
    "چھاپ": "PRINT",
    "چھاپیگا": "PRINT",
    "سچ": "TRUE",
    "کوڑ": "FALSE",
    "جھوٹ": "FALSE",
    "پندھ_شروع": "PROGRAM_START",
    "پندھ_مک_گیا": "PROGRAM_END",
}

# ── Merge multilingual keywords (Urdu, Punjabi, Saraiki) ──
try:
    from multilingual_keywords import MULTILINGUAL_KEYWORDS as _ML
    # ہمارے canonical token types برقرار رکھیں
    _OVERRIDES = {"PROG_START": "PROGRAM_START", "PROG_END": "PROGRAM_END"}
    for _k, _v in _ML.items():
        KEYWORDS.setdefault(_k, _OVERRIDES.get(_v, _v))
except Exception as _e:
    pass  # multilingual_keywords نہ ملے تو خاموشی سے چھوڑ دیں

