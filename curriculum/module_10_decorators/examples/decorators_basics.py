"""Decorators from first principles: closures, functools.wraps and stacking."""

from __future__ import annotations

import functools
from collections.abc import Callable
from typing import Any

# A decorator is a function that takes a function and returns a function.
# The inner "wrapper" is a closure: it remembers `func` after log_calls returns.


def log_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    """Print every call and its result."""

    @functools.wraps(func)  # copy __name__, __doc__ ... onto the wrapper
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)
        print(f"  {func.__name__}{args} -> {result}")
        return result

    return wrapper


@log_calls  # exactly the same as: add = log_calls(add)
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


print("1. A simple decorator")
add(2, 3)
print(f"  name={add.__name__!r} doc={add.__doc__!r}")  # thanks to wraps


# Without wraps the metadata of the original function is lost.
def careless(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that forgets functools.wraps (do not do this)."""

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)

    return wrapper


@careless
def documented() -> None:
    """I have a docstring."""


print(f"  without wraps: name={documented.__name__!r} doc={documented.__doc__!r}")


# Decorators can keep state between calls in a closure or on the wrapper.
def count_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    """Count how often ``func`` was called (stored as ``wrapper.calls``)."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        wrapper.calls += 1  # type: ignore[attr-defined]
        return func(*args, **kwargs)

    wrapper.calls = 0  # type: ignore[attr-defined]
    return wrapper


@count_calls
def ping() -> str:
    """Return a constant."""
    return "pong"


ping()
ping()
print("\n2. State in a decorator")
print(f"  ping was called {ping.calls} times")  # type: ignore[attr-defined]


# Stacking: the decorator closest to the function is applied FIRST.
def tag(name: str) -> Callable[[Callable[[], str]], Callable[[], str]]:
    """Wrap the returned text in <name>...</name>."""

    def decorator(func: Callable[[], str]) -> Callable[[], str]:
        @functools.wraps(func)
        def wrapper() -> str:
            return f"<{name}>{func()}</{name}>"

        return wrapper

    return decorator


@tag("outer")
@tag("inner")
def text() -> str:
    """Plain text."""
    return "hi"


print("\n3. Stacking order")
print(f"  {text()}")  # inner is applied first, so it sits closest to the text
