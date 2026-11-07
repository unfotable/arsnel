"""Exercise 01.1 - Greeting

Make ``greet`` return ``"Hello, <name>!"`` using an f-string.

Run:  python ex_01_greeting.py
"""

from __future__ import annotations


def greet(name: str) -> str:
    """Return a friendly greeting for ``name``."""
    # TODO: return the text "Hello, <name>!" (e.g. "Hello, Ada!") with an f-string.
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert greet("Ada") == "Hello, Ada!", "greet('Ada') should be 'Hello, Ada!'"
    assert greet("") == "Hello, !", "an empty name still gets the template"
    assert greet("Guido van Rossum") == "Hello, Guido van Rossum!"


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_01_greeting: {exc!r}")
    print("PASS ex_01_greeting")
