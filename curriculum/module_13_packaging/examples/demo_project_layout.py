"""Generate a tiny src-layout project in a temp dir and validate it.

Shows the recommended layout, a minimal pyproject.toml, and a validator that
checks the fields PyPI needs before you build.
"""

import tempfile
import tomllib
from pathlib import Path

PYPROJECT = """\
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "greeter"
version = "0.1.0"
description = "Greets people politely."
readme = "README.md"
requires-python = ">=3.11"
license = { text = "MIT" }
dependencies = []

[project.scripts]
greet = "greeter.cli:main"

[tool.setuptools.packages.find]
where = ["src"]
"""

FILES = {
    "pyproject.toml": PYPROJECT,
    "README.md": "# greeter\n\nGreets people politely.\n",
    "LICENSE": "MIT License\n",
    "src/greeter/__init__.py": '__version__ = "0.1.0"\n',
    "src/greeter/cli.py": "def main() -> None:\n    print('hello')\n",
    "tests/test_cli.py": "def test_ok() -> None:\n    assert True\n",
}

REQUIRED = ("name", "version", "description", "requires-python")


def write_project(root: Path) -> None:
    """Write every file in FILES below ``root``."""
    for relative, text in FILES.items():
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")


def validate(root: Path) -> list[str]:
    """Return a list of problems found in the project at ``root``."""
    problems: list[str] = []
    with (root / "pyproject.toml").open("rb") as handle:
        project = tomllib.load(handle).get("project", {})
    for field in REQUIRED:
        if field not in project:
            problems.append(f"missing [project] field: {field}")
    for name in ("readme", "license"):
        pointer = project.get(name)
        if isinstance(pointer, str) and not (root / pointer).exists():
            problems.append(f"{name} file not found: {pointer}")
    package = project.get("name", "").replace("-", "_")
    if not (root / "src" / package / "__init__.py").exists():
        problems.append(f"no importable package src/{package}/")
    return problems


with tempfile.TemporaryDirectory() as tmp:
    root = Path(tmp)
    write_project(root)
    print("project tree (src layout):")
    for path in sorted(root.rglob("*")):
        if path.is_file():
            print("  ", path.relative_to(root).as_posix())
    print("problems:", validate(root) or "none")

    # Break it on purpose: delete the package and the description.
    (root / "src/greeter/__init__.py").unlink()
    broken = (root / "pyproject.toml").read_text(encoding="utf-8")
    (root / "pyproject.toml").write_text(
        broken.replace('description = "Greets people politely."\n', ""),
        encoding="utf-8",
    )
    for problem in validate(root):
        print("  -", problem)
