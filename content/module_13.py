"""Module 13 content: packaging, pyproject.toml and publishing to PyPI."""

from __future__ import annotations

from arsnel.models import Example, Exercise, Lesson, ModuleContent, Question

CONTENT = ModuleContent(
    number=13,
    intro="A folder of scripts becomes a real package when it has metadata, a layout and a build. You will learn pyproject.toml, versioning and what actually happens when you publish to PyPI.",
    lessons=(
        Lesson(
            "Project layout",
            """
```text
my-package/
  pyproject.toml
  README.md
  LICENSE
  src/my_package/__init__.py
  tests/
```

The **src layout** prevents accidentally importing the uninstalled copy and forces you to test the installed package.
Install your own project in editable mode while developing: `python -m pip install -e .`
""",
        ),
        Lesson(
            "pyproject.toml",
            """
```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "my-package"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["requests>=2"]

[project.optional-dependencies]
dev = ["pytest"]

[project.scripts]
mytool = "my_package.cli:main"
```

`[build-system]` says *how to build*, `[project]` says *what it is*, `[tool.*]` configures tools.
Parse it yourself with the standard-library `tomllib`.
""",
        ),
        Lesson(
            "Versions and distributions",
            """
Use **Semantic Versioning**: `MAJOR.MINOR.PATCH` - breaking change / new feature / bug fix.
Build with `python -m build`, which produces:

- an **sdist** (`.tar.gz`, source) and
- a **wheel** (`.whl`) - a zip with your code plus a `*.dist-info/` metadata folder.

Pip prefers wheels because installing is just unzipping.
""",
        ),
        Lesson(
            "Publishing",
            """
```bash
python -m pip install build twine
python -m build
twine check dist/*
twine upload --repository testpypi dist/*   # rehearse first
twine upload dist/*
```

Prefer **trusted publishing** (OIDC) from GitHub Actions over long-lived API tokens.
You cannot re-upload the same version: bump it. Never publish secrets.
""",
        ),
    ),
    examples=(
        Example(
            "demo_project_layout.py",
            "Generate a src-layout project",
            "Create and validate a tiny project in a temp dir.",
            False,
        ),
        Example(
            "pyproject_anatomy.py",
            "Anatomy of pyproject.toml",
            "Parse it with tomllib.",
            False,
        ),
        Example(
            "semver_parser.py", "A SemVer parser", "Parse, compare and bump versions."
        ),
        Example(
            "wheel_anatomy.py",
            "What is a wheel?",
            "Build a wheel-like zip and look inside.",
            False,
        ),
        Example(
            "dist_info_metadata.py",
            "Package metadata",
            "Read installed metadata with importlib.metadata.",
            False,
        ),
    ),
    exercises=(
        Exercise(
            "ex_01_version_tools.py",
            "Version tools",
            "parse and bump MAJOR.MINOR.PATCH.",
            2,
        ),
        Exercise(
            "ex_02_validate_pyproject.py",
            "Validate metadata",
            "report every problem in [project].",
            2,
        ),
        Exercise(
            "ex_03_wheel_zip.py", "Wheel-like zip", "write and list a zip archive.", 1
        ),
    ),
    quiz=(
        Question(
            "Which file configures modern Python packaging?",
            (
                "setup.cfg only",
                "pyproject.toml",
                "requirements.txt",
                "MANIFEST.in only",
            ),
            1,
            "PEP 517/621 made pyproject.toml the standard.",
        ),
        Question(
            "What is a wheel?",
            (
                "A virtual environment",
                "A zip archive ready to install",
                "A Git tag",
                "A compiled .exe",
            ),
            1,
            "A .whl is a zip with code and dist-info metadata.",
        ),
        Question(
            "In SemVer, a breaking change bumps which number?",
            ("PATCH", "MINOR", "MAJOR", "None"),
            2,
            "MAJOR signals incompatible API changes.",
        ),
        Question(
            "Why use the src layout?",
            (
                "It is faster",
                "It stops tests importing uncommitted source by accident",
                "It is required by PyPI",
                "It hides code",
            ),
            1,
            "You must install the package to import it.",
        ),
        Question(
            "What command builds sdist and wheel?",
            ("python -m build", "pip build", "twine build", "python setup"),
            0,
            "The build frontend creates both distributions.",
        ),
        Question(
            "Where do console-script entry points go?",
            ("[project.scripts]", "[build-system]", "[tool.black]", "[project.urls]"),
            0,
            "Each name maps to module:function.",
        ),
        Question(
            "Can you overwrite version 1.0.0 on PyPI after uploading?",
            (
                "Yes with --force",
                "No, publish a new version",
                "Only on weekends",
                "Yes within an hour",
            ),
            1,
            "PyPI files are immutable.",
        ),
    ),
    cheatsheet=(
        "`pyproject.toml`: [build-system], [project], [tool.*]",
        "`python -m pip install -e .` editable install",
        "`python -m build` -> sdist + wheel",
        "`twine check` then `twine upload`",
        "MAJOR.MINOR.PATCH",
        "`tomllib.loads(text)` to read TOML",
    ),
    next_steps="Next: measure and improve speed in module 14.",
)
