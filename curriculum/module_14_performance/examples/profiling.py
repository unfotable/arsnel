"""Measure first: timeit, cProfile call counts and tracemalloc."""

import cProfile
import pstats
import timeit
import tracemalloc


def slow_sum(n: int) -> int:
    total = 0
    for i in range(n):
        total += i
    return total


def helper(n: int) -> int:
    return sum(range(n))


def work() -> int:
    return slow_sum(1000) + helper(1000)


# timeit runs code many times; compare *relative* results, not absolute numbers.
loop_time = timeit.timeit(lambda: slow_sum(1000), number=200)
builtin_time = timeit.timeit(lambda: helper(1000), number=200)
print("builtin sum faster:", builtin_time < loop_time)

profiler = cProfile.Profile()
profiler.enable()
work()
profiler.disable()
stats = pstats.Stats(profiler)
print("function calls recorded:", stats.total_calls > 0)  # type: ignore[attr-defined]

tracemalloc.start()
as_list = [n * n for n in range(50_000)]
_, list_peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.start()
as_generator = sum(n * n for n in range(50_000))
_, gen_peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print("generator uses less memory:", gen_peak < list_peak, len(as_list), as_generator)
