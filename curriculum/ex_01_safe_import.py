"""Exercise 06.1 - Safe import

Import by name at runtime and handle a missing module.

Run:  python ex_01_safe_import.py
"""

from __future__ import annotations

import importlib
from types import ModuleType


def safe_import(name: str) -> ModuleType | None:
    """Return the imported module, or ``None`` when it cannot be found."""
    # TODO: importlib.import_module(name); catch ModuleNotFoundError.
    raise NotImplementedError("TODO: your turn")


def has_function(module_name: str, attr: str) -> bool:
    """True when the module exists and ``attr`` is a callable inside it."""
    # TODO: use safe_import and getattr(..., None).
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    math = safe_import("math")
    assert math is not None and math.sqrt(9) == 3
    assert safe_import("definitely_not_a_module_xyz") is None
    assert has_function("json", "dumps") and not has_function("json", "nope")
    assert not has_function("definitely_not_a_module_xyz", "x")


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_01_safe_import: {exc!r}")
    print("PASS ex_01_safe_import")
