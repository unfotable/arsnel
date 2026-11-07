"""Red -> green -> refactor, shown as three versions of one function."""


def tests(fn) -> str:  # type: ignore[no-untyped-def]
    """The specification, written FIRST."""
    cases = {"": 0, "a": 1, "a b": 2, "  many   spaces here ": 3}
    failures = [text for text, want in cases.items() if fn(text) != want]
    return "green" if not failures else f"red: {failures}"


def v1_red(text: str) -> int:  # does not do the job yet
    return 0


def v2_green(text: str) -> int:  # simplest thing that passes
    return len(text.split())


def v3_refactor(text: str) -> int:  # same behaviour, clearer intent
    words = text.split()
    return len(words)


for fn in (v1_red, v2_green, v3_refactor):
    print(f"{fn.__name__:12} {tests(fn)}")
