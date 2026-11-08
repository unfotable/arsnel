"""Scan completed exercises -> XP, pixel XP bar, charts and README.

Usage:
    python progress.py              # run every exercise, update everything
    python progress.py --no-run     # do not execute exercises (all zero)
    python progress.py --no-charts  # skip matplotlib charts
    python progress.py --force      # rewrite everything even if nothing changed

When no exercise or quiz result changed since the last run, nothing is written,
so CI does not create empty "progress" commits.
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from typing import Any

import build_readme
from arsnel.assets import write_assets
from arsnel.paths import PROGRESS_FILE
from arsnel.progress_core import Snapshot, save, scan
from charts import progress_line, skill_radar


def unchanged(previous: dict[str, Any] | None, current: dict[str, Any]) -> bool:
    """True when two snapshots differ only by their timestamp."""
    if previous is None:
        return False
    strip = {"timestamp"}
    return {k: v for k, v in previous.items() if k not in strip} == {
        k: v for k, v in current.items() if k not in strip
    }


def _previous() -> dict[str, Any] | None:
    try:
        data = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    return data if isinstance(data, dict) else None


def summary(snapshot: Snapshot) -> str:
    """One-line progress summary for the terminal."""
    level, rank = snapshot.level
    return (
        f"XP {snapshot.xp}/{snapshot.max_xp} ({snapshot.percent:.1f}%)  "
        f"LVL {level} {rank}  exercises "
        f"{snapshot.exercises_done}/{snapshot.exercises_total}"
    )


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Update ARSNEL progress.")
    parser.add_argument(
        "--no-run", action="store_true", help="do not execute exercises"
    )
    parser.add_argument(
        "--no-charts", action="store_true", help="skip chart generation"
    )
    parser.add_argument(
        "--force", action="store_true", help="rewrite files even if nothing changed"
    )
    args = parser.parse_args(argv)

    snapshot = scan(run=not args.no_run)
    if not args.force and unchanged(_previous(), snapshot.to_dict()):
        print(f"{summary(snapshot)}  (no change, nothing written)")
        return 0
    save(snapshot)
    write_assets(snapshot)
    if not args.no_charts:
        skill_radar.main(snapshot=snapshot.to_dict())
        progress_line.main()
    build_readme.write(snapshot)
    print(summary(snapshot))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
