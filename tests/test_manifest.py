"""The manifest describes a consistent 19-module curriculum."""

from __future__ import annotations

from arsnel import NAME, TAGLINE
from arsnel.manifest import CONCEPTS, MODULES, SKILLS, get_module
from arsnel.paths import CURRICULUM


def test_identity() -> None:
    assert NAME == "ARSNEL"
    assert TAGLINE.startswith("ARSNEL")
    assert "print()" in TAGLINE


def test_nineteen_modules_in_order() -> None:
    assert [m.number for m in MODULES] == list(range(19))
    assert len({m.slug for m in MODULES}) == 19


def test_directories_exist() -> None:
    for meta in MODULES:
        base = CURRICULUM / meta.dirname
        assert base.is_dir(), meta.dirname
        for part in ("examples", "solutions", "exercises"):
            assert (base / part).is_dir(), f"{meta.dirname}/{part}"
        for name in ("README.md", "quiz.py"):
            assert (base / name).is_file(), f"{meta.dirname}/{name}"


def test_prerequisites_point_backwards() -> None:
    for meta in MODULES:
        assert all(p < meta.number for p in meta.prerequisites), meta.prompt


def test_skills_and_levels_valid() -> None:
    for meta in MODULES:
        assert meta.skill in SKILLS, meta.prompt
        assert meta.level in {"BEGINNER", "INTERMEDIATE", "ADVANCED"}


def test_concepts_reference_known_concepts() -> None:
    names = {c.name for c in CONCEPTS}
    assert len(names) == len(CONCEPTS)
    for concept in CONCEPTS:
        assert set(concept.requires) <= names, concept.name
        assert 0 <= concept.module < 19


def test_get_module() -> None:
    assert get_module(7).slug == "files_errors"
