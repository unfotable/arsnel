"""Every module's content meets the authoring minimums."""

from __future__ import annotations

import pytest

from arsnel.manifest import MODULES
from arsnel.paths import CURRICULUM
from content import all_content, load


def test_all_modules_have_content() -> None:
    assert sorted(all_content()) == list(range(19))


@pytest.mark.parametrize("number", range(19))
def test_module_minimums(number: int) -> None:
    content = load(number)
    assert content is not None
    assert content.number == number
    assert len(content.lessons) >= 4
    assert len(content.examples) >= 3
    assert len(content.exercises) >= 3
    assert len(content.quiz) >= 6
    assert content.cheatsheet
    assert content.next_steps.strip()


@pytest.mark.parametrize("number", range(19))
def test_quiz_questions_well_formed(number: int) -> None:
    content = load(number)
    assert content is not None
    for q in content.quiz:
        assert len(q.choices) >= 3
        assert len(set(q.choices)) == len(q.choices), q.prompt
        assert 0 <= q.answer < len(q.choices)
        assert q.explanation.strip()


def test_filenames_follow_convention() -> None:
    for meta in MODULES:
        content = load(meta.number)
        assert content is not None
        for index, exercise in enumerate(content.exercises, start=1):
            assert exercise.file.startswith(f"ex_{index:02d}_"), exercise.file
            assert 1 <= exercise.difficulty <= 3
        base = CURRICULUM / meta.dirname
        for example in content.examples:
            assert (base / "examples" / example.file).is_file()
