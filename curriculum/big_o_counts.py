"""Big-O by counting operations (deterministic, unlike wall-clock time)."""

from functools import cache


def linear_search(items: list[int], target: int) -> int:
    steps = 0
    for item in items:
        steps += 1
        if item == target:
            break
    return steps


def binary_search(items: list[int], target: int) -> int:
    low, high, steps = 0, len(items) - 1, 0
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if items[mid] == target:
            break
        if items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return steps


print(f"{'n':>9} {'O(n)':>9} {'O(log n)':>9}")
for n in (10, 1_000, 100_000):
    data = list(range(n))
    print(f"{n:>9} {linear_search(data, n - 1):>9} {binary_search(data, n - 1):>9}")

naive_calls = 0


def fib_naive(n: int) -> int:
    global naive_calls
    naive_calls += 1
    return n if n < 2 else fib_naive(n - 1) + fib_naive(n - 2)


memo_calls = 0


@cache
def fib_memo(n: int) -> int:
    global memo_calls
    memo_calls += 1
    return n if n < 2 else fib_memo(n - 1) + fib_memo(n - 2)


fib_naive(20)
fib_memo(20)
print("fib(20) calls  naive O(2^n):", naive_calls, " memoised O(n):", memo_calls)
pairs = sum(1 for i in range(100) for j in range(100))
print("nested loops O(n^2) for n=100:", pairs)
