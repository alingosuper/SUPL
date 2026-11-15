# -*- coding: utf-8 -*-
"""supl.interpreter — cli.py کے لیے رَیپر (اصل انٹرپریٹر root پر موجود ہے)"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def run_file(path: str) -> int:
    from lexer.lexer import Lexer
    from parser.parser import Parser
    from interpreter import Interpreter
    code = Path(path).read_text(encoding="utf-8")
    Interpreter(Parser(Lexer(code))).interpret()
    return 0


def run_repl() -> int:
    from cli import run_interactive_repl
    run_interactive_repl()
    return 0
