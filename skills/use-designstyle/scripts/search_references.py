#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


LIB = Path.home() / ".codex" / "designstyle-library"
REFERENCE_DIR = LIB / "references"

DIMENSION_ALIASES = {
    "scene": "scene",
    "layout-spacing": "layout_spacing",
    "type-copy": "type_copy",
    "color-surface": "color_surface",
    "assets": "assets",
    "motion-code": "motion_code",
    "components-states": "components_states",
}

GENERIC_MOTION_TOKENS = {
    "animation",
    "animations",
    "code",
    "css",
    "easing",
    "hover",
    "js",
    "motion",
    "scroll",
    "transition",
    "transitions",
}

GENERIC_PAGE_TOKENS = {
    "home",
    "homepage",
    "landing",
    "page",
    "pages",
}

CARD_WEIGHTS = [
    ("category_tags", 42),
    ("page_scope", 32),
    ("best_for", 28),
    ("style_tags", 14),
    ("structure_tags", 12),
    ("motion_tags", 5),
    ("code_tags", 4),
    ("title", 10),
    ("selection_note", 4),
]


def tokens(value: str) -> list[str]:
    return [t.lower() for t in re.split(r"[^\w\u4e00-\u9fff]+", value) if t]


def text_for(value: object) -> str:
    if isinstance(value, list):
        return " ".join(str(item) for item in value)
    if isinstance(value, dict):
        return " ".join(text_for(item) for item in value.values())
    return str(value or "")


def count_matches(query_tokens: list[str], value: object) -> int:
    blob = text_for(value).lower()
    return sum(blob.count(token) for token in query_tokens)


def card_score(query_tokens: list[str], card: dict[str, object]) -> tuple[int, dict[str, int]]:
    factors: dict[str, int] = {}
    raw = 0
    for field, weight in CARD_WEIGHTS:
        field_score = 0
        blob = text_for(card.get(field)).lower()
        for token in query_tokens:
            token_weight = 1.0
            if field in {"motion_tags", "code_tags"} and token in GENERIC_MOTION_TOKENS:
                token_weight = 0.25
            elif field in {"category_tags", "page_scope", "best_for", "structure_tags"} and token in GENERIC_PAGE_TOKENS:
                token_weight = 0.35
            field_score += int(blob.count(token) * weight * token_weight)
        factors[field] = field_score
        raw += field_score

    avoid_penalty = count_matches(query_tokens, card.get("avoid_for")) * 38
    factors["avoid_for_penalty"] = -avoid_penalty

    scene_fit = factors["category_tags"] + factors["page_scope"] + factors["best_for"]
    scene_gate = min(1.0, scene_fit / 90) if scene_fit > 0 else 0.0
    motion_code = factors["motion_tags"] + factors["code_tags"]
    gated_motion_code = int(motion_code * scene_gate)
    factors["scene_gate_percent"] = int(scene_gate * 100)
    factors["gated_motion_code"] = gated_motion_code

    total = (
        factors["category_tags"]
        + factors["page_scope"]
        + factors["best_for"]
        + factors["style_tags"]
        + factors["structure_tags"]
        + factors["title"]
        + factors["selection_note"]
        + gated_motion_code
        - avoid_penalty
    )
    return total, factors


def load_cards(lib: Path) -> list[dict[str, object]]:
    cards = []
    for path in sorted((lib / "indexes" / "cards").glob("*.json")):
        try:
            card = json.loads(path.read_text(encoding="utf-8"))
            card["_card_path"] = f"indexes/cards/{path.name}"
            cards.append(card)
        except json.JSONDecodeError:
            continue
    return cards


def parse_frontmatter(text: str) -> dict[str, object]:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    data: dict[str, object] = {}
    for line in parts[1].splitlines():
        if ":" not in line:
            continue
        key, raw = line.split(":", 1)
        raw = raw.strip()
        if raw.startswith("[") and raw.endswith("]"):
            try:
                data[key.strip()] = json.loads(raw)
            except json.JSONDecodeError:
                data[key.strip()] = raw
        else:
            data[key.strip()] = raw.strip("'\"")
    return data


