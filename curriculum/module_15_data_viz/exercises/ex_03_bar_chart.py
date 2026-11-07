"""Exercise 15.3 - Save a bar chart

Draw with matplotlib's object-oriented API and write a PNG.

Run:  python ex_03_bar_chart.py
"""

# requires: matplotlib

from __future__ import annotations

import tempfile
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


def save_bar_chart(data: dict[str, float], path: Path, title: str = "") -> Path:
    """Draw ``data`` as a bar chart (keys on x) and save it to ``path``."""
    # TODO: fig, ax = plt.subplots(); ax.bar(...); ax.set_title(...); fig.savefig(path).
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp) / "bars.png"
        result = save_bar_chart({"a": 3, "b": 5}, target, title="demo")
        assert result == target and target.exists()
        assert target.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n", "not a PNG file"


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_03_bar_chart: {exc!r}")
    print("PASS ex_03_bar_chart")
