#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


LIB = Path.home() / ".codex" / "designstyle-library"
REQUIRED_CARD_FIELDS = [
    "slug",
    "title",
    "reference_path",
    "category_tags",
    "style_tags",
    "structure_tags",
    "motion_tags",
    "code_tags",
    "page_scope",
    "best_for",
    "avoid_for",
    "evidence_strength",
    "dimension_paths",
    "design_system_paths",
    "selection_note",
    "evidence_limits",
]
REQUIRED_DIMENSIONS = [
    "scene",
    "layout_spacing",
    "type_copy",
    "color_surface",
    "assets",
    "motion_code",
    "components_states",
]
ALLOWED_STRENGTH = {"strong", "medium", "weak", "missing"}


def observed_has_values(text: str) -> bool:
    match = re.search(r"^## Observed\s*$([\s\S]*?)(?=^## |\Z)", text, re.M)
    if not match:
        return False
    observed = match.group(1)
    if "No observed values recorded" in observed:
        return False
    for line in observed.splitlines():
        cleaned = line.strip().lstrip("- ").strip()
        if not cleaned or cleaned.endswith(":"):
            continue
        if re.search(r"\btodo\b", cleaned, re.I):
            continue
        return True
    return False


def has_missing_section(text: str) -> bool:
    match = re.search(r"^## Missing Evidence\s*$([\s\S]*?)(?=^## |\Z)", text, re.M)
    return bool(match and match.group(1).strip())


def validate_card(path: Path, lib: Path) -> dict[str, object]:
    errors: list[str] = []
    try:
        card = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {"path": str(path), "valid": False, "errors": [f"invalid json: {exc}"]}

    for field in REQUIRED_CARD_FIELDS:
        if field not in card:
            errors.append(f"missing card field: {field}")

    slug = card.get("slug", path.stem)
    reference_path = card.get("reference_path")
    if isinstance(reference_path, str):
        if not (lib / reference_path).exists():
            errors.append(f"missing reference: {reference_path}")
    else:
        errors.append("reference_path must be a string")

    if "avoid_for" in card and not isinstance(card["avoid_for"], list):
        errors.append("avoid_for must be present as a list")

    strength = card.get("evidence_strength", {})
    if not isinstance(strength, dict):
        errors.append("evidence_strength must be an object")
        strength = {}
    for key in ["screenshot", "layout_spacing", "type_copy", "motion_code", "design_system"]:
        value = strength.get(key)
        if value not in ALLOWED_STRENGTH:
            errors.append(f"invalid evidence strength: {key}={value}")

    dim_paths = card.get("dimension_paths", {})
    if not isinstance(dim_paths, dict):
        errors.append("dimension_paths must be an object")
        dim_paths = {}
    for key in REQUIRED_DIMENSIONS:
        rel = dim_paths.get(key)
        if not isinstance(rel, str):
            errors.append(f"missing dimension path: {key}")
            continue
        dim_path = lib / rel
        if not dim_path.exists():
            errors.append(f"dimension missing: {rel}")
            continue
        text = dim_path.read_text(encoding="utf-8", errors="ignore")
        if "## Observed" not in text:
            errors.append(f"dimension lacks Observed section: {rel}")
        if "## Inference" not in text:
            errors.append(f"dimension lacks Inference section: {rel}")
        if "## Do Not Copy" not in text:
            errors.append(f"dimension lacks Do Not Copy section: {rel}")
        if not has_missing_section(text):
            errors.append(f"dimension lacks explicit Missing Evidence: {rel}")

        strength_key = key if key in {"layout_spacing", "type_copy", "motion_code"} else None
        if strength_key and strength.get(strength_key) == "strong" and not observed_has_values(text):
            errors.append(f"strong evidence claimed with no observed values: {slug}/{key}")

    system_paths = card.get("design_system_paths", {})
    if not isinstance(system_paths, dict):
        errors.append("design_system_paths must be an object")
        system_paths = {}
    for key in ["tokens", "palette", "moodboard", "component_styles"]:
        rel = system_paths.get(key)
        if not isinstance(rel, str):
            errors.append(f"missing design system path: {key}")
            continue
        path = lib / rel
        if not path.exists():
            errors.append(f"design system file missing: {rel}")
            continue
        if key == "tokens":
            try:
                tokens = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"invalid design system tokens: {rel}: {exc}")
                continue
            palette = tokens.get("palette", {})
            components = tokens.get("component_styles", {})
            colors = palette.get("colors", []) if isinstance(palette, dict) else []
            if not isinstance(colors, list) or not colors:
                errors.append(f"design system lacks palette colors: {rel}")
            if not isinstance(components, dict) or not components:
                errors.append(f"design system lacks component styles: {rel}")

    return {"path": str(path), "slug": slug, "valid": not errors, "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate progressive designstyle cards and dimension summaries.")
    parser.add_argument("--library", default=str(LIB))
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    lib = Path(args.library).expanduser()
    cards_dir = lib / "indexes" / "cards"
    cards = sorted(cards_dir.glob("*.json"))
    results = [validate_card(path, lib) for path in cards]
    errors = [error for row in results for error in row["errors"]]
    if not cards:
        errors.append(f"no cards found: {cards_dir}")

    payload = {
        "valid": not errors,
        "total_cards": len(cards),
        "invalid_cards": sum(1 for row in results if not row["valid"]),
        "errors": errors,
        "results": results,
    }
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"cards={payload['total_cards']} invalid={payload['invalid_cards']} errors={len(errors)}")
        for error in errors:
            print(f"- {error}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
