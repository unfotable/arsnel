"""Charts render, bootstrap helpers behave."""

from __future__ import annotations

from pathlib import Path

import pytest

import bootstrap
from charts import (
    big_o,
    dependency_graph,
    language_donut,
    progress_line,
    roadmap,
    skill_radar,
)

CHART_MODULES = [roadmap, big_o, dependency_graph, skill_radar, language_donut]


@pytest.mark.parametrize("module", CHART_MODULES, ids=lambda m: m.__name__)
def test_chart_writes_png_and_svg(module: object, tmp_path: Path) -> None:
    files = module.main(out_dir=tmp_path)  # type: ignore[attr-defined]
    suffixes = {Path(f).suffix for f in files}
    assert suffixes == {".png", ".svg"}
    for file in files:
        assert Path(file).stat().st_size > 1000


def test_progress_line_with_history(tmp_path: Path) -> None:
    history: list[dict[str, object]] = [
        {"t": "2026-01-01T00:00:00", "xp": 0, "percent": 0.0, "exercises": 0},
        {"t": "2026-01-02T00:00:00", "xp": 120, "percent": 12.4, "exercises": 9},
    ]
    files = progress_line.main(out_dir=tmp_path, history=history)
    assert {Path(f).suffix for f in files} == {".png", ".svg"}


def test_progress_line_handles_empty_history(tmp_path: Path) -> None:
    assert progress_line.main(out_dir=tmp_path, history=[])


def test_skill_percentages_zero_for_empty_progress() -> None:
    values = skill_radar.skill_percentages(
        {"modules": [{"number": 1, "done": 0, "total": 3, "quiz_passed": False}]}
    )
    assert values and all(v == 0 for v in values)


def test_skill_percentages_reflect_xp() -> None:
    module = {"number": 1, "done": 3, "total": 3, "quiz_passed": True}
    values = skill_radar.skill_percentages({"modules": [module]})
    assert max(values) == 100.0


def test_bootstrap_paths() -> None:
    python = bootstrap.venv_python()
    assert python.parts[-3] == ".venv" or python.parts[-2] == ".venv"
    assert bootstrap.MIN_PYTHON == (3, 11)
