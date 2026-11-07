"""Exercise 18.1 - Longest streak

Extend the habit tracker with a longest-streak statistic.

Run:  python ex_01_streaks.py
"""

from __future__ import annotations

from datetime import date, timedelta


def longest_streak(dates: list[str]) -> int:
    """Longest run of consecutive calendar days in ISO date strings (0 if empty)."""
    # TODO: sort the unique days; count runs where each day is previous + 1 day.
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert longest_streak([]) == 0
    assert longest_streak(["2025-03-01"]) == 1
    assert longest_streak(["2025-03-03", "2025-03-01", "2025-03-02", "2025-03-05"]) == 3
    assert longest_streak(["2025-03-01", "2025-03-01"]) == 1
    assert longest_streak(["2025-02-28", "2025-03-01", "2024-02-28", "2024-02-29"]) == 2
    assert longest_streak(["2024-02-28", "2024-02-29", "2024-03-01"]) == 3


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_01_streaks: {exc!r}")
    print("PASS ex_01_streaks")
