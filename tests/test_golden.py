"""SUPL — Golden File Tests"""
import subprocess
from pathlib import Path
import re
import pytest

PROJECT_ROOT = Path(__file__).parent.parent
GOLDEN = Path(__file__).parent / "golden"

# Unicode RTL/LTR markers (Terminal display کے لیے) ہٹا دیں
BIDI_MARKERS = re.compile(r'[\u2066-\u2069\u200e\u200f\u202a-\u202e]')


def clean_output(text: str) -> str:
    """Bidirectional markers صاف کریں"""
    return BIDI_MARKERS.sub('', text)


@pytest.mark.parametrize("src_file", sorted(GOLDEN.glob("*.slk")))
def test_golden(src_file):
    if not src_file.exists():
        pytest.skip(f"فائل نہیں: {src_file}")

    result = subprocess.run(
        ["saraiki", str(src_file)],
        capture_output=True, text=True, encoding="utf-8",
        cwd=str(PROJECT_ROOT),
        timeout=30,
    )

    assert result.returncode == 0, f"پروگرام ناکام:\n{result.stderr}"

    # ─── markers صاف کریں ───
    actual = clean_output(result.stdout).strip()

    checks = [
        "شامل کیا گیا: اردو پروگرامنگ سیکھنا",
        "آئٹم نمبر: 0",
    ]

    for check in checks:
        assert check in actual, f"متوقع: '{check}' نہیں ملا۔\nActual (پہلے 500):\n{actual[:500]}"

    print(f"✓ Golden test پاس: {src_file.name}")
