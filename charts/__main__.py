"""Draw all six charts:  python -m charts"""

from __future__ import annotations

from charts import (
    big_o,
    dependency_graph,
    language_donut,
    progress_line,
    roadmap,
    skill_radar,
)


def main() -> None:
    """Render every chart into ``assets/charts/``."""
    for module in (
        roadmap,
        big_o,
        dependency_graph,
        skill_radar,
        progress_line,
        language_donut,
    ):
        module.main()
        print("drew", module.__name__.split(".")[-1])


if __name__ == "__main__":
    main()
