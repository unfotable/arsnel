"""Module 15 content: data and visualisation with pandas, matplotlib and Plotly."""

from __future__ import annotations

from arsnel.models import Example, Exercise, Lesson, ModuleContent, Question

CONTENT = ModuleContent(
    number=15,
    intro="Data work is Python's superpower. You will load and reshape tables with pandas, summarise them with groupby and pivot tables, and turn numbers into pictures with matplotlib (static) and Plotly (interactive). These libraries come from the optional data extra.",
    lessons=(
        Lesson(
            "pandas: Series and DataFrames",
            """
```python
import pandas as pd
df = pd.read_csv("sales.csv")            # or io.StringIO(text)
df.head(); df.shape; df.dtypes; df.describe()
df["revenue"] = df["units"] * df["price"]
df.loc[df["price"] > 10, ["product", "price"]]   # label/boolean selection
df.iloc[0:2, 0:2]                                 # positional selection
```

A **DataFrame** is a table of named columns (each a **Series**). Operations are *vectorised*: write
`df["a"] * df["b"]`, not a loop. Install the extras with `pip install -e ".[data]"`.
""",
        ),
        Lesson(
            "Cleaning, grouping and joining",
            """
```python
df.isna().sum(); df.dropna(subset=["units"]); df.fillna({"units": 0})
df.groupby("region")["revenue"].sum().sort_values(ascending=False)
df.groupby("product").agg(units=("units", "sum"), avg=("price", "mean"))
df.merge(other, on="region", how="left")
df.pivot_table(index="region", columns="product", values="revenue", aggfunc="sum")
```

Think **split -> apply -> combine**. Methods return new frames; assign the result. Use `.copy()` before modifying a slice.
""",
        ),
        Lesson(
            "matplotlib",
            """
```python
import matplotlib
matplotlib.use("Agg")                  # render to files; no window
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 4), constrained_layout=True)
ax.plot(x, y, label="sin"); ax.bar(names, values); ax.scatter(a, b); ax.hist(data, bins=20)
ax.set(title="...", xlabel="x", ylabel="y"); ax.legend()
fig.savefig("chart.png", dpi=150); plt.close(fig)
```

Prefer the object-oriented API (`fig`, `ax`) over `plt.plot` state machines. Label axes, title the chart, and
keep colour and ink meaningful. PNG for slides, SVG for crisp scaling.
""",
        ),
        Lesson(
            "Plotly",
            """
```python
import plotly.express as px
fig = px.line(df, x="month", y="revenue", color="region", title="Revenue")
fig.write_html("revenue.html")        # a standalone interactive page
```

Plotly Express builds hover, zoom and legends for free from a DataFrame. It lives in the same optional
`data` extra. Use matplotlib for print/static, Plotly for exploration and dashboards.
""",
        ),
    ),
    examples=(
        Example(
            "pandas_basics.py",
            "pandas basics",
            "Load CSV text, select, filter, sort and inspect missing data.",
            False,
        ),
        Example(
            "pandas_groupby.py",
            "groupby, merge, pivot",
            "Aggregate and join tables.",
            False,
        ),
        Example(
            "matplotlib_basics.py",
            "matplotlib figures",
            "Line, bar, scatter and histogram saved as PNG and SVG.",
            False,
        ),
        Example(
            "plotly_basics.py",
            "Plotly Express",
            "Interactive charts saved as HTML.",
            False,
        ),
    ),
    exercises=(
        Exercise(
            "ex_01_clean_sales.py",
            "Clean a sales table",
            "dropna, a new column and reset_index.",
            2,
        ),
        Exercise(
            "ex_02_group_totals.py",
            "Totals per group",
            "groupby, sort and plain-Python results.",
            2,
        ),
        Exercise(
            "ex_03_bar_chart.py", "Save a bar chart", "matplotlib's OO API to a PNG.", 2
        ),
    ),
    quiz=(
        Question(
            "What is a DataFrame?",
            (
                "A list of lists only",
                "A table of labelled columns",
                "A plot",
                "A dictionary key",
            ),
            1,
            "Each column is a Series with its own dtype.",
        ),
        Question(
            "What does `df.loc[df['price'] > 10, 'product']` do?",
            (
                "Selects by position",
                "Selects rows by a condition and the product column",
                "Sorts",
                "Drops rows",
            ),
            1,
            "loc uses labels and boolean masks.",
        ),
        Question(
            "What does groupby follow?",
            (
                "Loop, append, return",
                "Split, apply, combine",
                "Sort, merge, plot",
                "Read, write, close",
            ),
            1,
            "Split into groups, apply a function, combine results.",
        ),
        Question(
            "Why call `matplotlib.use('Agg')` in scripts?",
            (
                "Colours",
                "Render to files without a GUI",
                "Speed up pandas",
                "Enable animation",
            ),
            1,
            "Agg is a non-interactive backend.",
        ),
        Question(
            "Which method fills missing values?",
            ("df.fillna(...)", "df.fix(...)", "df.nan(...)", "df.repair(...)"),
            0,
            "fillna replaces NaN, dropna removes rows.",
        ),
        Question(
            "What does `merge(..., how='left')` keep?",
            (
                "Only matching rows",
                "All rows of the left table",
                "All rows of both",
                "Nothing",
            ),
            1,
            "Left join keeps every left row; unmatched right values become NaN.",
        ),
        Question(
            "Which library makes interactive HTML charts?",
            ("matplotlib", "Plotly", "random", "json"),
            1,
            "Plotly writes standalone interactive HTML.",
        ),
    ),
    cheatsheet=(
        "`pd.read_csv`, `df.head/shape/dtypes/describe`",
        "`df.loc[mask, cols]`, `df.iloc[r, c]`",
        "`df.groupby(k)[col].sum()`, `merge`, `pivot_table`",
        "`dropna`, `fillna`, `isna`",
        "`fig, ax = plt.subplots()` then `ax.plot/bar/hist`",
        "`px.line(df, x=..., y=...)` -> `write_html`",
    ),
    next_steps="Next: serve data over HTTP in module 16.",
)