def load_reference_fallback(lib: Path) -> list[dict[str, object]]:
    cards = []
    for ref in sorted((lib / "references").glob("*.md")):
        text = ref.read_text(encoding="utf-8", errors="ignore")
        meta = parse_frontmatter(text)
        slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", ref.stem)
        cards.append(
            {
                "slug": slug,
                "title": meta.get("title") or slug,
                "reference_path": f"references/{ref.name}",
                "category_tags": meta.get("category_tags") or [],
                "style_tags": meta.get("style_tags") or [],
                "structure_tags": meta.get("structure_tags") or [],
                "motion_tags": meta.get("motion_tags") or [],
                "code_tags": meta.get("code_tags") or [],
                "page_scope": meta.get("page_scope") or "",
                "best_for": meta.get("best_for") or [],
                "avoid_for": meta.get("avoid_for") or [],
                "evidence_strength": {
                    "screenshot": "missing",
                    "layout_spacing": "missing",
                    "type_copy": "missing",
                    "motion_code": "missing",
                },
                "dimension_paths": {},
                "design_system_paths": {},
                "selection_note": meta.get("community_signal") or "Fallback card from reference frontmatter.",
                "evidence_limits": ["No progressive card found; read full reference before implementation."],
                "_card_path": "",
            }
        )
    return cards


def dimension_excerpt(lib: Path, card: dict[str, object], dimension: str, limit: int = 900) -> tuple[str, str]:
    rel = card.get("dimension_paths", {}).get(dimension) if isinstance(card.get("dimension_paths"), dict) else None
    if not isinstance(rel, str):
        return "", "dimension path missing"
    path = lib / rel
    if not path.exists():
        return rel, "dimension file missing"
    text = path.read_text(encoding="utf-8", errors="ignore")
    compact = " ".join(text.split())
    return rel, compact[:limit]


