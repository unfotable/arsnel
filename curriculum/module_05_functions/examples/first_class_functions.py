"""Functions are objects: pass them around, store them, use lambdas and sorting."""

from collections.abc import Callable
from functools import reduce


def shout(text: str) -> str:
    """Upper-case with emphasis."""
    return text.upper() + "!"


def whisper(text: str) -> str:
    """Lower-case with ellipsis."""
    return text.lower() + "..."


# A function is a value: bind it to another name, put it in a dict.
styles: dict[str, Callable[[str], str]] = {"shout": shout, "whisper": whisper}
for style_name, style in styles.items():
    print(style_name, "->", style("Hello"))


# Higher-order function: takes a function as an argument.
def apply_twice(func: Callable[[int], int], value: int) -> int:
    """Return ``func(func(value))``."""
    return func(func(value))


print("apply_twice:", apply_twice(lambda n: n + 10, 1))

# A lambda is an anonymous single-expression function. Great as a key=.
people = [("Ada", 36), ("Linus", 28), ("Grace", 45)]
print("youngest first:", sorted(people, key=lambda p: p[1]))
print("max by age:", max(people, key=lambda p: p[1]))

# map/filter work, but comprehensions are usually clearer.
nums = [1, 2, 3, 4, 5, 6]
print("map   :", list(map(lambda n: n * n, nums)))  # noqa: C417
print("filter:", list(filter(lambda n: n % 2 == 0, nums)))
print("comprehension:", [n * n for n in nums if n % 2 == 0])
print("reduce:", reduce(lambda acc, n: acc * n, nums))


# Compose small functions into a pipeline.
def compose(*funcs: Callable[[int], int]) -> Callable[[int], int]:
    """Return a function that applies ``funcs`` left to right."""

    def run(value: int) -> int:
        for func in funcs:
            value = func(value)
        return value

    return run


pipeline = compose(lambda n: n + 1, lambda n: n * 10, abs)
print("pipeline(-3):", pipeline(-3))

# Introspection: every function carries metadata.
print("name:", shout.__name__, "| doc:", shout.__doc__)
print("callable?", callable(shout), callable(42))
