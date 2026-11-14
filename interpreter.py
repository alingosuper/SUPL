# SarakLuk Interpreter — النگو ڈویلپرز
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
from lexer.lexer import Lexer
from parser.parser import Parser

class Interpreter:
    def __init__(self, parser):
        self.parser = parser
        self.variables = {}

    def interpret(self):
        # پندھ شروع چیک کرنا
        if self.parser.current_token.type == "PROGRAM_START":
            self.parser.eat("PROGRAM_START")
            if self.parser.current_token.type == "STRING":
                print(f"--- پروگرام شروع: {self.parser.current_token.value} (النگو ڈویلپرز) ---")
                self.parser.eat("STRING")

            while self.parser.current_token.type != "PROGRAM_END" and self.parser.current_token.type != "EOF":
                self.execute_statement()

            if self.parser.current_token.type == "PROGRAM_END":
                self.parser.eat("PROGRAM_END")
                print("--- پندھ مک گیا (کامیاب) ---")

    def execute_statement(self):
        token = self.parser.current_token

        # 1. ویری ایبل ڈیکلریشن (عدد عمر = 20)
        if token.type == "VAR":
            self.parser.eat("VAR")
            var_name_str = self.parser.current_token.value
            self.parser.eat("IDENTIFIER")
            self.parser.eat("ASSIGN")
            val = self.parser.current_token.value
            self.parser.eat(self.parser.current_token.type)
            self.variables[var_name_str] = val

        # 2. پرنٹ کمانڈ (چھاپ ...)
        elif token.type == "PRINT":
            self.parser.eat("PRINT")
            val = self.parser.current_token.value
            if self.parser.current_token.type == "IDENTIFIER" and val in self.variables:
                val = self.variables[val]
            self.parser.eat(self.parser.current_token.type)
            print(val)

        # 3. مشروط بیان (جے ... تاں)
        elif token.type == "IF":
            self.parser.eat("IF")
            left_var = self.parser.current_token.value
            self.parser.eat("IDENTIFIER")
            
            left_val = self.variables.get(left_var, 0)
            
            op = self.parser.current_token.type
            self.parser.eat(op)
            
            right_val = self.parser.current_token.value
            self.parser.eat(self.parser.current_token.type)

            if self.parser.current_token.type == "IDENTIFIER" and self.parser.current_token.value == "تاں":
                self.parser.eat("IDENTIFIER")

            condition_met = False
            if op == "GREATER_EQUAL":
                condition_met = left_val >= right_val
            elif op == "LESS_EQUAL":
                condition_met = left_val <= right_val
            elif op == "GREATER":
                condition_met = left_val > right_val
            elif op == "LESS":
                condition_met = left_val < right_val

            if condition_met:
                self.execute_statement()
                self.skip_to_else_or_end()
            else:
                self.skip_statement()
                if self.parser.current_token.type == "ELSE":
                    self.parser.eat("ELSE")
                    self.execute_statement()
                else:
                    self.skip_statement()

        # 4. ورنہ (ELSE) بلاک ہینڈلنگ
        elif token.type == "ELSE":
            self.parser.eat("ELSE")
            self.execute_statement()

        else:
            self.parser.error(f"نامعلوم بیان: {token.value}")

    def skip_statement(self):
        while self.parser.current_token.type not in ["PRINT", "IF", "ELSE", "PROGRAM_END", "EOF"]:
            self.parser.eat(self.parser.current_token.type)

    def skip_to_else_or_end(self):
        if self.parser.current_token.type == "ELSE":
            self.parser.eat("ELSE")
            self.skip_statement()

if __name__ == "__main__":
    kod = """
    پندھ_شروع "سرائیکی_پروگرام"
        عدد عمر = 20
        جے عمر >= 18 تاں
            چھاپ "تساں ووٹ ڈے سگدے او!"
        نہیں_تاں
            چھاپ "تساں حݨے نکے او!"
    پندھ_مک_گیا
    """
    
    lexer = Lexer(kod)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    interpreter.interpret()
