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
DESIGN_SYSTEM_FILES = {"tokens", "palette", "moodboard", "component_styles"}
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
        "live_dom": 30,
        "component_coverage": 15,
        "design_system": 15,
        "component_styles": 15,
        "interaction_states": 10,
        "retrieval_validation": 10,
        "hygiene": 5,
    }
    labels = {
        "live_dom": "live DOM/component evidence",
        "component_coverage": "component category coverage",
        "design_system": "design-system file completeness",
        "component_styles": "reusable computed component styles",
        "interaction_states": "hover/focus state evidence",
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
        live_dom += 12
    if sample_count:
        live_dom += 8
    live_dom += points(min(sample_count, 80) / 80 * 7, 7)
    live_dom += points(min(category_count, 4) / 4 * 3, 3)

    component_coverage = points(min(category_count, 6) / 6 * 10, 10)
    component_coverage += points(min(important_count, 5) / 5 * 5, 5)

    existing_system_files = sum(1 for key in DESIGN_SYSTEM_FILES if design_files.get(key) and design_files[key].exists())
    design_system = points(existing_system_files / 4 * 6, 6)
    design_system += points(min(len(colors), 8) / 8 * 4, 4)
    design_system += points(min(len(component_style_categories), 5) / 5 * 4, 4)
    design_system += 1 if design_strength == "strong" else 0

    component_styles = points(min(len(component_style_categories), 6) / 6 * 7, 7)
    component_styles += points(min(style_lines, 30) / 30 * 5, 5)
    component_styles += points(min(sample_count, 50) / 50 * 3, 3)

    interaction_states = points(min(state_attempts, 12) / 12 * 6, 6)
    interaction_states += points(min(changed_states, 6) / 6 * 4, 4)

    retrieval_validation = points(dimensions_present / len(DIMENSIONS) * 5, 5)
    retrieval_validation += 2 if reference_exists else 0
    retrieval_validation += 2 if isinstance(limits, list) and limits else 0
    retrieval_validation += 1 if design_strength in {"strong", "medium"} else 0

    hygiene = 5
    if blocked_risk:
        hygiene -= 3
    if scientific_noise:
        hygiene -= 2
    hygiene = max(0, hygiene)

    parts = {
        "live_dom": live_dom,
        "component_coverage": component_coverage,
        "design_system": design_system,
        "component_styles": component_styles,
        "interaction_states": interaction_states,
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
            "live_dom": 30,
            "component_coverage": 15,
            "design_system": 15,
            "component_styles": 15,
            "interaction_states": 10,
            "retrieval_validation": 10,
            "hygiene": 5,
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
        f"| Live DOM evidence | {rubric['live_dom']} | Component JSON exists, has broad live-browser samples, and comes from real rendered DOM. |",
        f"| Component coverage | {rubric['component_coverage']} | Captures several useful categories such as nav, buttons, cards, forms, icons, and sections. |",
        f"| Design-system retention | {rubric['design_system']} | Keeps tokens, palette, moodboard, component-styles, palette colors, and component system categories. |",
        f"| Component-style usefulness | {rubric['component_styles']} | `component-styles.md`/`tokens.json` contain reusable computed CSS, geometry, spacing, type, radii, borders, shadows, and transitions. |",
        f"| Interaction states | {rubric['interaction_states']} | Hover/focus attempts and actual computed deltas are captured when observable. |",
        f"| Retrieval/validation | {rubric['retrieval_validation']} | Reference has complete L1/L2/L3 paths, evidence limits, and design-system metadata. |",
        f"| Hygiene | {rubric['hygiene']} | No blocked/challenge text and no abnormal scientific-notation px noise in active evidence. |",
        "",
        "## Score Table",
        "",
        "| # | Slug | Score | Grade | Live DOM /30 | Coverage /15 | Design system /15 | Component styles /15 | States /10 | Retrieval /10 | Hygiene /5 | Samples | Cats | State attempts | Changed states | Palette colors | Penalties |",
        "|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for idx, row in enumerate(rows, 1):
        parts = row["parts"]
        penalties = "; ".join(row["penalties"])
        lines.append(
            "| {idx} | {slug} | {score} | {grade} | {live_dom} | {coverage} | {system} | {styles} | {states} | {retrieval} | {hygiene} | {samples} | {cats} | {attempts} | {changed} | {colors} | {penalties} |".format(
                idx=idx,
                slug=row["slug"],
                score=row["score"],
                grade=row["grade"],
                live_dom=parts["live_dom"],
                coverage=parts["component_coverage"],
                system=parts["design_system"],
                styles=parts["component_styles"],
                states=parts["interaction_states"],
                retrieval=parts["retrieval_validation"],
                hygiene=parts["hygiene"],
                samples=row["samples"],
                cats=row["category_count"],
                attempts=row["state_attempts"],
                changed=row["changed_states"],
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
