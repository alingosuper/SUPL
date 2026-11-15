# SUPL Parser — النگو ڈویلپرز
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from lexer.lexer import Lexer

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self, message):
        raise SyntaxError(f"پارسر کی خرابی (لائن {self.current_token.line}): {message}")

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f"متوقع ٹوکن {token_type}, لیکن ملا {self.current_token.type}")

    def parse(self):
        print("===== پارسنگ شروع ہو گئی ہے =====")
        # پندھ شروع سے آغاز
        if self.current_token.type == "PROGRAM_START":
            self.eat("PROGRAM_START")
            if self.current_token.type == "STRING":
                program_name = self.current_token.value
                self.eat("STRING")
                print(f"پروگرام کا نام: {program_name}")
            
            # ہدایات پڑھنا
            while self.current_token.type != "PROGRAM_END" and self.current_token.type != "EOF":
                self.statement()

            if self.current_token.type == "PROGRAM_END":
                self.eat("PROGRAM_END")
                print("===== پروگرام کامیابی سے پارس ہو گیا! =====")
        else:
            self.error("پروگرام 'پندھ_شروع' سے شروع ہونا چاہیے")

    def statement(self):
        # ویری ایبل ڈیکلریشن (عدد عمر = 20)
        if self.current_token.type == "VAR":
            self.eat("VAR")
            var_name = self.current_token.value
            self.eat("IDENTIFIER")
            self.eat("ASSIGN")
            val = self.current_token.value
            self.eat(self.current_token.type)
            print(f"ویری ایبل डیکلریشن: {var_name} = {val}")

        # پرنٹ کمانڈ (چھاپ ...)
        elif self.current_token.type == "PRINT":
            self.eat("PRINT")
            val = self.current_token.value
            self.eat(self.current_token.type)
            print(f"پرنٹ کمانڈ: {val}")

        # اگر (IF) کنڈیشن
        elif self.current_token.type == "IF":
            self.eat("IF")
            left = self.current_token.value
            self.eat("IDENTIFIER")
            op = self.current_token.value
            self.eat("GREATER_EQUAL") # عارضی طور پر آپریٹر ہینڈلنگ
            right = self.current_token.value
            self.eat("NUMBER")
            # 'تاں' کو اگنور کرنا
            if self.current_token.type == "IDENTIFIER" and self.current_token.value == "تاں":
                self.eat("IDENTIFIER")
            print(f"مشروط بیان (IF): {left} {op} {right}")

        # ورنہ (ELSE)
        elif self.current_token.type == "ELSE":
            self.eat("ELSE")
            print("ورنہ (ELSE) بلاک")

        else:
            self.error(f"نامعلوم بیان یا کمانڈ: {self.current_token.value}")

