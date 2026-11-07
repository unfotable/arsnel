"""ruff, black and mypy configured in pyproject.toml - validated with tomllib."""

import tomllib

PYPROJECT = """
[tool.black]
line-length = 88

[tool.ruff]
line-length = 88
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "W", "I", "B", "UP"]

[tool.mypy]
strict = true
python_version = "3.11"

[tool.pytest.ini_options]
testpaths = ["tests"]
"""

config = tomllib.loads(PYPROJECT)
for tool, settings in config["tool"].items():
    print(f"{tool:>7}: {sorted(settings)}")
print("rules:", config["tool"]["ruff"]["lint"]["select"])

COMMANDS = ["ruff check .", "black --check .", "mypy .", "pytest"]
print("CI gate:", " && ".join(COMMANDS))
