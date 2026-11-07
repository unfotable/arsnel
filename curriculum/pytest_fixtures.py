"""Fixtures, tmp_path, monkeypatch, capsys and markers."""

# requires: pytest

import os
from collections.abc import Iterator
from pathlib import Path

import pytest


@pytest.fixture
def numbers() -> list[int]:
    return [3, 1, 2]  # a fresh list for every test


@pytest.fixture
def opened_file(tmp_path: Path) -> Iterator[Path]:
    path = tmp_path / "data.txt"
    path.write_text("hello", encoding="utf-8")
    yield path  # test runs here
    path.unlink()  # teardown


def test_sorted(numbers: list[int]) -> None:
    assert sorted(numbers) == [1, 2, 3]


def test_file(opened_file: Path) -> None:
    assert opened_file.read_text(encoding="utf-8") == "hello"


def test_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ARSNEL_MODE", "test")
    assert os.environ["ARSNEL_MODE"] == "test"  # restored after the test


def test_output(capsys: pytest.CaptureFixture[str]) -> None:
    print("hi")
    assert capsys.readouterr().out == "hi\n"


@pytest.mark.skipif(os.name == "nt", reason="posix only")
def test_posix() -> None:
    assert os.sep == "/"


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q", "-p", "no:cacheprovider"]))
