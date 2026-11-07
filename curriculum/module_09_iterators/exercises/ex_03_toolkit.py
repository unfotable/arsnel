"""Exercise 09.3 - itertools and functools toolkit

Solve small tasks with the standard iteration tools.

Run:  python ex_03_toolkit.py
"""

from __future__ import annotations

import itertools
from collections.abc import Callable, Iterable
from functools import partial, reduce
from operator import mul


def product_of(numbers: Iterable[int]) -> int:
    """Multiply all numbers (1 for an empty input)."""
    # TODO: reduce with operator.mul and an initial value of 1.
    raise NotImplementedError("TODO: your turn")


def make_power(exponent: int) -> Callable[[int], int]:
    """Return a function that raises its argument to ``exponent``."""
    # TODO: use functools.partial with pow.
    raise NotImplementedError("TODO: your turn")


def flatten(nested: Iterable[Iterable[int]]) -> list[int]:
    """Flatten one level of nesting."""
    # TODO: itertools.chain.from_iterable.
    raise NotImplementedError("TODO: your turn")


def pairs_summing_to(numbers: list[int], target: int) -> list[tuple[int, int]]:
    """Return all index-ordered pairs of values that add up to ``target``."""
    # TODO: iterate itertools.combinations(numbers, 2) and filter.
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert product_of([2, 3, 4]) == 24 and product_of([]) == 1
    cube = make_power(3)
    assert cube(3) == 27 and make_power(2)(5) == 25
    assert flatten([[1, 2], [], [3]]) == [1, 2, 3]
    assert pairs_summing_to([1, 2, 3, 4, 5], 6) == [(1, 5), (2, 4)]


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_03_toolkit: {exc!r}")
    print("PASS ex_03_toolkit")
