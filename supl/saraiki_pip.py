#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""سرائیکی پیکیج مینیجر — AlinGo Developers"""

import sys
import subprocess
from importlib.metadata import version, PackageNotFoundError

COMMANDS = {
    "نصب": ["install"],
    "لڳاؤ": ["install"],
    "لگاؤ": ["install"],
    "ہٹاؤ": ["uninstall"],
    "ہٹاو": ["uninstall"],
    "کڍو": ["uninstall"],
    "کڈھو": ["uninstall"],
    "فہرست": ["list"],
    "لسٹ": ["list"],
    "ڈکھاؤ": ["show"],
    "دکھاو": ["show"],
    "وکھاؤ": ["show"],
    "بند": ["freeze"],
    "منجمد": ["freeze"],
    "اپگریڈ": ["install", "--upgrade"],
    "اپ_گریڈ": ["install", "--upgrade"],
    "ڈاؤنلوڈ": ["download"],
    "ڈاؤن_لوڈ": ["download"],
}

def run_pip(args):
    return subprocess.run(
        [sys.executable, "-m", "pip"] + args
    ).returncode

def get_version():
    try:
        return version("supl-lang")
    except PackageNotFoundError:
        return "2.0.0"

def print_help():
    print("""════════════════════════════════════════════════════
  سرائیکی پیکیج مینیجر — النگو ڈویلپرز
════════════════════════════════════════════════════

استعمال:

  سرائیکی نصب <پیکیج>       پیکیج نصب کریں
  سرائیکی ہٹاؤ <پیکیج>      پیکیج ہٹائیں
  سرائیکی فہرست             نصب شدہ پیکیجز
  سرائیکی ڈکھاؤ <پیکیج>     پیکیج کی تفصیل
  سرائیکی بند               پیکیجز کی فہرست محفوظ کریں
  سرائیکی اپگریڈ <پیکیج>    پیکیج اپ گریڈ کریں
  سرائیکی ڈاؤنلوڈ <پیکیج>   صرف ڈاؤن لوڈ کریں

انگریزی کمانڈز بھی معاون ہیں:

  سرائیکی install
  سرائیکی uninstall
  سرائیکی list
  سرائیکی show
  سرائیکی freeze

════════════════════════════════════════════════════
""")

def main():
    args = sys.argv[1:]

    if not args:
        return run_pip([])

    cmd = args[0]
    rest = args[1:]

    if cmd in ("--version", "-V", "نسخہ", "ورژن", "version"):
        print(
            f"سرائیکی پیکیج مینیجر v{get_version()} "
            "— النگو ڈویلپرز"
        )
        return run_pip(["--version"])

    if cmd in ("--help", "-h", "مدد", "help"):
        print_help()
        return 0

    if cmd in ("ڳولو", "ڳول", "تلاش", "search", "find"):
        print("pip search معاون نہیں۔ https://pypi.org استعمال کریں")
        return 2

    actual = COMMANDS.get(cmd, [cmd])

    return run_pip(actual + rest)

if __name__ == "__main__":
    sys.exit(main())
