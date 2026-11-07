"""Context managers: __enter__/__exit__, contextlib helpers and ExitStack."""

from __future__ import annotations

import contextlib
from collections.abc import Iterator
from types import TracebackType


# 1. The protocol: __enter__ runs on entry, __exit__ ALWAYS runs on exit.
class Tracer:
    """Print when a block is entered and left."""

    def __init__(self, name: str) -> None:
        self.name = name

    def __enter__(self) -> Tracer:
        print(f"  enter {self.name}")
        return self  # this is what `as` binds

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> bool:
        print(f"  exit {self.name} (error={exc_type.__name__ if exc_type else None})")
        return exc_type is KeyError  # True swallows the exception


print("1. Class-based")
with Tracer("a") as t:
    print(f"  inside {t.name}")
with Tracer("b"):
    raise KeyError("swallowed because __exit__ returned True")


# 2. A generator is shorter: code before yield = enter, after = exit.
@contextlib.contextmanager
def announce(label: str) -> Iterator[str]:
    """Wrap a block with start/end messages, even if it fails."""
    print(f"  start {label}")
    try:
        yield label.upper()
    finally:  # without try/finally an exception would skip the cleanup
        print(f"  end {label}")


print("\n2. @contextmanager")
with announce("job") as value:
    print(f"  got {value}")
try:
    with announce("bad job"):
        raise ValueError("oops")
except ValueError as exc:
    print(f"  caught outside: {exc}")

# 3. suppress: ignore specific exceptions, nothing else.
print("\n3. contextlib.suppress")
with contextlib.suppress(ZeroDivisionError):
    print(1 / 0)
print("  carried on after the ZeroDivisionError")

# 4. ExitStack: a dynamic number of context managers.
print("\n4. ExitStack")
with contextlib.ExitStack() as stack:
    for name in ("x", "y", "z"):
        stack.enter_context(announce(name))
    stack.callback(print, "  callback registered last runs first")
    print("  all three are open")
