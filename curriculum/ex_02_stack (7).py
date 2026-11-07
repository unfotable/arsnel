"""Exercise 12.2 - A tested Stack

Implement the class that the tests describe, including errors.

Run:  python ex_02_stack.py
"""

from __future__ import annotations


class EmptyStackError(Exception):
    """Raised when popping or peeking an empty stack."""


class Stack:
    """A last-in, first-out stack."""

    def __init__(self) -> None:
        self._items: list[int] = []

    def push(self, item: int) -> None:
        """Add ``item`` on top."""
        # TODO: append to the list.
        # --- solution ---
        self._items.append(item)
        # --- end ---

    def pop(self) -> int:
        """Remove and return the top item; raise EmptyStackError when empty."""
        # TODO: guard the empty case, then pop.
        # --- solution ---
        if not self._items:
            raise EmptyStackError("pop from empty stack")
        return self._items.pop()
        # --- end ---

    def peek(self) -> int:
        """Return the top item without removing it."""
        # TODO: same guard as pop.
        # --- solution ---
        if not self._items:
            raise EmptyStackError("peek at empty stack")
        return self._items[-1]
        # --- end ---

    def __len__(self) -> int:
        return len(self._items)


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    stack = Stack()
    assert len(stack) == 0
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2 and len(stack) == 2
    assert stack.pop() == 2 and stack.pop() == 1 and len(stack) == 0
    for action in (stack.pop, stack.peek):
        try:
            action()
        except EmptyStackError:
            pass
        else:
            raise AssertionError("empty stack must raise EmptyStackError")


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_02_stack: {exc!r}")
    print("PASS ex_02_stack")
