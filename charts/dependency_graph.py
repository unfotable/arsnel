"""Concept dependency graph: what you must know before each concept."""

from __future__ import annotations

import sys
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
from arsnel.manifest import CONCEPTS, get_module
from arsnel.paths import CHARTS


def layout() -> dict[str, tuple[float, float]]:
    """Column = module number, rows stacked and centred within the column."""
    columns: dict[int, list[str]] = {}
    for concept in CONCEPTS:
        columns.setdefault(concept.module, []).append(concept.name)
    coords: dict[str, tuple[float, float]] = {}
    for module, names in columns.items():
        for index, name in enumerate(names):
            coords[name] = (float(module), ((len(names) - 1) / 2 - index) * 1.25)
    return coords


def direct_edges() -> list[tuple[str, str]]:
    """Prerequisite edges with redundant ones removed (transitive reduction)."""
    requires = {c.name: set(c.requires) for c in CONCEPTS}
    cache: dict[str, set[str]] = {}

    def ancestors(name: str) -> set[str]:
        if name not in cache:
            found: set[str] = set()
            for parent in requires[name]:
                found |= {parent} | ancestors(parent)
            cache[name] = found
        return cache[name]

    edges = []
    for concept in CONCEPTS:
        for parent in concept.requires:
            others = requires[concept.name] - {parent}
            if not any(parent in ancestors(other) for other in others):
                edges.append((parent, concept.name))
    return edges


def main(out_dir: Path = CHARTS) -> list[Path]:
    """Draw and save the dependency graph; return the written files."""
    apply_style()
    fig, ax = plt.subplots(figsize=(17, 8.5))
    ax.axis("off")
    ax.grid(False)
    pos = layout()
    for required, name in direct_edges():
        if True:
            x1, y1 = pos[required]
            x2, y2 = pos[name]
            ax.annotate(
                "",
                xy=(x2, y2),
                xytext=(x1, y1),
                arrowprops={
                    "arrowstyle": "-|>",
                    "color": CARBON,
                    "alpha": 0.55,
                    "lw": 1,
                    "shrinkA": 16,
                    "shrinkB": 16,
                    "connectionstyle": "arc3,rad=0.08",
                },
                zorder=1,
            )
    for concept in CONCEPTS:
        x, y = pos[concept.name]
        level = get_module(concept.module).level
        ax.text(
            x,
            y,
            concept.name,
            ha="center",
            va="center",
            fontsize=7.2,
            zorder=3,
            bbox={
                "boxstyle": "square,pad=0.3",
                "fc": LEVEL_COLORS[level],
                "ec": BLACK,
                "lw": 1.2,
            },
        )
    for module in range(19):
        ax.text(
            module, -2.45, f"{module:02d}", ha="center", fontsize=9, fontweight="bold"
        )
    ax.set_xlim(-0.8, 18.8)
    ax.set_ylim(-2.8, 2.5)
    handles = [Patch(fc=c, ec=BLACK, label=lv) for lv, c in LEVEL_COLORS.items()]
    ax.legend(handles=handles, loc="upper left", ncol=3, fontsize=8)
    terminal_title(
        fig, "deps --graph", "arrow = 'learn this first'  |  column = module number"
    )
    fig.subplots_adjust(top=0.88, bottom=0.03, left=0.01, right=0.99)
    return save(fig, "dependency_graph", out_dir)


if __name__ == "__main__":
    for written in main():
        print("wrote", written)
