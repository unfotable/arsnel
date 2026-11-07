"""Shared fixtures: isolated state files and a parallel script runner."""

from __future__ import annotations

from collections.abc import Iterator
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pytest

from arsnel import progress_core, quizlib
from arsnel.manifest import MODULES
from arsnel.modcheck import missing_requirements, run_script
from arsnel.paths import CURRICULUM


@pytest.fixture
def isolated_state(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[Path]:
    """Redirect progress/quiz state files into ``tmp_path``."""
    quiz = tmp_path / "quiz_results.json"
    monkeypatch.setattr(quizlib, "QUIZ_FILE", quiz)
    monkeypatch.setattr(progress_core, "QUIZ_FILE", quiz)
    monkeypatch.setattr(progress_core, "STATE", tmp_path)
    monkeypatch.setattr(progress_core, "PROGRESS_FILE", tmp_path / "progress.json")
    monkeypatch.setattr(progress_core, "HISTORY_FILE", tmp_path / "history.json")
    yield tmp_path


def _collect() -> list[Path]:
    paths: list[Path] = []
    for meta in MODULES:
        base = CURRICULUM / meta.dirname
        paths += sorted((base / "examples").glob("*.py"))
        paths += sorted((base / "solutions").glob("ex_*.py"))
        paths += sorted((base / "exercises").glob("ex_*.py"))
    return paths


@pytest.fixture(scope="session")
def script_results() -> dict[Path, tuple[int, str] | None]:
    """Run every curriculum script once, in parallel. ``None`` = skipped."""
    paths = _collect()

    def job(path: Path) -> tuple[int, str] | None:
        if missing_requirements(path):
            return None
        return run_script(path)

    with ThreadPoolExecutor(max_workers=8) as pool:
        return dict(zip(paths, pool.map(job, paths), strict=True))
