"""The ARSNEL terminal quiz engine: score, feedback, rank and pixel badges."""

from __future__ import annotations

import json
import random
from collections.abc import Callable, Sequence

from arsnel.ascii_art import box, xp_bar
from arsnel.badges import Badge, badge_art, rank_for
from arsnel.models import ModuleMeta, Question
from arsnel.paths import QUIZ_FILE

PASS_MARK = 70.0
LETTERS = "ABCDEFGH"


def tier_for(percent: float) -> str | None:
    """Return the badge tier earned by ``percent`` (or ``None`` below the pass mark)."""
    if percent >= 90:
        return "gold"
    if percent >= 80:
        return "silver"
    if percent >= PASS_MARK:
        return "bronze"
    return None


def record_result(module_id: str, percent: float) -> None:
    """Persist the best score for ``module_id`` to ``.arsnel/quiz_results.json``."""
    try:
        data = json.loads(QUIZ_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        data = {}
    entry = data.get(module_id, {"best": 0.0, "attempts": 0})
    entry["best"] = max(float(entry.get("best", 0.0)), round(percent, 1))
    entry["attempts"] = int(entry.get("attempts", 0)) + 1
    data[module_id] = entry
    QUIZ_FILE.parent.mkdir(parents=True, exist_ok=True)
    QUIZ_FILE.write_text(
        json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def _parse(raw: str, count: int) -> int | None:
    """Turn ``"b"`` / ``"2"`` into a 0-based index, or ``None`` if invalid."""
    text = raw.strip().upper()
    if len(text) == 1 and text in LETTERS[:count]:
        return LETTERS.index(text)
    if text.isdigit() and 1 <= int(text) <= count:
        return int(text) - 1
    return None


def run_quiz(
    meta: ModuleMeta,
    questions: Sequence[Question],
    *,
    input_fn: Callable[[str], str] = input,
    out: Callable[[str], None] = print,
    shuffle: bool = True,
    record: bool = True,
    rng: random.Random | None = None,
) -> int:
    """Run an interactive quiz. Returns 0 on pass, 1 on fail, 2 if aborted."""
    rng = rng or random.Random()
    out("")
    out(
        box(
            [meta.title, f"{len(questions)} questions  |  pass mark {PASS_MARK:.0f}%"],
            title=f"> {meta.prompt} :: quiz",
        )
    )
    out("")
    score = 0
    for number, question in enumerate(questions, start=1):
        order = list(range(len(question.choices)))
        if shuffle:
            rng.shuffle(order)
        out(f"Q{number}/{len(questions)}  {question.prompt}")
        for slot, original in enumerate(order):
            out(f"   {LETTERS[slot]}) {question.choices[original]}")
        picked: int | None = None
        while picked is None:
            try:
                raw = input_fn("$ answer> ")
            except (EOFError, KeyboardInterrupt):
                out("\n[ABORTED] quiz cancelled - no score recorded.")
                return 2
            picked = _parse(raw, len(order))
            if picked is None:
                out(f"   enter a letter A-{LETTERS[len(order) - 1]}")
        correct_slot = order.index(question.answer)
        if picked == correct_slot:
            score += 1
            out("   [ OK ] correct!")
        else:
            out(
                f"   [FAIL] the answer was {LETTERS[correct_slot]}) "
                f"{question.choices[question.answer]}"
            )
        out(f"   -> {question.explanation}")
        out("")
    percent = 100.0 * score / len(questions) if questions else 0.0
    level, title = rank_for(percent)
    out(f"SCORE  {score}/{len(questions)}")
    out(xp_bar(percent))
    out(f"RANK   LVL {level} {title}")
    tier = tier_for(percent)
    if tier:
        badge = Badge("quiz", "QUIZ PASSED", "", "Q", tier, lambda _s: True)
        out("")
        for line in badge_art(badge, unlocked=True):
            out("  " + line)
        out(f"  {tier.upper()} BADGE EARNED for {meta.prompt}")
    else:
        out(f"Below {PASS_MARK:.0f}% - re-read the README and try again.")
    if record:
        record_result(meta.mid, percent)
    return 0 if tier else 1
