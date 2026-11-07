"""Exercise 10.2 - A retry decorator factory

Write a decorator that takes an argument.

Run:  python ex_02_retry.py
"""

from __future__ import annotations

import functools
from collections.abc import Callable
from typing import Any


def retry(times: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Retry the wrapped function up to ``times`` attempts on any Exception.

    Re-raise the last exception if every attempt fails.
    """

    # TODO: return a decorator; inside its wrapper loop `times` times with try/except.
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    attempts: list[int] = []

    @retry(3)
    def flaky() -> str:
        attempts.append(1)
        if len(attempts) < 3:
            raise RuntimeError("not yet")
        return "ok"

    assert flaky() == "ok" and len(attempts) == 3

    @retry(2)
    def broken() -> None:
        raise KeyError("always")

    try:
        broken()
    except KeyError:
        pass
    else:
        raise AssertionError("the last exception must be re-raised")


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_02_retry: {exc!r}")
    print("PASS ex_02_retry")
