"""Parameters: positional, keyword, defaults, keyword-only and the mutable trap."""


def describe(name: str, age: int, city: str = "Paris") -> str:
    """Positional parameters first, then parameters with defaults."""
    return f"{name} ({age}) lives in {city}"


# Arguments can be passed by position or by keyword.
print(describe("Ada", 36))
print(describe("Linus", 28, "Helsinki"))
print(describe(city="Lyon", age=41, name="Grace"))


def connect(host: str, *, port: int = 80, secure: bool = False) -> str:
    """Everything after the bare ``*`` MUST be passed by keyword."""
    scheme = "https" if secure else "http"
    return f"{scheme}://{host}:{port}"


print(connect("example.org", port=8080, secure=True))
try:
    connect("example.org", 8080)  # type: ignore[call-arg]
except TypeError as exc:
    print("TypeError:", exc)


def scale(value: float, factor: float, /) -> float:
    """Parameters before ``/`` are positional-only (names are not part of the API)."""
    return value * factor


print("scale:", scale(2.5, 4))


# THE MUTABLE DEFAULT TRAP: the default list is created ONCE, at definition time.
def add_bad(item: int, bucket: list[int] = []) -> list[int]:  # noqa: B006 - demo
    """Buggy: every call without ``bucket`` shares one list."""
    bucket.append(item)
    return bucket


print("bad :", add_bad(1), add_bad(2), add_bad(3))


def add_good(item: int, bucket: list[int] | None = None) -> list[int]:
    """Fixed: use ``None`` as the sentinel and create the list inside."""
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


print("good:", add_good(1), add_good(2), add_good(3))


# Functions return None unless they return something; return many values as a tuple.
def min_max(values: list[int]) -> tuple[int, int]:
    """Return both extremes at once; callers unpack the tuple."""
    return min(values), max(values)


low, high = min_max([4, 9, 2, 7])
print("low/high:", low, high)
print("defaults live on the function:", add_bad.__defaults__)
