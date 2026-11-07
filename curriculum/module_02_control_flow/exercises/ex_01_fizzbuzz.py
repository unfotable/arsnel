"""Exercise 02.1 - FizzBuzz

Loops, modulo and conditionals.

Run:  python ex_01_fizzbuzz.py
"""

from __future__ import annotations


def fizzbuzz(n: int) -> list[str]:
    """Return 1..n as text: Fizz (3), Buzz (5), FizzBuzz (both)."""
    # TODO: loop 1..n and append the right text for each number.
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert fizzbuzz(0) == []
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizzbuzz(15)[-1] == "FizzBuzz" and fizzbuzz(15)[8] == "Fizz"


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_01_fizzbuzz: {exc!r}")
    print("PASS ex_01_fizzbuzz")
