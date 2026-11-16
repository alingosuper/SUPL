#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
سرائیکی — pip کا سرائیکی نام (کمانڈ entry point)
تخلیق کار: النگو ڈویلپرز (AlinGo Developers)
"""

import sys
import subprocess

# کمانڈ میپ
COMMANDS = {
    "نصب": "install",
    "لڳاؤ": "install",
    "لگاؤ": "install",
    "ہٹاؤ": "uninstall",
    "ہٹاو": "uninstall",
    "کڍو": "uninstall",
    "کڈھو": "uninstall",
    "فہرست": "list",
    "لسٹ": "list",
    "ڈکھاؤ": "show",
    "دکھاو": "show",
    "وکھاؤ": "show",
    "بند": "freeze",
    "منجمد": "freeze",
    "اپگریڈ": "install --upgrade",
    "اپ_گریڈ": "install --upgrade",
    "ڈاؤنلوڈ": "download",
    "ڈاؤن_لوڈ": "download",
}


def main():
    if len(sys.argv) < 2:
        # کوئی آرگیومنٹ نہیں → pip
        subprocess.run([sys.executable, "-m", "pip"])
        return 0

    cmd = sys.argv[1]
    rest = sys.argv[2:]

    # ورژن
    if cmd in ("--version", "-V", "نسخہ", "ورژن", "version"):
        print("سرائیکی پیکیج مینیجر v1.0.0 — النگو ڈویلپرز")
        subprocess.run([sys.executable, "-m", "pip", "--version"])
        return 0

    # مدد
    if cmd in ("--help", "-h", "مدد", "help"):
        print_help()
        return 0

    # کمانڈ میپ
    actual_cmd = COMMANDS.get(cmd, cmd)

    # اگر "install --upgrade" ہے تو ٹوڑیں
    if " " in actual_cmd:
        parts = actual_cmd.split()
        return subprocess.run([sys.executable, "-m", "pip"] + parts + rest).returncode

    # باقی
    return subprocess.run([sys.executable, "-m", "pip", actual_cmd] + rest).returncode


def print_help():
    print("""═══════════════════════════════════════════════════════════
  سرائیکی — پیکیج مینیجر (pip کا سرائیکی نام)
  تخلیق کار: النگو ڈویلپرز (AlinGo Developers)
═══════════════════════════════════════════════════════════

استعمال:
  سرائیکی نصب <پیکیج>           — پیکیج نصب کریں
  سرائیکی ہٹاؤ <پیکیج>           — پیکیج ہٹائیں
  سرائیکی فہرست                 — نصب شدہ پیکیجز
  سرائیکی ڈکھاؤ <پیکیج>          — تفصیل
  سرائیکی بند                   — installed packages
  سرائیکی اپگریڈ <پیکیج>         — اپ گریڈ
  سرائیکی ڈاؤنلوڈ <پیکیج>        — صرف ڈاؤن لوڈ

انگریزی کمانڈز بھی چلیں گی:
  سرائیکی install <پیکیج>
  سرائیکی uninstall <پیکیج>
  سرائیکی list
  سرائیکی show <پیکیج>

═══════════════════════════════════════════════════════════
""")


if __name__ == "__main__":
    sys.exit(main())
