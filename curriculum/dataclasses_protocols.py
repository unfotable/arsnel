"""dataclasses, typing.Protocol and abc.ABC."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Protocol


@dataclass(order=True, frozen=True)
class Version:
    """Generates __init__, __repr__, __eq__ and ordering for free."""

    major: int
    minor: int = 0


@dataclass
class Team:
    name: str
    members: list[str] = field(default_factory=list)  # never use [] directly


print(Version(1, 2), Version(1, 2) == Version(1, 2), Version(1, 9) < Version(2))
team = Team("core")
team.members.append("ada")
print(team)


class Drawable(Protocol):
    """Structural typing: anything with draw() -> str fits."""

    def draw(self) -> str: ...


class Circle:
    def draw(self) -> str:
        return "()"


def render(items: list[Drawable]) -> str:
    return " ".join(item.draw() for item in items)


print(render([Circle(), Circle()]))


class Shape(ABC):
    """Nominal typing: subclasses MUST implement area()."""

    @abstractmethod
    def area(self) -> float: ...


class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side**2


print(Square(3).area())
try:
    Shape()  # type: ignore[abstract]
except TypeError as exc:
    print("TypeError:", exc)
