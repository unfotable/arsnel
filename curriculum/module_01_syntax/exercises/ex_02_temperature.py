"""Exercise 01.2 - Temperature converter

Convert between Celsius and Fahrenheit with float maths.

Run:  python ex_02_temperature.py
"""

from __future__ import annotations


def celsius_to_fahrenheit(celsius: float) -> float:
    """Return ``celsius`` converted to Fahrenheit (F = C * 9/5 + 32)."""
    # TODO: apply the formula and return the result.
    raise NotImplementedError("TODO: your turn")


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Return ``fahrenheit`` converted to Celsius (C = (F - 32) * 5/9)."""
    # TODO: apply the formula and return the result.
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert abs(fahrenheit_to_celsius(98.6) - 37.0) < 1e-9


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_02_temperature: {exc!r}")
    print("PASS ex_02_temperature")
