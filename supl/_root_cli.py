#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AlinGo CLI (کمانڈ لائن انٹرفیس)
تخلیق کار: النگو ڈویلپرز (AlinGo Developers)
"""

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import sys
import argparse
from pathlib import Path

# پراجیکٹ کے روٹ فولڈر کو پاتھ میں شامل کرنا
sys.path.append(str(Path(__file__).resolve().parent))

from lexer.lexer import Lexer
from parser.parser import Parser
from interpreter import Interpreter

VERSION = "1.0.0"
AUTHOR = "النگو ڈویلپرز (AlinGo Developers)"

def run_interactive_repl():
    """
    AlinGo کا لائیو انٹرایکٹو شیل (REPL) جو دیسی کی ورڈز پر لائیو کام کرتا ہے
    """
    print("=" * 60)
    print(f"  AlinGo — لائیو انٹرایکٹو شیل (REPL) v{VERSION}")
    print("  باہر نکلنے کے لیے 'باہر'، 'exit' یا 'ختم' لکھیں۔")
    print("=" * 60)
    
    variables = {}
    
    while True:
        try:
            line = input("سرائیکی> ")
            
            if not line.strip():
                continue
                
            if line.strip().lower() in ["باہر", "exit", "quit", "ختم"]:
                print("اللہ حافظ! AlinGo شیل بند ہو رہا ہے۔")
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
        description="AlinGo Saraiki (سرائیکی پروگرامنگ لینگویج) — ٹرمینل انٹرفیس",
        prog="saraiki"
    )
    parser.add_argument("file", nargs="?", help="چلانے کے لیے سرائیکی فائل (.slk)")
    parser.add_argument("-v", "--version", action="version", version=f"AlinGo v{VERSION} — {AUTHOR}")
    parser.add_argument("-i", "--interactive", action="store_true", help="انٹرایکٹو شیل (REPL) شروع کریں")

    args = parser.parse_args()

    # اگر فلیگ دیا گیا ہو یا کوئی فائل نہ دی گئی ہو تو لائیو REPL کھولیں
    if args.interactive or not args.file:
        if not args.interactive and not args.file:
            print(f"AlinGo v{VERSION} — {AUTHOR}")
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