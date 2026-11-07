"""ARSNEL > module_16 quiz.  Run:  python quiz.py"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from arsnel.manifest import get_module
from arsnel.quizlib import run_quiz
from content.module_16 import CONTENT

if __name__ == "__main__":
    raise SystemExit(run_quiz(get_module(16), CONTENT.quiz))
