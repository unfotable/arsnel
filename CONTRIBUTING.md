# Contributing to ARSNEL

Thanks for helping people learn Python one pixel at a time. This guide gets you from
clone to pull request.

## Setup

```bash
python bootstrap.py          # venv + dependencies + generated files
source .venv/bin/activate    # Windows: .venv\Scripts\activate
make check                   # ruff, black, mypy, pytest, generator drift
```

## How the repo is organised (read this first)

ARSNEL is a **Python-only** project: the lesson text, quizzes, README, charts, ASCII
art and the website are all produced by Python. Never hand-write an HTML page, and
never edit a generated file - edit its source and regenerate.

| You want to change | Edit this | Then run |
| --- | --- | --- |
| lesson text, quiz, cheatsheet | `content/module_NN.py` | `python generate.py` |
| a runnable example | `curriculum/<module>/examples/*.py` | `python generate.py` |
| an exercise (and its stub) | `curriculum/<module>/solutions/ex_*.py` | `python generate.py` |
| top-level README | `build_readme.py` | `python build_readme.py` |
| site look and feel | `arsnel/theme.py`, `arsnel/templates.py` | `python build_site.py` |
| a chart | `charts/<name>.py` | `python -m charts` |

**Generated, do not edit:** module `README.md`, `exercises/*.py`, `quiz.py`, `README.md`,
`assets/`, `site/`. CI fails (`generate.py --check`) when they drift from their source.

## Authoring rules for every Python file

- Runs with `python file.py` from its own folder, exits 0, stdin closed (no blocking
  `input()` - use the `sys.stdin.isatty()` fallback shown in module 01).
- No network access, no writes into the repo (use `tempfile`), no GUI windows, under 20 s.
- Fully type-annotated (`-> None` too), modern syntax (`X | None`, `list[int]`, f-strings).
- PEP 8, `black` (88 columns), `ruff` clean (E, F, W, I, B, UP, SIM, C4), `mypy --strict`.
  If a lesson *intentionally* shows a bad pattern, add `# noqa: <code>` with the reason.
- A docstring at the top; comments explain *why*, not *what*.
- Examples whose output appears in the README must be deterministic and standard-library
  only (no timing, unseeded randomness, dates, absolute paths, thread ids).
- Third-party packages: add `# requires: pkg` (import names) right after the docstring
  and set `show_output=False` on the example.

## Writing an exercise

Put the answer between solution markers, **indented inside a function or method**:

```python
def double(x: int) -> int:
    """Return x times two."""
    # TODO: multiply x by two and return it.
    # --- solution ---
    return x * 2
    # --- end ---
```

The generator swaps the region for `raise NotImplementedError`, so the learner's stub
fails until solved. Every exercise needs a `check()` that tests real behaviour
(including edge cases) with helpful assertion messages. Verify a module with:

```bash
python -m arsnel.modcheck 7   # generate, run examples, solutions pass, stubs fail, lint
```

Minimums per module: 4 lessons, 3 examples, 3 exercises, 6 quiz questions.

## Keeping the repo at least 97% Python

`tests/test_language_mix.py` measures languages the way GitHub Linguist does and fails
below 97% Python. Allowed non-Python: HTML templates, CSS, minimal vanilla JS, Markdown,
YAML, `.gitignore`, `LICENSE`. Put CSS/JS/HTML inside Python strings (see `arsnel/theme.py`).

## Design system (site and charts)

White background, black text, carbon `#232323` 24px grid, Press Start 2P headings,
VT323 / IBM Plex Mono body, 1px borders, **no rounded corners**, hard shadows
`4px 4px 0 #232323`, green-on-black terminal cards, scanline overlay, dark-mode tokens.
Charts use `arsnel/chartstyle.py` (validated palette, direct labels + legend).

## Pull requests

1. Branch from `main`; keep PRs focused (one module or one feature).
2. Run `make check` and `python generate.py`; commit generated files with their source.
3. Fill in the PR template. Be kind in review - see the [Code of Conduct](CODE_OF_CONDUCT.md).

By contributing you agree your work is released under the [MIT license](LICENSE).
