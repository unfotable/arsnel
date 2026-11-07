"""Exercise 00.4 - Simulate cd

Work out where ``cd`` lands, using pure path maths (no real folders).

Run:  python ex_04_simulate_cd.py
"""

from __future__ import annotations

import posixpath


def change_directory(cwd: str, target: str, home: str = "/home/ada") -> str:
    """Return the new working directory after ``cd target`` from ``cwd``.

    - ``""`` and ``"~"`` go home; ``"~/x"`` is ``x`` inside home.
    - An absolute target (starts with ``/``) ignores ``cwd``.
    - Otherwise ``target`` is relative to ``cwd``; ``..`` goes up, ``.`` stays.
    - You cannot go above ``/``.  The result has no trailing slash (except ``/``).
    """
    # TODO: handle "", "~" and "~/..." first by building a path from ``home``.
    # TODO: posixpath.join(cwd, target) then posixpath.normpath(...) does the rest.
    # --- solution ---
    if target in ("", "~"):
        return home
    if target.startswith("~/"):
        target = posixpath.join(home, target[2:])
    return posixpath.normpath(posixpath.join(cwd, target))
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    cd = change_directory
    assert cd("/home/ada", "docs") == "/home/ada/docs", "relative"
    assert cd("/home/ada/docs", "..") == "/home/ada", "parent"
    assert cd("/home/ada/docs", "../..") == "/home", "two parents"
    assert cd("/home", "../../..") == "/", "cannot go above the root"
    assert cd("/home/ada", "/etc/") == "/etc", "absolute, trailing slash removed"
    assert cd("/tmp", "") == "/home/ada", "bare cd goes home"
    assert cd("/tmp", "~") == "/home/ada", "~ is home"
    assert cd("/tmp", "~/src") == "/home/ada/src", "~/src"
    assert cd("/tmp", "~", home="/Users/bo") == "/Users/bo", "custom home"
    assert cd("/a/b", "./c/../d") == "/a/b/d", ". and .. inside a path"
    assert cd("/", "usr/local") == "/usr/local", "from the root"


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_04_simulate_cd: {exc!r}")
    print("PASS ex_04_simulate_cd")
