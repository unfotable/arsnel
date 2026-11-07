"""Generators: lazy sequences with yield, yield from and generator expressions."""

from collections.abc import Iterable, Iterator


def fibonacci() -> Iterator[int]:
    """An infinite sequence - possible because values are produced lazily."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def take(n: int, items: Iterable[int]) -> list[int]:
    result: list[int] = []
    for item in items:
        if len(result) == n:
            break
        result.append(item)
    return result


print(take(10, fibonacci()))


def chain_two(a: Iterable[int], b: Iterable[int]) -> Iterator[int]:
    yield from a  # delegate to another iterable
    yield from b


print(list(chain_two(range(3), [10, 20])))


# Execution pauses at each yield and resumes on the next next().
def trace() -> Iterator[str]:
    print("  start")
    yield "first"
    print("  middle")
    yield "second"
    print("  end")


gen = trace()
print(next(gen))
print(next(gen))
print(list(gen))

# Generator expressions + pipelines never build intermediate lists.
squares = (n * n for n in range(1_000_000))
evens = (n for n in squares if n % 2 == 0)
print(next(evens), next(evens), next(evens))
print(sum(n for n in range(101)))
