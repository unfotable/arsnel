"""Exercise 11.3 - Process pool

Spread CPU-bound work over processes.

Run:  python ex_03_process_pool.py
"""

from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor


def is_prime(n: int) -> bool:
    """Trial-division primality test."""
    if n < 2:
        return False
    return all(n % d for d in range(2, int(n**0.5) + 1))


def count_primes(limit: int) -> int:
    """How many primes are < ``limit``."""
    # TODO: count is_prime(n) for n in range(limit).
    # --- solution ---
    return sum(1 for n in range(limit) if is_prime(n))
    # --- end ---


def parallel_counts(limits: list[int], workers: int = 2) -> list[int]:
    """Run ``count_primes`` for every limit in a process pool (input order kept)."""
    # TODO: with ProcessPoolExecutor(max_workers=workers) as pool: pool.map(...)
    # --- solution ---
    with ProcessPoolExecutor(max_workers=workers) as pool:
        return list(pool.map(count_primes, limits))
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert count_primes(10) == 4 and count_primes(2) == 0
    assert parallel_counts([10, 100, 1000]) == [4, 25, 168]
    assert parallel_counts([]) == []


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_03_process_pool: {exc!r}")
    print("PASS ex_03_process_pool")
