"""Exercise 00.1 - Parse a command line

Split a shell command into program, positional arguments and flags.

Run:  python ex_01_parse_command.py
"""

from __future__ import annotations

import shlex


def parse_command(line: str) -> tuple[str, list[str], list[str]]:
    """Return ``(program, arguments, flags)`` for a shell-style command line.

    Words starting with ``-`` are flags (a lone ``-`` is an argument, as in
    ``cat -``). Quotes group words: ``echo "a b"`` has the argument ``a b``.
    An empty or blank line gives ``("", [], [])``.
    """
    # TODO: shlex.split(line) understands quotes - use it instead of str.split.
    # TODO: the first word is the program; sort the rest into two lists.
    # --- solution ---
    words = shlex.split(line)
    if not words:
        return "", [], []
    program = words[0]
    arguments: list[str] = []
    flags: list[str] = []
    for word in words[1:]:
        if word.startswith("-") and word != "-":
            flags.append(word)
        else:
            arguments.append(word)
    return program, arguments, flags
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert parse_command("ls -la") == ("ls", [], ["-la"]), "ls -la"
    assert parse_command("python app.py --debug data.csv") == (
        "python",
        ["app.py", "data.csv"],
        ["--debug"],
    ), "flags and arguments must be separated, keeping their order"
    assert parse_command('git commit -m "first commit"') == (
        "git",
        ["commit", "first commit"],
        ["-m"],
    ), "quoted text is ONE argument"
    assert parse_command("echo 'a  b'") == ("echo", ["a  b"], []), "keep inner spaces"
    assert parse_command("cat -") == ("cat", ["-"], []), "a lone '-' is an argument"
    assert parse_command("   ") == ("", [], []), "blank line"
    assert parse_command("") == ("", [], []), "empty line"
    assert parse_command("pwd") == ("pwd", [], []), "program only"


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_01_parse_command: {exc!r}")
    print("PASS ex_01_parse_command")
