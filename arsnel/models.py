"""Typed data structures shared by the curriculum, generators and tools."""

from __future__ import annotations

from dataclasses import dataclass

LEVELS: tuple[str, ...] = ("BEGINNER", "INTERMEDIATE", "ADVANCED")


@dataclass(frozen=True)
class ModuleMeta:
    """Static facts about one curriculum module (see ``manifest.py``)."""

    number: int
    slug: str
    title: str
    tagline: str
    level: str
    skill: str
    est_hours: float
    prerequisites: tuple[int, ...] = ()

    @property
    def mid(self) -> str:
        """Zero-padded module id, e.g. ``"01"``."""
        return f"{self.number:02d}"

    @property
    def prompt(self) -> str:
        """Terminal-style module name, e.g. ``"module_01"``."""
        return f"module_{self.mid}"

    @property
    def dirname(self) -> str:
        """Directory name under ``curriculum/``."""
        return f"module_{self.mid}_{self.slug}"


@dataclass(frozen=True)
class Lesson:
    """One Markdown section of a module README."""

    title: str
    body: str


@dataclass(frozen=True)
class Example:
    """A runnable file in ``examples/``.

    ``show_output`` embeds the real captured stdout in the README. Only enable it
    for deterministic, standard-library-only examples.
    """

    file: str
    title: str
    blurb: str
    show_output: bool = True


@dataclass(frozen=True)
class Exercise:
    """An exercise; its stub is derived from ``solutions/<file>``."""

    file: str
    title: str
    brief: str
    difficulty: int = 1


@dataclass(frozen=True)
class Question:
    """A multiple-choice quiz question. ``answer`` is a 0-based index."""

    prompt: str
    choices: tuple[str, ...]
    answer: int
    explanation: str


@dataclass(frozen=True)
class ModuleContent:
    """All learner-facing content of a module, kept as plain Python data."""

    number: int
    intro: str
    lessons: tuple[Lesson, ...]
    examples: tuple[Example, ...]
    exercises: tuple[Exercise, ...]
    quiz: tuple[Question, ...]
    cheatsheet: tuple[str, ...] = ()
    next_steps: str = ""
