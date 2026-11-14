import re
import sys
from pathlib import Path

متغیر = {}

def پروگرام_چلاؤ(فائل):
    سطراں = Path(فائل).read_text(
        encoding="utf-8"
    ).splitlines()

    شروع_تھیا = False
    مکمل_تھیا = False

    for نمبر, سطر in enumerate(سطراں, 1):
        سطر = سطر.strip()

        if not سطر:
            continue

        if سطر.startswith("پندھ شروع"):
            if شروع_تھیا:
                raise ValueError("پندھ پہلے شروع تھی چکیا اے")
            شروع_تھیا = True
            continue

        if سطر == "پندھ مک گیا":
            مکمل_تھیا = True
            break

        if not شروع_تھیا:
            raise ValueError(f"لائن {نمبر}: پندھ شروع کرو")

        عدد = re.fullmatch(
            r"عدد\s+([^\s=]+)\s*=\s*(-?\d+(?:\.\d+)?)",
            سطر
        )

        if عدد:
            ناں, قدر = عدد.groups()
            متغیر[اں] = (
                float(قدر) if "." in قدر else int(قدر)
            )
            continue

        لکھو = re.fullmatch(r"لکھو\s+(.+)", سطر)

        if لکھو:
            قدر = لکھو.group(1).strip()

            if قدر.startswith('"') and قدر.endswith('"'):
                print(قدر[1:-1])
            elif قدر in متغیر:
                print(متغیر[قدر])
            else:
                raise ValueError(
                    f"لائن {نمبر}: ایہہ ناں موجود کائنی: {قدر}"
                )
            continue

        raise ValueError(
            f"لائن {نمبر}: نامعلوم کمانڈ: {سطر}"
        )

    if not شروع_تھیا:
        raise ValueError("پندھ شروع کائنی تھیا")

    if not مکمل_تھیا:
        raise ValueError("پندھ مک گیا کمانڈ موجود کائنی")

    print("پندھ مک گیا")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("استعمال: تشریح_کار.py پروگرام.slk")
        sys.exit(1)

    try:
        پروگرام_چلاؤ(sys.argv[1])
    except Exception as خرابی:
        print("خرابی:", خرابی)
        sys.exit(1)
