"""Exercise 12.1 - TDD: slugify

Make the described test-suite pass (red -> green).

Run:  python ex_01_slugify.py
"""

from __future__ import annotations

import re


def slugify(text: str) -> str:
    """Lowercase, replace runs of non-alphanumerics with ``-`` and trim dashes.

    "Hello, World!" -> "hello-world"; "  A  B " -> "a-b"; "" -> "".
    """
    # TODO: use re.sub(r"[^a-z0-9]+", "-", ...) on the lowered text, then strip("-").
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    cases = {
        "Hello, World!": "hello-world",
        "  A  B ": "a-b",
        "already-slug": "already-slug",
        "": "",
        "***": "",
        "Python 3.13 rocks": "python-3-13-rocks",
    }
    for text, expected in cases.items():
        assert slugify(text) == expected, f"slugify({text!r}) -> {slugify(text)!r}"


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_01_slugify: {exc!r}")
    print("PASS ex_01_slugify")
