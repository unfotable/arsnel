"""Exercise 07.2 - Safe parsing with exceptions

Use try/except/else to turn failures into values.

Run:  python ex_02_safe_parsing.py
"""

from __future__ import annotations


def parse_int(text: str, default: int | None = None) -> int | None:
    """Return ``int(text)`` or ``default`` when the text is not an integer."""
    # TODO: try int(text); on ValueError return the default.
    # --- solution ---
    try:
        return int(text)
    except ValueError:
        return default
    # --- end ---


def safe_divide(a: float, b: float) -> float | None:
    """Return ``a / b`` or ``None`` when dividing by zero."""
    # TODO: catch ZeroDivisionError and return None.
    # --- solution ---
    try:
        return a / b
    except ZeroDivisionError:
        return None
    # --- end ---


def sum_valid(items: list[str]) -> tuple[int, list[str]]:
    """Sum the integer strings; also return the strings that were invalid."""
    # TODO: use parse_int; collect invalid strings in order.
    # --- solution ---
    total = 0
    invalid: list[str] = []
    for item in items:
        value = parse_int(item)
        if value is None:
            invalid.append(item)
        else:
            total += value
    return total, invalid
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert parse_int("42") == 42 and parse_int("4x") is None
    assert parse_int("x", default=-1) == -1
    assert safe_divide(6, 3) == 2 and safe_divide(1, 0) is None
    assert sum_valid(["1", "two", "3", ""]) == (4, ["two", ""])


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_02_safe_parsing: {exc!r}")
    print("PASS ex_02_safe_parsing")
