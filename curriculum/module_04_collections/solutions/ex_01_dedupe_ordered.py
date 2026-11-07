"""Exercise 04.1 - Dedupe, keep order

Remove duplicates from a list while keeping the first occurrence of each item.

Run:  python ex_01_dedupe_ordered.py
"""

from __future__ import annotations


def dedupe(items: list[str]) -> list[str]:
    """Return ``items`` without repeats, in first-seen order."""
    # TODO: remember what you have seen in a set (fast membership).
    # TODO: append an item to the result only if it is not in the set yet.
    # --- solution ---
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
    # --- end ---


def common_sorted(a: list[int], b: list[int]) -> list[int]:
    """Return the sorted values that appear in BOTH lists, without repeats."""
    # TODO: use set intersection, then sorted().
    # --- solution ---
    return sorted(set(a) & set(b))
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert dedupe(["b", "a", "b", "c", "a"]) == ["b", "a", "c"], "keep first-seen order"
    assert dedupe([]) == [], "empty input gives empty output"
    original = ["x", "x"]
    dedupe(original)
    assert original == ["x", "x"], "do not modify the input list"
    assert common_sorted([3, 1, 2, 3], [3, 2, 5, 2]) == [2, 3], "intersection, sorted"
    assert common_sorted([1], [2]) == [], "no overlap gives an empty list"


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_01_dedupe_ordered: {exc!r}")
    print("PASS ex_01_dedupe_ordered")
