"""Render module Markdown to site HTML (terminal-window code blocks, link fixes)."""

from __future__ import annotations

import html
import re

import markdown

REPO_URL = "https://github.com/unfotable/arsnel"

_PRE = re.compile(
    r'<pre><code(?: class="language-([\w+-]+)")?>(.*?)</code></pre>', re.DOTALL
)
_HREF = re.compile(r'href="([^"#:]+?)(#[^"]*)?"')
_COMMENT = re.compile(r"<!--.*?-->\s*", re.DOTALL)
_TITLES = {"python": "python", "text": "output", "bash": "bash", "toml": "toml"}


def _window(match: re.Match[str]) -> str:
    lang = match.group(1) or "text"
    title = _TITLES.get(lang, lang)
    return (
        '<div class="term"><div class="titlebar"><i></i><i></i><i></i>'
        f"<span>{html.escape(title)}</span>"
        '<button class="copy" type="button">copy</button></div>'
        f"<pre><code>{match.group(2)}</code></pre></div>"
    )


def _fix_link(match: re.Match[str], dirname: str) -> str:
    target, anchor = match.group(1), match.group(2) or ""
    if target.endswith("../../README.md"):
        return f'href="../index.html{anchor}"'
    sibling = re.fullmatch(r"\.\./(module_\d\d_\w+)/README\.md", target)
    if sibling:
        return f'href="{sibling.group(1)}.html{anchor}"'
    if target.endswith("README.md") and "/" not in target:
        return f'href="{dirname}.html{anchor}"'
    if target.startswith(("../", "./")) or "/" in target or "." in target:
        clean = target.removeprefix("./")
        return f'href="{REPO_URL}/blob/main/curriculum/{dirname}/{clean}{anchor}"'
    return match.group(0)


def render_markdown(text: str, dirname: str) -> str:
    """Convert ``text`` (a module README) to HTML for page ``dirname``."""
    body = markdown.markdown(text, extensions=["fenced_code", "tables", "sane_lists"])
    body = _COMMENT.sub("", body)
    body = _PRE.sub(_window, body)
    return _HREF.sub(lambda m: _fix_link(m, dirname), body)
