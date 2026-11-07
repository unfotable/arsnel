"""Exercise 06.2 - Make a package

Create a package directory and import it.

Run:  python ex_02_make_package.py
"""

from __future__ import annotations

import importlib
import sys
import tempfile
from pathlib import Path


def make_package(root: Path, name: str, modules: dict[str, str]) -> Path:
    """Create ``root/name/`` with an ``__init__.py`` and one file per module.

    ``modules`` maps a module name (no ``.py``) to its source text.
    """
    # TODO: mkdir the package, write __init__.py (empty) and each module file.
    # --- solution ---
    package = root / name
    package.mkdir(parents=True, exist_ok=True)
    (package / "__init__.py").write_text("", encoding="utf-8")
    for module, source in modules.items():
        (package / f"{module}.py").write_text(source, encoding="utf-8")
    return package
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        package = make_package(
            root, "demo_pkg_ex", {"maths": "def two() -> int:\n    return 2\n"}
        )
        assert (package / "__init__.py").is_file() and (package / "maths.py").is_file()
        sys.path.insert(0, tmp)
        try:
            module = importlib.import_module("demo_pkg_ex.maths")
            assert module.two() == 2
        finally:
            sys.path.remove(tmp)
            for loaded in [m for m in sys.modules if m.startswith("demo_pkg_ex")]:
                del sys.modules[loaded]


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_02_make_package: {exc!r}")
    print("PASS ex_02_make_package")
