"""Exercise 14.1 - Binary search

Find an item in a sorted list in O(log n) steps.

Run:  python ex_01_binary_search.py
"""

from __future__ import annotations


def binary_search(items: list[int], target: int) -> tuple[int, int]:
    """Return ``(index, steps)``; index is -1 when ``target`` is missing.

    ``steps`` counts loop iterations and must stay <= log2(n) + 1.
    """
    # TODO: keep low/high bounds, check the middle, halve the range each step.
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    data = list(range(0, 2000, 2))
    assert binary_search(data, 0)[0] == 0
    assert binary_search(data, 1998)[0] == 999
    assert binary_search(data, 7)[0] == -1
    assert binary_search([], 1) == (-1, 0)
    _, steps = binary_search(data, 1998)
    assert steps <= 11, f"too many steps: {steps} (is it really halving?)"


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_01_binary_search: {exc!r}")
    print("PASS ex_01_binary_search")
