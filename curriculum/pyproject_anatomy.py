"""Anatomy of a pyproject.toml: parse it with the standard-library tomllib.

pyproject.toml is plain TOML. ``tomllib`` (Python 3.11+) turns it into dicts,
so you can inspect or validate a project's metadata with ordinary code.
"""

import tomllib

PYPROJECT = """
[build-system]                       # how to BUILD the project (PEP 517/518)
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]                            # what the project IS (PEP 621)
name = "pixel-tools"
version = "0.3.1"
description = "Small helpers for pixel art."
readme = "README.md"
requires-python = ">=3.11"
dependencies = ["pillow>=10", "click>=8.1"]

[project.optional-dependencies]      # extras: pip install pixel-tools[dev]
dev = ["pytest>=8", "ruff>=0.4"]

[project.scripts]                    # console commands created on install
pixel = "pixel_tools.cli:main"

[tool.ruff]                          # any tool may keep settings under [tool.*]
line-length = 88
"""

data = tomllib.loads(PYPROJECT)

print("top-level tables:", sorted(data))
print("build backend   :", data["build-system"]["build-backend"])

project = data["project"]
print(f"project         : {project['name']} {project['version']}")
print("runtime deps    :", ", ".join(project["dependencies"]))
print("extras          :", sorted(project["optional-dependencies"]))
print("dev extra       :", project["optional-dependencies"]["dev"])

# [project.scripts] maps command name -> "module:function".
for command, target in project["scripts"].items():
    module, _, function = target.partition(":")
    print(f"command '{command}' runs {function}() from module {module}")

# Tool tables are free-form: the build backend ignores them.
print("ruff line length:", data["tool"]["ruff"]["line-length"])

# TOML is strictly typed: this is a string, not a list - a classic mistake.
try:
    tomllib.loads('dependencies = "click"\nname = ')
except tomllib.TOMLDecodeError as exc:
    print("broken TOML is rejected:", type(exc).__name__)
