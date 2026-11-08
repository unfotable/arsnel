"""The ``arsnel`` command: one front door for learners.

    python -m arsnel              where am I and what is next?
    python -m arsnel next         your next exercise (or quiz)
    python -m arsnel check [N]    grade the exercises of module N (default: all)
    python -m arsnel quiz N       take the quiz for module N
    python -m arsnel modules      progress per module
    python -m arsnel status       XP, rank and totals

After ``pip install -e .`` the same commands work as ``arsnel next`` etc.
"""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from pathlib import Path

from arsnel import NAME, TAGLINE
from arsnel.ascii_art import xp_bar
from arsnel.manifest import MODULES, get_module
from arsnel.paths import CURRICULUM, ROOT
from arsnel.progress_core import (
    QUIZ_PASS,
    XP_EXERCISE,
    discover,
    load_quiz_results,
    run_exercise_detail,
    scan,
)

COMMANDS = "status  modules  next  check [N]  quiz N"


def _rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def _clean(message: str, path: Path) -> str:
    """Drop the redundant ``FAIL <stem>:`` prefix the exercise footer prints."""
    return message.removeprefix(f"FAIL {path.stem}: ")


def _quiz_passed(mid: str) -> bool:
    best = load_quiz_results().get(mid, {}).get("best")
    return isinstance(best, int | float) and best >= QUIZ_PASS


def cmd_status(curriculum: Path) -> int:
    """Print rank, XP bar and totals (runs the exercises to measure them)."""
    snap = scan(curriculum)
    level, rank = snap.level
    print(f"{NAME}  LVL {level}  {rank}")
    print(xp_bar(snap.percent, 40))
    print(
        f"XP {snap.xp}/{snap.max_xp}   exercises {snap.exercises_done}/"
        f"{snap.exercises_total}   quizzes {snap.quizzes_passed}/{len(MODULES)}"
    )
    return 0


def cmd_modules(curriculum: Path) -> int:
    """Print one line per module with exercise and quiz progress."""
    snap = scan(curriculum)
    done = {m.number: m for m in snap.modules}
    for meta in MODULES:
        item = done.get(meta.number)
        d, total = (item.done, item.total) if item else (0, 0)
        filled = round(10 * d / total) if total else 0
        bar = "█" * filled + "░" * (10 - filled)
        quiz = "quiz ✓" if item and item.quiz_passed else "quiz -"
        print(f"{meta.mid}  {meta.title[:44]:<44} {bar} {d}/{total}  {quiz}")
    return 0


def cmd_next(curriculum: Path) -> int:
    """Point at the first exercise that does not pass yet, else the next quiz."""
    for number, files in sorted(discover(curriculum).items()):
        if number >= len(MODULES):
            continue
        meta = get_module(number)
        for path in files:
            ok, message = run_exercise_detail(path)
            if ok:
                continue
            print(f"NEXT  {meta.prompt}  {meta.title}")
            print(f"  learn {_rel(path.parents[1] / 'README.md')}")
            print(f"  open  {_rel(path)}")
            print("  do    replace the '# TODO' with working code")
            print(f"  check python -m arsnel check {number}")
            print(f"  now   {_clean(message, path)}")
            return 0
        if not _quiz_passed(meta.mid):
            print(f"NEXT  {meta.prompt}  quiz time - all exercises pass")
            print(f"  run   python -m arsnel quiz {number}")
            return 0
    print("Every exercise and quiz passes. You are an ARSNEL MASTER.")
    return 0


def cmd_check(curriculum: Path, number: int | None) -> int:
    """Run exercises (one module or all) and print PASS/FAIL per file."""
    found = discover(curriculum)
    numbers = sorted(found) if number is None else [number]
    if number is not None and number not in found:
        print(f"no module {number:02d}; choose 0-{len(MODULES) - 1}")
        return 2
    failed = 0
    for n in numbers:
        files = found[n]
        passed = 0
        for path in files:
            ok, message = run_exercise_detail(path)
            passed += ok
            failed += not ok
            print(
                f"{'PASS' if ok else 'FAIL'}  {path.stem}"
                + ("" if ok else f"  {_clean(message, path)}")
            )
        print(
            f"module {n:02d}: {passed}/{len(files)} passed (+{passed * XP_EXERCISE} XP)"
        )
    if not failed:
        print("All clear. Run `python progress.py` to update your XP bar.")
    return 1 if failed else 0


def cmd_quiz(number: int) -> int:
    """Run the interactive quiz for module ``number``."""
    from arsnel.quizlib import run_quiz
    from content import load

    if not 0 <= number < len(MODULES):
        print(f"no module {number:02d}; choose 0-{len(MODULES) - 1}")
        return 2
    content = load(number)
    if content is None:
        print(f"module {number:02d} has no quiz")
        return 2
    return run_quiz(get_module(number), content.quiz)


def main(argv: Sequence[str] | None = None, curriculum: Path = CURRICULUM) -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(prog="arsnel", description=TAGLINE)
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("status", help="XP, rank and totals")
    sub.add_parser("modules", help="progress per module")
    sub.add_parser("next", help="your next exercise or quiz")
    check = sub.add_parser("check", help="grade exercises")
    check.add_argument(
        "module", nargs="?", type=int, help="module number (default: all)"
    )
    quiz = sub.add_parser("quiz", help="take a module quiz")
    quiz.add_argument("module", type=int, help="module number")
    args = parser.parse_args(argv)

    if args.command == "status":
        return cmd_status(curriculum)
    if args.command == "modules":
        return cmd_modules(curriculum)
    if args.command == "next":
        return cmd_next(curriculum)
    if args.command == "check":
        return cmd_check(curriculum, args.module)
    if args.command == "quiz":
        return cmd_quiz(args.module)
    print(f"{NAME}: {TAGLINE.replace('`', '')}\n")
    print(f"commands: {COMMANDS}\n")
    return cmd_next(curriculum)


if __name__ == "__main__":
    raise SystemExit(main())
