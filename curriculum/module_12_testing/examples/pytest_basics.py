"""pytest basics: plain asserts, parametrize and pytest.raises/approx.

Run directly (``python pytest_basics.py``) - the last lines launch pytest.
"""

# requires: pytest

import pytest


def add(a: float, b: float) -> float:
    return a + b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("b must not be zero")
    return a / b


def test_add() -> None:
    assert add(2, 3) == 5  # plain assert: pytest explains failures


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(1, 1, 2), (0, 0, 0), (-1, 1, 0), (0.5, 0.25, 0.75)],
)
def test_add_many(a: float, b: float, expected: float) -> None:
    assert add(a, b) == expected


def test_float_compare() -> None:
    assert pytest.approx(0.3) == 0.1 + 0.2


def test_divide_error() -> None:
    with pytest.raises(ZeroDivisionError, match="zero"):
        divide(1, 0)


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q", "-p", "no:cacheprovider"]))
