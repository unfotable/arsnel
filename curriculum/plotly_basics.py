"""Plotly Express: interactive charts saved as standalone HTML.

Needs the optional data extra: ``pip install -e ".[data]"``.
"""

# requires: plotly

import tempfile
from pathlib import Path

import plotly.express as px

months = ["Jan", "Feb", "Mar", "Apr"]
revenue = [120, 150, 170, 210]

line = px.line(x=months, y=revenue, title="Revenue", labels={"x": "month", "y": "$"})
bars = px.bar(x=months, y=revenue, title="Revenue by month")

with tempfile.TemporaryDirectory() as tmp:
    for name, figure in (("line.html", line), ("bars.html", bars)):
        target = Path(tmp) / name
        figure.write_html(target)  # self-contained, open in any browser
        print(name, target.stat().st_size > 0)
