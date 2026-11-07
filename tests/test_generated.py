"""Generated files match their sources; the stub derivation behaves."""

from __future__ import annotations

import pytest

from arsnel.manifest import get_module
from arsnel.paths import CURRICULUM
from arsnel.scaffold import ScaffoldError, derive_stub, expected_files, render_quiz_py
from content import all_content

SOLUTION = '''"""Doc."""


def double(x: int) -> int:
    """Double."""
    # TODO: do it
    # --- solution ---
    return x * 2
    # --- end ---
'''


def test_derive_stub_replaces_region() -> None:
    stub = derive_stub(SOLUTION, "t")
    assert "return x * 2" not in stub
    assert 'raise NotImplementedError("TODO: your turn")' in stub
    assert "# TODO: do it" in stub


@pytest.mark.parametrize(
    "bad",
    [
        "def f() -> None:\n    pass\n",
        "# --- solution ---\nx = 1\n# --- end ---\n# TODO\n",
        "def f() -> None:\n    # TODO\n    # --- solution ---\n    pass\n",
        "def f() -> None:\n    # TODO\n    # --- end ---\n",
    ],
)
def test_derive_stub_rejects_bad_markers(bad: str) -> None:
    with pytest.raises(ScaffoldError):
        derive_stub(bad, "t")


def test_quiz_runner_source() -> None:
    text = render_quiz_py(get_module(3))
    assert "get_module(3)" in text
    assert "content.module_03" in text
    compile(text, "quiz.py", "exec")


def test_stubs_and_quizzes_in_sync() -> None:
    """READMEs embed program output (slow), so CI checks them via generate.py."""
    for number, content in all_content().items():
        meta = get_module(number)
        files = expected_files(meta, content, CURRICULUM, with_output=False)
        for path, text in files.items():
            if path.name == "README.md":
                continue
            assert path.read_text(encoding="utf-8") == text, f"drift: {path}"
