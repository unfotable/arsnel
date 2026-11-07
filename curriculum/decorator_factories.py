"""Decorators with arguments, class-based decorators and class decorators."""

from __future__ import annotations

import functools
from collections.abc import Callable
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


# Three layers: factory(args) -> decorator(func) -> wrapper(*args)
def retry(times: int, exceptions: tuple[type[Exception], ...] = (Exception,)) -> Any:
    """Retry the call up to ``times`` times when one of ``exceptions`` is raised."""

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    print(f"  attempt {attempt} failed: {exc}")
                    if attempt == times:
                        raise

        return wrapper  # type: ignore[return-value]

    return decorator


calls = {"n": 0}


@retry(times=3, exceptions=(ConnectionError,))  # type: ignore[untyped-decorator]
def flaky() -> str:
    """Fail twice, then succeed."""
    calls["n"] += 1
    if calls["n"] < 3:
        raise ConnectionError(f"boom #{calls['n']}")
    return "connected"


print("1. Decorator factory")
print(f"  result: {flaky()}")


# A class can be a decorator too: __call__ makes instances callable.
class Memoize:
    """Cache results by positional arguments."""

    def __init__(self, func: Callable[..., int]) -> None:
        functools.update_wrapper(self, func)
        self.func = func
        self.cache: dict[tuple[int, ...], int] = {}

    def __call__(self, *args: int) -> int:
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]


@Memoize
def slow_square(n: int) -> int:
    """Pretend this is expensive."""
    print(f"  computing {n}")
    return n * n


print("\n2. Class-based decorator")
print(f"  {slow_square(4)} {slow_square(4)}")  # 'computing 4' appears once

# A class decorator receives a class and returns a class (usually the same one).
REGISTRY: dict[str, type] = {}


def register(cls: type) -> type:
    """Record the class in REGISTRY under its lower-case name."""
    REGISTRY[cls.__name__.lower()] = cls
    return cls


@register
class Dog:
    """A registered class."""


@register
class Cat:
    """Another registered class."""


print("\n3. Class decorator")
print(f"  registry: {sorted(REGISTRY)}")
