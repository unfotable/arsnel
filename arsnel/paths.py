"""Filesystem locations used across ARSNEL."""

from __future__ import annotations

from pathlib import Path

ROOT: Path = Path(__file__).resolve().parents[1]
CURRICULUM: Path = ROOT / "curriculum"
ASSETS: Path = ROOT / "assets"
CHARTS: Path = ASSETS / "charts"
SITE: Path = ROOT / "site"
STATE: Path = ROOT / ".arsnel"
README: Path = ROOT / "README.md"

PROGRESS_FILE: Path = STATE / "progress.json"
QUIZ_FILE: Path = STATE / "quiz_results.json"
