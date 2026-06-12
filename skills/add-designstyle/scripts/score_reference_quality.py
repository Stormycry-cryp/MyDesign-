#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path
from statistics import mean, median


LIB = Path.home() / ".codex" / "designstyle-library"
DIMENSIONS = {
    "scene",
    "layout_spacing",
    "type_copy",
    "color_surface",
    "assets",
    "motion_code",
    "components_states",
}
DESIGN_SYSTEM_FILES = {
    "tokens",
    "palette",
    "moodboard",
    "component_styles",
    "motion",
    "variables_css",
    "tailwind_theme",
    "motion_presets",
}
BLOCKED_PATTERNS = re.compile(
    r"Attention Required!\s*\|\s*Cloudflare|Cloudflare Ray ID|Performance\s*&\s*security by Cloudflare|verify you are human|checking your browser|security challenge|cf-chl|challenge-platform",
    re.I,
)
SCIENTIFIC_PX = re.compile(r"\b\d+(?:\.\d+)?e[+-]?\d+px\b", re.I)


def grade(score: float) -> str:
    if score >= 95:
        return "A"
    if score >= 90:
        return "A-"
    if score >= 85:
        return "B+"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C+"
    if score >= 60:
        return "C"
    return "D"


def points(value: float, cap: int) -> int:
    return max(0, min(cap, round(value)))


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def asset_path_for_slug(lib: Path, slug: str) -> Path | None:
    matches = sorted((lib / "assets").glob(f"*-{slug}-component-styles.json"))
    return matches[-1] if matches else None


def text_has_pattern(path: Path, pattern: re.Pattern[str]) -> bool:
    try:
        return bool(pattern.search(path.read_text(encoding="utf-8", errors="ignore")))
    except OSError:
        return False


def summarize_penalties(parts: dict[str, int], row: dict[str, object]) -> list[str]:
    penalties: list[str] = []
    caps = {
        "live_dom": 24,
        "component_coverage": 12,
        "design_system": 12,
        "component_styles": 12,
        "interaction_states": 8,
        "motion_structure": 10,
        "apply_pack": 10,
        "retrieval_validation": 8,
        "hygiene": 4,
    }
    labels = {
        "live_dom": "retained browser component evidence",
        "component_coverage": "component category coverage",
        "design_system": "design-system file completeness",
        "component_styles": "reusable computed component styles",
        "interaction_states": "hover/focus state evidence",
        "motion_structure": "structured motion evidence",
        "apply_pack": "reusable apply-token pack",
        "retrieval_validation": "progressive retrieval metadata",
        "hygiene": "blocked/noise hygiene",
    }
    for key, cap in caps.items():
        lost = cap - parts.get(key, 0)
        if lost:
            penalties.append(f"-{lost} {labels[key]}")
    if not penalties:
        penalties.append("none")
    if row.get("blocked_risk"):
        penalties.append("blocked/security text present")
    if row.get("scientific_px_noise"):
        penalties.append("scientific-notation px noise present")
    return penalties


