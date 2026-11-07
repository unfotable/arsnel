"""Exercise 00.2 - Venv activation command

Build the right "activate this virtual environment" command for each OS.

Run:  python ex_02_activation_command.py
"""

from __future__ import annotations


def activation_command(system: str, shell: str = "", venv_dir: str = ".venv") -> str:
    """Return the command that activates ``venv_dir``.

    ``system`` is what ``platform.system()`` returns: ``"Linux"``, ``"Darwin"``
    (macOS) or ``"Windows"``; anything else raises ``ValueError``.

    - Linux/macOS default: ``source .venv/bin/activate``
      (``shell="fish"`` ends in ``activate.fish``, ``"csh"`` in ``activate.csh``)
    - Windows default (cmd): ``.venv\\Scripts\\activate.bat``
      (``shell="powershell"`` uses ``Activate.ps1``)
    """
    # TODO: branch on ``system`` first, then on ``shell`` (compare lower-case).
    # TODO: Windows uses backslashes and "Scripts"; the others use "/" and "bin".
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert activation_command("Linux") == "source .venv/bin/activate", "Linux"
    assert activation_command("Darwin", "zsh") == "source .venv/bin/activate", "zsh"
    assert activation_command("Linux", "fish") == "source .venv/bin/activate.fish"
    assert activation_command("Linux", "CSH") == "source .venv/bin/activate.csh"
    assert activation_command("Windows") == ".venv\\Scripts\\activate.bat", "cmd"
    assert (
        activation_command("Windows", "PowerShell") == ".venv\\Scripts\\Activate.ps1"
    ), "PowerShell uses Activate.ps1 (capital A)"
    assert activation_command("Linux", venv_dir="env") == "source env/bin/activate"
    try:
        activation_command("Plan9")
    except ValueError:
        pass
    else:
        raise AssertionError("an unknown system should raise ValueError")


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_02_activation_command: {exc!r}")
    print("PASS ex_02_activation_command")
