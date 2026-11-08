"""Shared matplotlib look: white paper, carbon grid, square pixel boxes."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from arsnel.paths import CHARTS

WHITE = "#ffffff"
BLACK = "#000000"
CARBON = "#232323"
BLUE = "#2a78d6"
MUTED = "#52514e"

# Validated categorical slots (blue, orange, aqua, yellow, magenta, green).
SERIES = ("#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300")

# Sequential single-hue ramp for the three levels (light -> dark).
LEVEL_COLORS = {"BEGINNER": "#cfe3fb", "INTERMEDIATE": "#8ebcf0", "ADVANCED": "#2a78d6"}

MONO = ["DejaVu Sans Mono", "Menlo", "Consolas", "monospace"]


def apply_style() -> None:
    """Install the ARSNEL matplotlib defaults (monospace, hard edges, faint grid)."""
    plt.rcParams.update(
        {
            "figure.facecolor": WHITE,
            "axes.facecolor": WHITE,
            "savefig.facecolor": WHITE,
            "font.family": "monospace",
            "font.monospace": MONO,
            "text.color": BLACK,
            "axes.edgecolor": CARBON,
            "axes.labelcolor": BLACK,
            "axes.linewidth": 1.5,
            "axes.titleweight": "bold",
            "axes.titlesize": 13,
            "axes.titlelocation": "left",
            "axes.grid": True,
            "grid.color": CARBON,
            "grid.alpha": 0.12,
            "grid.linewidth": 1.0,
            "xtick.color": CARBON,
            "ytick.color": CARBON,
            "legend.frameon": True,
            "legend.edgecolor": CARBON,
            "legend.fancybox": False,
            "legend.framealpha": 1.0,
            "lines.solid_capstyle": "butt",
        }
    )


def terminal_title(fig: Figure, text: str, subtitle: str = "") -> None:
    """Add a ``> title`` prompt heading (and optional dim subtitle) above the plot."""
    fig.text(0.015, 0.975, f"> {text}", fontsize=15, fontweight="bold", va="top")
    if subtitle:
        fig.text(0.015, 0.93, subtitle, fontsize=9, color=MUTED, va="top")


def save(fig: Figure, name: str, out_dir: Path = CHARTS) -> list[Path]:
    """Save ``fig`` as ``name.png`` and ``name.svg`` in ``out_dir``."""
    out_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for ext in ("png", "svg"):
        path = out_dir / f"{name}.{ext}"
        fig.savefig(path, dpi=150, metadata={"Date": None} if ext == "png" else None)
        paths.append(path)
    plt.close(fig)
    return paths