def score_card(lib: Path, card_path: Path) -> dict[str, object]:
    card = read_json(card_path)
    slug = str(card.get("slug") or card_path.stem)
    asset_path = asset_path_for_slug(lib, slug)
    asset = read_json(asset_path) if asset_path else {}
    component = asset.get("component_evidence", {}) if isinstance(asset, dict) else {}
    samples = component.get("samples", []) if isinstance(component, dict) else []
    counts = component.get("counts", {}) if isinstance(component, dict) else {}
    state_samples = component.get("stateSamples", []) if isinstance(component, dict) else []

    sample_count = len(samples) if isinstance(samples, list) else 0
    category_count = len([key for key, value in counts.items() if value]) if isinstance(counts, dict) else 0
    categories = set(counts.keys()) if isinstance(counts, dict) else set()
    important_categories = {"Navigation", "Button", "Card", "Form", "Icon", "Section"}
    important_count = len(categories & important_categories)

    system_paths = card.get("design_system_paths", {})
    if not isinstance(system_paths, dict):
        system_paths = {}
    design_files = {key: lib / rel for key, rel in system_paths.items() if isinstance(rel, str)}
    tokens = read_json(design_files["tokens"]) if "tokens" in design_files else {}
    palette = tokens.get("palette", {}) if isinstance(tokens, dict) else {}
    token_components = tokens.get("component_styles", {}) if isinstance(tokens, dict) else {}
    apply = tokens.get("apply", {}) if isinstance(tokens, dict) else {}
    colors = palette.get("colors", []) if isinstance(palette, dict) else []
    component_style_categories = [
        key
        for key, value in token_components.items()
        if isinstance(value, dict) and value.get("style_evidence")
    ] if isinstance(token_components, dict) else []
    style_lines = sum(
        len(value.get("style_evidence", []))
        for value in token_components.values()
        if isinstance(value, dict) and isinstance(value.get("style_evidence"), list)
    ) if isinstance(token_components, dict) else 0

    state_attempts = len(state_samples) if isinstance(state_samples, list) else 0
    changed_states = 0
    if isinstance(state_samples, list):
        for state in state_samples:
            if not isinstance(state, dict):
                continue
            hover = state.get("hover_changed")
            focus = state.get("focus_changed")
            if (isinstance(hover, dict) and hover) or (isinstance(focus, dict) and focus):
                changed_states += 1

    dimension_paths = card.get("dimension_paths", {})
    if not isinstance(dimension_paths, dict):
        dimension_paths = {}
    dimensions_present = sum(
        1
        for key in DIMENSIONS
        if isinstance(dimension_paths.get(key), str) and (lib / dimension_paths[key]).exists()
    )
    evidence_strength = card.get("evidence_strength", {})
    design_strength = evidence_strength.get("design_system") if isinstance(evidence_strength, dict) else None
    limits = card.get("evidence_limits", [])
    reference_path = card.get("reference_path")
    reference_exists = isinstance(reference_path, str) and (lib / reference_path).exists()

    active_paths = []
    if asset_path:
        active_paths.append(asset_path)
    active_paths.extend(path for path in design_files.values() if path.exists())
    if reference_exists:
        active_paths.append(lib / str(reference_path))
    blocked_risk = any(text_has_pattern(path, BLOCKED_PATTERNS) for path in active_paths)
    scientific_noise = any(text_has_pattern(path, SCIENTIFIC_PX) for path in active_paths)

    live_dom = 0
    if asset_path and asset_path.exists():
        live_dom += 9
    if sample_count:
        live_dom += 6
    live_dom += points(min(sample_count, 80) / 80 * 6, 6)
    live_dom += points(min(category_count, 4) / 4 * 3, 3)

    component_coverage = points(min(category_count, 6) / 6 * 8, 8)
    component_coverage += points(min(important_count, 5) / 5 * 4, 4)

    existing_system_files = sum(1 for key in DESIGN_SYSTEM_FILES if design_files.get(key) and design_files[key].exists())
    design_system = points(existing_system_files / len(DESIGN_SYSTEM_FILES) * 4, 4)
    design_system += points(min(len(colors), 8) / 8 * 4, 4)
    design_system += points(min(len(component_style_categories), 5) / 5 * 3, 3)
    design_system += 1 if design_strength == "strong" else 0

    component_styles = points(min(len(component_style_categories), 6) / 6 * 6, 6)
    component_styles += points(min(style_lines, 30) / 30 * 4, 4)
    component_styles += points(min(sample_count, 50) / 50 * 2, 2)

    interaction_states = points(min(state_attempts, 12) / 12 * 5, 5)
    interaction_states += points(min(changed_states, 6) / 6 * 3, 3)

    motion_payload = read_json(design_files["motion"]) if "motion" in design_files else {}
    motion_items = motion_payload.get("items", []) if isinstance(motion_payload, dict) else []
    if not isinstance(motion_items, list):
        motion_items = []
    complete_motion = 0
    for item in motion_items:
        if not isinstance(item, dict):
            continue
        required = ["selector_role", "trigger", "property", "duration_ms", "delay_ms", "easing", "description"]
        if all(item.get(key) not in {None, "", "missing"} or key in {"delay_ms"} for key in required):
            complete_motion += 1
    motion_structure = points(min(len(motion_items), 8) / 8 * 4, 4)
    motion_structure += points(min(complete_motion, 6) / 6 * 4, 4)
    motion_structure += 1 if motion_payload.get("source_motion_path") not in {None, "", "missing"} else 0
    motion_structure += 1 if (lib / str(system_paths.get("motion", ""))).exists() else 0

    apply_sections = [key for key in ["color", "type", "spacing", "radius", "shadow", "motion"] if isinstance(apply, dict) and key in apply]
    apply_files = [
        key
        for key in ["variables_css", "tailwind_theme", "motion_presets"]
        if design_files.get(key) and design_files[key].exists()
    ]
    apply_pack = points(len(apply_sections) / 6 * 5, 5)
    apply_pack += points(len(apply_files) / 3 * 4, 4)
    apply_pack += 1 if isinstance(apply.get("motion"), dict) and apply.get("motion") else 0

    retrieval_validation = points(dimensions_present / len(DIMENSIONS) * 4, 4)
    retrieval_validation += 1 if reference_exists else 0
    retrieval_validation += 2 if isinstance(limits, list) and limits else 0
    retrieval_validation += 1 if design_strength in {"strong", "medium"} else 0

    hygiene = 4
    if blocked_risk:
        hygiene -= 2
    if scientific_noise:
        hygiene -= 2
    hygiene = max(0, hygiene)

    parts = {
        "live_dom": live_dom,
        "component_coverage": component_coverage,
        "design_system": design_system,
        "component_styles": component_styles,
        "interaction_states": interaction_states,
        "motion_structure": motion_structure,
        "apply_pack": apply_pack,
        "retrieval_validation": retrieval_validation,
        "hygiene": hygiene,
    }
    total = sum(parts.values())
    row: dict[str, object] = {
        "slug": slug,
        "title": card.get("title", slug),
        "score": total,
        "grade": grade(total),
        "parts": parts,
        "samples": sample_count,
        "categories": sorted(categories),
        "category_count": category_count,
        "state_attempts": state_attempts,
        "changed_states": changed_states,
        "component_style_categories": sorted(component_style_categories),
        "component_style_category_count": len(component_style_categories),
        "palette_colors": len(colors) if isinstance(colors, list) else 0,
        "dimensions_present": dimensions_present,
        "design_system_files_present": existing_system_files,
        "motion_items": len(motion_items),
        "complete_motion_items": complete_motion,
        "apply_sections": sorted(apply_sections),
        "apply_files": sorted(apply_files),
        "asset_path": str(asset_path.relative_to(lib)) if asset_path else "",
        "tokens_path": system_paths.get("tokens", ""),
        "component_styles_path": system_paths.get("component_styles", ""),
        "reference_path": reference_path or "",
        "blocked_risk": blocked_risk,
        "scientific_px_noise": scientific_noise,
    }
    row["penalties"] = summarize_penalties(parts, row)
    if total >= 90:
        row["usefulness"] = "strong implementation reference"
    elif total >= 80:
        row["usefulness"] = "usable with selective follow-up"
    elif total >= 70:
        row["usefulness"] = "usable mainly for aesthetic or narrow component cues"
    else:
        row["usefulness"] = "weak active reference; consider replacement or manual enrichment"
    return row


