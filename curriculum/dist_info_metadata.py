"""Read installed-package metadata with importlib.metadata.

After ``pip install``, a package leaves a ``*.dist-info`` folder on sys.path.
``importlib.metadata`` reads it. Here we fabricate one in a temp dir so the
example works anywhere, then query it exactly like any installed package.
"""

import sys
import tempfile
from importlib import metadata
from pathlib import Path

METADATA = """\
Metadata-Version: 2.1
Name: pixel-tools
Version: 0.3.1
Summary: Small helpers for pixel art.
Requires-Python: >=3.11
Requires-Dist: pillow>=10
Requires-Dist: pytest>=8; extra == 'dev'
Provides-Extra: dev
"""
ENTRY_POINTS = "[console_scripts]\npixel = pixel_tools.cli:main\n"

with tempfile.TemporaryDirectory() as tmp:
    dist_info = Path(tmp) / "pixel_tools-0.3.1.dist-info"
    dist_info.mkdir()
    (dist_info / "METADATA").write_text(METADATA, encoding="utf-8")
    (dist_info / "entry_points.txt").write_text(ENTRY_POINTS, encoding="utf-8")

    sys.path.insert(0, tmp)  # make the fake "installation" discoverable
    try:
        dist = metadata.distribution("pixel-tools")
        print("name           :", dist.metadata["Name"])
        print("version        :", metadata.version("pixel-tools"))
        print("summary        :", dist.metadata["Summary"])
        print("requires-python:", dist.metadata["Requires-Python"])
        print("requires       :")
        for requirement in dist.requires or []:
            print("   ", requirement)
        for entry in dist.entry_points:
            print(f"entry point    : {entry.group}: {entry.name} -> {entry.value}")
    finally:
        sys.path.remove(tmp)

# Names are normalised: '-', '_' and '.' are equivalent, case is ignored.
try:
    metadata.version("definitely-not-installed-xyz")
except metadata.PackageNotFoundError as exc:
    print("missing package raises:", type(exc).__name__)

# The standard library is also introspectable the same way.
print(
    "pip installed?",
    "pip" in {d.metadata["Name"].lower() for d in metadata.distributions()}
    or "unknown",
)
