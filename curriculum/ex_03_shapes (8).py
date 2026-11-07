"""Exercise 08.3 - Shapes with a Protocol

Use a dataclass, an ABC and polymorphism.

Run:  python ex_03_shapes.py
"""

from __future__ import annotations

import math
from abc import ABC, abstractmethod
from collections.abc import Iterable
from dataclasses import dataclass


class Shape(ABC):
    """Every shape can report its area."""

    @abstractmethod
    def area(self) -> float:
        """Return the area."""


@dataclass(frozen=True)
class Rectangle(Shape):
    width: float
    height: float

    def area(self) -> float:
        """Width times height."""
        # TODO: return the area.
        # --- solution ---
        return self.width * self.height
        # --- end ---


@dataclass(frozen=True)
class Circle(Shape):
    radius: float

    def area(self) -> float:
        """Pi r squared."""
        # TODO: use math.pi.
        # --- solution ---
        return math.pi * self.radius**2
        # --- end ---


def total_area(shapes: Iterable[Shape]) -> float:
    """Sum the areas of all shapes (works for any Shape subclass)."""
    # TODO: add up shape.area() for every shape.
    # --- solution ---
    return sum(shape.area() for shape in shapes)
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert Rectangle(2, 3).area() == 6
    assert abs(Circle(1).area() - math.pi) < 1e-9
    assert abs(total_area([Rectangle(1, 1), Circle(2)]) - (1 + 4 * math.pi)) < 1e-9
    assert total_area([]) == 0
    assert Rectangle(1, 2) == Rectangle(1, 2)
    try:
        Shape()  # type: ignore[abstract]
    except TypeError:
        pass
    else:
        raise AssertionError("Shape must stay abstract")


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_03_shapes: {exc!r}")
    print("PASS ex_03_shapes")
