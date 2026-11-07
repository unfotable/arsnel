"""Exercise 02.3 - Primes and Collatz

Nested loops, while and for/else.

Run:  python ex_03_primes_and_collatz.py
"""

from __future__ import annotations


def primes_up_to(limit: int) -> list[int]:
    """Return all primes <= ``limit`` in ascending order."""
    # TODO: for each candidate check divisors up to its square root.
    # --- solution ---
    primes: list[int] = []
    for candidate in range(2, limit + 1):
        for divisor in range(2, int(candidate**0.5) + 1):
            if candidate % divisor == 0:
                break
        else:
            primes.append(candidate)
    return primes
    # --- end ---


def collatz_steps(n: int) -> int:
    """Count the steps for ``n`` to reach 1 (even: n/2, odd: 3n+1)."""
    # TODO: use a while loop and a counter.
    # --- solution ---
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert primes_up_to(1) == [] and primes_up_to(2) == [2]
    assert primes_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert collatz_steps(1) == 0 and collatz_steps(6) == 8 and collatz_steps(27) == 111


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_03_primes_and_collatz: {exc!r}")
    print("PASS ex_03_primes_and_collatz")
