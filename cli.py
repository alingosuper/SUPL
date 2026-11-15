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

def run_interactive_repl():
    """
    SUPL کا لائیو انٹرایکٹو شیل (REPL) جو دیسی کی ورڈز پر لائیو کام کرتا ہے
    """
    print("=" * 60)
    print(f"  SarakLuk — لائیو انٹرایکٹو شیل (REPL) v{VERSION}")
    print("  باہر نکلنے کے لیے 'باہر'، 'exit' یا 'ختم' لکھیں۔")
    print("=" * 60)
    
    variables = {}
    
    while True:
        try:
            line = input("سرائیکی> ")
            
            if not line.strip():
                continue
                
            if line.strip().lower() in ["باہر", "exit", "quit", "ختم"]:
                print("اللہ حافظ! SarakLuk شیل بند ہو رہا ہے۔")
                break

            # سطر کو بلاک یا انفرادی کمانڈ کے طور پر رن کرنا
            kod = f'پندھ_شروع "REPL"\n    {line}\nپندھ_مک_گیا'
            lexer = Lexer(kod)
            p = Parser(lexer)
            interp = Interpreter(p)
            interp.variables = variables
            interp.interpret()
            variables = interp.variables
            
        except KeyboardInterrupt:
            print("\nشیل بند کر دیا گیا ہے۔")
            break
        except Exception as e:
            print(f"خرابی (Error): {e}")

def main():
    parser = argparse.ArgumentParser(
        description="SarakLuk (سرائیکی پروگرامنگ لینگویج) — ٹرمینل انٹرفیس",
        prog="saraiki"
    )
    parser.add_argument("file", nargs="?", help="چلانے کے لیے سرائیکی فائل (.slk)")
    parser.add_argument("-v", "--version", action="version", version=f"SarakLuk v{VERSION} — {AUTHOR}")
    parser.add_argument("-i", "--interactive", action="store_true", help="انٹرایکٹو شیل (REPL) شروع کریں")

    args = parser.parse_args()

    # اگر فلیگ دیا گیا ہو یا کوئی فائل نہ دی گئی ہو تو لائیو REPL کھولیں
    if args.interactive or not args.file:
        if not args.interactive and not args.file:
            print(f"SarakLuk v{VERSION} — {AUTHOR}")
            print("استعمال کا طریقہ: saraiki <فائل_کا_نام.slk> یا saraiki -i\n")
        run_interactive_repl()
        return

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
