"""Scan completed exercises -> XP, pixel XP bar, charts and README.

Usage:
    python progress.py              # run every exercise, update everything
    python progress.py --no-run     # do not execute exercises (all zero)
    python progress.py --no-charts  # skip matplotlib charts
"""

from __future__ import annotations

import argparse
from collections.abc import Sequence

import build_readme
from arsnel.assets import write_assets
from arsnel.progress_core import save, scan
from charts import progress_line, skill_radar


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Update ARSNEL progress.")
    parser.add_argument(
        "--no-run", action="store_true", help="do not execute exercises"
    )
    parser.add_argument(
        "--no-charts", action="store_true", help="skip chart generation"
    )
    args = parser.parse_args(argv)

    snapshot = scan(run=not args.no_run)
    save(snapshot)
    write_assets(snapshot)
    if not args.no_charts:
        skill_radar.main(snapshot=snapshot.to_dict())
        progress_line.main()
    build_readme.write(snapshot)
    level, rank = snapshot.level
    print(
        f"XP {snapshot.xp}/{snapshot.max_xp} ({snapshot.percent:.1f}%)  "
        f"LVL {level} {rank}  exercises "
        f"{snapshot.exercises_done}/{snapshot.exercises_total}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
