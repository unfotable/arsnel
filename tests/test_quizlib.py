"""Quiz engine: scoring, feedback, badges and persistence."""

from __future__ import annotations

import json
import random
from pathlib import Path

import pytest

from arsnel.manifest import get_module
from arsnel.models import Question
from arsnel.quizlib import PASS_MARK, run_quiz, tier_for

QUESTIONS = (
    Question("Q one?", ("a", "b", "c"), 0, "because a"),
    Question("Q two?", ("a", "b", "c"), 2, "because c"),
    Question("Q three?", ("a", "b", "c", "d"), 1, "because b"),
    Question("Q four?", ("a", "b", "c"), 1, "because b"),
)


def scripted(answers: list[str]) -> tuple[object, list[str]]:
    lines: list[str] = []
    feed = iter(answers)

    def fake_input(_prompt: str) -> str:
        return next(feed)

    return fake_input, lines


def play(answers: list[str], isolated: Path | None = None) -> tuple[int, str]:
    feed = iter(answers)
    lines: list[str] = []

    def fake_input(_prompt: str) -> str:
        try:
            return next(feed)
        except StopIteration:
            raise EOFError from None

    code = run_quiz(
        get_module(1),
        QUESTIONS,
        input_fn=fake_input,
        out=lines.append,
        shuffle=False,
        record=isolated is not None,
    )
    return code, "\n".join(lines)


def test_tiers() -> None:
    assert tier_for(100) == "gold"
    assert tier_for(85) == "silver"
    assert tier_for(PASS_MARK) == "bronze"
    assert tier_for(69.9) is None


def test_perfect_score_earns_gold() -> None:
    code, out = play(["a", "c", "b", "b"])
    assert code == 0
    assert "SCORE  4/4" in out
    assert "GOLD BADGE EARNED" in out
    assert "because a" in out


def test_failing_score_shows_correct_answer() -> None:
    code, out = play(["b", "a", "a", "a"])
    assert code == 1
    assert "[FAIL] the answer was A) a" in out
    assert "re-read the README" in out


def test_invalid_input_is_reprompted() -> None:
    code, out = play(["zzz", "9", "a", "c", "b", "b"])
    assert code == 0
    assert "enter a letter A-C" in out


def test_digits_accepted() -> None:
    code, _ = play(["1", "3", "2", "2"])
    assert code == 0


def test_eof_aborts_without_score() -> None:
    code, out = play(["a"])
    assert code == 2
    assert "ABORTED" in out


def test_result_is_recorded(isolated_state: Path) -> None:
    play(["a", "c", "b", "b"], isolated_state)
    data = json.loads((isolated_state / "quiz_results.json").read_text())
    assert data["01"]["best"] == 100.0
    assert data["01"]["attempts"] == 1
    play(["b", "b", "b", "b"], isolated_state)
    data = json.loads((isolated_state / "quiz_results.json").read_text())
    assert data["01"]["best"] == 100.0
    assert data["01"]["attempts"] == 2


def test_shuffle_still_scores_correctly() -> None:
    """With shuffling, picking the displayed correct letter still scores."""
    lines: list[str] = []
    rng = random.Random(7)
    answers: list[str] = []

    def fake_input(_prompt: str) -> str:
        # Find the letter whose text matches the correct choice of this question.
        index = len(answers)
        question = QUESTIONS[index]
        shown = [ln for ln in lines if ln.startswith("   ") and ") " in ln]
        block = shown[-len(question.choices) :]
        for line in block:
            letter, text = line.strip().split(") ", 1)
            if text == question.choices[question.answer]:
                answers.append(letter)
                return letter
        raise AssertionError("correct choice not displayed")

    code = run_quiz(
        get_module(1),
        QUESTIONS,
        input_fn=fake_input,
        out=lines.append,
        record=False,
        rng=rng,
    )
    assert code == 0


@pytest.mark.parametrize("number", [0, 18])
def test_every_module_quiz_is_playable(number: int) -> None:
    from content import load

    content = load(number)
    assert content is not None
    lines: list[str] = []
    answers = iter("ABCD"[q.answer] for q in content.quiz)
    code = run_quiz(
        get_module(number),
        content.quiz,
        input_fn=lambda _p: next(answers),
        out=lines.append,
        shuffle=False,
        record=False,
    )
    assert code == 0
