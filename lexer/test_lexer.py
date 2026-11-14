import sys
from pathlib import Path

# پراجیکٹ کے روٹ فولڈر کو پاتھ میں شامل کرنا
sys.path.append(str(Path(__file__).resolve().parent.parent))

from lexer.lexer import Lexer

kod = """
پندھ_شروع "ٹیسٹ"
    عدد عمر = 20
    جے عمر >= 18 تاں
        چھاپ "تساں ووٹ ڈے سگدے او"
    نہیں_تاں
        چھاپ "نکے او"
پندھ_مک_گیا
"""

l = Lexer(kod)
token = l.get_next_token()
while token.type != "EOF":
    print(token)
    token = l.get_next_token()
