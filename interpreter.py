# SUPL Interpreter & UI Engine — النگو ڈویلپرز
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
from lexer.lexer import Lexer
from parser.parser import Parser
from urdu.runtime.naksha import NakshaUI

class Interpreter:
    def __init__(self, parser):
        self.parser = parser
        self.variables = {}
        self.ui = NakshaUI("سرائیکی زبردست ایپ")

    def interpret(self):
        if self.parser.current_token.type == "PROGRAM_START":
            self.parser.eat("PROGRAM_START")
            if self.parser.current_token.type == "STRING":
                prog_name = self.parser.current_token.value
                print(f"--- پروگرام شروع: {prog_name} (النگو ڈویلپرز) ---")
                self.ui.صفحہ_شروع(prog_name)
                self.parser.eat("STRING")

            while self.parser.current_token.type != "PROGRAM_END" and self.parser.current_token.type != "EOF":
                self.execute_statement()

            if self.parser.current_token.type == "PROGRAM_END":
                self.parser.eat("PROGRAM_END")
                self.ui.صفحہ_ختم()
                self.ui.محفوظ_کرو("supl_out.html")
                print("--- پندھ مک گیا (ویب UI محفوظ ہو گیا ہے) ---")

    def execute_statement(self):
        token = self.parser.current_token

        # 1. ویری ایبل ڈیکلریشن
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
            self.ui.متن_لکھو(str(val))

        # 3. گرافکس / UI کمانڈز کی شناخت (جیسے سرخی، بٹن)
        elif token.type == "IDENTIFIER" and token.value in ["سرخی", "بٹن", "ڈبہ"]:
            cmd = token.value
            self.parser.eat("IDENTIFIER")
            # ویلیو یا سٹرنگ پڑھنا
            val = self.parser.current_token.value
            self.parser.eat(self.parser.current_token.type)

            if cmd == "سرخی":
                self.ui.سرخی_بناؤ(val)
                print(f"[UI سرخی]: {val}")
            elif cmd == "بٹن":
                self.ui.بٹن_بناؤ(val, "بٹن دبایا گیا!")
                print(f"[UI بٹن]: {val}")
            elif cmd == "ڈبہ":
                self.ui.ڈبہ_بناؤ(val)
                print(f"[UI ڈبہ]: {val}")

        # 4. مشروط بیان (جے ... تاں)
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
            if op == "GREATER_EQUAL": condition_met = left_val >= right_val
            elif op == "LESS_EQUAL": condition_met = left_val <= right_val
            elif op == "GREATER": condition_met = left_val > right_val
            elif op == "LESS": condition_met = left_val < right_val

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
