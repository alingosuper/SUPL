import json
from pathlib import Path

لغت_فائل = Path("سرائیکی.لغت")

لغت = json.loads(
    لغت_فائل.read_text(encoding="utf-8")
)

لفظ_فہرست = {}

for حصہ, الفاظ in لغت.items():
    for لفظ in الفاظ:
        لفظ_فہرست[لفظ] = حصہ

def لفظ_پہچانو(متن):
    نتائج = []

    for لفظ in sorted(
        لفظ_فہرست,
        key=len,
        reverse=True
    ):
        if لفظ in متن:
            نتائج.append({
                "لفظ": لفظ,
                "قسم": لفظ_فہرست[لفظ]
            })

    return نتائج

if __name__ == "__main__":
    print("سرائیکی لفظ شناس نظام تیار اے")
    print("کوئی سرائیکی کمانڈ لکھو:")
    
    while True:
        متن = input("سرائیکی > ")

        if متن == "بند کرو":
            print("نظام بند تھی ڳیا")
            break

        for نتیجہ in لفظ_پہچانو(متن):
            print(
                نتیجہ["لفظ"],
                "—",
                نتیجہ["قسم"]
            )
