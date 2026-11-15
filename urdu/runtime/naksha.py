# SUPL Graphics & UI Engine — النگو ڈویلپرز
# سرائیکی گرافکس اور ویب UI ڈیزائننگ ماڈیول

class NakshaUI:
    def __init__(self, title="سرائیکی ویب UI"):
        self.title = title
        self.elements = []

    def صفحہ_شروع(self, title=None):
        if title:
            self.title = title
        self.elements.append(f"<!DOCTYPE html><html lang='skr'><head><meta charset='utf-8'><title>{self.title}</title><style>body {{ font-family: sans-serif; text-align: right; direction: rtl; background: #f4f4f9; padding: 20px; }} .btn {{ background: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; }}</style></head><body>")

    def بٹن_بناؤ(self, text, action=""):
        self.elements.append(f"<button class='btn' onclick='alert(\"{action}\")'>{text}</button><br><br>")

    def ڈبہ_بناؤ(self, text):
        self.elements.append(f"<div style='border: 2px solid #ccc; padding: 15px; margin: 10px; background: white; border-radius: 8px;'>{text}</div>")

    def سرخی_بناؤ(self, text, level=1):
        self.elements.append(f"<h{level}>{text}</h{level}>")

    def متن_لکھو(self, text):
        self.elements.append(f"<p>{text}</p>")

    def صفحہ_ختم(self):
        self.elements.append("</body></html>")

    def محفوظ_کرو(self, filename="naksha_out.html"):
        full_html = "\n".join(self.elements)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"✨ آپ کا ویب UI صفحہ کامیابی کے ساتھ '{filename}' کے طور پر محفوظ ہو گیا ہے!")

if __name__ == "__main__":
    ui = NakshaUI("سرائیکی زبردست ایپ")
    ui.صفحہ_شروع("النگو ڈویلپرز UI")
    ui.سرخی_بناؤ("خوش آمدید SUPL گرافکس میں!")
    ui.متن_لکھو("یہ گرافیکل انٹرفیس مکمل طور پر سرائیکی زبان میں تیار کیا گیا ہے۔")
    ui.بٹن_بناؤ("کلک کرو", "سلام سرائیکی دنیا!")
    ui.صفحہ_ختم()
    ui.محفوظ_کرو("مثال_صفحہ.html")
