"""Progress over time: percent of ARSNEL completed at each recorded snapshot."""

from __future__ import annotations

import sys
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from arsnel.badges import RANKS
from arsnel.chartstyle import (
    BLACK,
    BLUE,
    CARBON,
    MUTED,
    apply_style,
    save,
    terminal_title,
)
from arsnel.paths import CHARTS
from arsnel.progress_core import load_history


def main(
    out_dir: Path = CHARTS, history: list[dict[str, object]] | None = None
) -> list[Path]:
    """Draw and save the progress line; return the written files."""
    points = history if history is not None else load_history()
    apply_style()
    fig, ax = plt.subplots(figsize=(10, 5))
    for threshold, rank in RANKS[1:]:
        ax.axhline(threshold, color=CARBON, alpha=0.25, lw=1, ls="--")
        ax.text(
            1.005,
            threshold,
            rank,
            transform=ax.get_yaxis_transform(),
            fontsize=7,
            color=MUTED,
            va="center",
        )
    if points:
        times = [datetime.fromisoformat(str(p["t"])) for p in points]
        percents = [float(str(p["percent"])) for p in points]
        ax.step(times, percents, where="post", color=BLUE, lw=3)
        ax.scatter(
            times, percents, marker="s", s=70, color=BLUE, edgecolor=BLACK, zorder=5
        )
        if len(points) == 1:
            ax.annotate(
                "you are here: solve an exercise,\nthen run `make progress`",
                (times[0], percents[0]),
                xytext=(20, 40),
                textcoords="offset points",
                fontsize=9,
                arrowprops={"arrowstyle": "-|>", "color": BLACK},
            )
        span = max(times) - min(times)
        if span < timedelta(days=1):
            # One snapshot (or several close together): zoom in instead of letting
            # matplotlib stretch the axis over years.
            centre = min(times)
            ax.set_xlim(centre - timedelta(hours=12), centre + timedelta(hours=12))
            ax.xaxis.set_major_locator(mdates.HourLocator(interval=6))
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d %H:%M"))
        else:
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    ax.set(ylim=(0, 100), ylabel="% complete")
    ax.set_title("xp over time")
    terminal_title(
        fig, "progress --history", "each point is one `make progress` snapshot"
    )
    fig.subplots_adjust(top=0.84, right=0.86, bottom=0.14)
    return save(fig, "progress_line", out_dir)


if __name__ == "__main__":
    for written in main():
        print("wrote", written)
