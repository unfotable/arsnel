# ARSNEL - tiny task runner. Everything real lives in Python scripts.
PY ?= python

.PHONY: setup generate lint fmt test check charts progress readme site quiz clean

setup:
	$(PY) bootstrap.py
generate:
	$(PY) generate.py
lint:
	ruff check . && black --check . && mypy arsnel content charts curriculum tests *.py
fmt:
	ruff check --fix . && black .
test:
	pytest
check: lint test
	$(PY) generate.py --check
charts:
	$(PY) -m charts
progress:
	$(PY) progress.py
readme:
	$(PY) build_readme.py
site:
	$(PY) build_site.py
quiz:
	cd curriculum/module_01_syntax && $(PY) quiz.py
clean:
	$(PY) -c "import shutil,pathlib; [shutil.rmtree(p, True) for p in pathlib.Path().rglob(\"__pycache__\")]; shutil.rmtree(\"site\", True)"
