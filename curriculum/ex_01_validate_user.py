"""Exercise 16.1 - Validate a request body

Return every problem with a user payload, like an API would.

Run:  python ex_01_validate_user.py
"""

from __future__ import annotations


def validate_user(data: dict[str, object]) -> list[str]:
    """Return error messages (empty list when valid), in this order.

    - ``name``: required, non-empty string        -> "name is required"
    - ``email``: required string containing "@"    -> "email is invalid"
    - ``age``: optional int between 0 and 150      -> "age must be 0-150"
    """
    # TODO: check each field and append the exact messages above.
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert validate_user({"name": "Ada", "email": "ada@x.io"}) == []
    assert validate_user({"name": "Ada", "email": "ada@x.io", "age": 36}) == []
    assert validate_user({}) == ["name is required", "email is invalid"]
    assert validate_user({"name": " ", "email": "nope"}) == [
        "name is required",
        "email is invalid",
    ]
    assert validate_user({"name": "A", "email": "a@b", "age": 200}) == [
        "age must be 0-150"
    ]
    assert validate_user({"name": "A", "email": "a@b", "age": True}) == [
        "age must be 0-150"
    ]


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_01_validate_user: {exc!r}")
    print("PASS ex_01_validate_user")
