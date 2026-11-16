# SUPL Tokens & Keywords — النگو ڈویلپرز
# 6 زبانیں: سرائیکی + اردو + پنجابی + بلوچی + پشتو + سندھی

TOKEN_EOF = "EOF"
TOKEN_IDENTIFIER = "IDENTIFIER"
TOKEN_NUMBER = "NUMBER"
TOKEN_STRING = "STRING"

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
    "ټولګه": "CLASS",
    "گروپ": "CLASS",
    "گروہ": "CLASS",
    "ڪلاس": "CLASS",

    # ═══ THEN ═══
    "تاں": "THEN",
    "تو": "THEN",
    "{": "LBRACE",
    "}": "RBRACE",

    # ═══ VAR / CONST (تمام زبانیں) ═══
    "عدد": "VAR",
    "شے": "VAR",
    "متغیر": "VAR",
    "چیز": "VAR",
    "توکی": "VAR",
    "شی": "VAR",
    "شئي": "VAR",
    "پکی": "CONST",
    "مستقل": "CONST",
    "ثابت": "CONST",
    "پڪي": "CONST",

    # ═══ IF / ELSE ═══
    "جے": "IF",
    "اگر": "IF",
    "گَر": "IF",
    "که": "IF",
    "جيڪڏهن": "IF",
    "نہیں_تاں": "ELSE",
    "نہ_تاں": "ELSE",
    "ورنہ": "ELSE",
    "نہیں_تے": "ELSE",
    "نہ_کن": "ELSE",
    "نو": "ELSE",
    "بلکه": "ELSE",
    "نه_ته": "ELSE",

    # ═══ WHILE ═══
    "جئیں_ویلے_تئیں": "WHILE",
    "جتھاں": "WHILE",
    "جدوں_تک": "WHILE",
    "جدوں_تئیں": "WHILE",
    "جبکہ": "WHILE",
    "تا_کہ": "WHILE",
    "تر_چې": "WHILE",
    "جستائين": "WHILE",

    # ═══ FOR ═══
    "برائے": "FOR",
    "ہر": "FOR",
    "ہر_ہک_کیتے": "FOR",
    "کے_لیے": "FOR",
    "ہر_اک_لئی": "FOR",
    "پَر_ہر": "FOR",
    "ہر_یک": "FOR",
    "د_هر": "FOR",
    "هر_یو": "FOR",
    "هر_هڪ_لاءِ": "FOR",

    # ═══ FUNCTION ═══
    "کم": "FUNCTION",
    "کام": "FUNCTION",
    "فعل": "FUNCTION",
    "فنکشن": "FUNCTION",
    "کار": "FUNCTION",
    "ڪم": "FUNCTION",

    # ═══ RETURN ═══
    "واپس": "RETURN",
    "واپس_ڈیو": "RETURN",
    "واپس_کرو": "RETURN",
    "واپس_دیو": "RETURN",
    "موڑ": "RETURN",
    "برگرد": "RETURN",
    "بیرته": "RETURN",
    "موٽايو": "RETURN",

    # ═══ PRINT ═══
    "چھاپ": "PRINT",
    "چھاپیگا": "PRINT",
    "لکھو": "PRINT",
    "دسّو": "PRINT",
    "بنڈ": "PRINT",
    "ولیکه": "PRINT",
    "لکو": "PRINT",

    # ═══ TRUE / FALSE / NULL ═══
    "سچ": "TRUE",
    "راست": "TRUE",
    "ریښتین": "TRUE",
    "کوڑ": "FALSE",
    "جھوٹ": "FALSE",
    "دروغ": "FALSE",
    "درواغ": "FALSE",
    "ڪوڙ": "FALSE",
    "خالی": "NULL",
    "ہیچ": "NULL",
    "خالي": "NULL",

    # ═══ ARITHMETIC (arithmetic operators) ═══
    "جمع": "PLUS",
    "جوڑ": "PLUS",
    "زیات": "PLUS",
    "منفی": "MINUS",
    "گھٹاؤ": "MINUS",
    "ضرب": "STAR",
    "تقسیم": "SLASH",
    "ونڈ": "SLASH",
    "باقی": "MODULO",
    "طاقت": "POWER",

    # ═══ COMPARISON (موازنہ) ═══
    "وڈا": "GREATER",
    "بڑا": "GREATER",
    "لوی": "GREATER",
    "نکا": "LESS",
    "چھوٹا": "LESS",
    "کوچنی": "LESS",
    "برابر": "EQUAL_EQUAL",
    "نہیں_برابر": "NOT_EQUAL",
    "نئیں_برابر": "NOT_EQUAL",

    # ═══ LOGICAL ═══
    "تے": "AND",
    "اور": "AND",
    "و": "AND",
    "او": "AND",
    "۽": "AND",
    "یا": "OR",
    "برابر": "EQUAL_EQUAL",
    "نہیں_برابر": "NOT_EQUAL",
    "وڈا": "GREATER",
    "نکا": "LESS",
    "يا": "OR",
    "کائنی": "NOT",
    "نہیں": "NOT",
    "نئیں": "NOT",
    "نہ": "NOT",
    "نه": "NOT",

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
    "تہ": "IN",
    "په": "IN",
    "۾": "IN",
    "تک": "TO",
    "تئیں": "TO",
    "توڑ": "TO",
    "تا": "TO",
    "تر": "TO",
    "تائين": "TO",
    # ═══ UNIVERSAL keywords ═══
    "غیر_متزامن": "ASYNC",
    "غیر_ہم_وقت": "ASYNC",
    "انتظار": "AWAIT",
    "پیداوار": "YIELD",
    "منتخب": "SWITCH",
    "منتخب_کرو": "SWITCH",
    "چنو": "SWITCH",
    "چُنو": "SWITCH",
    "صورت": "CASE",
    "ڈیفالٹ": "DEFAULT",
    "بصورت_دیگر": "DEFAULT",
    "توڑ_دو": "BREAK",
    "روک_ڈیو": "BREAK",
    "روک_دیو": "BREAK",
    "جاری_رکھو": "CONTINUE",
    "اگوں_ٹرو": "CONTINUE",
    "اگے_ٹرو": "CONTINUE",
    "آخر_میں": "FINALLY",
    "آخر_وچ": "FINALLY",
    "آخر_چ": "FINALLY",
    "پھینکو": "THROW",
    "سُٹو": "THROW",
    "خالی_بیان": "PASS",
    "گزر": "PASS",
    "دعویٰ": "ASSERT",
    "تصدیق": "ASSERT",
    "ساتھ": "WITH",
    "نال": "WITH",
    "ملاؤ": "MATCH",
    "جوڑو": "MATCH",
    "لَمڈا": "LAMBDA",
    "مختصر": "LAMBDA",
    "لپیٹو": "DECORATOR",
    "سجاؤ": "DECORATOR",
    "ٹائپ": "TYPEOF",
    "مثال": "INSTANCEOF",
    "بطور": "AS",
    "طور": "AS",
    "حذف": "DELETE",
    "مٹاؤ": "DELETE",
    "انٹرفیس": "INTERFACE",
    "خاکہ": "ABSTRACT",
    "جامد": "STATIC",
    "آخری": "FINAL",
    "اوور_رائڈ": "OVERRIDE",
    "عوامی": "PUBLIC",
    "نجی": "PRIVATE",
    "محفوظ": "PROTECTED",
    "صرف_پڑھو": "READONLY",
    "والد": "SUPER",
    "ماں": "SUPER",
    "پیرنٹ": "SUPER",
    "عالمی": "GLOBAL",
    "برآمد": "EXPORT",
    "باہر_کڈھو": "EXPORT",
    "سے": "FROM",
    "کولوں": "FROM",
    "پیکیج": "PACKAGE",
    "بنڈل": "PACKAGE",
    "ماڈیول": "MODULE",
    "ٹکڑا": "MODULE",
    "نام_جگہ": "NAMESPACE",
    "اقسام": "ENUM",
    "خلاء": "VOID",
    "غیر_معرف": "UNDEFINED",
    "غیر_متعین": "UNDEFINED",
}

# ── Merge multilingual keywords ──
try:
    from multilingual_keywords import MULTILINGUAL_KEYWORDS as _ML
    _OVERRIDES = {"PROG_START": "PROGRAM_START", "PROG_END": "PROGRAM_END"}
    for _k, _v in _ML.items():
        KEYWORDS.setdefault(_k, _OVERRIDES.get(_v, _v))
except Exception:
    pass
