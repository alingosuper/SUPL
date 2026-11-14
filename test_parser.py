import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
from lexer.lexer import Lexer
from parser.parser import Parser

kod = """
پندھ_شروع "سرائیکی_ٹیسٹ"
    عدد عمر = 20
    جے عمر >= 18 تاں
        چھاپ "تساں ووٹ ڈے سگدے او"
    نہیں_تاں
        چھاپ "نکے او"
پندھ_مک_گیا
"""

lexer = Lexer(kod)
parser = Parser(lexer)
parser.parse()
