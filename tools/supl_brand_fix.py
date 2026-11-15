from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path.cwd()
BACKUP = ROOT.parent / (
    "SUPL-backup-" + datetime.now().strftime("%Y%m%d-%H%M%S")
)

changes = {
    "setup.py": [
        ('name="sarakluk"', 'name="supl-lang"'),
        ('description="AlinGo -', 'description="SUPL -'),
        ('author="Alango Developers"', 'author="AlinGo Developers"'),
    ],
    "README.md": [
        ('# AlinGo (SUPL)', '# SUPL'),
        ('**AlinGo (SUPL)**', '**SUPL**'),
    ],
    "LICENSE": [
        ('سرائیکی پروگرامنگ زبان (AlinGo)', 'SUPL پروگرامنگ زبان'),
        ('پراجیکٹ: AlinGo (سرائیکی پروگرامنگ زبان)',
         'پراجیکٹ: SUPL (سرائیکی پروگرامنگ زبان)'),
        ('Alango Developers', 'AlinGo Developers'),
    ],
    "interpreter.py": [
        ('# AlinGo Interpreter', '# SUPL Interpreter'),
        ('sarakluk_out.html', 'supl_out.html'),
    ],
    "lexer/tokens.py": [
        ('# AlinGo Tokens', '# SUPL Tokens'),
    ],
    "lexer/lexer.py": [
        ('# AlinGo Lexer', '# SUPL Lexer'),
    ],
    "parser/parser.py": [
        ('# AlinGo Parser', '# SUPL Parser'),
    ],
    "urdu/runtime/naksha.py": [
        ('# AlinGo Graphics', '# SUPL Graphics'),
        ('AlinGo گرافکس', 'SUPL گرافکس'),
    ],
    "cli.py": [
        ('AlinGo CLI', 'SUPL CLI'),
        ('AlinGo — لائیو', 'SUPL — لائیو'),
        ('AlinGo شیل', 'SUPL شیل'),
        ('AlinGo (سرائیکی', 'SUPL (سرائیکی'),
        ('AlinGo v{VERSION}', 'SUPL v{VERSION}'),
        ('Alango Developers', 'AlinGo Developers'),
    ],
    "security/suraksha.py": [
        ('# AlinGo Security', '# SUPL Security'),
    ],
    "test_security.py": [
        ('# AlinGo Security', '# SUPL Security'),
    ],
    "help_supl.py": [
        ('AlinGo / SUPL', 'SUPL'),
        ('Alango Developers', 'AlinGo Developers'),
    ],
    "rtl_helper.py": [
        ('AlinGo فریم ورک', 'SUPL فریم ورک'),
    ],
    "bhooj_dictionary.py": [
        ('AlinGo ایک کثیر اللسانی', 'SUPL ایک کثیر اللسانی'),
    ],
    "show_dictionary.py": [
        ('AlinGo دیسی لغت', 'SUPL دیسی لغت'),
    ],
    "supl/cli.py": [
        ('AlinGo v1.0.0', 'SUPL v1.0.0'),
        ('AlinGo (SUPL)', 'SUPL'),
    ],
    ".gitignore": [
        ('AlinGo compilation cache', 'SUPL compilation cache'),
    ],
    "ui_مثال.slk": [
        ('AlinGo سرائیکی زبان', 'SUPL سرائیکی زبان'),
    ],
    "مثال_صفحہ.html": [
        ('AlinGo گرافکس', 'SUPL گرافکس'),
    ],
    "urdu/__init__.py": [
        ('Alango Developers', 'AlinGo Developers'),
    ],
}

BACKUP.mkdir(parents=True, exist_ok=True)

for filename, replacements in changes.items():
    path = ROOT / filename

    if not path.is_file():
        print("SKIP:", filename)
        continue

    original = path.read_text(encoding="utf-8")
    updated = original

    for old, new in replacements:
        updated = updated.replace(old, new)

    if updated != original:
        target = BACKUP / filename
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        path.write_text(updated, encoding="utf-8")
        print("UPDATED:", filename)

print("\nBackup created:", BACKUP)
print("Brand correction finished.")
