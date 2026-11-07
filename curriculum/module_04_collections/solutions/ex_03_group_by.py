"""Exercise 04.3 - Group by

Group items with defaultdict and invert a mapping with a comprehension.

Run:  python ex_03_group_by.py
"""

from __future__ import annotations

from collections import defaultdict


def group_by_length(words: list[str]) -> dict[int, list[str]]:
    """Map each word length to the words of that length (input order kept)."""
    # TODO: create a defaultdict(list) and append each word under len(word).
    # TODO: return a plain dict(...) of it.
    # --- solution ---
    groups: defaultdict[int, list[str]] = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return dict(groups)
    # --- end ---


def invert(mapping: dict[str, str]) -> dict[str, list[str]]:
    """Return value -> sorted list of the keys that had that value."""
    # TODO: group keys by value (defaultdict again), then sort each key list.
    # --- solution ---
    inverted: defaultdict[str, list[str]] = defaultdict(list)
    for key, value in mapping.items():
        inverted[value].append(key)
    return {value: sorted(keys) for value, keys in inverted.items()}
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    got = group_by_length(["a", "bb", "cc", "d", "eee"])
    assert got == {1: ["a", "d"], 2: ["bb", "cc"], 3: ["eee"]}, got
    assert type(group_by_length([])) is dict, "return a plain dict"
    assert group_by_length([]) == {}, "empty input gives an empty dict"
    colours = {"apple": "red", "cherry": "red", "lime": "green"}
    assert invert(colours) == {"red": ["apple", "cherry"], "green": ["lime"]}
    assert invert({"b": "x", "a": "x"}) == {"x": ["a", "b"]}, "key lists are sorted"
    assert invert({}) == {}, "empty mapping"


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_03_group_by: {exc!r}")
    print("PASS ex_03_group_by")
