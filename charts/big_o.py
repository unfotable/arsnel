"""Big-O complexity curves with the algorithms taught in ARSNEL."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt
import numpy as np

from arsnel.chartstyle import BLACK, MUTED, SERIES, apply_style, save, terminal_title
from arsnel.manifest import ALGORITHMS, COMPLEXITY_ORDER
from arsnel.paths import CHARTS

N = np.linspace(1, 30, 300)
CURVES = {
    "O(1)": np.ones_like(N),
    "O(log n)": np.log2(N),
    "O(n)": N,
    "O(n log n)": N * np.log2(N),
    "O(n^2)": N**2,
    "O(2^n)": 2**N,
}
LABEL_NUDGE = {"O(1)": -9, "O(log n)": 8, "O(n)": 10}
STYLES = ("-", "--", "-.", ":", "-", "--")


def main(out_dir: Path = CHARTS) -> list[Path]:
    """Draw and save the Big-O chart; return the written files."""
    apply_style()
    fig, (ax, side) = plt.subplots(
        1, 2, figsize=(13, 6.2), gridspec_kw={"width_ratios": [1.6, 1]}
    )
    ymax = 400
    for (label, curve), color, style in zip(
        CURVES.items(), SERIES, STYLES, strict=True
    ):
        ax.plot(
            N,
            np.minimum(curve, ymax * 2),
            color=color,
            linestyle=style,
            lw=2.6,
            label=label,
        )
        visible = np.where(curve <= ymax)[0]
        x_end = N[visible[-1]] if len(visible) else N[-1]
        y_end = min(curve[visible[-1]] if len(visible) else ymax, ymax)
        ax.text(
            min(x_end, 29.2) + 0.2, y_end, label, color=BLACK, fontsize=9, va="center"
        )
    ax.set(xlim=(1, 33), ylim=(-18, ymax), xlabel="input size n", ylabel="operations")
    ax.legend(loc="upper left", fontsize=9)
    ax.set_title("growth of work")

    side.axis("off")
    side.grid(False)
    side.set_title("taught in ARSNEL")
    y = 0.97
    for complexity, color in zip(COMPLEXITY_ORDER, SERIES, strict=True):
        side.text(
            0.0,
            y,
            complexity,
            fontsize=11,
            fontweight="bold",
            color=BLACK,
            va="top",
            bbox={"boxstyle": "square,pad=0.25", "fc": "white", "ec": color, "lw": 2.5},
        )
        y -= 0.065
        for label, kind, module in ALGORITHMS:
            if kind == complexity:
                side.text(
                    0.04,
                    y,
                    f"- {label}  (module {module:02d})",
                    fontsize=8.5,
                    color=MUTED,
                    va="top",
                )
                y -= 0.05
        y -= 0.02
    terminal_title(
        fig,
        "big_o --chart",
        "work grows with n: pick the right algorithm and container",
    )
    fig.subplots_adjust(top=0.86, bottom=0.1, left=0.07, right=0.98, wspace=0.08)
    return save(fig, "big_o", out_dir)


if __name__ == "__main__":
    for written in main():
        print("wrote", written)
