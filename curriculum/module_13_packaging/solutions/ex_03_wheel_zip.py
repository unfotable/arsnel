"""Exercise 13.3 - Build a wheel-like zip

A wheel is a zip file: write one and list its contents.

Run:  python ex_03_wheel_zip.py
"""

from __future__ import annotations

import tempfile
import zipfile
from pathlib import Path


def make_archive(path: Path, files: dict[str, str]) -> None:
    """Write ``files`` (name -> text) into a zip archive at ``path``."""
    # TODO: open a ZipFile in "w" mode with ZIP_DEFLATED and writestr each file.
    # --- solution ---
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
        for name, text in files.items():
            archive.writestr(name, text)
    # --- end ---


def list_members(path: Path) -> list[str]:
    """Return the archive's member names, sorted."""
    # TODO: open the zip for reading and return sorted(namelist()).
    # --- solution ---
    with zipfile.ZipFile(path) as archive:
        return sorted(archive.namelist())
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    with tempfile.TemporaryDirectory() as tmp:
        wheel = Path(tmp) / "demo-0.1.0-py3-none-any.whl"
        make_archive(
            wheel,
            {
                "demo/__init__.py": "VERSION = '0.1.0'\n",
                "demo-0.1.0.dist-info/METADATA": "Name: demo\n",
            },
        )
        assert zipfile.is_zipfile(wheel)
        assert list_members(wheel) == [
            "demo-0.1.0.dist-info/METADATA",
            "demo/__init__.py",
        ]


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_03_wheel_zip: {exc!r}")
    print("PASS ex_03_wheel_zip")