def design_system_summary(lib: Path, card: dict[str, object], limit: int = 900) -> list[str]:
    paths = card.get("design_system_paths") if isinstance(card.get("design_system_paths"), dict) else {}
    if not paths:
        return ["design_system: missing"]

    lines = [f"design_system_paths: {paths}"]
    token_rel = paths.get("tokens")
    if isinstance(token_rel, str):
        token_path = lib / token_rel
        if token_path.exists():
            try:
                tokens_payload = json.loads(token_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                lines.append(f"tokens: invalid JSON: {exc}")
            else:
                palette = tokens_payload.get("palette", {})
                colors = palette.get("colors", []) if isinstance(palette, dict) else []
                color_parts = []
                for color in colors[:8]:
                    if not isinstance(color, dict):
                        continue
                    share = color.get("share")
                    share_text = f", share {share}" if share is not None else ""
                    color_parts.append(
                        f"{color.get('role', 'color')} {color.get('hex')} ({color.get('source', 'source missing')}{share_text})"
                    )
                lines.append(f"palette_colors: {'; '.join(color_parts) or 'missing'}")

                components = tokens_payload.get("component_styles", {})
                if isinstance(components, dict) and components:
                    lines.append(f"component_style_sections: {', '.join(components.keys())}")
                else:
                    lines.append("component_style_sections: missing")
        else:
            lines.append(f"tokens: missing file {token_rel}")

    for key in ["palette", "component_styles"]:
        rel = paths.get(key)
        if not isinstance(rel, str):
            continue
        path = lib / rel
        if path.exists():
            compact = " ".join(path.read_text(encoding="utf-8", errors="ignore").split())
            lines.append(f"{key}_excerpt: {compact[:limit]}")
        else:
            lines.append(f"{key}_excerpt: missing file {rel}")
    return lines


def print_card(
    lib: Path,
    card: dict[str, object],
    score: int,
    factors: dict[str, int],
    args: argparse.Namespace,
) -> None:
    print(f"{score}\t{card.get('title')}\t{card.get('reference_path')}")
    print(f"  card: {card.get('_card_path') or 'fallback frontmatter'}")
    print(f"  category: {card.get('category_tags') or []}")
    print(f"  page_scope: {card.get('page_scope') or 'missing'}")
    print(f"  best_for: {card.get('best_for') or []}")
    print(f"  avoid_for: {card.get('avoid_for') or []}")
    print(f"  evidence_strength: {card.get('evidence_strength') or {}}")
    limits = card.get("evidence_limits") or []
    print(f"  missing/evidence limits: {limits}")
    if args.explain_selection:
        visible = {
            key: value
            for key, value in factors.items()
            if value or key in {"scene_gate_percent", "avoid_for_penalty"}
        }
        print(f"  ranking: {visible}")
    if args.dimension:
        dimension_key = DIMENSION_ALIASES[args.dimension]
        rel, snippet = dimension_excerpt(lib, card, dimension_key)
        print(f"  dimension[{args.dimension}]: {rel or 'missing'}")
        print(f"  excerpt: {snippet or 'Missing Evidence: no dimension summary available.'}")
    if args.full:
        print(f"  full_reference: {lib / str(card.get('reference_path'))}")
    if args.matrix:
        paths = card.get("dimension_paths") if isinstance(card.get("dimension_paths"), dict) else {}
        print(f"  dimensions: {paths}")
        system_paths = card.get("design_system_paths") if isinstance(card.get("design_system_paths"), dict) else {}
        print(f"  design_system: {system_paths}")
    if args.design_system:
        for line in design_system_summary(lib, card):
            print(f"  {line}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Search local designstyle references by progressive cards first.")
    parser.add_argument("query")
    parser.add_argument("--library", default=str(LIB))
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--matrix", action="store_true", help="Print dimension paths for composing multiple references.")
    parser.add_argument("--dimension", choices=sorted(DIMENSION_ALIASES), help="Include one L2 dimension summary excerpt.")
    parser.add_argument("--design-system", action="store_true", help="Include retained palette, moodboard, token, and component-style evidence.")
    parser.add_argument("--full", action="store_true", help="Include the L3 full reference path.")
    parser.add_argument("--explain-selection", action="store_true", help="Show ranking factors and penalties.")
    args = parser.parse_args()

    lib = Path(args.library).expanduser()
    if not lib.exists():
        print(f"No designstyle library found at {lib}")
        return 0

    query_tokens = tokens(args.query)
    cards = load_cards(lib)
    source = "L1 cards"
    if not cards:
        cards = load_reference_fallback(lib)
        source = "fallback L3 reference frontmatter"

    rows = []
    for card in cards:
        score, factors = card_score(query_tokens, card)
        if score > 0:
            rows.append((score, card, factors))
    rows.sort(key=lambda item: (-item[0], str(item[1].get("title"))))

    print(f"# Evidence layer: {source}")
    print(f"# Query tokens: {', '.join(query_tokens)}")
    for score, card, factors in rows[: args.limit]:
        print_card(lib, card, score, factors, args)

    if args.matrix and rows:
        print("\n# Dimension Leaders")
        for dimension in sorted(DIMENSION_ALIASES):
            key = DIMENSION_ALIASES[dimension]
            leaders = []
            for score, card, _ in rows:
                strength = card.get("evidence_strength", {})
                if isinstance(strength, dict) and strength.get(key) in {"strong", "medium"}:
                    leaders.append(str(card.get("title")))
                if len(leaders) >= 3:
                    break
            print(f"{dimension}: {', '.join(leaders) or 'no strong/medium match'}")
        system_leaders = []
        for _, card, _ in rows:
            strength = card.get("evidence_strength", {})
            if isinstance(strength, dict) and strength.get("design_system") in {"strong", "medium"}:
                system_leaders.append(str(card.get("title")))
            if len(system_leaders) >= 3:
                break
        print(f"design-system: {', '.join(system_leaders) or 'no strong/medium match'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
