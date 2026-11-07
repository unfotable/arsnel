"""The iterator protocol: iter(), next(), StopIteration and custom iterators."""

numbers = [10, 20, 30]
iterator = iter(numbers)
print(next(iterator), next(iterator), next(iterator))
try:
    next(iterator)
except StopIteration:
    print("exhausted")
print(next(iter([]), "default"))  # next() with a default


class Countdown:
    """An iterable that creates a fresh iterator each time."""

    def __init__(self, start: int) -> None:
        self.start = start

    def __iter__(self) -> "CountdownIterator":
        return CountdownIterator(self.start)


class CountdownIterator:
    def __init__(self, current: int) -> None:
        self.current = current

    def __iter__(self) -> "CountdownIterator":
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1


countdown = Countdown(3)
print(list(countdown), list(countdown), sum(countdown))
for value in countdown:
    print("T-", value)

# A for loop is just iter() + next() until StopIteration.
it = iter("ab")
while True:
    try:
        print(next(it))
    except StopIteration:
        break
