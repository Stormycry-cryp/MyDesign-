#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
import os


LIB = Path(os.environ.get("DESIGNSTYLE_LIBRARY", str(Path.home() / ".codex" / "designstyle-library")))
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
    "missing_evidence",
    "dna",
    "component_json_path",
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
MEASURABLE_DNA = re.compile(r"\d")
CHALLENGE_PATTERNS = [
    "Attention Required | Cloudflare",
    "Cloudflare Ray ID",
    "Performance & security by Cloudflare",
    "checking your browser",
    "verify you are human",
    "cf-chl",
    "challenge-platform",
]


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
    if not isinstance(card.get("best_for"), list) or not card.get("best_for"):
        errors.append("best_for must be present as a non-empty list")
    if not isinstance(card.get("missing_evidence"), list):
        errors.append("missing_evidence must be present as a list")
    dna = card.get("dna")
    if not isinstance(dna, list):
        errors.append("dna must be present as a list")
        dna = []
    if len(dna) > 12:
        errors.append("dna must contain no more than 12 entries")
    for index, item in enumerate(dna):
        if not isinstance(item, dict):
            errors.append(f"dna item must be an object: {slug}#{index}")
            continue
        decision = item.get("decision")
        source = item.get("evidence_source")
        if not isinstance(decision, str) or not decision.strip():
            errors.append(f"dna item missing decision: {slug}#{index}")
        elif not MEASURABLE_DNA.search(decision):
            errors.append(f"dna decision is not measurable: {slug}#{index}")
        if not isinstance(source, str) or not source.strip():
            errors.append(f"dna item missing evidence_source: {slug}#{index}")
    component_json = card.get("component_json_path")
    if component_json is not None and not isinstance(component_json, str):
        errors.append("component_json_path must be a string when present")

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
    for key in [
        "tokens",
        "palette",
        "moodboard",
        "component_styles",
        "variables_css",
        "tailwind_theme",
        "motion_presets",
    ]:
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
            apply = tokens.get("apply")
            if not isinstance(apply, dict):
                errors.append(f"design system lacks apply tokens: {rel}")
            else:
                for apply_key in ["color", "type", "spacing", "radius", "shadow", "motion"]:
                    if apply_key not in apply:
                        errors.append(f"design system apply missing {apply_key}: {rel}")
            evidence = tokens.get("evidence")
            if not isinstance(evidence, dict):
                errors.append(f"design system lacks evidence layer: {rel}")
        elif key == "tailwind_theme":
            try:
                theme = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"invalid tailwind theme: {rel}: {exc}")
            else:
                if not isinstance(theme.get("theme"), dict):
                    errors.append(f"tailwind theme lacks theme object: {rel}")
        elif key in {"variables_css", "motion_presets"}:
            text = path.read_text(encoding="utf-8", errors="ignore")
            if key == "variables_css" and ":root" not in text:
                errors.append(f"variables css lacks :root: {rel}")
            if key == "motion_presets" and "prefers-reduced-motion" not in text:
                errors.append(f"motion presets lack reduced-motion fallback: {rel}")

    motion_rel = system_paths.get("motion")
    if not isinstance(motion_rel, str):
        errors.append("missing design system path: motion")
    else:
        motion_path = lib / motion_rel
        if not motion_path.exists():
            errors.append(f"motion system file missing: {motion_rel}")
        else:
            try:
                motion = json.loads(motion_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"invalid motion json: {motion_rel}: {exc}")
            else:
                items = motion.get("items") if isinstance(motion, dict) else None
                if not isinstance(items, list):
                    errors.append(f"motion items must be a list: {motion_rel}")
                    items = []
                for index, item in enumerate(items):
                    if not isinstance(item, dict):
                        errors.append(f"motion item must be an object: {motion_rel}#{index}")
                        continue
                    for field in ["selector_role", "trigger", "property", "duration_ms", "delay_ms", "easing", "description"]:
                        if field not in item:
                            errors.append(f"motion item missing {field}: {motion_rel}#{index}")
                    for field in ["duration_ms", "delay_ms"]:
                        value = item.get(field)
                        if not (isinstance(value, int) or value == "missing"):
                            errors.append(f"invalid motion duration: {motion_rel}#{index}.{field}={value}")
                    for field in ["selector_role", "trigger", "property", "easing", "description"]:
                        value = item.get(field)
                        if not isinstance(value, str) or not value.strip():
                            errors.append(f"invalid motion text field: {motion_rel}#{index}.{field}")

    joined_payload = json.dumps(card, ensure_ascii=False)
    if "assets-excluded" in joined_payload or "design-systems-excluded" in joined_payload:
        errors.append("active card points at excluded assets or design systems")
    for pattern in CHALLENGE_PATTERNS:
        if pattern.lower() in joined_payload.lower():
            errors.append(f"active card contains challenge-page evidence: {pattern}")

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
