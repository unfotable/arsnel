"""Verify one module end to end: ``python -m arsnel.modcheck 07``.

Checks (in order): generate files, run every example, solutions pass, stubs fail,
quiz data sanity, then ruff, black --check and mypy on the module's files.
Scripts declaring ``# requires: pkg`` for a package that is not installed are
skipped (and reported), never silently passed.
"""

from __future__ import annotations

import importlib.util
import os
import shutil
import subprocess
import sys
from collections.abc import Sequence
from pathlib import Path

from arsnel.manifest import get_module
from arsnel.paths import CURRICULUM, ROOT
from arsnel.scaffold import ScaffoldError, generate, required_modules


def run_script(path: Path, timeout: float = 120.0) -> tuple[int, str]:
    """Run ``path`` in its folder with no stdin; return ``(exit_code, output)``."""
    env = {**os.environ, "PYTHONHASHSEED": "0", "PYTHONDONTWRITEBYTECODE": "1"}
    try:
        proc = subprocess.run(
            [sys.executable, path.name],
            cwd=path.parent,
            env=env,
            stdin=subprocess.DEVNULL,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return 124, "timeout"
    return proc.returncode, (proc.stdout + proc.stderr)[-600:]


def missing_requirements(path: Path) -> list[str]:
    """Return declared third-party modules that are not importable."""
    names = required_modules(path.read_text(encoding="utf-8"))
    return [n for n in names if importlib.util.find_spec(n) is None]


def _tool(*args: str) -> str:
    """Run a dev tool (binary on PATH, else ``python -m``); return failure output."""
    exe = shutil.which(args[0])
    command = [exe, *args[1:]] if exe else [sys.executable, "-m", *args]
    proc = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return "" if proc.returncode == 0 else (proc.stdout + proc.stderr)[-1500:]


def check_module(number: int) -> tuple[list[str], list[str]]:
    """Return ``(problems, notes)`` for module ``number``."""
    meta = get_module(number)
    base = CURRICULUM / meta.dirname
    problems: list[str] = []
    notes: list[str] = []
    try:
        generate(only=number)
        if generate(only=number, check=True):
            problems.append("generated files unstable (second run changed them)")
    except ScaffoldError as exc:
        return [f"generate: {exc}"], notes

    for path in sorted((base / "examples").glob("*.py")):
        if missing := missing_requirements(path):
            notes.append(f"SKIPPED examples/{path.name} (needs {', '.join(missing)})")
            continue
        code, out = run_script(path)
        if code != 0:
            problems.append(f"example {path.name} exited {code}: {out}")
    for path in sorted((base / "solutions").glob("ex_*.py")):
        if missing := missing_requirements(path):
            notes.append(f"SKIPPED solutions/{path.name} (needs {', '.join(missing)})")
            continue
        code, out = run_script(path)
        if code != 0:
            problems.append(f"solution {path.name} FAILS: {out}")
        stub = base / "exercises" / path.name
        stub_code, _ = run_script(stub)
        if stub_code == 0:
            problems.append(f"stub {path.name} PASSES without being solved")
    from content import load

    content = load(number)
    if content is None:
        problems.append("content module missing")
    else:
        if len(content.lessons) < 4:
            problems.append("need at least 4 lessons")
        if len(content.examples) < 3:
            problems.append("need at least 3 examples")
        if len(content.exercises) < 3:
            problems.append("need at least 3 exercises")
        if len(content.quiz) < 6:
            problems.append("need at least 6 quiz questions")
        for q in content.quiz:
            if not 0 <= q.answer < len(q.choices) or len(q.choices) < 3:
                problems.append(f"bad quiz question: {q.prompt[:40]}")
    targets = [str(base), f"content/module_{meta.mid}.py"]
    for name, args in (
        ("ruff", ("ruff", "check", *targets)),
        ("black", ("black", "--check", "-q", *targets)),
        ("mypy", ("mypy", *targets)),
    ):
        if report := _tool(*args):
            problems.append(f"{name}:\n{report}")
    return problems, notes


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point."""
    numbers = [int(a) for a in (argv if argv is not None else sys.argv[1:])]
    if not numbers:
        print("usage: python -m arsnel.modcheck N [N ...]")
        return 2
    failed = False
    for number in numbers:
        problems, notes = check_module(number)
        label = get_module(number).prompt
        for note in notes:
            print(f"[note] {label}: {note}")
        if problems:
            failed = True
            print(f"[FAIL] {label}")
            for problem in problems:
                print(f"   - {problem}")
        else:
            print(f"[ OK ] {label}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
