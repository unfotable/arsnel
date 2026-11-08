"""XP, ranks and the exercise scanner."""

from __future__ import annotations

import json
from pathlib import Path

from arsnel.badges import BADGES, rank_for
from arsnel.progress_core import (
    ModuleProgress,
    Snapshot,
    discover,
    load_history,
    run_exercise,
    save,
    scan,
)


def make_module(root: Path, passing: int, failing: int) -> None:
    folder = root / "module_01_demo" / "exercises"
    folder.mkdir(parents=True)
    for i in range(passing):
        (folder / f"ex_{i + 1:02d}_ok.py").write_text("print('PASS')\n")
    for i in range(failing):
        name = f"ex_{passing + i + 1:02d}_bad.py"
        (folder / name).write_text("raise SystemExit('FAIL')\n")


def test_ranks_are_monotonic() -> None:
    assert rank_for(0) == (1, "NOOB")
    levels = [rank_for(p)[0] for p in range(0, 101, 5)]
    assert levels == sorted(levels)
    assert rank_for(100)[1] == "ARSNEL MASTER"


def test_scan_without_running_is_all_zero(isolated_state: Path) -> None:
    snap = scan(run=False)
    assert snap.xp == 0
    assert snap.exercises_total == 59
    assert snap.max_xp == 970
    assert snap.percent == 0.0


def test_scan_counts_passing_exercises(tmp_path: Path, isolated_state: Path) -> None:
    make_module(tmp_path / "cur", passing=2, failing=1)
    snap = scan(tmp_path / "cur")
    module = snap.modules[0]
    assert (module.done, module.total) == (2, 3)
    assert snap.xp == 20
    assert not module.complete


def test_discover_ignores_foreign_folders(tmp_path: Path) -> None:
    make_module(tmp_path, 1, 0)
    (tmp_path / "notes").mkdir()
    assert list(discover(tmp_path)) == [1]


def test_run_exercise(tmp_path: Path) -> None:
    ok = tmp_path / "ok.py"
    ok.write_text("pass\n")
    bad = tmp_path / "bad.py"
    bad.write_text("raise SystemExit(3)\n")
    assert run_exercise(ok)
    assert not run_exercise(bad)


def test_module_complete_requires_quiz() -> None:
    done = ModuleProgress(number=1, done=3, total=3, quiz_best=None, quiz_passed=False)
    assert not done.complete
    done = ModuleProgress(number=1, done=3, total=3, quiz_best=80.0, quiz_passed=True)
    assert done.complete
    assert done.xp == done.max_xp == 50


def test_save_appends_history_only_on_change(isolated_state: Path) -> None:
    snap = Snapshot(timestamp="2026-01-01T00:00:00")
    snap.modules = [ModuleProgress(1, 1, 3, None, False)]
    save(snap)
    save(snap)
    assert len(load_history()) == 1
    snap.modules = [ModuleProgress(1, 2, 3, None, False)]
    save(snap)
    assert len(load_history()) == 2
    data = json.loads((isolated_state / "progress.json").read_text())
    assert data["xp"] == 20


def test_badges_unlock_with_progress() -> None:
    empty = Snapshot(timestamp="t").stats()
    assert not any(b.unlocked(empty) for b in BADGES)
    full = Snapshot(timestamp="t")
    full.modules = [
        ModuleProgress(number=n, done=3, total=3, quiz_best=100.0, quiz_passed=True)
        for n in range(19)
    ]
    stats = full.stats()
    assert sum(b.unlocked(stats) for b in BADGES) >= len(BADGES) - 2


def test_progress_cli_skips_timestamp_only_changes() -> None:
    from progress import unchanged

    old = {"timestamp": "a", "xp": 10, "modules": [{"number": 1, "done": 1}]}
    assert unchanged(old, {**old, "timestamp": "b"})
    assert not unchanged(old, {**old, "xp": 20})
    assert not unchanged(None, old)
