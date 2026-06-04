#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


LIB = Path.home() / ".codex" / "designstyle-library"

DIMENSIONS = {
    "scene": {
        "file": "scene.md",
        "title": "Scene",
        "observed": [
            ("Product scene", "category_tags"),
            ("Audience", "best_for"),
            ("Page scope", "page_scope"),
            ("Community signal", "community_signal"),
            ("Essence", "Essence"),
            ("When to use", "When To Use"),
            ("When not to use", "When Not To Use"),
        ],
        "inference": ["Borrow"],
    },
    "layout_spacing": {
        "file": "layout-spacing.md",
        "title": "Layout And Spacing",
        "observed": [
            ("Visual layout", "Visual System"),
            ("Layout geometry", "Layout Geometry And Spacing"),
            ("Dimension ratios", "Dimension And Ratio System"),
            ("Implementation notes", "Implementation Notes"),
        ],
        "inference": ["Borrow"],
    },
    "type_copy": {
        "file": "type-copy.md",
        "title": "Type And Copy",
        "observed": [
            ("Typography rhythm", "Typography And Reading Rhythm"),
            ("Reference text", "Reference Text And Copy Grammar"),
            ("H1/H2/navigation samples", "Evidence Snapshot"),
            ("Visual typography", "Visual System"),
        ],
        "inference": ["Borrow"],
    },
    "color_surface": {
        "file": "color-surface.md",
        "title": "Color And Surface",
        "observed": [
            ("Color/material", "Color, Material, And Contrast"),
            ("Surface grammar", "Style Tokens And Surface Grammar"),
            ("Visual color", "Visual System"),
        ],
        "inference": ["Borrow"],
    },
    "assets": {
        "file": "assets.md",
        "title": "Assets",
        "observed": [
            ("Assets", "Assets"),
            ("Images/video observed", "Evidence Snapshot"),
            ("Asset loading", "Code Surface"),
        ],
        "inference": ["Borrow"],
    },
    "motion_code": {
        "file": "motion-code.md",
        "title": "Motion And Code",
        "observed": [
            ("Motion", "Motion"),
            ("Motion code", "Motion Code And Runtime Evidence"),
            ("Code surface", "Code Surface"),
            ("Implementation notes", "Implementation Notes"),
        ],
        "inference": ["Borrow"],
    },
    "components_states": {
        "file": "components-states.md",
        "title": "Components And States",
        "observed": [
            ("Components", "Interaction And Components"),
            ("Component grammar", "Component Grammar"),
            ("Code surface", "Code Surface"),
        ],
        "inference": ["Borrow"],
    },
}

CARD_STRENGTH_DIMS = {
    "layout_spacing": "layout_spacing",
    "type_copy": "type_copy",
    "motion_code": "motion_code",
}

LIST_FIELDS = {
    "tags",
    "category_tags",
    "style_tags",
    "structure_tags",
    "motion_tags",
    "code_tags",
    "best_for",
    "avoid_for",
}


def slug_from_reference(path: Path) -> str:
    slug = path.stem
    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", slug)
    return slug or path.stem


def parse_list(value: str) -> list[str]:
    value = value.strip()
    if not value or value == "[]":
        return []
    if value.startswith("[") and value.endswith("]"):
        try:
            data = json.loads(value)
            if isinstance(data, list):
                return [str(item).strip() for item in data if str(item).strip()]
        except json.JSONDecodeError:
            inner = value[1:-1]
            return [item.strip().strip("'\"") for item in inner.split(",") if item.strip().strip("'\"")]
    return [value.strip("'\"")]


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
        key = key.strip()
        raw = raw.strip()
        if key in LIST_FIELDS:
            data[key] = parse_list(raw)
        else:
            data[key] = raw.strip("'\"")
    return data


def section(text: str, name: str) -> str:
    match = re.search(rf"^## {re.escape(name)}\s*$([\s\S]*?)(?=^## |\Z)", text, re.M)
    return match.group(1).strip() if match else ""


def source_value(text: str, meta: dict[str, object], source: str) -> str:
    if source in meta:
        value = meta[source]
        if isinstance(value, list):
            return ", ".join(value)
        return str(value)
    return section(text, source)


def clean_value(value: str) -> str:
    value = re.sub(r"\n{3,}", "\n\n", value.strip())
    return value


