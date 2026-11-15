"""
╔══════════════════════════════════════════════════════╗
║         اردو پروگرامنگ لینگویج                        ║
║         Urdu Programming Language                      ║
╠══════════════════════════════════════════════════════╣
║  Developer : AlinGo Developers                   ║
║  Version   : 1.0.1                                     ║
║  Platform  : Windows | Linux | macOS                   ║
║  License   : UPL-1.0                                   ║
╚══════════════════════════════════════════════════════╝
"""

VERSION = "1.0.1"
VERSION_TUPLE = (1, 0, 1)
DEVELOPER = "AlinGo Developers"
LANGUAGE_NAME = "اردو پروگرامنگ لینگویج"
LANGUAGE_NAME_EN = "Urdu Programming Language"
RELEASE_DATE = "2026-05-28"


def version_info() -> str:
    line = "=" * 56
    info = [
        line,
        "  Urdu Programming Language",
        f"  (Urdu: اردو پروگرامنگ لینگویج)",
        line,
        f"  Version   : {VERSION}",
        f"  Developer : {DEVELOPER}",
        f"  Released  : {RELEASE_DATE}",
        "  Platform  : Windows | Linux | macOS",
        "  Features  : OOP | Async | GUI | ML | DB | Web | Threads | TensorBoard | Arduino | DataStructures | Algorithms | Text",
        "  License   : UPL-1.0",
        line,
    ]
    return "\n".join(info)


__version__ = VERSION
__author__ = DEVELOPER
__all__ = ["VERSION", "DEVELOPER", "LANGUAGE_NAME", "version_info"]
