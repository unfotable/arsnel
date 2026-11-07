"""Capstone 1: a habit tracker CLI (argparse + JSON persistence + pure logic).

Run ``python capstone_1_cli_tool.py`` for a scripted demo in a temp folder.
"""

import argparse
import json
import tempfile
from collections.abc import Sequence
from datetime import date, timedelta
from pathlib import Path

Data = dict[str, list[str]]


def current_streak(dates: list[str], today: date) -> int:
    """Consecutive checked days ending today (or yesterday: the streak is alive)."""
    days = {date.fromisoformat(d) for d in dates}
    cursor = today if today in days else today - timedelta(days=1)
    streak = 0
    while cursor in days:
        streak += 1
        cursor -= timedelta(days=1)
    return streak


def load(path: Path) -> Data:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def save(path: Path, data: Data) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="habits")
    parser.add_argument("--file", type=Path, required=True)
    parser.add_argument("--today", type=date.fromisoformat, default=date.today())
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("add", "check", "streak"):
        sub.add_parser(name).add_argument("habit")
    sub.add_parser("list")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    data = load(args.file)
    if args.command == "add":
        data.setdefault(args.habit, [])
        print(f"tracking {args.habit}")
    elif args.command == "list":
        for habit in sorted(data):
            print(f"{habit}: {len(data[habit])} check-ins")
    elif args.habit not in data:
        print(f"unknown habit: {args.habit}")
        return 1
    elif args.command == "check":
        if args.today.isoformat() not in data[args.habit]:
            data[args.habit].append(args.today.isoformat())
        print(f"checked {args.habit} for {args.today}")
    else:
        print(f"{args.habit} streak: {current_streak(data[args.habit], args.today)}")
    save(args.file, data)
    return 0


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        store = str(Path(tmp) / "habits.json")
        script = [("2025-03-01", ["add", "read"])]
        script += [(f"2025-03-0{d}", ["check", "read"]) for d in (1, 2, 3)]
        script += [
            ("2025-03-03", ["streak", "read"]),
            ("2025-03-06", ["streak", "read"]),
            ("2025-03-06", ["list"]),
        ]
        for today, command in script:
            print(f"$ habits {' '.join(command)}   (today={today})")
            main(["--file", store, "--today", today, *command])
