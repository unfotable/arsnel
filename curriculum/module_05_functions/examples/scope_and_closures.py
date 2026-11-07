"""Scope (LEGB), nonlocal, closures and the late-binding gotcha."""

from collections.abc import Callable

# LEGB: Local -> Enclosing -> Global -> Built-in. Python looks in that order.
level = "global"


def outer() -> None:
    """Show each scope, innermost first."""
    level = "enclosing"

    def inner() -> None:
        level = "local"
        print("inner sees:", level)

    inner()
    print("outer sees:", level)


outer()
print("module sees:", level)

# Assigning inside a function creates a LOCAL, even if a global has that name.
counter = 0


def broken() -> None:
    """Reading before assignment in the same scope raises UnboundLocalError."""
    try:
        counter += 1  # noqa: F823, F841 - demo
    except UnboundLocalError as exc:
        print("UnboundLocalError:", exc)


broken()


# A closure remembers variables from the function that created it.
def make_counter(start: int = 0) -> Callable[[], int]:
    """Return a function with private, persistent state."""
    count = start

    def tick() -> int:
        nonlocal count  # rebind the ENCLOSING variable, not a new local
        count += 1
        return count

    return tick


a, b = make_counter(), make_counter(100)
print("a:", a(), a(), a(), "| b:", b(), b())


def make_multiplier(factor: int) -> Callable[[int], int]:
    """A factory: each call produces a function with its own ``factor``."""
    return lambda x: x * factor


double, triple = make_multiplier(2), make_multiplier(3)
print("double/triple 7:", double(7), triple(7))

# Late binding: closures look the variable up when CALLED, not when created.
late = [lambda: i for i in range(3)]  # noqa: B023 - late-binding demo
print("late:", [f() for f in late])
fixed = [lambda i=i: i for i in range(3)]  # default captures the current value
print("fixed:", [f() for f in fixed])
