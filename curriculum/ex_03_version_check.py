"""Exercise 00.3 - Compare Python versions

Parse "3.11.4" into a tuple and compare versions numerically, not as text.

Run:  python ex_03_version_check.py
"""

from __future__ import annotations


def parse_version(text: str) -> tuple[int, ...]:
    """Turn ``"3.11.4"`` into ``(3, 11, 4)``; ``"3.12"`` into ``(3, 12)``.

    Surrounding whitespace is ignored. Non-numeric parts raise ``ValueError``.
    """
    # TODO: strip the text, split it on ".", convert each piece with int().
    # TODO: build a list of ints, then return tuple(that_list).
    raise NotImplementedError("TODO: your turn")


def is_supported(version: str, minimum: str = "3.11") -> bool:
    """Return True when ``version`` is at least ``minimum``."""
    # TODO: compare the two parsed tuples - tuples compare element by element.
    raise NotImplementedError("TODO: your turn")


def newest(versions: list[str]) -> str:
    """Return the highest version string; raise ``ValueError`` for an empty list."""
    # TODO: loop, keep the best (by parsed tuple) seen so far.
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert parse_version("3.11.4") == (3, 11, 4), "three parts"
    assert parse_version(" 3.12 ") == (3, 12), "two parts and whitespace"
    try:
        parse_version("3.x")
    except ValueError:
        pass
    else:
        raise AssertionError("'3.x' should raise ValueError")
    assert is_supported("3.13.1"), "3.13.1 >= 3.11"
    assert is_supported("3.11"), "equal versions are supported"
    assert not is_supported("3.9.18"), "3.9 is older than 3.11"
    assert is_supported("3.10", minimum="3.9"), "10 > 9 numerically, not as text"
    assert not is_supported("3.8", minimum="3.10"), "3.8 < 3.10"
    assert newest(["3.9.1", "3.11.4", "3.10.12"]) == "3.11.4", "3.11 beats 3.9, 3.10"
    assert newest(["3.12"]) == "3.12", "single item"
    try:
        newest([])
    except ValueError:
        pass
    else:
        raise AssertionError("newest([]) should raise ValueError")


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_03_version_check: {exc!r}")
    print("PASS ex_03_version_check")
