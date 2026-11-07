"""Build a recommended src-layout project in a temp dir and print it as a tree."""

import tempfile
from pathlib import Path

FILES = [
    "pyproject.toml",
    "README.md",
    "src/mypkg/__init__.py",
    "src/mypkg/core.py",
    "tests/test_core.py",
    ".gitignore",
]


def tree(root: Path) -> list[str]:
    """Return indented lines for every file below ``root`` (sorted)."""
    lines: list[str] = []
    for path in sorted(root.rglob("*")):
        depth = len(path.relative_to(root).parts) - 1
        lines.append("  " * depth + path.name + ("/" if path.is_dir() else ""))
    return lines


with tempfile.TemporaryDirectory() as tmp:
    base = Path(tmp) / "project"
    for relative in FILES:
        target = base / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.touch()
    print("project/")
    print("\n".join("  " + line for line in tree(base)))
