"""Dunder (special) methods make your objects feel built in."""

from __future__ import annotations

from collections.abc import Iterator
from functools import total_ordering


@total_ordering
class Money:
    """Cents-based money with arithmetic, comparison and printing."""

    def __init__(self, cents: int) -> None:
        self.cents = cents

    def __repr__(self) -> str:  # for developers
        return f"Money({self.cents})"

    def __str__(self) -> str:  # for users
        return f"${self.cents / 100:.2f}"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Money) and self.cents == other.cents

    def __lt__(self, other: Money) -> bool:
        return self.cents < other.cents

    def __add__(self, other: Money) -> Money:
        return Money(self.cents + other.cents)

    def __mul__(self, factor: int) -> Money:
        return Money(self.cents * factor)

    def __bool__(self) -> bool:
        return self.cents != 0

    def __hash__(self) -> int:
        return hash(self.cents)


a, b = Money(250), Money(199)
print(repr(a), str(a), a + b, a * 3)
print(a > b, a == Money(250), sorted([a, b]), max(a, b))
print(bool(Money(0)), len({a, Money(250)}))


class Playlist:
    """Container protocol: __len__, __getitem__, __contains__, __iter__."""

    def __init__(self, *songs: str) -> None:
        self._songs = list(songs)

    def __len__(self) -> int:
        return len(self._songs)

    def __getitem__(self, index: int) -> str:
        return self._songs[index]

    def __iter__(self) -> Iterator[str]:
        return iter(self._songs)

    def __contains__(self, song: object) -> bool:
        return song in self._songs


playlist = Playlist("one", "two", "three")
print(len(playlist), playlist[0], playlist[-1], "two" in playlist, list(playlist))
