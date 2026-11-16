# SUPL Tokens & Keywords — النگو ڈویلپرز

TOKEN_EOF = "EOF"
TOKEN_IDENTIFIER = "IDENTIFIER"
TOKEN_NUMBER = "NUMBER"
TOKEN_STRING = "STRING"

# آسان سرائیکی کی ورڈز کی لغت
KEYWORDS = {
    # ═══ IMPORT ═══
    "شامل_کرو": "IMPORT",

    # ═══ TRY/CATCH ═══
    "کوشش": "TRY",
    "پکڑو": "CATCH",
    "غلطی": "ERROR_VAR",

    # ═══ OOP ═══
    "تعمیر": "CONSTRUCTOR",
    "نیا": "NEW",
    "نواں": "NEW",
    "یہ": "SELF",
    "ایہہ": "SELF",
    "کلاس": "CLASS",
    "ٹولی": "CLASS",

    # ═══ THEN ═══
    "تاں": "THEN",
    "تو": "THEN",
    "{": "LBRACE",
    "}": "RBRACE",

    # ═══ VAR / CONST (تینوں زبانیں) ═══
    "عدد": "VAR",
    "شے": "VAR",
    "متغیر": "VAR",
    "پکی": "CONST",
    "مستقل": "CONST",

    # ═══ IF / ELSE ═══
    "جے": "IF",
    "اگر": "IF",
    "نہیں_تاں": "ELSE",
    "نہ_تاں": "ELSE",
    "نہیں_تے": "ELSE",
    "ورنہ": "ELSE",

    # ═══ WHILE ═══
    "جئیں_ویلے_تئیں": "WHILE",
    "جتھاں": "WHILE",
    "جدوں_تک": "WHILE",
    "جدوں_تئیں": "WHILE",
    "جبکہ": "WHILE",

    # ═══ FOR ═══
    "برائے": "FOR",
    "ہر": "FOR",
    "ہر_ہک_کیتے": "FOR",
    "کے_لیے": "FOR",
    "ہر_اک_لئی": "FOR",

    # ═══ FUNCTION ═══
    "کم": "FUNCTION",
    "کام": "FUNCTION",
    "فعل": "FUNCTION",
    "فنکشن": "FUNCTION",

    # ═══ RETURN ═══
    "واپس": "RETURN",
    "واپس_ڈیو": "RETURN",
    "واپس_کرو": "RETURN",
    "واپس_دیو": "RETURN",
    "موڑ": "RETURN",

    # ═══ PRINT ═══
    "چھاپ": "PRINT",
    "چھاپیگا": "PRINT",
    "لکھو": "PRINT",
    "دسّو": "PRINT",

    # ═══ TRUE / FALSE / NULL ═══
    "سچ": "TRUE",
    "کوڑ": "FALSE",
    "جھوٹ": "FALSE",
    "خالی": "NULL",

    # ═══ LOGICAL ═══
    "تے": "AND",
    "اور": "AND",
    "یا": "OR",
    "کائنی": "NOT",
    "نہیں": "NOT",
    "نئیں": "NOT",

    # ═══ PROGRAM START/END ═══
    "پندھ_شروع": "PROGRAM_START",
    "شروع": "PROGRAM_START",
    "شروع_کرو": "PROGRAM_START",
    "پندھ_مک_گیا": "PROGRAM_END",
    "ختم": "PROGRAM_END",
    "مک_گیا": "PROGRAM_END",

    # ═══ LOOP END ═══
    "ختم_لوپ": "END_LOOP",
    "مک_لوپ": "END_LOOP",

    # ═══ FOR LOOP keywords ═══
    "میں": "IN",
    "وچ": "IN",
    "تک": "TO",
    "تئیں": "TO",
    "توڑ": "TO",
}

# ── Merge multilingual keywords ──
try:
    from multilingual_keywords import MULTILINGUAL_KEYWORDS as _ML
    _OVERRIDES = {"PROG_START": "PROGRAM_START", "PROG_END": "PROGRAM_END"}
    for _k, _v in _ML.items():
        KEYWORDS.setdefault(_k, _OVERRIDES.get(_v, _v))
except Exception:
    pass
