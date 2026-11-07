"""Exercise 10.3 - Context manager and typed helper

Build a context manager and a generic function.

Run:  python ex_03_temp_chdir.py
"""

from __future__ import annotations

import os
import tempfile
from collections.abc import Iterator, Sequence
from contextlib import contextmanager
from pathlib import Path
from typing import TypeVar

T = TypeVar("T")


@contextmanager
def temp_chdir(path: Path) -> Iterator[Path]:
    """Change into ``path`` inside the ``with`` block and always change back."""
    # TODO: remember os.getcwd(), os.chdir(path), yield, restore in finally.
    # --- solution ---
    previous = os.getcwd()
    os.chdir(path)
    try:
        yield path
    finally:
        os.chdir(previous)
    # --- end ---


def first(items: Sequence[T], default: T | None = None) -> T | None:
    """Return the first item, or ``default`` for an empty sequence."""
    # TODO: return items[0] when there is one, else default.
    # --- solution ---
    return items[0] if items else default
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    start = os.getcwd()
    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp).resolve()
        with temp_chdir(target):
            assert Path(os.getcwd()).resolve() == target
        assert os.getcwd() == start, "must restore the directory"
        try:
            with temp_chdir(target):
                raise RuntimeError("boom")
        except RuntimeError:
            pass
        assert os.getcwd() == start, "must restore even after an exception"
    assert first([5, 6]) == 5 and first([]) is None and first([], 0) == 0


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_03_temp_chdir: {exc!r}")
    print("PASS ex_03_temp_chdir")
