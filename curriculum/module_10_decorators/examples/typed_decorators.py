"""Fully typed decorators with ParamSpec, plus a taste of the mypy workflow."""

from __future__ import annotations

import functools
from collections.abc import Callable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")  # captures a function's parameter list
R = TypeVar("R")  # captures its return type


def trace(func: Callable[P, R]) -> Callable[P, R]:
    """Print the call; the decorated function keeps its exact signature."""

    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"  calling {func.__name__} args={args} kwargs={sorted(kwargs)}")
        return func(*args, **kwargs)

    return wrapper


@trace
def power(base: int, exponent: int = 2) -> int:
    """Raise ``base`` to ``exponent``."""
    return base**exponent


print("1. ParamSpec keeps the signature")
print(f"  result: {power(3, exponent=3)}")
# mypy now knows power(base: int, exponent: int = 2) -> int, so:
#   power("x")      -> error: Argument 1 has incompatible type "str"
#   power(2) + 1    -> fine, the result is still an int


def repeat(times: int) -> Callable[[Callable[P, R]], Callable[P, list[R]]]:
    """Factory: call the function ``times`` times and collect the results."""

    def decorator(func: Callable[P, R]) -> Callable[P, list[R]]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> list[R]:
            return [func(*args, **kwargs) for _ in range(times)]

        return wrapper

    return decorator


@repeat(3)
def shout(word: str) -> str:
    """Return the word in capitals."""
    return word.upper()


print("\n2. The return type can change too")
print(f"  {shout('hey')}")  # mypy infers list[str]

print("\n3. The mypy workflow")
print("  1) add hints to function signatures")
print("  2) run `mypy --strict yourfile.py`")
print("  3) fix errors, or silence ONE line: # type: ignore[code]")
print("  4) run mypy in CI so hints never rot")
