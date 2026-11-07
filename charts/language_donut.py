"""Repo-language donut: proof the repository is >= 97% Python."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from arsnel.chartstyle import BLACK, SERIES, apply_style, save, terminal_title
from arsnel.langstats import MIN_PYTHON_PERCENT, breakdown
from arsnel.paths import CHARTS

PYTHON_COLOR = "#2a78d6"


def main(out_dir: Path = CHARTS) -> list[Path]:
    """Draw and save the donut; return the written files."""
    totals = breakdown()
    total = sum(totals.values()) or 1
    ordered = sorted(totals.items(), key=lambda kv: -kv[1])
    labels = [name for name, _ in ordered]
    sizes = [size for _, size in ordered]
    others = iter(c for c in SERIES if c != PYTHON_COLOR)
    colors = [PYTHON_COLOR if n == "Python" else next(others) for n in labels]
    apply_style()
    fig, ax = plt.subplots(figsize=(7.5, 6.2))
    ax.pie(
        sizes,
        colors=colors,
        startangle=90,
        counterclock=False,
        wedgeprops={"width": 0.38, "edgecolor": BLACK, "linewidth": 2},
    )
    percent = 100.0 * totals["Python"] / total
    ax.text(
        0,
        0.08,
        f"{percent:.1f}%",
        ha="center",
        va="center",
        fontsize=26,
        fontweight="bold",
    )
    ax.text(0, -0.14, "PYTHON", ha="center", va="center", fontsize=11)
    ax.legend(
        [f"{n}  {100 * s / total:.2f}%" for n, s in ordered],
        loc="lower center",
        bbox_to_anchor=(0.5, -0.12),
        ncol=2,
        fontsize=9,
    )
    terminal_title(
        fig,
        "cloc --languages",
        f"enforced: >= {MIN_PYTHON_PERCENT:.0f}% Python (tests/test_language_mix.py)",
    )
    fig.subplots_adjust(top=0.86, bottom=0.12)
    return save(fig, "language_donut", out_dir)


if __name__ == "__main__":
    for written in main():
        print("wrote", written)
