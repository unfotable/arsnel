"""Exercise 17.3 - Validate input clearly

Raise specific, helpful errors.

Run:  python ex_03_validate_input.py
"""

from __future__ import annotations


def parse_age(text: str) -> int:
    """Parse an age from user input.

    Raise ValueError("age must be a whole number") for non-integers and
    ValueError("age must be between 0 and 150") when out of range.
    """
    # TODO: strip, try int(), then range-check; keep the exact messages.
    raise NotImplementedError("TODO: your turn")


def safe_get(data: dict[str, object], path: str, default: object = None) -> object:
    """Read a dotted path like ``"user.address.city"`` without raising KeyError."""
    # TODO: walk the dict level by level; return default when a step is missing.
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert parse_age(" 42 ") == 42 and parse_age("0") == 0
    for text, message in (
        ("abc", "whole number"),
        ("", "whole number"),
        ("200", "between"),
    ):
        try:
            parse_age(text)
        except ValueError as exc:
            assert message in str(exc), f"{text!r}: {exc}"
        else:
            raise AssertionError(f"{text!r} should be rejected")
    doc: dict[str, object] = {"user": {"address": {"city": "Pune"}}, "n": 1}
    assert safe_get(doc, "user.address.city") == "Pune"
    assert safe_get(doc, "user.phone", "n/a") == "n/a"
    assert safe_get(doc, "n.x") is None


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_03_validate_input: {exc!r}")
    print("PASS ex_03_validate_input")
