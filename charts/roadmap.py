"""Learning-path roadmap: 19 modules along a winding trail."""

from __future__ import annotations

import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

from arsnel.chartstyle import (
    BLACK,
    CARBON,
    LEVEL_COLORS,
    apply_style,
    save,
    terminal_title,
)
from arsnel.manifest import MODULES
from arsnel.paths import CHARTS

PER_ROW = 5
SHORT = {
    0: "Setup & terminal",
    1: "Syntax, types, I/O",
    2: "Operators & loops",
    3: "Strings & f-strings",
    4: "Lists, dicts, sets",
    5: "Functions & closures",
    6: "Modules & packages",
    7: "Files & exceptions",
    8: "OOP & dataclasses",
    9: "Iterators & generators",
    10: "Decorators & typing",
    11: "Async & threads",
    12: "Testing (pytest)",
    13: "Packaging & PyPI",
    14: "Performance",
    15: "Data & viz",
    16: "Web & CLI",
    17: "Best practices & CI",
    18: "Capstone projects",
}


def positions() -> list[tuple[float, float]]:
    """Snake layout: left-to-right, then right-to-left, row by row."""
    coords = []
    for index in range(len(MODULES)):
        row, col = divmod(index, PER_ROW)
        x = col if row % 2 == 0 else PER_ROW - 1 - col
        coords.append((float(x), -float(row)))
    return coords


def main(out_dir: Path = CHARTS) -> list[Path]:
    """Draw and save the roadmap; return the written files."""
    apply_style()
    fig, ax = plt.subplots(figsize=(13, 7.4))
    ax.grid(False)
    ax.axis("off")
    pts = positions()
    for (x1, y1), (x2, y2) in zip(pts, pts[1:], strict=False):
        if y1 == y2:
            ax.plot([x1, x2], [y1, y2], color=CARBON, linewidth=5, zorder=1)
        else:  # row turn: loop around the outside so labels stay clear
            side = 0.55 if x1 > PER_ROW / 2 else -0.55
            ax.plot(
                [x1, x1 + side, x1 + side, x2],
                [y1, y1, y2, y2],
                color=CARBON,
                linewidth=5,
                zorder=1,
                solid_joinstyle="miter",
            )
    for meta, (x, y) in zip(MODULES, pts, strict=True):
        ax.text(
            x,
            y,
            f"{meta.number:02d}",
            ha="center",
            va="center",
            fontsize=15,
            fontweight="bold",
            zorder=3,
            bbox={
                "boxstyle": "square,pad=0.55",
                "fc": LEVEL_COLORS[meta.level],
                "ec": BLACK,
                "lw": 2,
            },
        )
        ax.text(
            x,
            y - 0.3,
            textwrap.fill(SHORT[meta.number], 18),
            ha="center",
            va="top",
            fontsize=8.5,
        )
    ax.text(
        pts[0][0] - 0.45, pts[0][1] + 0.38, "START >_", fontsize=9, fontweight="bold"
    )
    ax.text(
        pts[-1][0] - 0.4, pts[-1][1] + 0.38, "SHIP IT", fontsize=9, fontweight="bold"
    )
    ax.set_xlim(-0.7, PER_ROW - 0.3)
    ax.set_ylim(-4.2, 0.7)
    handles = [Patch(fc=c, ec=BLACK, label=level) for level, c in LEVEL_COLORS.items()]
    ax.legend(
        handles=handles, loc="lower left", ncol=3, fontsize=8, bbox_to_anchor=(0, -0.02)
    )
    terminal_title(
        fig,
        "arsnel --roadmap",
        "19 modules  |  beginner -> advanced  |  follow the trail",
    )
    fig.subplots_adjust(top=0.88, bottom=0.04, left=0.03, right=0.97)
    return save(fig, "roadmap", out_dir)


if __name__ == "__main__":
    for written in main():
        print("wrote", written)
