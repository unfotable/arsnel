"""Exercise 10.1 - Count calls with a decorator

Write a decorator that keeps metadata with functools.wraps.

Run:  python ex_01_count_calls.py
"""

from __future__ import annotations

import functools
from collections.abc import Callable
from typing import Any


def count_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    """Wrap ``func`` so ``wrapper.calls`` counts invocations (keep its metadata)."""

    # TODO: define wrapper(*args, **kwargs), use @functools.wraps(func),
    # TODO: increment wrapper.calls before calling func, start it at 0.
    # --- solution ---
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        wrapper.calls += 1  # type: ignore[attr-defined]
        return func(*args, **kwargs)

    wrapper.calls = 0  # type: ignore[attr-defined]
    return wrapper
    # --- end ---


@count_calls
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert add.calls == 0  # type: ignore[attr-defined]
    assert add(1, 2) == 3 and add(b=5, a=1) == 6
    assert add.calls == 2  # type: ignore[attr-defined]
    assert add.__name__ == "add" and add.__doc__ == "Add two numbers."


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_01_count_calls: {exc!r}")
    print("PASS ex_01_count_calls")
