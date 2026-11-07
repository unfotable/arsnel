"""Scan completed exercises and quizzes and turn them into XP.

An exercise counts as *completed* when ``python exercises/<file>.py`` exits 0
(its built-in ``check()`` passes). Stubs always fail until the TODO is solved.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections.abc import Sequence
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from arsnel.badges import Stats, rank_for
from arsnel.paths import CURRICULUM, PROGRESS_FILE, QUIZ_FILE, ROOT, STATE

XP_EXERCISE = 10
XP_QUIZ = 20
QUIZ_PASS = 70.0
HISTORY_FILE: Path = STATE / "history.json"
_DIR_RE = re.compile(r"^module_(\d{2})_")


@dataclass
class ModuleProgress:
    """Progress inside one module."""

    number: int
    done: int
    total: int
    quiz_best: float | None
    quiz_passed: bool

    @property
    def complete(self) -> bool:
        """All exercises pass and the quiz is passed."""
        return self.total > 0 and self.done == self.total and self.quiz_passed

    @property
    def xp(self) -> int:
        """XP earned in this module."""
        return self.done * XP_EXERCISE + (XP_QUIZ if self.quiz_passed else 0)

    @property
    def max_xp(self) -> int:
        """XP available in this module."""
        return self.total * XP_EXERCISE + XP_QUIZ


@dataclass
class Snapshot:
    """A point-in-time view of the learner's progress."""

    timestamp: str
    modules: list[ModuleProgress] = field(default_factory=list)

    @property
    def xp(self) -> int:
        return sum(m.xp for m in self.modules)

    @property
    def max_xp(self) -> int:
        return sum(m.max_xp for m in self.modules)

    @property
    def percent(self) -> float:
        return 100.0 * self.xp / self.max_xp if self.max_xp else 0.0

    @property
    def exercises_done(self) -> int:
        return sum(m.done for m in self.modules)

    @property
    def exercises_total(self) -> int:
        return sum(m.total for m in self.modules)

    @property
    def quizzes_passed(self) -> int:
        return sum(1 for m in self.modules if m.quiz_passed)

    @property
    def level(self) -> tuple[int, str]:
        return rank_for(self.percent)

    def stats(self) -> Stats:
        """Convert to the :class:`~arsnel.badges.Stats` that badge rules use."""
        done = frozenset(m.number for m in self.modules if m.complete)
        return Stats(
            percent=self.percent,
            exercises_done=self.exercises_done,
            quizzes_passed=self.quizzes_passed,
            modules_done=done,
            total_quizzes=len(self.modules),
            all_done=bool(self.modules) and len(done) == len(self.modules),
        )

    def to_dict(self) -> dict[str, Any]:
        """JSON-serialisable form."""
        level, title = self.level
        return {
            "timestamp": self.timestamp,
            "xp": self.xp,
            "max_xp": self.max_xp,
            "percent": round(self.percent, 2),
            "level": level,
            "rank": title,
            "exercises_done": self.exercises_done,
            "exercises_total": self.exercises_total,
            "quizzes_passed": self.quizzes_passed,
            "modules": [asdict(m) for m in self.modules],
        }


def discover(root: Path = CURRICULUM) -> dict[int, list[Path]]:
    """Map module number -> its ``exercises/ex_*.py`` files."""
    found: dict[int, list[Path]] = {}
    for module_dir in sorted(root.glob("module_*")):
        match = _DIR_RE.match(module_dir.name)
        if match:
            found[int(match.group(1))] = sorted(
                (module_dir / "exercises").glob("ex_*.py")
            )
    return found


def run_exercise(path: Path, timeout: float = 30.0) -> bool:
    """Run one exercise file; ``True`` when it exits 0."""
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    try:
        proc = subprocess.run(
            [sys.executable, path.name],
            cwd=path.parent,
            env=env,
            stdin=subprocess.DEVNULL,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
    except (subprocess.TimeoutExpired, OSError):
        return False
    return proc.returncode == 0


def load_quiz_results(path: Path | None = None) -> dict[str, Any]:
    """Read saved quiz scores (empty when none exist)."""
    try:
        data = json.loads((path or QUIZ_FILE).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return data if isinstance(data, dict) else {}


def scan(curriculum: Path = CURRICULUM, run: bool = True, workers: int = 8) -> Snapshot:
    """Scan every module. With ``run=False`` nothing is executed (all zero)."""
    exercises = discover(curriculum)
    quizzes = load_quiz_results()
    jobs = [(n, p) for n, files in exercises.items() for p in files]
    passed: dict[int, int] = dict.fromkeys(exercises, 0)
    if run and jobs:
        with ThreadPoolExecutor(max_workers=workers) as pool:
            for (number, _), ok in zip(
                jobs, pool.map(lambda j: run_exercise(j[1]), jobs), strict=True
            ):
                passed[number] += int(ok)
    snap = Snapshot(timestamp=datetime.now(UTC).isoformat(timespec="seconds"))
    for number, files in sorted(exercises.items()):
        best = quizzes.get(f"{number:02d}", {}).get("best")
        best_f = float(best) if best is not None else None
        snap.modules.append(
            ModuleProgress(
                number=number,
                done=passed[number],
                total=len(files),
                quiz_best=best_f,
                quiz_passed=best_f is not None and best_f >= QUIZ_PASS,
            )
        )
    return snap


def load_history(path: Path | None = None) -> list[dict[str, Any]]:
    """Read the saved progress history (oldest first)."""
    try:
        data = json.loads((path or HISTORY_FILE).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []
    return data if isinstance(data, list) else []


def save(snapshot: Snapshot) -> None:
    """Write ``progress.json`` and append to ``history.json`` when XP changed."""
    STATE.mkdir(parents=True, exist_ok=True)
    PROGRESS_FILE.write_text(
        json.dumps(snapshot.to_dict(), indent=2) + "\n", encoding="utf-8"
    )
    history = load_history()
    point = {
        "t": snapshot.timestamp,
        "xp": snapshot.xp,
        "percent": round(snapshot.percent, 2),
        "exercises": snapshot.exercises_done,
    }
    if not history or history[-1]["xp"] != point["xp"]:
        history.append(point)
        HISTORY_FILE.write_text(json.dumps(history, indent=2) + "\n", encoding="utf-8")


def main(argv: Sequence[str] | None = None) -> int:
    """CLI: print a progress summary (``arsnel-progress``)."""
    parser = argparse.ArgumentParser(description="Show ARSNEL progress.")
    parser.add_argument(
        "--no-run", action="store_true", help="do not execute exercises"
    )
    parser.add_argument("--json", action="store_true", help="print JSON")
    args = parser.parse_args(argv)
    snap = scan(run=not args.no_run)
    if args.json:
        print(json.dumps(snap.to_dict(), indent=2))
    else:
        level, title = snap.level
        print(f"XP {snap.xp}/{snap.max_xp} ({snap.percent:.1f}%)  LVL {level} {title}")
        print(
            f"exercises {snap.exercises_done}/{snap.exercises_total}  "
            f"quizzes {snap.quizzes_passed}/{len(snap.modules)}  root={ROOT.name}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
