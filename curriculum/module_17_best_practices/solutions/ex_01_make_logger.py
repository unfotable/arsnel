"""Exercise 17.1 - Configure a logger

Create a logger with a handler, level and format.

Run:  python ex_01_make_logger.py
"""

from __future__ import annotations

import io
import logging
from typing import TextIO


def make_logger(name: str, stream: TextIO, level: int = logging.INFO) -> logging.Logger:
    """Return a logger writing ``LEVEL:name:message`` lines to ``stream``.

    It must not propagate to the root logger and must not add duplicate handlers
    when called twice with the same name.
    """
    # TODO: getLogger, setLevel, add a StreamHandler(stream) with a Formatter once.
    # --- solution ---
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False
    if not logger.handlers:
        handler = logging.StreamHandler(stream)
        handler.setFormatter(logging.Formatter("%(levelname)s:%(name)s:%(message)s"))
        logger.addHandler(handler)
    return logger
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    stream = io.StringIO()
    log = make_logger("arsnel.ex17", stream)
    log.debug("hidden")
    log.info("hello %s", "world")
    log.error("bad")
    again = make_logger("arsnel.ex17", stream)
    again.warning("once")
    assert again is log
    lines = stream.getvalue().splitlines()
    assert lines == [
        "INFO:arsnel.ex17:hello world",
        "ERROR:arsnel.ex17:bad",
        "WARNING:arsnel.ex17:once",
    ], lines


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_01_make_logger: {exc!r}")
    print("PASS ex_01_make_logger")
