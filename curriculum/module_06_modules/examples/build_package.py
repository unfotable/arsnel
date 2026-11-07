"""Create a tiny package on disk, put it on sys.path and import it."""

import importlib
import sys
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as tmp:
    root = Path(tmp)
    package = root / "greeter"
    package.mkdir()
    (package / "__init__.py").write_text(
        'from .core import greet\n\n__all__ = ["greet"]\n', encoding="utf-8"
    )
    (package / "core.py").write_text(
        'def greet(name: str) -> str:\n    return f"hello {name}"\n', encoding="utf-8"
    )

    sys.path.insert(0, tmp)
    try:
        greeter = importlib.import_module("greeter")
        print(greeter.greet("ARSNEL"))
        print(sorted(name for name in dir(greeter) if not name.startswith("__")))
    finally:
        sys.path.remove(tmp)
        for loaded in [m for m in sys.modules if m.split(".")[0] == "greeter"]:
            del sys.modules[loaded]
