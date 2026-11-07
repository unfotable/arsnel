"""Exercise 07.1 - Read a config file

Parse key=value text with comments and raise clear errors.

Run:  python ex_01_read_config.py
"""

from __future__ import annotations

import tempfile
from pathlib import Path


class ConfigError(ValueError):
    """Raised for a malformed configuration line."""


def read_config(path: Path) -> dict[str, str]:
    """Parse ``key = value`` lines; skip blanks and ``#`` comments.

    Raise :class:`ConfigError` (mentioning the line number) when a line has no ``=``.
    """
    # TODO: read the lines, skip blanks/comments, split each on the first "=".
    # --- solution ---
    result: dict[str, str] = {}
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        key, sep, value = line.partition("=")
        if not sep or not key.strip():
            raise ConfigError(f"line {number}: expected key = value")
        result[key.strip()] = value.strip()
    return result
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    with tempfile.TemporaryDirectory() as tmp:
        good = Path(tmp) / "good.cfg"
        good.write_text("# demo\nname = arsnel\n\nmode=a=b\n", encoding="utf-8")
        assert read_config(good) == {"name": "arsnel", "mode": "a=b"}
        bad = Path(tmp) / "bad.cfg"
        bad.write_text("ok = 1\nnonsense\n", encoding="utf-8")
        try:
            read_config(bad)
        except ConfigError as exc:
            assert "line 2" in str(exc), "message should name the line"
        else:
            raise AssertionError("malformed line must raise ConfigError")


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_01_read_config: {exc!r}")
    print("PASS ex_01_read_config")
