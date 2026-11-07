"""Exercise 03.2 - Caesar cipher

Shift letters with ord/chr and keep everything else.

Run:  python ex_02_caesar.py
"""

from __future__ import annotations


def caesar(text: str, shift: int) -> str:
    """Shift letters by ``shift`` (wrapping a-z / A-Z); leave other characters alone."""
    # TODO: for each letter compute the shifted position with % 26.
    # --- solution ---
    out: list[str] = []
    for ch in text:
        if ch.isascii() and ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            out.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            out.append(ch)
    return "".join(out)
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert caesar("abc", 1) == "bcd" and caesar("xyz", 3) == "abc"
    assert caesar("Hello, World!", 13) == "Uryyb, Jbeyq!"
    assert caesar(caesar("Round Trip", 7), -7) == "Round Trip"
    assert caesar("", 5) == "" and caesar("123", 5) == "123"


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_02_caesar: {exc!r}")
    print("PASS ex_02_caesar")
