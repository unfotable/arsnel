"""Capstone 2: synthetic sales -> pandas aggregation -> chart + Markdown report."""

# requires: numpy, pandas, matplotlib

import tempfile
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def make_sales(seed: int = 7, rows: int = 300) -> pd.DataFrame:
    """Deterministic synthetic data."""
    rng = np.random.default_rng(seed)
    regions = ["north", "south", "east", "west"]
    return pd.DataFrame(
        {
            "region": rng.choice(regions, rows),
            "month": rng.integers(1, 13, rows),
            "units": rng.integers(1, 20, rows),
            "price": rng.choice([9.5, 14.0, 22.0], rows),
        }
    )


def summarise(sales: pd.DataFrame) -> pd.DataFrame:
    """Revenue per region and month."""
    sales = sales.assign(revenue=sales["units"] * sales["price"])
    table = sales.pivot_table(
        index="month", columns="region", values="revenue", aggfunc="sum", fill_value=0
    )
    return table.sort_index()


def plot(table: pd.DataFrame, path: Path) -> None:
    fig, ax = plt.subplots(figsize=(8, 4), constrained_layout=True)
    table.plot(ax=ax, marker="o")
    ax.set(title="Monthly revenue by region", xlabel="month", ylabel="revenue")
    fig.savefig(path, dpi=100)
    plt.close(fig)


def write_report(table: pd.DataFrame, chart: Path, path: Path) -> None:
    totals = table.sum().sort_values(ascending=False)
    lines = [
        "# Sales report",
        "",
        f"![chart]({chart.name})",
        "",
        "| region | revenue |",
        "| --- | ---: |",
    ]
    lines += [f"| {region} | {value:,.2f} |" for region, value in totals.items()]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp)
        table = summarise(make_sales())
        plot(table, out / "revenue.png")
        write_report(table, out / "revenue.png", out / "report.md")
        print((out / "report.md").read_text(encoding="utf-8"))
        print("chart written:", (out / "revenue.png").stat().st_size > 0)
