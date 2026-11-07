"""Exercise 02.2 - Leap years and grades

Combine and/or with if/elif chains.

Run:  python ex_02_leap_year_and_grade.py
"""

from __future__ import annotations


def is_leap_year(year: int) -> bool:
    """Divisible by 4, except centuries, unless divisible by 400."""
    # TODO: combine the three rules with and/or.
    # --- solution ---
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    # --- end ---


def letter_grade(score: float) -> str:
    """90+ A, 80+ B, 70+ C, 60+ D, otherwise F; raise ValueError outside 0..100."""
    # TODO: validate the range first, then use an if/elif chain.
    # --- solution ---
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    for cutoff, letter in ((90, "A"), (80, "B"), (70, "C"), (60, "D")):
        if score >= cutoff:
            return letter
    return "F"
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert [is_leap_year(y) for y in (1900, 2000, 2023, 2024)] == [
        False,
        True,
        False,
        True,
    ]
    assert [letter_grade(s) for s in (100, 90, 89.9, 70, 60, 12)] == list("AABCDF")
    try:
        letter_grade(101)
    except ValueError:
        pass
    else:
        raise AssertionError("101 must raise ValueError")


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_02_leap_year_and_grade: {exc!r}")
    print("PASS ex_02_leap_year_and_grade")