def score_library(lib: Path) -> dict[str, object]:
    card_paths = sorted((lib / "indexes" / "cards").glob("*.json"))
    rows = [score_card(lib, path) for path in card_paths]
    scores = [int(row["score"]) for row in rows]
    buckets = {
        "A_or_A_minus_90_plus": sum(1 for score in scores if score >= 90),
        "B_80_to_89": sum(1 for score in scores if 80 <= score < 90),
        "C_70_to_79": sum(1 for score in scores if 70 <= score < 80),
        "below_70": sum(1 for score in scores if score < 70),
    }
    return {
        "generated_at": date.today().isoformat(),
        "library": str(lib),
        "rubric": {
            "live_dom": 24,
            "component_coverage": 12,
            "design_system": 12,
            "component_styles": 12,
            "interaction_states": 8,
            "motion_structure": 10,
            "apply_pack": 10,
            "retrieval_validation": 8,
            "hygiene": 4,
        },
        "summary": {
            "reference_count": len(rows),
            "average_score": round(mean(scores), 1) if scores else 0,
            "median_score": round(median(scores), 1) if scores else 0,
            "min_score": min(scores) if scores else 0,
            "max_score": max(scores) if scores else 0,
            "buckets": buckets,
            "blocked_risk_count": sum(1 for row in rows if row["blocked_risk"]),
            "scientific_px_noise_count": sum(1 for row in rows if row["scientific_px_noise"]),
        },
        "references": rows,
    }


