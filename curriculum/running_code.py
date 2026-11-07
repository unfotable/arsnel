"""Four ways to run Python, driven from Python with ``subprocess``.

``sys.executable`` is the exact interpreter running this script, so the child
processes always use the same Python (and the same venv).
"""

import subprocess
import sys
import tempfile
from pathlib import Path


def run(*args: str, stdin: str | None = None) -> subprocess.CompletedProcess[str]:
    """Run ``python <args>`` and capture its text output."""
    return subprocess.run(
        [sys.executable, *args],
        input=stdin,
        capture_output=True,
        text=True,
        check=False,
    )


def main() -> None:
    # 1. python -c "code": one-liners, great for quick checks.
    print("-c    :", run("-c", "print(2 ** 10)").stdout.strip())

    # 2. python -m module: run a library as a program.
    pretty = run("-m", "json.tool", stdin='{"b": 2, "a": [1, 2]}').stdout
    print("-m    :", pretty.replace("\n", " ").strip())

    # 3. python script.py args: the normal way. Exit codes report success.
    with tempfile.TemporaryDirectory() as tmp:
        script = Path(tmp) / "demo.py"
        script.write_text(
            "import sys\n"
            "print('__name__ =', __name__)\n"
            "print('args     =', sys.argv[1:])\n"
            "sys.exit(3)\n"
        )
        result = run(str(script), "one", "two")
        print(result.stdout, end="")
        print("exit code:", result.returncode, "(0 = success, anything else = error)")

    # 4. The REPL (just `python`) is interactive, so it cannot run here.
    print("REPL  : type `python`, then 2 + 2, then exit() (or Ctrl-D)")


if __name__ == "__main__":
    main()
