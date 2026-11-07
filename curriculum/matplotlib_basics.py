"""matplotlib's object-oriented API: figures, axes, and saving to files."""

# requires: matplotlib, numpy

import tempfile
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # render to files, no window

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
rng = np.random.default_rng(seed=42)

fig, axes = plt.subplots(2, 2, figsize=(8, 6), constrained_layout=True)
axes[0, 0].plot(x, np.sin(x), label="sin")
axes[0, 0].plot(x, np.cos(x), label="cos", linestyle="--")
axes[0, 0].set(title="Lines", xlabel="x", ylabel="y")
axes[0, 0].legend()
axes[0, 1].bar(["a", "b", "c"], [3, 7, 5], color="black")
axes[0, 1].set_title("Bars")
axes[1, 0].scatter(rng.normal(size=50), rng.normal(size=50))
axes[1, 0].set_title("Scatter")
axes[1, 1].hist(rng.normal(size=500), bins=20)
axes[1, 1].set_title("Histogram")

with tempfile.TemporaryDirectory() as tmp:
    for name in ("chart.png", "chart.svg"):
        fig.savefig(Path(tmp) / name, dpi=100)
    print([(Path(tmp) / n).stat().st_size > 0 for n in ("chart.png", "chart.svg")])
plt.close(fig)
