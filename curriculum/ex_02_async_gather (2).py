"""Exercise 11.2 - Async gather

Write coroutines and run them concurrently.

Run:  python ex_02_async_gather.py
"""

from __future__ import annotations

import asyncio


async def double_later(value: int, delay: float = 0.0) -> int:
    """Wait ``delay`` seconds (asyncio.sleep) then return ``value * 2``."""
    # TODO: await asyncio.sleep(delay) and return the doubled value.
    # --- solution ---
    await asyncio.sleep(delay)
    return value * 2
    # --- end ---


async def double_all(values: list[int]) -> list[int]:
    """Double every value concurrently; results keep the input order."""
    # TODO: asyncio.gather(*(double_later(v, ...) for v in values)).
    # --- solution ---
    results = await asyncio.gather(
        *(double_later(v, 0.01 * (5 - v % 5)) for v in values)
    )
    return list(results)
    # --- end ---


async def first_error(values: list[int]) -> str:
    """Return the message of the first ValueError raised for a negative value."""

    # TODO: gather with return_exceptions=True and inspect the results.
    # --- solution ---
    async def check_value(v: int) -> int:
        if v < 0:
            raise ValueError(f"negative: {v}")
        return v

    outcomes = await asyncio.gather(
        *(check_value(v) for v in values), return_exceptions=True
    )
    for outcome in outcomes:
        if isinstance(outcome, ValueError):
            return str(outcome)
    return "none"
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert asyncio.run(double_later(4)) == 8
    assert asyncio.run(double_all([1, 2, 3])) == [2, 4, 6]
    assert asyncio.run(double_all([])) == []
    assert asyncio.run(first_error([1, -2, -3])) == "negative: -2"
    assert asyncio.run(first_error([1, 2])) == "none"


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_02_async_gather: {exc!r}")
    print("PASS ex_02_async_gather")
