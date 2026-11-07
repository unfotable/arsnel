"""Create a virtual environment from Python and peek inside it.

``python -m venv .venv`` is the command-line spelling of ``venv.create``. We skip
pip (``with_pip=False``) so the script is fast and needs no network. Output
depends on your operating system, hence not embedded in the README.
"""

import subprocess
import sys
import tempfile
import venv
from pathlib import Path

# Windows puts executables in Scripts, macOS/Linux in bin.
SCRIPTS = "Scripts" if sys.platform == "win32" else "bin"
EXE = "python.exe" if sys.platform == "win32" else "python"


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        env_dir = Path(tmp) / ".venv"
        venv.create(env_dir, with_pip=False)
        print("created folder  :", env_dir.name)
        print("top-level items :", sorted(p.name for p in env_dir.iterdir()))

        # pyvenv.cfg is how the interpreter knows it is inside a venv.
        print("pyvenv.cfg keys :", end=" ")
        cfg = (env_dir / "pyvenv.cfg").read_text().splitlines()
        print([line.split("=")[0].strip() for line in cfg])

        # You do not need to "activate" to use it: call its python directly.
        python = env_dir / SCRIPTS / EXE
        code = "import sys; print(sys.prefix != sys.base_prefix)"
        result = subprocess.run(
            [str(python), "-c", code], capture_output=True, text=True, check=True
        )
        print("venv python says 'inside a venv':", result.stdout.strip())


if __name__ == "__main__":
    main()
