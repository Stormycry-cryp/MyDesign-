#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


LIB = Path.home() / ".codex" / "designstyle-library" / "references"

DIMENSIONS = {
    "scene": [
        ("title", 8),
        ("tags", 14),
        ("style_tags", 18),
        ("best_for", 12),
        ("Essence", 6),
        ("When To Use", 8),
    ],
    "structure": [
        ("structure_tags", 18),
        ("Layout Geometry And Spacing", 10),
        ("Dimension And Ratio System", 12),
        ("Visual System", 5),
        ("Implementation Notes", 5),
    ],
    "type_color": [
        ("Typography And Reading Rhythm", 12),
        ("Color, Material, And Contrast", 12),
        ("Visual System", 5),
    ],
    "assets": [
        ("Assets", 14),
        ("Evidence Snapshot", 5),
        ("Color, Material, And Contrast", 4),
    ],
    "motion": [
        ("motion_tags", 20),
        ("Motion", 12),
        ("Motion Code And Runtime Evidence", 14),
        ("code_tags", 8),
    ],
    "code": [
        ("code_tags", 20),
        ("Motion Code And Runtime Evidence", 14),
        ("Implementation Notes", 10),
        ("Dimension And Ratio System", 4),
    ],
}


def tokens(value: str) -> list[str]:
    return [t.lower() for t in re.split(r"[^\w\u4e00-\u9fff]+", value) if t]


def field(text: str, name: str) -> str:
    match = re.search(rf"^{re.escape(name)}:\s*(.*?)\s*$", text, re.M)
    return match.group(1).strip().strip('"') if match else ""


def section(text: str, name: str) -> str:
    match = re.search(rf"^## {re.escape(name)}\s*$([\s\S]*?)(?=^## |\Z)", text, re.M)
    return match.group(1).strip() if match else ""


def blob(text: str, name: str) -> str:
    if name in {
        "title",
        "tags",
        "style_tags",
        "structure_tags",
        "motion_tags",
        "code_tags",
        "best_for",
        "avoid_for",
    }:
        return field(text, name).lower()
    return section(text, name).lower()


def dimension_scores(query_tokens: list[str], text: str) -> dict[str, int]:
    scores: dict[str, int] = {}
    avoid = field(text, "avoid_for").lower() + "\n" + section(text, "When Not To Use").lower()
    for dimension, weights in DIMENSIONS.items():
        score = 0
        for token in query_tokens:
            score += sum(blob(text, name).count(token) * weight for name, weight in weights)
            score -= avoid.count(token) * 4
        scores[dimension] = score
    scores["total"] = sum(scores.values())
    return scores


def best_dimensions(scores: dict[str, int]) -> list[str]:
    dims = [(name, score) for name, score in scores.items() if name != "total" and score > 0]
    dims.sort(key=lambda item: (-item[1], item[0]))
    return [f"{name}:{score}" for name, score in dims[:3]]


def excerpt(text: str, names: list[str], limit: int = 180) -> str:
    for name in names:
        value = field(text, name) if name.endswith("_tags") or name in {"tags", "best_for"} else section(text, name)
        value = " ".join(value.split())
        if value:
            return value[:limit]
    return ""


def line_value(text: str, prefix: str, limit: int = 220) -> str:
    match = re.search(rf"^- {re.escape(prefix)}\s*(.*?)\s*$", text, re.M)
    if not match:
        return ""
    return " ".join(match.group(1).split())[:limit]


def main() -> int:
    parser = argparse.ArgumentParser(description="Search local designstyle references by reusable design dimensions.")
    parser.add_argument("query")
    parser.add_argument("--library", default=str(LIB))
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--matrix", action="store_true", help="Print a dimension matrix for composing multiple references.")
    args = parser.parse_args()

    query = tokens(args.query)
    root = Path(args.library).expanduser()
    if not root.exists():
        print(f"No designstyle library found at {root}")
        return 0

    rows = []
    for path in root.glob("*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        scores = dimension_scores(query, text)
        if scores["total"] <= 0:
            continue
        title = field(text, "title") or path.stem
        rows.append((scores["total"], title, path, text, scores))

    rows.sort(key=lambda item: (-item[0], item[1]))
    visible_rows = rows[: args.limit]
    for total, title, path, text, scores in visible_rows:
        dims = ", ".join(best_dimensions(scores)) or "weak"
        print(f"{total}\t{title}\t{dims}\t{path}")
        print(f"  tags: {field(text, 'style_tags') or field(text, 'tags')}")
        print(f"  use: {excerpt(text, ['best_for', 'Essence'])}")
        if args.matrix:
            print(f"  structure: {excerpt(text, ['structure_tags', 'Dimension And Ratio System'])}")
            motion = excerpt(text, ['motion_tags', 'code_tags'])
            exact = line_value(text, 'Exact motion parameters:', 260)
            print(f"  motion/code: {motion}")
            if exact:
                print(f"  exact motion: {exact}")

    if args.matrix and visible_rows:
        print("\n# Dimension Leaders")
        for dimension in DIMENSIONS:
            leaders = sorted(visible_rows, key=lambda item: (-item[4][dimension], item[1]))[:3]
            picked = [f"{title}({scores[dimension]})" for _, title, _, _, scores in leaders if scores[dimension] > 0]
            print(f"{dimension}: {', '.join(picked) or 'no clear match'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
