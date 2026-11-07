"""What is a wheel? Build a wheel-like zip by hand and look inside.

A real wheel (``.whl``) is just a zip with a strict layout: your package files
plus a ``<name>-<version>.dist-info/`` folder of metadata. We write one with
``zipfile`` so nothing is magic. (Use ``python -m build`` for real projects.)
"""

import base64
import hashlib
import tempfile
import zipfile
from pathlib import Path

NAME, VERSION = "greeter", "0.1.0"
DIST_INFO = f"{NAME}-{VERSION}.dist-info"
FIXED_DATE = (2020, 1, 1, 0, 0, 0)  # reproducible archives

PACKAGE_FILES = {
    f"{NAME}/__init__.py": f'__version__ = "{VERSION}"\n',
    f"{NAME}/cli.py": "def main() -> None:\n    print('hello')\n",
}
METADATA = (
    "Metadata-Version: 2.1\n"
    f"Name: {NAME}\n"
    f"Version: {VERSION}\n"
    "Summary: Greets people politely.\n"
    "Requires-Python: >=3.11\n"
)
WHEEL = (
    "Wheel-Version: 1.0\nGenerator: demo\nRoot-Is-Purelib: true\nTag: py3-none-any\n"
)
ENTRY_POINTS = "[console_scripts]\ngreet = greeter.cli:main\n"


def record_line(path: str, data: bytes) -> str:
    """One RECORD row: path, urlsafe-base64 sha256 and size."""
    digest = hashlib.sha256(data).digest()
    encoded = base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")
    return f"{path},sha256={encoded},{len(data)}"


def build_wheel(directory: Path) -> Path:
    """Write the wheel into ``directory`` and return its path."""
    contents = {
        **{p: t.encode() for p, t in PACKAGE_FILES.items()},
        f"{DIST_INFO}/METADATA": METADATA.encode(),
        f"{DIST_INFO}/WHEEL": WHEEL.encode(),
        f"{DIST_INFO}/entry_points.txt": ENTRY_POINTS.encode(),
    }
    rows = [record_line(path, data) for path, data in contents.items()]
    rows.append(f"{DIST_INFO}/RECORD,,")  # RECORD cannot hash itself
    contents[f"{DIST_INFO}/RECORD"] = ("\n".join(rows) + "\n").encode()

    # Filename convention: name-version-pythontag-abitag-platformtag.whl
    wheel_path = directory / f"{NAME}-{VERSION}-py3-none-any.whl"
    with zipfile.ZipFile(wheel_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for path, data in contents.items():
            archive.writestr(zipfile.ZipInfo(path, FIXED_DATE), data)
    return wheel_path


with tempfile.TemporaryDirectory() as tmp:
    wheel = build_wheel(Path(tmp))
    print("wheel file:", wheel.name)
    with zipfile.ZipFile(wheel) as archive:
        print("contents:")
        for name in archive.namelist():
            print("  ", name)
        print("\nMETADATA:")
        print(archive.read(f"{DIST_INFO}/METADATA").decode())
        print("RECORD:")
        print(archive.read(f"{DIST_INFO}/RECORD").decode())
        # Installing a pure-Python wheel is basically: unzip into site-packages.
        print("test zip integrity:", archive.testzip() or "ok")
