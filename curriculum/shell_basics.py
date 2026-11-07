"""The shell's core ideas (pwd, ls, cd, mkdir, cat) done with pathlib.

Everything happens inside a throw-away temp folder, and only paths *relative to
that sandbox* are printed, so the output is the same on every machine.
"""

import os
import tempfile
from pathlib import Path


def pwd(root: Path) -> str:
    """Return the current directory, shown relative to the sandbox root."""
    rel = Path.cwd().resolve().relative_to(root).as_posix()
    return "<sandbox>" if rel == "." else f"<sandbox>/{rel}"


def ls(path: str = ".") -> list[str]:
    """Return the sorted names inside ``path`` (what ``ls`` prints)."""
    return sorted(item.name for item in Path(path).iterdir())


def main() -> None:
    start = Path.cwd()
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp).resolve()
        try:
            os.chdir(root)
            print("$ pwd              ->", pwd(root))

            Path("project/src").mkdir(parents=True)  # mkdir -p project/src
            Path("project/notes.txt").write_text("remember to commit\n")
            Path("project/src/app.py").write_text("print('hi')\n")
            print("$ ls               ->", ls())
            print("$ ls project       ->", ls("project"))

            os.chdir("project/src")  # cd project/src (a RELATIVE path)
            print("$ cd project/src   ->", pwd(root))
            os.chdir("..")  # '..' means "the parent folder"
            print("$ cd ..            ->", pwd(root))

            print("$ cat notes.txt    ->", Path("notes.txt").read_text().strip())
            print("$ ls *.txt         ->", sorted(p.name for p in Path().glob("*.txt")))

            absolute = Path("notes.txt").resolve()  # relative -> absolute
            print("is_absolute()      ->", Path("notes.txt").is_absolute())
            print("resolved           ->", absolute.relative_to(root).as_posix())
            print("'~' expands to home->", Path("~/x").expanduser().is_absolute())
        finally:
            os.chdir(start)  # always leave, or the temp dir cannot be removed


if __name__ == "__main__":
    main()
