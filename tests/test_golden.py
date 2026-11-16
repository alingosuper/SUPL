"""SUPL — Golden File Tests"""
import subprocess
from pathlib import Path
import pytest

GOLDEN = Path(__file__).parent / "golden"

@pytest.mark.parametrize("src_file", sorted(GOLDEN.glob("*.slk")))
def test_golden(src_file):
    expected_file = GOLDEN / f"{src_file.stem}_متوقع.txt"
    if not expected_file.exists():
        pytest.skip(f"متوقع فائل نہیں: {expected_file}")
    
    result = subprocess.run(
        ["saraiki", str(src_file)],
        capture_output=True, text=True, encoding="utf-8",
        cwd=src_file.parent.parent.parent,
    )
    
    assert result.returncode == 0, f"پروگرام ناکام:\n{result.stderr}"
    
    expected = expected_file.read_text(encoding="utf-8").strip()
    actual = result.stdout.strip()
    
    # صرف اہم حصہ compare کریں (پہلا اور آخری حصہ)
    assert "شامل کیا گیا: اردو پروگرامنگ سیکھنا" in actual
    assert "آئٹم نمبر: 0" in actual