def has_observed_value(value: str) -> bool:
    value = clean_value(value).lower()
    if not value:
        return False
    weak = {"todo", "n/a", "none recorded yet", "missing", "unknown"}
    compact = re.sub(r"[^a-z0-9]+", " ", value).strip()
    if compact in weak:
        return False
    lines = [line.strip() for line in value.splitlines() if line.strip()]
    useful = 0
    for line in lines:
        stripped = line.lstrip("- ").strip()
        if not stripped:
            continue
        if stripped.endswith(":") or stripped.lower() in weak:
            continue
        if re.search(r"\btodo\b", stripped, re.I):
            continue
        useful += 1
    return useful > 0


def bullet_block(label: str, value: str) -> str:
    value = clean_value(value)
    if not has_observed_value(value):
        return ""
    if "\n" not in value:
        return f"- {label}: {value}"
    indented = "\n".join(f"  {line}" if line else "" for line in value.splitlines())
    return f"- {label}:\n{indented}"


def markdown_list(values: list[str]) -> str:
    if not values:
        return "- None recorded."
    return "\n".join(f"- {item}" for item in values)


def dimension_markdown(name: str, text: str, meta: dict[str, object]) -> str:
    spec = DIMENSIONS[name]
    observed_blocks = []
    missing = []
    for label, source in spec["observed"]:
        value = source_value(text, meta, source)
        block = bullet_block(label, value)
        if block:
            observed_blocks.append(block)
        else:
            missing.append(f"{label} from {source}")

    inference_blocks = []
    for source in spec["inference"]:
        value = source_value(text, meta, source)
        block = bullet_block(source, value)
        if block:
            inference_blocks.append(block)

    limits = section(text, "Avoid Copying") or "Brand identity, proprietary assets, product names, claims, and exact copy."
    observed = "\n".join(observed_blocks) if observed_blocks else "- No observed values recorded in the full reference."
    inference = "\n".join(inference_blocks) if inference_blocks else "- No generator inference. Read the full reference before adapting."
    missing_text = markdown_list(missing) if missing else "- None recorded."
    return f"""# {spec["title"]}

## Observed
{observed}

## Inference
{inference}

## Missing Evidence
{missing_text}

## Do Not Copy
{clean_value(limits)}
"""


def observed_count(dimension_text: str) -> int:
    match = re.search(r"^## Observed\s*$([\s\S]*?)(?=^## |\Z)", dimension_text, re.M)
    if not match:
        return 0
    observed = match.group(1)
    if "No observed values recorded" in observed:
        return 0
    return sum(1 for line in observed.splitlines() if has_observed_value(line))


def evidence_strength(dimension_text: str, dimension_name: str) -> str:
    count = observed_count(dimension_text)
    missing_only = "No observed values recorded" in dimension_text
    if count == 0 or missing_only:
        return "missing"
    if dimension_name == "motion_code" and "no direct code evidence" in dimension_text.lower():
        return "weak"
    if count >= 5:
        return "strong"
    if count >= 2:
        return "medium"
    return "weak"


def screenshot_strength(meta: dict[str, object], lib: Path) -> str:
    screenshot = str(meta.get("evidence_screenshot", "")).strip()
    if not screenshot:
        return "missing"
    if (lib / screenshot).exists():
        return "strong"
    return "weak"


def section_lines(text: str, name: str) -> list[str]:
    content = section(text, name)
    lines = []
    for line in content.splitlines():
        cleaned = line.strip().lstrip("- ").strip()
        if cleaned and not re.search(r"\btodo\b", cleaned, re.I):
            lines.append(cleaned)
    return lines


def excerpt(value: str, limit: int = 180) -> str:
    value = " ".join(clean_value(value).split())
    return value[:limit]


