"""Build the ARSNEL static site into ``site/`` using only Python.

Usage:  python build_site.py [--out site] [--no-demo]

Jinja2 renders the pages, ``markdown`` renders each module README, and the
terminal-demo outputs are captured by really running the example scripts.
"""

from __future__ import annotations

import argparse
import json
import shutil
from collections.abc import Sequence
from datetime import date
from pathlib import Path
from typing import Any

import build_readme
from arsnel import NAME, TAGLINE, __version__
from arsnel.ascii_art import hero, mascot, xp_bar
from arsnel.badges import BADGES, badge_grid
from arsnel.langstats import python_percent
from arsnel.manifest import MODULES
from arsnel.mdrender import REPO_URL, render_markdown
from arsnel.paths import ASSETS, CURRICULUM, SITE
from arsnel.progress_core import Snapshot
from arsnel.scaffold import ScaffoldError, capture_output
from arsnel.templates import environment
from arsnel.theme import CSS, FONTS_URL, JS
from content import all_content

CHART_TITLES = build_readme.CHARTS
DEMO_EXAMPLES = {
    "python hello_world.py": ("module_01_syntax", "hello_world.py"),
    "python variables_and_types.py": ("module_01_syntax", "variables_and_types.py"),
}


def tagline_html() -> str:
    """Tagline with Markdown backticks turned into ``<code>``."""
    return build_readme.html_tagline()


def search_index() -> dict[str, str]:
    """Map module id -> lowercase searchable text."""
    docs: dict[str, str] = {}
    content = all_content()
    for meta in MODULES:
        parts = [meta.title, meta.tagline, meta.level, meta.skill, meta.prompt]
        item = content.get(meta.number)
        if item:
            parts += [lesson.title for lesson in item.lessons]
            parts += [e.title for e in item.exercises]
            parts.append(item.intro)
        docs[meta.mid] = " ".join(parts).lower()
    return docs


def demo_data(snapshot: Snapshot, capture: bool = True) -> dict[str, Any]:
    """Commands for the in-page terminal; outputs come from real runs."""
    level, rank = snapshot.level
    commands: dict[str, str] = {
        "help": "commands: help, ls, whoami, banner, mascot, progress, quiz, clear,\n"
        "          python hello_world.py, python variables_and_types.py",
        "ls": "\n".join(f"{m.dirname}/" for m in MODULES),
        "whoami": f"learner  LVL {level} {rank}",
        "banner": hero(),
        "mascot": mascot(),
        "progress": f"{xp_bar(snapshot.percent, 32)}\n"
        f"XP {snapshot.xp}/{snapshot.max_xp}",
        "quiz": "$ cd curriculum/module_01_syntax && python quiz.py\n"
        "Q1/7 answer with a number, 'q' quits. Pass mark: 70%.",
    }
    for command, (folder, name) in DEMO_EXAMPLES.items():
        path = CURRICULUM / folder / "examples" / name
        try:
            commands[command] = capture_output(path, limit=18) if capture else ""
        except ScaffoldError:
            commands[command] = "(example unavailable)"
    return {
        "prompt": "learner@arsnel:~$",
        "intro": "ARSNEL terminal v" + __version__ + " - type 'help'",
        "commands": commands,
    }


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _json_for_html(data: object) -> str:
    """JSON safe to embed inside <script>."""
    return json.dumps(data, ensure_ascii=False).replace("</", "<\\/")


def build(out: Path = SITE, snapshot: Snapshot | None = None) -> list[Path]:
    """Render the whole site; return the list of written files."""
    snap = snapshot or build_readme.snapshot_from_disk()
    env = environment()
    level, rank = snap.level
    py = python_percent()
    common: dict[str, Any] = {
        "fonts_url": FONTS_URL,
        "repo_url": REPO_URL,
        "version": __version__,
        "built": date.today().isoformat(),
        "tagline_plain": TAGLINE.replace("`", ""),
    }
    if out.exists():
        shutil.rmtree(out)
    written: list[Path] = []

    def emit(rel: str, text: str) -> None:
        _write(out / rel, text)
        written.append(out / rel)

    emit("static/arsnel.css", CSS)
    emit("static/arsnel.js", JS)
    emit(".nojekyll", "")
    docs = search_index()
    emit("search.json", json.dumps(docs, ensure_ascii=False, indent=1))
    demo = demo_data(snap)
    modules = [
        {
            "mid": m.mid,
            "dirname": m.dirname,
            "prompt": m.prompt,
            "title": m.title,
            "tagline": m.tagline,
            "level": m.level.title(),
            "hours": f"{m.est_hours:g}",
            "skill": m.skill,
        }
        for m in MODULES
    ]
    emit(
        "index.html",
        env.get_template("index.html").render(
            **common,
            root="",
            title=f"{NAME} - Learn Python, one pixel at a time",
            hero=hero(),
            tagline_html=tagline_html(),
            modules=modules,
            exercises=snap.exercises_total,
            badges=len(BADGES),
            python_percent=f"{py:.1f}",
            level=level,
            rank=rank,
            percent=f"{snap.percent:.0f}",
            filled=round(40 * snap.percent / 100),
            xp=snap.xp,
            max_xp=snap.max_xp,
            demo_chips=["help", "ls", "python hello_world.py", "progress", "mascot"],
            demo_json=_json_for_html(demo),
            search_json=_json_for_html(docs),
            badges_art=badge_grid(snap.stats()),
        ),
    )
    for meta in MODULES:
        readme = (CURRICULUM / meta.dirname / "README.md").read_text(encoding="utf-8")
        prev = MODULES[meta.number - 1] if meta.number > 0 else None
        nxt = MODULES[meta.number + 1] if meta.number + 1 < len(MODULES) else None
        emit(
            f"modules/{meta.dirname}.html",
            env.get_template("module.html").render(
                **common,
                root="../",
                title=f"{meta.prompt} {meta.title} | {NAME}",
                m=modules[meta.number],
                body=render_markdown(readme, meta.dirname),
                prev=prev,
                next=nxt,
            ),
        )
    emit(
        "charts.html",
        env.get_template("charts.html").render(
            **common,
            root="",
            title=f"Charts | {NAME}",
            charts=[{"name": n, "title": t} for n, t in CHART_TITLES],
        ),
    )
    if ASSETS.exists():
        shutil.copytree(ASSETS, out / "assets")
        written += [p for p in (out / "assets").rglob("*") if p.is_file()]
    return written


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Build the ARSNEL site.")
    parser.add_argument("--out", type=Path, default=SITE)
    args = parser.parse_args(argv)
    files = build(args.out)
    print(f"{NAME}: wrote {len(files)} files to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
