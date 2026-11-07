"""Exercise 05.2 - Closures: counters and compose

Use nonlocal and functions that return functions.

Run:  python ex_02_make_counter.py
"""

from __future__ import annotations

from collections.abc import Callable


def make_counter(start: int = 0, step: int = 1) -> Callable[[], int]:
    """Return a function that returns start, start+step, ... on each call."""
    # TODO: keep the count in the enclosing scope and update it with nonlocal.
    # --- solution ---
    count = start - step

    def counter() -> int:
        nonlocal count
        count += step
        return count

    return counter
    # --- end ---


def compose(*funcs: Callable[[int], int]) -> Callable[[int], int]:
    """Return f(x) = funcs[-1](...funcs[1](funcs[0](x))) - apply left to right."""

    # TODO: return a function that feeds x through every function in order.
    # --- solution ---
    def composed(x: int) -> int:
        for func in funcs:
            x = func(x)
        return x

    return composed
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    a, b = make_counter(), make_counter(10, 5)
    assert [a(), a(), a()] == [0, 1, 2]
    assert [b(), b()] == [10, 15]
    assert a() == 3, "counters must keep independent state"
    add_one = lambda n: n + 1  # noqa: E731
    double = lambda n: n * 2  # noqa: E731
    assert compose(add_one, double)(5) == 12
    assert compose(double, add_one)(5) == 11
    assert compose()(7) == 7


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_02_make_counter: {exc!r}")
    print("PASS ex_02_make_counter")