def build_card(reference: Path, lib: Path, dimensions: dict[str, str]) -> dict[str, object]:
    text = reference.read_text(encoding="utf-8", errors="ignore")
    meta = parse_frontmatter(text)
    slug = slug_from_reference(reference)
    evidence_limits = section_lines(text, "Evidence Limits")
    if not evidence_limits:
        evidence_limits = ["No explicit evidence limits recorded."]
    title = str(meta.get("title") or slug)
    relative_reference = f"references/{reference.name}"
    selection = str(meta.get("community_signal") or excerpt(section(text, "Essence")) or "Selected from existing reference library.")
    strength = {
        "screenshot": screenshot_strength(meta, lib),
        "layout_spacing": evidence_strength(dimensions["layout_spacing"], "layout_spacing"),
        "type_copy": evidence_strength(dimensions["type_copy"], "type_copy"),
        "motion_code": evidence_strength(dimensions["motion_code"], "motion_code"),
    }
    return {
        "slug": slug,
        "title": title,
        "reference_path": relative_reference,
        "category_tags": list(meta.get("category_tags") or []),
        "style_tags": list(meta.get("style_tags") or []),
        "structure_tags": list(meta.get("structure_tags") or []),
        "motion_tags": list(meta.get("motion_tags") or []),
        "code_tags": list(meta.get("code_tags") or []),
        "page_scope": str(meta.get("page_scope") or ""),
        "best_for": list(meta.get("best_for") or []),
        "avoid_for": list(meta.get("avoid_for") or []),
        "evidence_strength": strength,
        "dimension_paths": {
            "scene": f"dimensions/{slug}/scene.md",
            "layout_spacing": f"dimensions/{slug}/layout-spacing.md",
            "type_copy": f"dimensions/{slug}/type-copy.md",
            "color_surface": f"dimensions/{slug}/color-surface.md",
            "assets": f"dimensions/{slug}/assets.md",
            "motion_code": f"dimensions/{slug}/motion-code.md",
            "components_states": f"dimensions/{slug}/components-states.md",
        },
        "selection_note": selection,
        "evidence_limits": evidence_limits,
    }


def references_for_args(args: argparse.Namespace, lib: Path) -> list[Path]:
    if args.reference:
        return [Path(args.reference).expanduser()]
    if args.all:
        return sorted((lib / "references").glob("*.md"))
    raise SystemExit("Use --reference PATH or --all")


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def build_outputs(reference: Path, lib: Path) -> tuple[dict[str, object], dict[str, str]]:
    text = reference.read_text(encoding="utf-8", errors="ignore")
    meta = parse_frontmatter(text)
    dimensions = {name: dimension_markdown(name, text, meta) for name in DIMENSIONS}
    card = build_card(reference, lib, dimensions)
    return card, dimensions


def update_indexes(lib: Path) -> None:
    cards_dir = lib / "indexes" / "cards"
    cards = []
    facets: dict[str, dict[str, int]] = {
        "category_tags": {},
        "style_tags": {},
        "structure_tags": {},
        "motion_tags": {},
        "code_tags": {},
        "page_scope": {},
    }
    for path in sorted(cards_dir.glob("*.json")):
        card = json.loads(path.read_text(encoding="utf-8"))
        cards.append({
            "slug": card["slug"],
            "title": card["title"],
            "reference_path": card["reference_path"],
            "card_path": f"indexes/cards/{path.name}",
        })
        for key in ["category_tags", "style_tags", "structure_tags", "motion_tags", "code_tags"]:
            for value in card.get(key, []):
                facets[key][value] = facets[key].get(value, 0) + 1
        scope = card.get("page_scope", "")
        if scope:
            facets["page_scope"][scope] = facets["page_scope"].get(scope, 0) + 1
    write_json(lib / "indexes" / "manifest.json", {"cards": cards, "total_cards": len(cards)})
    write_json(lib / "indexes" / "facets.json", facets)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build progressive designstyle cards and dimension summaries.")
    parser.add_argument("--library", default=str(LIB))
    parser.add_argument("--reference")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    lib = Path(args.library).expanduser()
    refs = references_for_args(args, lib)
    planned_dimensions = 0
    cards = []
    for ref in refs:
        if not ref.exists():
            raise SystemExit(f"Reference not found: {ref}")
        card, dimensions = build_outputs(ref, lib)
        cards.append(card)
        planned_dimensions += len(dimensions)
        if args.dry_run:
            continue
        slug = str(card["slug"])
        write_json(lib / "indexes" / "cards" / f"{slug}.json", card)
        dim_dir = lib / "dimensions" / slug
        dim_dir.mkdir(parents=True, exist_ok=True)
        for key, content in dimensions.items():
            filename = DIMENSIONS[key]["file"]
            (dim_dir / filename).write_text(content, encoding="utf-8")

    if not args.dry_run:
        update_indexes(lib)

    action = "dry_run" if args.dry_run else "wrote"
    print(f"{action} planned_cards={len(cards)} planned_dimensions={planned_dimensions}")
    for card in cards:
        print(f"- {card['slug']}: {card['reference_path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
