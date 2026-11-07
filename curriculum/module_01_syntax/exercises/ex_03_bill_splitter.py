"""Exercise 01.3 - Bill splitter

Combine ints, floats, rounding and type conversion.

Run:  python ex_03_bill_splitter.py
"""

from __future__ import annotations


def split_bill(total: float, people: int, tip_percent: float = 0.0) -> float:
    """Return what each person pays, rounded to 2 decimals.

    The tip is a percentage of ``total`` that is added before splitting.
    """
    # TODO: add the tip to the total, divide by the people, round to 2 decimals.
    raise NotImplementedError("TODO: your turn")


def describe_value(value: object) -> str:
    """Name the kind of value: 'flag', 'whole number', 'decimal', 'text' or 'nothing'.

    Remember that ``bool`` is a subclass of ``int`` - check it first!
    """
    # TODO: use isinstance() (check bool before int) and return one of the labels.
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert split_bill(100, 4) == 25.0
    assert split_bill(90, 3, 10) == 33.0
    assert split_bill(50, 3) == 16.67
    assert describe_value(True) == "flag"
    assert describe_value(7) == "whole number"
    assert describe_value(7.0) == "decimal"
    assert describe_value("7") == "text"
    assert describe_value(None) == "nothing"


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_03_bill_splitter: {exc!r}")
    print("PASS ex_03_bill_splitter")
