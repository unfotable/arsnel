"""Exercise 04.2 - Word counts

Count words with a dict (or Counter) and report the most frequent ones.

Run:  python ex_02_word_counts.py
"""

from __future__ import annotations


def word_counts(text: str) -> dict[str, int]:
    """Return how often each lower-cased word occurs in ``text``."""
    # TODO: split the text on whitespace and lower-case each word.
    # TODO: strip surrounding punctuation with word.strip(".,!?;:").
    # TODO: tally into a dict (dict.get(word, 0) + 1) or a Counter.
    raise NotImplementedError("TODO: your turn")


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    """Return the ``n`` most common words; ties are sorted alphabetically."""
    # TODO: sort the (word, count) pairs with a key that puts big counts first
    # TODO: and breaks ties by word: key=lambda p: (-p[1], p[0]).
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    counts = word_counts("The cat. The hat! the BAT, and a cat")
    assert counts == {"the": 3, "cat": 2, "hat": 1, "bat": 1, "and": 1, "a": 1}, counts
    assert word_counts("") == {}, "empty text has no words"
    assert word_counts("...") == {}, "punctuation alone is not a word"
    top = top_words("b a b c a b d", 2)
    assert top == [("b", 3), ("a", 2)], top
    assert top_words("z y x", 2) == [("x", 1), ("y", 1)], "ties sort alphabetically"


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_02_word_counts: {exc!r}")
    print("PASS ex_02_word_counts")
