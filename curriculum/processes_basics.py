"""Processes: real parallelism for CPU-bound work (no shared GIL)."""

from concurrent.futures import ProcessPoolExecutor


def count_primes(limit: int) -> int:
    """Deliberately CPU-heavy."""
    total = 0
    for n in range(2, limit):
        if all(n % d for d in range(2, int(n**0.5) + 1)):
            total += 1
    return total


if __name__ == "__main__":  # REQUIRED: child processes re-import this file
    limits = [2_000, 3_000, 4_000, 5_000]
    with ProcessPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(count_primes, limits))
    print(dict(zip(limits, results, strict=True)))
