import arabic_reshaper
from bidi.algorithm import get_display

def fix_urdu_text(text):
    try:
        # حروف کو جوڑنا (Reshaping) اور دائیں سے بائیں ترتیب دینا (BiDi)
        reshaped_text = arabic_reshaper.reshape(text)
        bidi_text = get_display(reshaped_text)
        return bidi_text
    except Exception:
        return text

if __name__ == "__main__":
    sample = "خوش آمدید! SarakLuk فریم ورک تیار ہے۔"
    print(fix_urdu_text(sample))
