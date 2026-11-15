#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AlinGo v1.0.0 — مرکزی کمانڈ لائن انٹرفیس اور CLI ڈسپیچر (مع ویب ٹولز)
"""
import sys
from pathlib import Path

# جب اسکرپٹ ڈائریکٹ چلایا جائے (python3 supl/cli.py) تو روٹ کو sys.path میں شامل کریں
_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import subprocess
from supl.dictionary import search_word, add_word, delete_word, list_all_words

def print_help():
    print("=" * 65)
    print(" AlinGo — دیسی ٹرمینل، لغت اور ویب ٹولز سوٹ v1.0.0")
    print("=" * 65)
    print(" استعمال کا طریقہ:")
    print("   saraiki -i                  (لائیو انٹرایکٹو شیل شروع کریں)")
    print("   saraiki <فائل.slk>          (AlinGo سورس کوڈ فائل چلائیں)")
    print("   -----------------------------------------------------------")
    print("    لغت کی کمانڈز:")
    print("     saraiki تلاش <لفظ>         (لغت میں لفظ تلاش کریں)")
    print("     saraiki شامل <لفظ> <معنی>  (نیا لفظ لغت میں درج کریں)")
    print("     saraiki مٹاؤ <لفظ>         (لغت سے لفظ حذف کریں)")
    print("     saraiki فہرست              (لغت کے تمام الفاظ دیکھیں)")
    print("   -----------------------------------------------------------")
    print("    جدید ویب اور سرور ٹولز:")
    print("     saraiki نوڈ <فائل.js>      (Node.js اسکرپٹ یا سرور چلائیں)")
    print("     saraiki گو <فائل.go>        (Go زبان کا پروگرام چلائیں)")
    print("     saraiki سرور [پورٹ]        (HTML/CSS کے لیے لوکل ویب سرور)")
    print("=" * 65)

def run_node(args):
    """Node.js فائل چلانے کے لیے"""
    if not args:
        print("❌ خرابی: برائے مہربانی Node.js فائل کا نام بتائیں۔ (مثال: saraiki نوڈ server.js)")
        return
    subprocess.run(["node"] + args)

def run_go(args):
    """Go زبان کی فائل چلانے کے لیے"""
    if not args:
        print("❌ خرابی: برائے مہربانی Go فائل کا نام بتائیں۔ (مثال: saraiki گو main.go)")
        return
    subprocess.run(["go", "run"] + args)

def run_web_server(args):
    """مقامی ویب سرور (HTML/CSS) شروع کرنے کے لیے"""
    port = args[0] if args else "8000"
    print(f"🚀 لوکل ویب سرور http://localhost:{port} پر شروع ہو رہا ہے...")
    print(f"   (بند کرنے کے لیے Ctrl+C دبائیں)")
    try:
        subprocess.run(["python3", "-m", "http.server", str(port)])
    except KeyboardInterrupt:
        # صاف بندش — کوئی traceback نہیں
        print("\n🛑 سرور بند کر دیا گیا۔ اللہ حافظ!")

def main():
    args = sys.argv[1:]
    
    if not args:
        print_help()
        return

    command = args[0]

    if command == "-i" or command == "شیل":
        from supl.interpreter import run_repl
        run_repl()
    
    elif command == "تلاش" and len(args) > 1:
        search_word(" ".join(args[1:]))
        
    elif command == "شامل" and len(args) >= 3:
        add_word(args[1], " ".join(args[2:]))
        
    elif command == "مٹاؤ" and len(args) > 1:
        delete_word(args[1])
        
    elif command == "فہرست":
        list_all_words()

    elif command == "نوڈ":
        run_node(args[1:])

    elif command == "گو":
        run_go(args[1:])

    elif command == "سرور":
        run_web_server(args[1:])
    
    else:
        # اگر کوئی .slk فائل یا عام سورس فائل دی گئی ہو
        from supl.interpreter import run_file
        run_file(command)

if __name__ == "__main__":
    main()
