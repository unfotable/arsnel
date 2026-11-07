"""Exercise 13.2 - Validate project metadata

Check parsed pyproject data and report every problem.

Run:  python ex_02_validate_pyproject.py
"""

from __future__ import annotations

import tomllib


def validate(data: dict[str, object]) -> list[str]:
    """Return a list of problems with the ``[project]`` table (empty when valid).

    Required: ``name`` (str), ``version`` (str), ``requires-python`` (str).
    """
    # TODO: look inside data["project"]; add a message per missing/wrong field.
    # --- solution ---
    project = data.get("project")
    if not isinstance(project, dict):
        return ["missing [project] table"]
    problems: list[str] = []
    for field in ("name", "version", "requires-python"):
        value = project.get(field)
        if not isinstance(value, str) or not value:
            problems.append(f"project.{field} is required")
    return problems
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    good = tomllib.loads(
        '[project]\nname = "demo"\nversion = "0.1.0"\nrequires-python = ">=3.11"\n'
    )
    assert validate(good) == []
    partial = tomllib.loads('[project]\nname = "demo"\n')
    assert validate(partial) == [
        "project.version is required",
        "project.requires-python is required",
    ]
    assert validate({}) == ["missing [project] table"]


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_02_validate_pyproject: {exc!r}")
    print("PASS ex_02_validate_pyproject")
