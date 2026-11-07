"""Run every curriculum script: examples work, solutions pass, stubs fail."""

from __future__ import annotations

from pathlib import Path

import pytest

from arsnel.manifest import MODULES
from arsnel.paths import CURRICULUM

Results = dict[Path, tuple[int, str] | None]


def _paths(folder: str, pattern: str) -> list[Path]:
    found: list[Path] = []
    for meta in MODULES:
        found += sorted((CURRICULUM / meta.dirname / folder).glob(pattern))
    return found


def _id(path: Path) -> str:
    return f"{path.parents[1].name}/{path.name}"


@pytest.mark.parametrize("path", _paths("examples", "*.py"), ids=_id)
def test_example_runs(path: Path, script_results: Results) -> None:
    result = script_results[path]
    if result is None:
        pytest.skip("optional third-party package not installed")
        return
    assert result[0] == 0, result[1]


@pytest.mark.parametrize("path", _paths("solutions", "ex_*.py"), ids=_id)
def test_solution_passes(path: Path, script_results: Results) -> None:
    result = script_results[path]
    if result is None:
        pytest.skip("optional third-party package not installed")
        return
    assert result[0] == 0, result[1]
    assert "PASS" in result[1]


@pytest.mark.parametrize("path", _paths("exercises", "ex_*.py"), ids=_id)
def test_stub_fails_until_solved(path: Path, script_results: Results) -> None:
    result = script_results[path]
    if result is None:
        pytest.skip("optional third-party package not installed")
        return
    assert result[0] != 0, "stub passes without being solved"
    assert "TODO" in path.read_text(encoding="utf-8")
