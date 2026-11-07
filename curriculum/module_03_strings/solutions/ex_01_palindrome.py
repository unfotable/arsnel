"""Exercise 03.1 - Palindromes

Normalise text with string methods, then compare with its reverse.

Run:  python ex_01_palindrome.py
"""

from __future__ import annotations


def normalize(text: str) -> str:
    """Lowercase ``text`` and keep only letters and digits."""
    # TODO: filter with str.isalnum() and lower the result.
    # --- solution ---
    return "".join(ch.lower() for ch in text if ch.isalnum())
    # --- end ---


def is_palindrome(text: str) -> bool:
    """True when ``text`` reads the same backwards (ignoring case and punctuation)."""
    # TODO: compare the normalised text with its reverse slice.
    # --- solution ---
    cleaned = normalize(text)
    return cleaned == cleaned[::-1]
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert normalize("A man, a plan!") == "amanaplan"
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert is_palindrome("") and is_palindrome("x")
    assert not is_palindrome("ARSNEL")


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_01_palindrome: {exc!r}")
    print("PASS ex_01_palindrome")
