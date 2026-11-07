"""The repository must stay at least 97% Python (GitHub Linguist style)."""

from __future__ import annotations

from pathlib import Path

from arsnel.langstats import MIN_PYTHON_PERCENT, breakdown, python_percent


def test_repository_is_mostly_python() -> None:
    totals = breakdown()
    percent = python_percent()
    others = {k: v for k, v in totals.items() if k != "Python"}
    assert percent >= MIN_PYTHON_PERCENT, f"{percent:.2f}% Python; others: {others}"


def test_only_allowed_languages_are_counted() -> None:
    allowed = {"Python", "Makefile", "HTML", "CSS", "JavaScript"}
    assert set(breakdown()) <= allowed


def test_breakdown_rules(tmp_path: Path) -> None:
    (tmp_path / "a.py").write_text("x" * 90)
    (tmp_path / "b.css").write_text("x" * 10)
    (tmp_path / "notes.md").write_text("x" * 1000)  # prose is not counted
    (tmp_path / "data.json").write_text("x" * 1000)
    gen = tmp_path / "gen"
    gen.mkdir()
    (gen / "big.js").write_text("x" * 5000)
    (tmp_path / ".gitattributes").write_text("gen/** linguist-generated=true\n")
    totals = breakdown(tmp_path)
    assert totals == {"Python": 90, "CSS": 10}
    assert python_percent(tmp_path) == 90.0
