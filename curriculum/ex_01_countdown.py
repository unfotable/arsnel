"""Exercise 09.1 - A countdown iterator

Implement the iterator protocol by hand.

Run:  python ex_01_countdown.py
"""

from __future__ import annotations


class Countdown:
    """Iterate from ``start`` down to 1; can be iterated many times."""

    def __init__(self, start: int) -> None:
        self.start = start

    def __iter__(self) -> CountdownIterator:
        """Return a fresh iterator each time."""
        # TODO: return CountdownIterator(self.start).
        raise NotImplementedError("TODO: your turn")


class CountdownIterator:
    """Holds the state of one pass."""

    def __init__(self, current: int) -> None:
        self.current = current

    def __iter__(self) -> CountdownIterator:
        return self

    def __next__(self) -> int:
        """Return the next number or raise StopIteration at zero."""
        # TODO: stop when current <= 0, otherwise return and decrement.
        raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    countdown = Countdown(3)
    assert list(countdown) == [3, 2, 1]
    assert list(countdown) == [3, 2, 1], "must be re-iterable"
    assert list(Countdown(0)) == []
    it = iter(Countdown(1))
    assert next(it) == 1
    try:
        next(it)
    except StopIteration:
        pass
    else:
        raise AssertionError("should raise StopIteration when exhausted")


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_01_countdown: {exc!r}")
    print("PASS ex_01_countdown")
