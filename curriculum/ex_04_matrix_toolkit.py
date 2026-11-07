"""Exercise 04.4 - Matrix toolkit

Comprehensions over nested lists, and a copy that does not share rows.

Run:  python ex_04_matrix_toolkit.py
"""

from __future__ import annotations

import copy


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """Swap rows and columns: ``[[1, 2], [3, 4]]`` -> ``[[1, 3], [2, 4]]``."""
    # TODO: zip(*matrix) yields the columns; turn each into a list.
    raise NotImplementedError("TODO: your turn")


def flatten(matrix: list[list[int]]) -> list[int]:
    """Return all values row by row as one flat list."""
    # TODO: a nested comprehension: [v for row in matrix for v in row].
    raise NotImplementedError("TODO: your turn")


def scaled_copy(matrix: list[list[int]], factor: int) -> list[list[int]]:
    """Return a NEW matrix with every value multiplied by ``factor``."""
    # TODO: build new inner lists so the original is never modified.
    raise NotImplementedError("TODO: your turn")


def independent_copy(matrix: list[list[int]]) -> list[list[int]]:
    """Return a copy whose rows can be edited without touching ``matrix``."""
    # TODO: a shallow copy shares the rows - use the copy module instead.
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    m = [[1, 2, 3], [4, 5, 6]]
    assert transpose(m) == [[1, 4], [2, 5], [3, 6]], "columns become rows"
    assert transpose([[7]]) == [[7]], "1x1 matrix"
    assert flatten(m) == [1, 2, 3, 4, 5, 6], "row-major order"
    assert flatten([]) == [], "empty matrix"
    doubled = scaled_copy(m, 2)
    assert doubled == [[2, 4, 6], [8, 10, 12]], doubled
    assert m == [[1, 2, 3], [4, 5, 6]], "scaled_copy must not modify its input"
    clone = independent_copy(m)
    clone[0][0] = 99
    assert m[0][0] == 1, "rows of the copy must not be shared with the original"
    assert clone is not m and clone[1] == m[1]


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_04_matrix_toolkit: {exc!r}")
    print("PASS ex_04_matrix_toolkit")
