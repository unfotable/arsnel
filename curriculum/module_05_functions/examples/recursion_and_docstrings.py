"""Recursion, base cases, the recursion limit and good docstrings."""

import sys


def factorial(n: int) -> int:
    """Return ``n!`` for a non-negative integer.

    Args:
        n: The number to take the factorial of; must be >= 0.

    Returns:
        The product 1 * 2 * ... * n (``0! == 1``).

    Raises:
        ValueError: If ``n`` is negative.
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    if n <= 1:  # BASE CASE: stops the recursion
        return 1
    return n * factorial(n - 1)  # RECURSIVE CASE: a smaller problem


print("5! =", factorial(5))
print("docstring first line:", (factorial.__doc__ or "").splitlines()[0])


def depth_sum(data: list[object], depth: int = 1) -> int:
    """Sum nested lists of ints, weighting each number by its depth."""
    total = 0
    for item in data:
        if isinstance(item, list):
            total += depth_sum(item, depth + 1)
        elif isinstance(item, int):
            total += item * depth
    return total


print("depth_sum:", depth_sum([1, [2, [3]], 4]))


def fib(n: int, memo: dict[int, int] | None = None) -> int:
    """Fibonacci with a dict cache (without it the calls explode)."""
    if memo is None:
        memo = {}
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


print("fib(60):", fib(60))


# Python does not optimise tail calls: very deep recursion fails.
def count_down(n: int) -> int:
    """Recurse n levels deep."""
    return 0 if n == 0 else 1 + count_down(n - 1)


limit = sys.getrecursionlimit()
print("limit is a safety net:", limit >= 1000)
try:
    count_down(limit * 2)
except RecursionError:
    print("RecursionError: use a loop for deep problems")
print("loop version:", sum(1 for _ in range(limit * 2)))
