"""Exercise 09.2 - Generator functions

Write lazy generators with yield.

Run:  python ex_02_generators.py
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator


def fibonacci(limit: int) -> Iterator[int]:
    """Yield Fibonacci numbers while they are <= ``limit``."""
    # TODO: keep two variables and yield inside a while loop.
    raise NotImplementedError("TODO: your turn")


def chunked(items: Iterable[int], size: int) -> Iterator[list[int]]:
    """Yield lists of ``size`` items (the last one may be shorter)."""
    # TODO: fill a buffer list; yield it when full, and the leftovers at the end.
    raise NotImplementedError("TODO: your turn")


def running_total(items: Iterable[int]) -> Iterator[int]:
    """Yield the cumulative sum after each item."""
    # TODO: keep a total and yield it after adding each item.
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert list(fibonacci(30)) == [0, 1, 1, 2, 3, 5, 8, 13, 21]
    assert list(chunked(range(7), 3)) == [[0, 1, 2], [3, 4, 5], [6]]
    assert list(chunked([], 2)) == []
    assert list(running_total([1, 2, 3, 4])) == [1, 3, 6, 10]
    lazy = running_total(iter(range(10**9)))
    assert next(lazy) == 0 and next(lazy) == 1, "must be lazy"


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_02_generators: {exc!r}")
    print("PASS ex_02_generators")
