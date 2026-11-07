"""Exercise 08.2 - A 2D vector

Implement dunder methods so Vector behaves like a number-like value.

Run:  python ex_02_vector.py
"""

from __future__ import annotations

import math


class Vector:
    """An immutable-style 2D vector."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """Return ``Vector(x, y)``."""
        # TODO: use an f-string with {self.x!r} and {self.y!r}.
        # --- solution ---
        return f"Vector({self.x!r}, {self.y!r})"
        # --- end ---

    def __eq__(self, other: object) -> bool:
        """Equal when both coordinates are equal."""
        # TODO: check isinstance(other, Vector) first.
        # --- solution ---
        return isinstance(other, Vector) and (self.x, self.y) == (other.x, other.y)
        # --- end ---

    def __add__(self, other: Vector) -> Vector:
        """Component-wise addition."""
        # TODO: return a new Vector.
        # --- solution ---
        return Vector(self.x + other.x, self.y + other.y)
        # --- end ---

    def __mul__(self, factor: float) -> Vector:
        """Scale by a number."""
        # TODO: return a new Vector.
        # --- solution ---
        return Vector(self.x * factor, self.y * factor)
        # --- end ---

    def __abs__(self) -> float:
        """Length of the vector."""
        # TODO: use math.hypot.
        # --- solution ---
        return math.hypot(self.x, self.y)
        # --- end ---

    def __hash__(self) -> int:
        return hash((self.x, self.y))


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    a, b = Vector(1, 2), Vector(3, 4)
    assert repr(a) == "Vector(1, 2)"
    assert a + b == Vector(4, 6)
    assert a * 3 == Vector(3, 6)
    assert abs(b) == 5.0
    assert a == Vector(1, 2) and a != b and a != "Vector(1, 2)"
    assert len({a, Vector(1, 2)}) == 1


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_02_vector: {exc!r}")
    print("PASS ex_02_vector")
