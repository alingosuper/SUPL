# Multilingual Syntax Mapping for SUPL (Urdu, Punjabi, Saraiki)

MULTILINGUAL_KEYWORDS = {
    # ═══ VAR / CONST — تینوں زبانیں ═══
    "شے": "VAR",
    "متغیر": "VAR",
    "پکی": "CONST",
    "مستقل": "CONST",
    # ═══ for loop keywords (تینوں زبانیں) ═══
    "میں": "IN",
    "وچ": "IN",
    "تک": "TO",
    "تئیں": "TO",
    "توڑ": "TO",
    # --- Saraiki (سرائیکی) ---
    "پندھ_شروع": "PROG_START",
    "پندھ_مک_گیا": "PROG_END",
    "عدد": "VAR",
    "متن": "STRING_TYPE",
    "چھاپ": "PRINT",
    "جے": "IF",
    "تاں": "THEN",
    "نہیں_تاں": "ELSE",
    "سرخی": "UI_HEADER",
    "بٹن": "UI_BUTTON",

    # --- Urdu (اردو) ---
    "شروع": "PROG_START",
    "ختم": "PROG_END",
    "عدد": "VAR",
    "متن": "STRING_TYPE",
    "لکھو": "PRINT",
    "اگر": "IF",
    "تو": "THEN",
    "ورنہ": "ELSE",
    "سرخی": "UI_HEADER",
    "بٹن": "UI_BUTTON",

    # --- Punjabi (پنجابی) ---
    "شروع_کرو": "PROG_START",
    "مک_گیا": "PROG_END",
    "گنتی": "NUMBER_TYPE",
    "بول": "STRING_TYPE",
    "دسّو": "PRINT",
    "جے": "IF",
    "تاں": "THEN",
    "نہیں_تاں": "ELSE",
    "سرخی": "UI_HEADER",
    "بٹن": "UI_BUTTON",
}

print("===== تمام تینوں زبانوں کے کی ورڈز کامیابی سے لوڈ ہو گئے ہیں! =====")

# --- Multilingual Function & Return Keywords Extension ---
MULTILINGUAL_KEYWORDS.update({
    # Saraiki (سرائیکی)
    "کم": "FUNC_DEF",
    "واپس": "RETURN",
    
    # Urdu (اردو)
    "کام": "FUNC_DEF",
    "واپس": "RETURN",
    
    # Punjabi (پنجابی)
    "فعل": "FUNC_DEF",
    "موڑ": "RETURN",
})

# --- Multilingual Loop Keywords Extension ---
MULTILINGUAL_KEYWORDS.update({
    # --- Saraiki (سرائیکی) ---
    "جب_تک": "WHILE",
    "دورانیہ": "FOR",
    "ختم_لوپ": "END_LOOP",

    # --- Urdu (اردو) ---
    "جب_تک": "WHILE",
    "دورانیہ": "FOR",
    "ختم_لوپ": "END_LOOP",

    # --- Punjabi (پنجابی) ---
    "جدوں_تک": "WHILE",
    "مدت": "FOR",
    "مک_لوپ": "END_LOOP",

    # ═══ مکمل keywords ═══
    "تے": "AND", "اور": "AND",
    "یا": "OR",
    "کائنی": "NOT", "نہیں": "NOT", "نئیں": "NOT",
    "خالی": "NULL",
    "واپس_ڈیو": "RETURN", "واپس_کرو": "RETURN", "واپس_دیو": "RETURN",
    "نہ_تاں": "ELSE",
    "جبکہ": "WHILE", "جدوں_تئیں": "WHILE",
    "ہر_ہک_کیتے": "FOR", "کے_لیے": "FOR", "ہر_اک_لئی": "FOR",
    "ٹولی": "CLASS",
    "کم": "FUNCTION", "کام": "FUNCTION", "فعل": "FUNCTION",
    "سچ": "TRUE", "جھوٹ": "FALSE", "کوڑ": "FALSE",
    "نیا": "NEW", "نواں": "NEW",
    "یہ": "SELF", "ایہہ": "SELF",
})
