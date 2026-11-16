"""Token types and Urdu keyword mappings for the Urdu Programming Language."""

from enum import Enum, auto


class TokenType(Enum):
    # Literals
    NUMBER = auto()
    STRING = auto()
    TEMPLATE_STRING = auto()
    IDENTIFIER = auto()
    REGEX = auto()

    # Variable declarations
    VAR = auto()           # متغیر
    CONST = auto()         # مستقل
    LET = auto()           # چھوٹا (alias)

    # Control flow
    IF = auto()            # اگر
    ELSE = auto()          # ورنہ
    ELIF = auto()          # ورنہ_اگر
    WHILE = auto()         # جبکہ
    FOR = auto()           # کے_لیے
    IN = auto()            # میں   (for...in / for...of)
    OF = auto()            # کا    (for...of)
    BREAK = auto()         # ٹوٹنا
    CONTINUE = auto()      # جاری
    RETURN = auto()        # واپس
    DO = auto()            # کرو

    # Switch
    SWITCH = auto()        # منتخب
    CASE = auto()          # صورت
    SWITCH_DEFAULT = auto()  # بصورت_دیگر

    # Functions
    FUNCTION = auto()      # فنکشن
    ASYNC = auto()         # غیر_متزامن
    AWAIT = auto()         # انتظار
    YIELD = auto()         # پیداوار

    # Classes / OOP
    CLASS = auto()         # کلاس
    EXTENDS = auto()       # توسیع
    CONSTRUCTOR = auto()   # تعمیر
    THIS = auto()          # یہ
    SUPER = auto()         # سپر
    NEW = auto()           # نیا
    PUBLIC = auto()        # عوامی
    PRIVATE = auto()       # نجی
    PROTECTED = auto()     # محفوظ
    STATIC = auto()        # جامد
    ABSTRACT = auto()      # خاکہ
    INTERFACE = auto()     # انٹرفیس
    IMPLEMENTS = auto()    # نافذ
    READONLY = auto()      # صرف_پڑھو
    OVERRIDE = auto()      # اوور_رائڈ
    GET = auto()           # حاصل_کرو
    SET = auto()           # مقرر_کرو

    # Exception handling
    TRY = auto()           # کوشش
    CATCH = auto()         # پکڑو
    FINALLY = auto()       # آخر
    THROW = auto()         # پھینکو

    # Import / Export
    IMPORT = auto()        # درآمد
    FROM = auto()          # سے
    EXPORT = auto()        # برآمد
    DEFAULT = auto()       # ڈیفالٹ
    AS = auto()            # بطور

    # Boolean / null
    TRUE = auto()          # سچ
    FALSE = auto()         # جھوٹ
    NULL = auto()          # خالی
    UNDEFINED = auto()     # غیر_معرف

    # Logical keyword operators
    AND = auto()           # اور
    OR = auto()            # یا
    NOT = auto()           # نہیں

    # Type operators
    TYPEOF = auto()        # قسم
    INSTANCEOF = auto()    # مثال
    DELETE = auto()        # حذف
    IN_OP = auto()         # میں_ہے
    VOID = auto()          # خلاء

    # Built-in functions
    PRINT = auto()         # لکھو
    INPUT_FN = auto()      # پڑھو

    # --- Operators ---
    PLUS = auto()                # +
    MINUS = auto()               # -
    MULTIPLY = auto()            # *
    DIVIDE = auto()              # /
    MODULO = auto()              # %
    POWER = auto()               # **
    FLOOR_DIVIDE = auto()        # //

    PLUS_ASSIGN = auto()         # +=
    MINUS_ASSIGN = auto()        # -=
    MULTIPLY_ASSIGN = auto()     # *=
    DIVIDE_ASSIGN = auto()       # /=
    MODULO_ASSIGN = auto()       # %=
    POWER_ASSIGN = auto()        # **=
    AND_ASSIGN = auto()          # &&=
    OR_ASSIGN = auto()           # ||=
    NULLISH_ASSIGN = auto()      # ??=
    BITAND_ASSIGN = auto()       # &=
    BITOR_ASSIGN = auto()        # |=

    EQUALS = auto()              # ==
    NOT_EQUALS = auto()          # !=
    STRICT_EQUALS = auto()       # ===
    STRICT_NOT_EQUALS = auto()   # !==
    LESS_THAN = auto()           # <
    GREATER_THAN = auto()        # >
    LESS_EQUAL = auto()          # <=
    GREATER_EQUAL = auto()       # >=

    ASSIGN = auto()              # =

    LOGICAL_AND = auto()         # &&
    LOGICAL_OR = auto()          # ||
    LOGICAL_NOT = auto()         # !

    BITWISE_AND = auto()         # &
    BITWISE_OR = auto()          # |
    BITWISE_XOR = auto()         # ^
    BITWISE_NOT = auto()         # ~
    LEFT_SHIFT = auto()          # <<
    RIGHT_SHIFT = auto()         # >>
    UNSIGNED_RIGHT_SHIFT = auto() # >>>

    ARROW = auto()               # => or ->
    OPTIONAL_CHAIN = auto()      # ?.
    NULLISH = auto()             # ??

    INCREMENT = auto()           # ++
    DECREMENT = auto()           # --
    SPREAD = auto()              # ...

    # Punctuation
    LEFT_BRACE = auto()     # {
    RIGHT_BRACE = auto()    # }
    LEFT_PAREN = auto()     # (
    RIGHT_PAREN = auto()    # )
    LEFT_BRACKET = auto()   # [
    RIGHT_BRACKET = auto()  # ]
    SEMICOLON = auto()      # ;
    COMMA = auto()          # ,
    DOT = auto()            # .
    COLON = auto()          # :
    QUESTION = auto()       # ?
    AT = auto()             # @ (decorators)
    HASH = auto()           # # (private fields)

    # Special
    EOF = auto()
    NEWLINE = auto()


