"""The ``arsnel`` learner command."""

from __future__ import annotations

import io
from pathlib import Path

import pytest

from arsnel import cli
from arsnel.manifest import MODULES


def make_curriculum(root: Path, passing: int, failing: int) -> Path:
    folder = root / "module_01_syntax" / "exercises"
    folder.mkdir(parents=True)
    for i in range(passing):
        (folder / f"ex_{i + 1:02d}_ok.py").write_text("print('PASS ok')\n")
    for i in range(failing):
        name = f"ex_{passing + i + 1:02d}_bad.py"
        text = f"raise SystemExit(\"FAIL {Path(name).stem}: AssertionError('nope')\")\n"
        (folder / name).write_text(text)
    return root


def test_check_reports_each_file(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    curriculum = make_curriculum(tmp_path, passing=2, failing=1)
    code = cli.main(["check", "1"], curriculum)
    out = capsys.readouterr().out
    assert code == 1
    assert "PASS  ex_01_ok" in out
    assert "FAIL  ex_03_bad  AssertionError('nope')" in out
    assert "FAIL ex_03_bad: FAIL" not in out
    assert "2/3 passed (+20 XP)" in out


def test_check_all_pass_exits_zero(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    curriculum = make_curriculum(tmp_path, passing=2, failing=0)
    assert cli.main(["check"], curriculum) == 0
    assert "All clear" in capsys.readouterr().out


def test_unknown_module_is_a_clean_error(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    curriculum = make_curriculum(tmp_path, 1, 0)
    assert cli.main(["check", "42"], curriculum) == 2
    assert "no module 42" in capsys.readouterr().out
    assert cli.main(["quiz", "42"], curriculum) == 2


def test_next_points_at_first_failing_exercise(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    curriculum = make_curriculum(tmp_path, passing=1, failing=2)
    assert cli.main(["next"], curriculum) == 0
    out = capsys.readouterr().out
    assert "ex_02_bad.py" in out
    assert "ex_03_bad.py" not in out
    assert "python -m arsnel check 1" in out
    assert "README.md" in out


def test_next_suggests_quiz_when_exercises_pass(
    tmp_path: Path, isolated_state: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    curriculum = make_curriculum(tmp_path / "cur", passing=2, failing=0)
    cli.main(["next"], curriculum)
    assert "python -m arsnel quiz 1" in capsys.readouterr().out


def test_modules_lists_every_module(
    tmp_path: Path, isolated_state: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    curriculum = make_curriculum(tmp_path / "cur", 1, 1)
    assert cli.main(["modules"], curriculum) == 0
    lines = capsys.readouterr().out.strip().splitlines()
    assert len(lines) == len(MODULES)
    assert "1/2" in lines[1]


def test_status_and_default_screen(
    tmp_path: Path, isolated_state: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    curriculum = make_curriculum(tmp_path / "cur", 1, 0)
    assert cli.main(["status"], curriculum) == 0
    assert "LVL" in capsys.readouterr().out
    assert cli.main([], curriculum) == 0
    out = capsys.readouterr().out
    assert "commands:" in out and "`" not in out.splitlines()[0]


def test_quiz_aborts_cleanly_without_input(
    isolated_state: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("sys.stdin", io.StringIO(""))  # input() hits EOF
    assert cli.main(["quiz", "1"]) == 2


def test_serve_serves_a_directory(tmp_path: Path) -> None:
    import threading
    import urllib.request

    (tmp_path / "index.html").write_text("<title>ARSNEL</title>")
    server = cli.make_server(tmp_path, port=0)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        port = server.server_address[1]
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/") as response:
            assert response.status == 200
            assert b"ARSNEL" in response.read()
    finally:
        server.shutdown()
        server.server_close()


def test_serve_reports_a_busy_port(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    (tmp_path / "index.html").write_text("x")
    monkeypatch.setattr(cli, "SITE", tmp_path)  # never rebuild the real site here
    busy = cli.make_server(tmp_path, port=0)
    try:
        port = busy.server_address[1]
        assert cli.cmd_serve(port, "127.0.0.1", build=False, open_browser=False) == 1
        assert f"try --port {port + 1}" in capsys.readouterr().out
    finally:
        busy.server_close()
