"""Exercise 13.1 - Version tools

Parse, compare and bump SemVer strings.

Run:  python ex_01_version_tools.py
"""

from __future__ import annotations


def parse_version(text: str) -> tuple[int, int, int]:
    """Parse ``"MAJOR.MINOR.PATCH"``; raise ValueError for anything else."""
    # TODO: split on ".", require exactly 3 integer parts, return them as a tuple.
    # --- solution ---
    parts = text.strip().split(".")
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        raise ValueError(f"not a MAJOR.MINOR.PATCH version: {text!r}")
    major, minor, patch = (int(p) for p in parts)
    return major, minor, patch
    # --- end ---


def bump(text: str, part: str) -> str:
    """Return the version with ``part`` ('major', 'minor' or 'patch') incremented."""
    # TODO: bump the chosen part and reset the lower ones to 0.
    # --- solution ---
    major, minor, patch = parse_version(text)
    if part == "major":
        return f"{major + 1}.0.0"
    if part == "minor":
        return f"{major}.{minor + 1}.0"
    if part == "patch":
        return f"{major}.{minor}.{patch + 1}"
    raise ValueError(f"unknown part: {part!r}")
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert parse_version("1.2.3") == (1, 2, 3)
    assert parse_version("1.10.0") > parse_version("1.9.9"), "compare as numbers"
    for bad in ("1.2", "1.2.x", "a.b.c", ""):
        try:
            parse_version(bad)
        except ValueError:
            continue
        raise AssertionError(f"{bad!r} should be rejected")
    assert bump("1.2.3", "patch") == "1.2.4"
    assert bump("1.2.3", "minor") == "1.3.0"
    assert bump("1.2.3", "major") == "2.0.0"


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_01_version_tools: {exc!r}")
    print("PASS ex_01_version_tools")
