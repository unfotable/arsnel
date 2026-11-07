"""Exercise 18.2 - Markdown table

Render report rows as a Markdown table.

Run:  python ex_02_markdown_table.py
"""

from __future__ import annotations


def markdown_table(rows: list[dict[str, object]], columns: list[str]) -> str:
    """Render ``rows`` as a Markdown table with the given ``columns`` (in order).

    Floats use 2 decimals; missing keys become empty cells; no rows -> header only.
    """

    # TODO: header line, separator line "| --- | --- |", then one line per row.
    # --- solution ---
    def cell(value: object) -> str:
        if value is None:
            return ""
        return f"{value:.2f}" if isinstance(value, float) else str(value)

    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(cell(row.get(c)) for c in columns) + " |")
    return "\n".join(lines)
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    got = markdown_table(
        [{"region": "north", "revenue": 12.5}, {"region": "south"}],
        ["region", "revenue"],
    )
    assert got == "\n".join(
        [
            "| region | revenue |",
            "| --- | --- |",
            "| north | 12.50 |",
            "| south |  |",
        ]
    ), got
    assert markdown_table([], ["a"]) == "| a |\n| --- |"


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_02_markdown_table: {exc!r}")
    print("PASS ex_02_markdown_table")
