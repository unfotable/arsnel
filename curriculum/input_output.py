"""Talking to the user with input() and print().

When there is no terminal attached (CI, README generation) the defaults are
used, so this script always runs to completion.
"""

import sys


def ask(prompt: str, default: str) -> str:
    """Ask a question in a real terminal, otherwise return ``default``."""
    if sys.stdin.isatty():
        return input(prompt).strip() or default
    print(f"{prompt}{default}  (default, no terminal)")
    return default


name = ask("> your name: ", "Ada")
raw_age = ask("> your age: ", "36")

# input() ALWAYS returns text. Convert it before doing maths.
age = int(raw_age)
print(f"Hello, {name}! In 10 years you will be {age + 10}.")

# Output to stderr is separate from normal output.
print("(this line goes to stderr)", file=sys.stderr)