def markdown_report(payload: dict[str, object]) -> str:
    summary = payload["summary"]
    rubric = payload["rubric"]
    rows = payload["references"]
    lines = [
        "# Per-Reference Design-System Quality Scores",
        "",
        f"Date: {payload['generated_at']}",
        "",
        "This report scores each active reference individually for practical design-system and component-style reuse. It is not a pure aesthetic taste score; it measures how useful each reference is as implementation-grade evidence.",
        "",
        "## Summary",
        "",
        f"- Active references scored: {summary['reference_count']}",
        f"- Average score: {summary['average_score']}/100",
        f"- Median score: {summary['median_score']}/100",
        f"- Score range: {summary['min_score']} to {summary['max_score']}",
        f"- 90+: {summary['buckets']['A_or_A_minus_90_plus']}",
        f"- 80-89: {summary['buckets']['B_80_to_89']}",
        f"- 70-79: {summary['buckets']['C_70_to_79']}",
        f"- Below 70: {summary['buckets']['below_70']}",
        f"- Blocked/security contamination in active scored files: {summary['blocked_risk_count']}",
        f"- Scientific-notation px noise in active scored files: {summary['scientific_px_noise_count']}",
        "",
        "## Rubric",
        "",
        "| Dimension | Points | Meaning |",
        "|---|---:|---|",
        f"| Retained component evidence | {rubric['live_dom']} | Component JSON exists, has broad live-browser samples, and comes from real rendered DOM without retaining raw DOM snapshots in the library. |",
        f"| Component coverage | {rubric['component_coverage']} | Captures several useful categories such as nav, buttons, cards, forms, icons, and sections. |",
        f"| Design-system retention | {rubric['design_system']} | Keeps tokens, palette, moodboard, component-styles, palette colors, and component system categories. |",
        f"| Component-style usefulness | {rubric['component_styles']} | `component-styles.md`/`tokens.json` contain reusable computed CSS, geometry, spacing, type, radii, borders, shadows, and transitions. |",
        f"| Interaction states | {rubric['interaction_states']} | Hover/focus attempts and actual computed deltas are captured when observable. |",
        f"| Motion structure | {rubric['motion_structure']} | `motion.json` contains structured selector roles, triggers, properties, timing, easing, descriptions, and source evidence. |",
        f"| Apply pack | {rubric['apply_pack']} | `tokens.json` has apply-layer tokens and generated `variables.css`, `tailwind.theme.json`, and `motion-presets.css`. |",
        f"| Retrieval/validation | {rubric['retrieval_validation']} | Reference has complete L1/L2/L3 paths, evidence limits, and design-system metadata. |",
        f"| Hygiene | {rubric['hygiene']} | No blocked/challenge text and no abnormal scientific-notation px noise in active evidence. |",
        "",
        "## Score Table",
        "",
        "| # | Slug | Score | Grade | Component evidence /24 | Coverage /12 | Design system /12 | Component styles /12 | States /8 | Motion /10 | Apply /10 | Retrieval /8 | Hygiene /4 | Samples | Cats | State attempts | Changed states | Motion items | Palette colors | Penalties |",
        "|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for idx, row in enumerate(rows, 1):
        parts = row["parts"]
        penalties = "; ".join(row["penalties"])
        lines.append(
            "| {idx} | {slug} | {score} | {grade} | {live_dom} | {coverage} | {system} | {styles} | {states} | {motion} | {apply} | {retrieval} | {hygiene} | {samples} | {cats} | {attempts} | {changed} | {motion_items} | {colors} | {penalties} |".format(
                idx=idx,
                slug=row["slug"],
                score=row["score"],
                grade=row["grade"],
                live_dom=parts["live_dom"],
                coverage=parts["component_coverage"],
                system=parts["design_system"],
                styles=parts["component_styles"],
                states=parts["interaction_states"],
                motion=parts["motion_structure"],
                apply=parts["apply_pack"],
                retrieval=parts["retrieval_validation"],
                hygiene=parts["hygiene"],
                samples=row["samples"],
                cats=row["category_count"],
                attempts=row["state_attempts"],
                changed=row["changed_states"],
                motion_items=row["motion_items"],
                colors=row["palette_colors"],
                penalties=penalties,
            )
        )
    lines.extend([
        "",
        "## Lowest Scores",
        "",
    ])
    for row in sorted(rows, key=lambda item: (item["score"], item["slug"]))[:12]:
        lines.append(
            f"- `{row['slug']}`: {row['score']}/100 ({row['grade']}) — {row['usefulness']}; penalties: {'; '.join(row['penalties'])}."
        )
    lines.extend([
        "",
        "## Evidence Paths",
        "",
        "| Slug | Component JSON | Tokens | Component styles | Full reference |",
        "|---|---|---|---|---|",
    ])
    for row in rows:
        lines.append(
            f"| {row['slug']} | {row['asset_path']} | {row['tokens_path']} | {row['component_styles_path']} | {row['reference_path']} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Score each active designstyle reference for design-system usefulness.")
    parser.add_argument("--library", default=str(LIB))
    parser.add_argument("--markdown-output")
    parser.add_argument("--json-output")
    args = parser.parse_args()

    lib = Path(args.library).expanduser()
    payload = score_library(lib)

    if args.json_output:
        Path(args.json_output).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.markdown_output:
        Path(args.markdown_output).write_text(markdown_report(payload), encoding="utf-8")
    if not args.json_output and not args.markdown_output:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        summary = payload["summary"]
        print(
            f"scored={summary['reference_count']} average={summary['average_score']} "
            f"median={summary['median_score']} min={summary['min_score']} max={summary['max_score']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
