"""pathlib: paths as objects - building, inspecting, searching and editing."""

import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as tmp:
    root = Path(tmp)

    # The / operator joins paths; it works on every operating system.
    report = root / "reports" / "2024" / "summary.txt"
    print("name  :", report.name)
    print("stem  :", report.stem)
    print("suffix:", report.suffix)
    print("parent:", report.parent.name)
    print("other :", report.with_suffix(".md").name)

    # Create folders (parents=True like `mkdir -p`) and files in one go.
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("total: 42\n", encoding="utf-8")
    (root / "reports" / "index.txt").write_text("index\n", encoding="utf-8")
    (root / "data.csv").write_text("a,b\n1,2\n", encoding="utf-8")
    (root / "reports" / "2024" / "chart.png").write_bytes(b"\x89PNG")

    print("exists:", report.exists(), "| is_file:", report.is_file())
    print("text  :", report.read_text(encoding="utf-8").strip())
    print("size  :", report.stat().st_size, "bytes")

    # glob() matches in one folder, rglob() searches the whole tree.
    # Sort results: the order of directory listings is not guaranteed.
    def rel(paths: list[Path]) -> list[str]:
        return sorted(p.relative_to(root).as_posix() for p in paths)

    print("*.csv      :", rel(list(root.glob("*.csv"))))
    print("**/*.txt   :", rel(list(root.rglob("*.txt"))))
    print("iterdir    :", sorted(p.name for p in root.iterdir()))

    # Rename and delete.
    moved = report.rename(report.with_name("final.txt"))
    print("renamed    :", moved.name, "| old exists:", report.exists())
    moved.unlink()
    print("after unlink:", rel(list(root.rglob("*.txt"))))

    # missing_ok avoids an exception when the file is already gone.
    moved.unlink(missing_ok=True)