# ─── Urdu Keyword → TokenType mapping ───────────────────────────────────────
# ─── Saraiki + Urdu + Punjabi Keyword → TokenType mapping ───────────────────
SUPL_KEYWORDS: dict[str, TokenType] = {

    # ═══ متغیر اعلانات / Variable declarations ═══
    "متغیر":         TokenType.VAR,
    "شے":            TokenType.VAR,
    "مستقل":         TokenType.CONST,
    "پکی":           TokenType.CONST,
    "چھوٹا":         TokenType.LET,

    # ═══ کنٹرول فلو / Control flow ═══
    "اگر":           TokenType.IF,
    "جے":            TokenType.IF,
    "ورنہ":          TokenType.ELSE,
    "نہیں_تے":       TokenType.ELSE,
    "نہ_تاں":        TokenType.ELSE,
    "ورنہ_اگر":      TokenType.ELIF,
    "جے_نہیں_تے":    TokenType.ELIF,
    "جے_نہ_تاں":     TokenType.ELIF,
    "جبکہ":          TokenType.WHILE,
    "جدوں_تک":       TokenType.WHILE,
    "جدوں_تئیں":     TokenType.WHILE,
    "کے_لیے":        TokenType.FOR,
    "ہر_اک_لئی":     TokenType.FOR,
    "ہر_ہک_کیتے":    TokenType.FOR,
    "میں":           TokenType.IN,
    "وچ":            TokenType.IN,
    "کا":            TokenType.OF,
    "دا":            TokenType.OF,
    "توڑ_دو":        TokenType.BREAK,
    "روک_دیو":       TokenType.BREAK,
    "روک_ڈیو":       TokenType.BREAK,
    "جاری_رکھو":     TokenType.CONTINUE,
    "اگے_ٹرو":       TokenType.CONTINUE,
    "اگوں_ٹرو":      TokenType.CONTINUE,
    "واپس_کرو":      TokenType.RETURN,
    "واپس_دیو":      TokenType.RETURN,
    "واپس_ڈیو":      TokenType.RETURN,
    "کرو":           TokenType.DO,

    # ═══ Switch ═══
    "منتخب_کرو":     TokenType.SWITCH,
    "چنو":           TokenType.SWITCH,
    "چُنو":          TokenType.SWITCH,
    "صورت":          TokenType.CASE,
    "بصورت_دیگر":    TokenType.SWITCH_DEFAULT,

    # ═══ فنکشنز / Functions ═══
    "فنکشن":         TokenType.FUNCTION,
    "کم":            TokenType.FUNCTION,
    "غیر_متزامن":    TokenType.ASYNC,
    "غیر_ہم_وقت":    TokenType.ASYNC,
    "انتظار":        TokenType.AWAIT,
    "پیداوار":       TokenType.YIELD,

    # ═══ کلاسز / Classes ═══
    "کلاس":          TokenType.CLASS,
    "ٹولی":          TokenType.CLASS,
    "توسیع":         TokenType.EXTENDS,
    "ودھاؤ":         TokenType.EXTENDS,
    "ورثے_وچ":       TokenType.EXTENDS,
    "تعمیر":         TokenType.CONSTRUCTOR,
    "بݨاؤ":          TokenType.CONSTRUCTOR,
    "یہ":            TokenType.THIS,
    "ایہہ":          TokenType.THIS,
    "سپر":           TokenType.SUPER,
    "پیرنٹ":         TokenType.SUPER,
    "نیا":           TokenType.NEW,
    "نواں":          TokenType.NEW,
    "عوامی":         TokenType.PUBLIC,
    "نجی":           TokenType.PRIVATE,
    "محفوظ":         TokenType.PROTECTED,
    "جامد":          TokenType.STATIC,
    "خاکہ":          TokenType.ABSTRACT,
    "انٹرفیس":       TokenType.INTERFACE,
    "نافذ":          TokenType.IMPLEMENTS,
    "لاگو_کرو":      TokenType.IMPLEMENTS,
    "صرف_پڑھو":      TokenType.READONLY,
    "اوور_رائڈ":     TokenType.OVERRIDE,
    "حاصل_کرو":      TokenType.GET,
    "لے_لو":         TokenType.GET,
    "مقرر_کرو":      TokenType.SET,
    "رکھو":          TokenType.ASSIGN,    # سرائیکی/پنجابی assignment

    # ═══ استثناء / Exception handling ═══
    "کوشش":          TokenType.TRY,
    "کوشش_کرو":      TokenType.TRY,
    "پکڑو":          TokenType.CATCH,
    "پھڑو":          TokenType.CATCH,
    "آخر_میں":       TokenType.FINALLY,
    "آخر_چ":         TokenType.FINALLY,
    "آخر_وچ":        TokenType.FINALLY,
    "پھینکو":        TokenType.THROW,
    "سُٹو":          TokenType.THROW,

    # ═══ درآمد / برآمد / Import / Export ═══
    "درآمد_کرو":     TokenType.IMPORT,
    "لے_آؤ":         TokenType.IMPORT,
    "گھن_آؤ":        TokenType.IMPORT,
    "سے":            TokenType.FROM,
    "توں":           TokenType.FROM,
    "کولوں":         TokenType.FROM,
    "برآمد_کرو":     TokenType.EXPORT,
    "باہر_کڈھو":     TokenType.EXPORT,
    "ڈیفالٹ":        TokenType.DEFAULT,
    "بطور":          TokenType.AS,
    "طور":           TokenType.AS,

    # ═══ منطقی / Boolean ═══
    "سچ":            TokenType.TRUE,
    "جھوٹ":          TokenType.FALSE,
    "کوڑ":           TokenType.FALSE,
    "خالی":          TokenType.NULL,
    "غیر_معرف":      TokenType.UNDEFINED,
    "غیر_متعین":     TokenType.UNDEFINED,

    # ═══ منطقی آپریٹرز / Logical operators ═══
    "اور":           TokenType.AND,
    "تے":            TokenType.AND,
    "یا":            TokenType.OR,
    "نہیں":          TokenType.NOT,
    "نئیں":          TokenType.NOT,
    "کائنی":         TokenType.NOT,

    # ═══ قسم کے آپریٹرز / Type operators ═══
    "قسم":           TokenType.TYPEOF,
    "مثال":          TokenType.INSTANCEOF,
    "حذف_کرو":       TokenType.DELETE,
    "مٹاؤ":          TokenType.DELETE,
    "میں_ہے":        TokenType.IN_OP,
    "وچ_اے":         TokenType.IN_OP,
    "خلاء":          TokenType.VOID,

    # ═══ Built-in فنکشنز ═══
    "لکھو":          TokenType.PRINT,
    "پوچھو":         TokenType.INPUT_FN,
    "پچھو":          TokenType.INPUT_FN,
    "پُچھو":         TokenType.INPUT_FN,

    # ═══ موازنہ (Comparison) — تینوں زبانیں ═══
    "وڈا":           TokenType.GREATER_THAN,    # سرائیکی/پنجابی >
    "بڑا":           TokenType.GREATER_THAN,    # اردو >
    "نکا":           TokenType.LESS_THAN,       # سرائیکی/پنجابی <
    "چھوٹا":         TokenType.LESS_THAN,       # اردو <
    "برابر":         TokenType.EQUALS,          # تینوں ==
    "نہیں_برابر":    TokenType.NOT_EQUALS,      # اردو !=
    "نئیں_برابر":    TokenType.NOT_EQUALS,      # پنجابی !=
    "کائنی_برابر":   TokenType.NOT_EQUALS,      # سرائیکی !=
}

# Backward compatibility — پرانا نام
URDU_KEYWORDS = SUPL_KEYWORDS

