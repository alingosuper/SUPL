#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SarakLuk CLI (کمانڈ لائن انٹرفیس)
تخلیق کار: النگو ڈویلپرز (Alango Developers)
"""

import sys
import argparse
from pathlib import Path

# پراجیکٹ کے روٹ فولڈر کو پاتھ میں شامل کرنا
sys.path.append(str(Path(__file__).resolve().parent))

from lexer.lexer import Lexer
from parser.parser import Parser
from interpreter import Interpreter

VERSION = "1.0.0"
AUTHOR = "النگو ڈویلپرز (Alango Developers)"

def main():
    parser = argparse.ArgumentParser(
        description="SarakLuk (سرائیکی پروگرامنگ لینگویج) — ٹرمینل انٹرفیس",
        prog="saraiki"
    )
    parser.add_argument("file", nargs="?", help="چلانے کے لیے سرائیکی فائل (.slk)")
    parser.add_argument("-v", "--version", action="version", version=f"SarakLuk v{VERSION} — {AUTHOR}")
    parser.add_argument("-i", "--interactive", action="store_true", help="انٹرایکٹو شیل (REPL) شروع کریں")

    args = parser.parse_args()

    if args.interactive:
        print(f"--- SarakLuk انٹرایکٹو شیل (REPL) v{VERSION} — {AUTHOR} ---")
        print("باہر نکلنے کے لیے 'باہر' یا 'exit' لکھیں۔\n")
        variables = {}
        while True:
            try:
                line = input("سرائیکی> ")
                if line.strip() in ["باہر", "exit", "quit"]:
                    break
                if not line.strip():
                    continue
                
                # عارضی ریپل ایگزیکوشن
                kod = f'پندھ_شروع "REPL"\n    {line}\nپندھ_مک_گیا'
                lexer = Lexer(kod)
                p = Parser(lexer)
                interp = Interpreter(p)
                interp.variables = variables
                interp.interpret()
                variables = interp.variables
            except Exception as e:
                print(f"خرابی: {e}")
        return

    if not args.file:
        print(f"SarakLuk v{VERSION} — {AUTHOR}")
        print("استعمال کا طریقہ: saraiki <فائل_کا_نام.slk>")
        print("مدد کے لیے لکھیں: saraiki --help")
        sys.exit(1)

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"خطہ: فائل '{args.file}' نہیں ملی!")
        sys.exit(1)

    try:
        code = file_path.read_text(encoding="utf-8")
        lexer = Lexer(code)
        p = Parser(lexer)
        interpreter = Interpreter(p)
        interpreter.interpret()
    except Exception as e:
        print(f"پروگرام چلانے میں خرابی: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
