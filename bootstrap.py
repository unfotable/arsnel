"""One-command ARSNEL setup:  python bootstrap.py [--no-venv] [--extras all]

Creates ``.venv``, installs the package in editable mode with the chosen
extras, regenerates module files and prints what to do next.  Uses only the
standard library, so it works on a fresh clone.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import venv
from collections.abc import Sequence
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV = ROOT / ".venv"
MIN_PYTHON = (3, 11)


def venv_python() -> Path:
    """Path of the interpreter inside ``.venv`` (platform aware)."""
    sub = "Scripts/python.exe" if sys.platform == "win32" else "bin/python"
    return VENV / sub


def run(command: list[str]) -> None:
    """Run a command in the repo root, echoing it first."""
    print("$", " ".join(command))
    subprocess.run(command, cwd=ROOT, check=True)


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Set up ARSNEL.")
    parser.add_argument("--no-venv", action="store_true", help="install in place")
    parser.add_argument(
        "--extras", default="dev,data,web", help="pip extras (default: dev,data,web)"
    )
    args = parser.parse_args(argv)

    if sys.version_info < MIN_PYTHON:
        need = ".".join(map(str, MIN_PYTHON))
        print(f"ARSNEL needs Python {need}+ (found {sys.version.split()[0]})")
        return 1
    if args.no_venv:
        python = Path(sys.executable)
    else:
        if not VENV.exists():
            print(f"creating {VENV.name}/ ...")
            venv.EnvBuilder(with_pip=True).create(VENV)
        python = venv_python()
    run([str(python), "-m", "pip", "install", "--quiet", "--upgrade", "pip"])
    run([str(python), "-m", "pip", "install", "--quiet", "-e", f".[{args.extras}]"])
    run([str(python), "generate.py"])
    run([str(python), "progress.py", "--no-run"])
    activate = (
        r".venv\Scripts\activate"
        if sys.platform == "win32"
        else ("source .venv/bin/activate")
    )
    print("\nARSNEL is ready.  Next:")
    print(f"  {activate}")
    print("  cd curriculum/module_00_setup && python examples/running_code.py")
    print("  make progress   # after solving exercises")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
