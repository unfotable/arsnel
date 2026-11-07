"""Exercise 06.3 - Print a layout tree

Turn path strings into an indented tree.

Run:  python ex_03_layout_tree.py
"""

from __future__ import annotations


def layout_tree(paths: list[str]) -> str:
    """Return an indented tree for ``paths`` (two spaces per level, folders end in /).

    Each folder is printed once, entries are sorted, and files appear after the
    folder that contains them.
    """
    # TODO: collect every folder prefix and every file, sort, then indent by depth.
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    got = layout_tree(
        ["src/pkg/__init__.py", "README.md", "src/pkg/core.py", "tests/t.py"]
    )
    assert got == "\n".join(
        [
            "README.md",
            "src/",
            "  pkg/",
            "    __init__.py",
            "    core.py",
            "tests/",
            "  t.py",
        ]
    ), got
    assert layout_tree([]) == ""


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_03_layout_tree: {exc!r}")
    print("PASS ex_03_layout_tree")
