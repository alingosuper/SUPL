<div align="center">

<img src="assets/logo/alingo_logo.svg" alt="AlinGo Saraiki Logo" width="280" />

<h1>AlinGo Saraiki</h1>

<p><strong>دیسی پروگرامنگ لینگویج — سرائیکی، اردو، پنجابی</strong></p>

<p><em>Saraiki · Urdu · Punjabi Programming Language & Terminal Suite</em></p>

<p>
<img src="https://img.shields.io/badge/Version-1.0.1-success?style=for-the-badge" alt="Version" />
<img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License" />
<img src="https://img.shields.io/badge/Languages-Saraiki%20%7C%20Urdu%20%7C%20Punjabi-green?style=for-the-badge" alt="Languages" />
</p>

</div>

## 🚀 AlinGo — دیسی پروگرامنگ زبان اور ٹرمینل سوٹ

**AlinGo Saraiki** ایک منفرد اور کثیر اللسانی (Multilingual) پروگرامنگ زبان اور ٹرمینل ٹول کٹ ہے جسے خاص طور پر اردو، پنجابی اور سرائیکی بولنے والے ڈویلپرز کے لیے ٹرمیکس (Termux) اور لینوکس ماحول میں تیار کیا گیا ہے۔

اس کا مقصد معیاری لینوکس اور ڈویلپمنٹ کمانڈز کو اپنی مادری زبان کے آسان الفاظ کے ذریعے چلانا اور جدید ویب اسٹیک (Node.js, Go, HTML/CSS) کو دیسی رنگ دینا ہے۔

### 🌟 اہم خصوصیات (Features)

* **لائیو انٹرایکٹو شیل (REPL):** اردو اور دیسی کی ورڈز کے ساتھ لائیو کوڈنگ کا ماحول۔
* **دیسی لغت (Dictionary Engine):** JSON اور CSV پر مبنی بلٹ ان آف لائن لغت جس میں الفاظ تلاش کرنا، شامل کرنا اور حذف کرنا انتہائی آسان ہے۔
* **جدید ویب اور سرور ٹولز:** Node.js، Go، اور لوکل ویب سرور چلانے کے لیے دیسی شارٹ کٹس۔
* **پیکیج مینجمنٹ:** گلوبل انسٹالیشن (`pip install --editable .`) تاکہ کسی بھی فولڈر سے کمانڈز چلائی جا سکیں۔

### 📥 تنصیب (Installation)

پراجیکٹ کو کلون کرنے کے بعد ٹرمیکس یا ٹرمینل میں گلوبل انسٹال کرنے کے لیے درج ذیل کمانڈز چلائیں:

```bash
# 1. ریپوزٹری کلون کریں
git clone https://github.com/alingosuper/SUPL.git
cd SUPL

# 2. ایڈیٹیبل انسٹال کریں
pip install -e .

# 3. چیک کریں
saraiki -v
# لائیو شیل کھولیں
saraiki -i

# کوئی فائل چلائیں
saraiki hello.slk

# لغت میں لفظ تلاش کریں
saraiki تلاش کتاب

---

### مرحلہ 3: ایک ہی کمانڈ میں گٹ کمٹ اور پش

اب جب کہ آپ کی نئی `alingo_logo.svg` اور برانڈڈ `README.md` تیار ہیں، انہیں گٹ ہب پر اپ لوڈ کرنے کے لیے یہ کمانڈ چلائیں:

```bash
cd ~/SUPL

# پرانی "زمین آسمان" والی فائلیں صاف کریں (اگر موجود ہیں)
rm -f assets/branding/alingo-logo.svg
rm -f assets/branding/alingo-banner-dark.svg
rm -f assets/branding/alingo-icon.svg

# نئی فائلیں شامل کریں اور کمٹ کریں
git add assets/logo/alingo_logo.svg README.md
git commit -m "feat(branding): add custom high-fidelity SVG logo in official green/gold theme and update README"
git push origin main
