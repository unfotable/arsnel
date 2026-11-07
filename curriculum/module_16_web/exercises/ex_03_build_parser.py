"""Exercise 16.3 - Build a CLI parser

Create argparse subcommands that parse arguments the way the tool needs.

Run:  python ex_03_build_parser.py
"""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    """Return a parser for ``tool [-v] add|done|list`` subcommands.

    ``add TITLE [--priority N]``, ``done NUMBER`` and ``list``.

    ``--priority`` is an int defaulting to 1, ``NUMBER`` is an int, ``-v`` counts up
    (``-vv`` -> 2) and a command is required.
    """
    # TODO: -v uses action="count"; add subparsers with dest="command".
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    parser = build_parser()
    args = parser.parse_args(["add", "write", "--priority", "3"])
    assert (args.command, args.title, args.priority, args.verbose) == (
        "add",
        "write",
        3,
        0,
    )
    assert parser.parse_args(["add", "x"]).priority == 1
    assert parser.parse_args(["-vv", "done", "4"]).number == 4
    assert parser.parse_args(["-vv", "list"]).verbose == 2
    for bad in ([], ["done", "four"], ["nope"]):
        try:
            parser.parse_args(bad)
        except SystemExit:
            continue
        raise AssertionError(f"{bad} should be rejected")


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_03_build_parser: {exc!r}")
    print("PASS ex_03_build_parser")
