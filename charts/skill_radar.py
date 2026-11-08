"""Skill radar: how much of each skill area you have completed."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt
import numpy as np

from arsnel.chartstyle import BLUE, CARBON, MUTED, apply_style, save, terminal_title
from arsnel.manifest import SKILLS, get_module
from arsnel.paths import CHARTS, PROGRESS_FILE


def skill_percentages(snapshot: dict[str, Any] | None) -> list[float]:
    """XP percentage per skill area (all zero without a snapshot)."""
    earned = dict.fromkeys(SKILLS, 0.0)
    possible = dict.fromkeys(SKILLS, 0.0)
    for module in (snapshot or {}).get("modules", []):
        skill = get_module(int(module["number"])).skill
        xp = module["done"] * 10 + (20 if module["quiz_passed"] else 0)
        earned[skill] += xp
        possible[skill] += module["total"] * 10 + 20
    return [100.0 * earned[s] / possible[s] if possible[s] else 0.0 for s in SKILLS]


def main(out_dir: Path = CHARTS, snapshot: dict[str, Any] | None = None) -> list[Path]:
    """Draw and save the radar for ``snapshot`` (or the saved progress file)."""
    if snapshot is None and PROGRESS_FILE.exists():
        snapshot = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    values = skill_percentages(snapshot)
    apply_style()
    angles = np.linspace(0, 2 * np.pi, len(SKILLS), endpoint=False)
    closed_angles = np.append(angles, angles[0])
    closed_values = np.append(values, values[0])
    fig = plt.figure(figsize=(9, 7.4))
    ax = fig.add_subplot(111, projection="polar")
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.plot(closed_angles, [100] * len(closed_angles), color=CARBON, lw=1.5, ls="--")
    ax.plot(closed_angles, closed_values, color=BLUE, lw=3)
    ax.fill(closed_angles, closed_values, color=BLUE, alpha=0.35)
    ax.scatter(
        angles, values, marker="s", s=60, color=BLUE, edgecolor="black", zorder=5
    )
    ax.set_xticks(angles)
    ax.set_xticklabels(SKILLS, fontsize=9)
    ax.tick_params(axis="x", pad=14)  # keep labels clear of the outer ring
    for label, angle in zip(ax.get_xticklabels(), angles, strict=True):
        side = float(np.sin(angle))  # >0 right half, <0 left half
        label.set_horizontalalignment(
            "left" if side > 0.2 else "right" if side < -0.2 else "center"
        )
    ax.set_yticks([25, 50, 75, 100])
    ax.set_yticklabels(["25%", "50%", "75%", ""], fontsize=7, color=MUTED)
    ax.set_ylim(0, 100)
    ax.spines["polar"].set_linewidth(1.5)
    terminal_title(
        fig,
        "skills --radar",
        "dashed ring = everything ARSNEL teaches; fill = what you finished",
    )
    fig.subplots_adjust(top=0.82, bottom=0.09, left=0.2, right=0.8)
    return save(fig, "skill_radar", out_dir)


if __name__ == "__main__":
    for written in main():
        print("wrote", written)
