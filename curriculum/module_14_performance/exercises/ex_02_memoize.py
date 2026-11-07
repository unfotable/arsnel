"""Exercise 14.2 - Write a memoize decorator

Cache results by arguments to turn O(2^n) into O(n).

Run:  python ex_02_memoize.py
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any


def memoize(func: Callable[[int], int]) -> Callable[[int], int]:
    """Cache ``func(n)`` results in a dict."""
    # TODO: create a dict, return a wrapper that looks up n before calling func.
    raise NotImplementedError("TODO: your turn")


calls = {"n": 0}


@memoize
def fib(n: int) -> int:
    """Fibonacci that counts how often it really computes."""
    calls["n"] += 1
    return n if n < 2 else fib(n - 1) + fib(n - 2)


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert fib(30) == 832040
    assert calls["n"] == 31, f"expected 31 computations, got {calls['n']}"
    assert fib(30) == 832040 and calls["n"] == 31, "second call must hit the cache"
    _unused: Any = None


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_02_memoize: {exc!r}")
    print("PASS ex_02_memoize")
