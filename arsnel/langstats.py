"""Approximate GitHub Linguist's language breakdown for this repository.

Linguist counts only *programming* and *markup* languages; prose (Markdown) and
data (YAML, JSON, TOML, SVG ...) are excluded, and ``linguist-generated`` paths
from ``.gitattributes`` are skipped. This module reproduces those rules so the
ratio can be shown in a chart and enforced by a test. It is an approximation of
Linguist, not Linguist itself.
"""

from __future__ import annotations

import fnmatch
from collections import Counter
from pathlib import Path

from arsnel.paths import ROOT

COUNTED_EXT = {
    ".py": "Python",
    ".html": "HTML",
    ".htm": "HTML",
    ".css": "CSS",
    ".js": "JavaScript",
    ".sh": "Shell",
    ".ps1": "PowerShell",
    ".ipynb": "Jupyter Notebook",
    ".j2": "Jinja",
}
COUNTED_NAMES = {"Makefile": "Makefile", "Dockerfile": "Dockerfile"}
SKIP_DIRS = {
    ".git",
    ".scratch",
    "__pycache__",
    ".mypy_cache",
    ".ruff_cache",
    ".pytest_cache",
    ".venv",
    "venv",
    "node_modules",
    "build",
    "dist",
}
MIN_PYTHON_PERCENT = 97.0


def generated_patterns(root: Path = ROOT) -> list[str]:
    """Return the linguist-generated/vendored globs from ``.gitattributes``."""
    attrs = root / ".gitattributes"
    if not attrs.exists():
        return []
    patterns: list[str] = []
    for line in attrs.read_text(encoding="utf-8").splitlines():
        parts = line.split()
        if len(parts) >= 2 and any(
            p.startswith(("linguist-generated", "linguist-vendored"))
            and "=false" not in p
            for p in parts[1:]
        ):
            patterns.append(parts[0])
    return patterns


def _skipped(rel: Path, patterns: list[str]) -> bool:
    text = rel.as_posix()
    return any(
        fnmatch.fnmatch(text, pat) or text.startswith(pat.rstrip("*").rstrip("/") + "/")
        for pat in patterns
    )


def breakdown(root: Path = ROOT) -> Counter[str]:
    """Return ``{language: bytes}`` for the files Linguist would count."""
    patterns = generated_patterns(root)
    totals: Counter[str] = Counter()
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if any(part in SKIP_DIRS or part.endswith(".egg-info") for part in rel.parts):
            continue
        if _skipped(rel, patterns):
            continue
        language = COUNTED_NAMES.get(path.name) or COUNTED_EXT.get(path.suffix.lower())
        if language:
            totals[language] += path.stat().st_size
    return totals


def python_percent(root: Path = ROOT) -> float:
    """Share of counted bytes that are Python, as a percentage."""
    totals = breakdown(root)
    total = sum(totals.values())
    return 100.0 * totals["Python"] / total if total else 0.0
