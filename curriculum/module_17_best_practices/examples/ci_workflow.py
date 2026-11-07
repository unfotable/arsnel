"""A GitHub Actions workflow that runs the quality gate, printed from a string."""

WORKFLOW = """\
name: ci
on: [push, pull_request]
jobs:
  quality:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12", "3.13"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: python -m pip install -e ".[dev]"
      - run: ruff check .
      - run: black --check .
      - run: mypy .
      - run: pytest
"""

print(WORKFLOW)
steps = [
    line.strip()[2:] for line in WORKFLOW.splitlines() if line.strip().startswith("- ")
]
print(f"{len(steps)} steps; fail fast on the first red check:")
for step in steps:
    print("  *", step)
