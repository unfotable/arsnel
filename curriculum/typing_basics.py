"""Type hints: unions, generics, Callable, TypedDict, Literal and Protocol."""

from __future__ import annotations

from collections.abc import Callable, Iterable, Sequence
from typing import Literal, Protocol, TypedDict, TypeVar, get_type_hints

# Hints are ignored at runtime. Tools such as mypy read them for you.


def find_user(users: dict[int, str], user_id: int) -> str | None:
    """Return the name, or None when the id is unknown (Optional)."""
    return users.get(user_id)


name = find_user({1: "Ada"}, 2)
# mypy forces you to handle None before using the value as a str:
print("1. Optional")
print(f"  {name.upper() if name is not None else 'nobody'}")

# 2. Generics: T links the input type to the output type.
T = TypeVar("T")


def first(items: Sequence[T]) -> T:
    """Return the first item; the result type follows the element type."""
    return items[0]


def apply_all(funcs: Iterable[Callable[[int], int]], value: int) -> list[int]:
    """Call every function with ``value``."""
    return [f(value) for f in funcs]


print("\n2. Generics and Callable")
print(f"  {first([10, 20])} {first('xyz')}")
print(f"  {apply_all([abs, lambda n: n * 2], -4)}")


# 3. TypedDict describes dict shapes; Literal restricts to exact values.
class Movie(TypedDict):
    """A dict with exactly these keys."""

    title: str
    year: int


Mode = Literal["r", "w"]


def describe(movie: Movie, mode: Mode = "r") -> str:
    """Show a movie; ``mode`` can only be "r" or "w" for the type checker."""
    return f"{movie['title']} ({movie['year']}) [{mode}]"


print("\n3. TypedDict and Literal")
print(f"  {describe({'title': 'Alien', 'year': 1979})}")


# 4. Protocol = structural typing ("duck typing, checked statically").
class Speaker(Protocol):
    """Anything with a speak() method returning str."""

    def speak(self) -> str: ...


class Robot:
    """Does not inherit from Speaker but still satisfies it."""

    def speak(self) -> str:
        return "beep"


def greet(who: Speaker) -> str:
    """Accept any object that matches the Speaker protocol."""
    return who.speak()


print("\n4. Protocol")
print(f"  {greet(Robot())}")

# Hints are plain data you can inspect.
print("\n5. Introspection")
print(f"  {get_type_hints(find_user)}")
