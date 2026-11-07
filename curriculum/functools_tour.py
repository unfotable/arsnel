"""functools: partial, reduce, lru_cache, singledispatch and total_ordering."""

import operator
from functools import cache, partial, reduce, singledispatch

print(reduce(operator.mul, [1, 2, 3, 4, 5]), reduce(lambda a, b: a + b, "abc", ""))

square = partial(pow, exp=2)
hex_to_int = partial(int, base=16)
print(square(7), hex_to_int("ff"))

calls = 0


@cache
def fib(n: int) -> int:
    global calls
    calls += 1
    return n if n < 2 else fib(n - 1) + fib(n - 2)


print(fib(40), "computed", calls, "times;", fib.cache_info().hits, "cache hits")


@singledispatch
def describe(value: object) -> str:
    return f"object {value!r}"


@describe.register
def _(value: int) -> str:
    return f"int {value}"


@describe.register
def _(value: list) -> str:
    return f"list of {len(value)}"


print(describe(5), describe([1, 2]), describe("x"))
