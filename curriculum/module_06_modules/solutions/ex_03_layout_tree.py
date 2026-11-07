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
    # --- solution ---
    entries: set[tuple[str, ...]] = set()
    for path in paths:
        parts = tuple(path.strip("/").split("/"))
        for end in range(1, len(parts) + 1):
            entries.add(parts[:end])
    folders = {entry[:end] for entry in entries for end in range(1, len(entry))}
    lines = []
    for entry in sorted(entries):
        suffix = "/" if entry in folders else ""
        lines.append("  " * (len(entry) - 1) + entry[-1] + suffix)
    return "\n".join(lines)
    # --- end ---


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
