"""Exercise 05.1 - Clamp and stats

Practice defaults, keyword-only parameters and *args.

Run:  python ex_01_clamp_and_stats.py
"""

from __future__ import annotations


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    """Return ``value`` limited to the range ``low`` .. ``high``."""
    # TODO: return low if value < low, high if value > high, else value.
    # --- solution ---
    return max(low, min(value, high))
    # --- end ---


def summarize(*numbers: float, digits: int = 2) -> dict[str, float]:
    """Return min, max and mean of ``numbers`` (mean rounded to ``digits``)."""
    # TODO: build {"min": ..., "max": ..., "mean": ...}; raise ValueError if empty.
    # --- solution ---
    if not numbers:
        raise ValueError("need at least one number")
    mean = round(sum(numbers) / len(numbers), digits)
    return {"min": min(numbers), "max": max(numbers), "mean": mean}
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert clamp(5) == 1.0 and clamp(-3) == 0.0 and clamp(0.5) == 0.5
    assert clamp(15, 0, 10) == 10 and clamp(5, low=6, high=9) == 6
    assert summarize(1, 2, 3, 4) == {"min": 1, "max": 4, "mean": 2.5}
    assert summarize(1, 2, 2, digits=1)["mean"] == 1.7
    try:
        summarize()
    except ValueError:
        pass
    else:
        raise AssertionError("summarize() with no numbers must raise ValueError")


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_01_clamp_and_stats: {exc!r}")
    print("PASS ex_01_clamp_and_stats")
