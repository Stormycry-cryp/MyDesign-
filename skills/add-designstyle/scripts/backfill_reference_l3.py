#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
import os


LIB = Path(os.environ.get("DESIGNSTYLE_LIBRARY", str(Path.home() / ".codex" / "designstyle-library")))


def read_json(path: Path) -> dict[str, object]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def has_section(text: str, name: str) -> bool:
    return bool(re.search(rf"^## {re.escape(name)}\s*$", text, re.M))


def section_text(text: str, name: str) -> str:
    match = re.search(rf"^## {re.escape(name)}\s*$([\s\S]*?)(?=^## |\Z)", text, re.M)
    return match.group(1).strip() if match else ""


def line_value(text: str, marker: str) -> str:
    match = re.search(rf"^- {re.escape(marker)}:\s*(.*?)\s*$", text, re.M)
    value = match.group(1).strip() if match else ""
    return value or "missing"


def block(title: str, lines: list[str]) -> str:
    body = "\n".join(lines or ["- missing: no evidence available."])
    return f"\n## {title}\n{body}\n"


def insert_after_section(text: str, anchor: str, section_block: str) -> str:
    match = re.search(rf"^## {re.escape(anchor)}\s*$[\s\S]*?(?=^## |\Z)", text, re.M)
    if not match:
        return text.rstrip() + section_block + "\n"
    return text[: match.end()].rstrip() + "\n" + section_block + text[match.end():]


def append_line_to_section(text: str, section: str, line: str) -> str:
    match = re.search(rf"^## {re.escape(section)}\s*$[\s\S]*?(?=^## |\Z)", text, re.M)
    if not match:
        return text.rstrip() + f"\n\n## {section}\n{line}\n"
    section_body = match.group(0).rstrip()
    if line in section_body:
        return text
    return text[: match.start()] + section_body + "\n" + line + "\n" + text[match.end():]


def slug_from_reference(path: Path) -> str:
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)


def card_for_reference(reference: Path, lib: Path) -> dict[str, object]:
    slug = slug_from_reference(reference)
    card = read_json(lib / "indexes" / "cards" / f"{slug}.json")
    if card:
        return card
    for path in sorted((lib / "indexes" / "cards").glob("*.json")):
        candidate = read_json(path)
        if candidate.get("reference_path") == f"references/{reference.name}":
            return candidate
    return {}


def motion_payload(card: dict[str, object], lib: Path) -> dict[str, object]:
    paths = card.get("design_system_paths") if isinstance(card.get("design_system_paths"), dict) else {}
    rel = paths.get("motion") if isinstance(paths, dict) else None
    return read_json(lib / rel) if isinstance(rel, str) else {}


def style_dna_block(card: dict[str, object]) -> str:
    dna = card.get("dna") if isinstance(card.get("dna"), list) else []
    lines: list[str] = []
    for item in dna[:12]:
        if not isinstance(item, dict):
            continue
        decision = str(item.get("decision") or "missing").strip()
        source = str(item.get("evidence_source") or "missing").strip()
        if decision and source:
            lines.append(f"- {decision}; source: {source}")
    if not lines:
        lines = ["- missing: no measurable Style DNA could be extracted from existing evidence."]
    return block("Style DNA", lines)


def reference_text_block(text: str) -> str:
    visual = section_text(text, "Visual System")
    sample = " ".join(visual.split())
    words = len(sample.split()) if sample else 0
    lines = [
        f"- H1/H2/eyebrow/CTA samples: H1 {line_value(text, 'H1 observed')}; H2 {line_value(text, 'H2 samples')}; navigation {line_value(text, 'Navigation samples')}",
        f"- Sentence rhythm: {words} words in the captured Visual System summary; source: Visual System",
        f"- Claim density: existing numeric claims remain in Evidence Snapshot and Visual System; source: L3 text",
        f"- Voice and naming: page title {line_value(text, 'Page title')}; source: Evidence Snapshot",
        "- Copy boundaries: reuse grammar and role hierarchy only; exact copy, claims, product names, and brand voice are not reusable.",
    ]
    return block("Reference Text And Copy Grammar", lines)


def style_tokens_block(text: str) -> str:
    lines = [
        f"- Surface/background system: {line_value(text, 'Observed backgrounds')}; source: Color, Material, And Contrast",
        f"- Borders/dividers/radii: {line_value(text, 'Observed border radii')}; source: Layout Geometry And Spacing",
        f"- Shadow/depth/material: {line_value(text, 'Shadow/depth')}; source: Visual System",
        f"- Button/input/control density: buttons {line_value(text, 'Buttons/links')}; forms {line_value(text, 'Forms/inputs')}; source: Interaction And Components",
        f"- Icon/illustration stroke style: {line_value(text, 'Illustration/icon style')}; source: Assets",
    ]
    return block("Style Tokens And Surface Grammar", lines)


def motion_parameter_summary(motion: dict[str, object]) -> str:
    items = motion.get("items") if isinstance(motion.get("items"), list) else []
    values: list[str] = []
    for item in items[:8]:
        if not isinstance(item, dict):
            continue
        duration = item.get("duration_ms", "missing")
        duration_text = f"{duration}ms" if isinstance(duration, int) else str(duration)
        values.append(
            f"{item.get('selector_role', 'missing')} {item.get('trigger', 'missing')} {item.get('property', 'missing')} {duration_text} {item.get('easing', 'missing')}"
        )
    return "; ".join(values) if values else "missing"


def source_url_summary(motion: dict[str, object]) -> str:
    for key in ["source_urls", "checked_urls"]:
        value = motion.get(key)
        if isinstance(value, list) and value:
            return "; ".join(str(item) for item in value[:10])
    return "missing"


def backfill_text(text: str, card: dict[str, object], motion: dict[str, object]) -> tuple[str, list[str]]:
    changed: list[str] = []
    if not has_section(text, "Style DNA"):
        text = insert_after_section(text, "When Not To Use", style_dna_block(card))
        changed.append("Style DNA")
    if not has_section(text, "Reference Text And Copy Grammar"):
        text = insert_after_section(text, "Typography And Reading Rhythm", reference_text_block(text))
        changed.append("Reference Text And Copy Grammar")
    if not has_section(text, "Style Tokens And Surface Grammar"):
        text = insert_after_section(text, "Layout Geometry And Spacing", style_tokens_block(text))
        changed.append("Style Tokens And Surface Grammar")
    if "- Public stylesheet/script URLs:" not in text:
        text = append_line_to_section(text, "Code Surface", f"- Public stylesheet/script URLs: {source_url_summary(motion)}")
        changed.append("Public stylesheet/script URLs")
    if "- Exact motion parameters:" not in text:
        text = append_line_to_section(text, "Motion Code And Runtime Evidence", f"- Exact motion parameters: {motion_parameter_summary(motion)}")
        changed.append("Exact motion parameters")
    return text.rstrip() + "\n", changed


def backfill_reference(reference: Path, lib: Path, dry_run: bool = False) -> dict[str, object]:
    text = reference.read_text(encoding="utf-8", errors="ignore")
    card = card_for_reference(reference, lib)
    motion = motion_payload(card, lib)
    updated, changed = backfill_text(text, card, motion)
    if changed and not dry_run:
        reference.write_text(updated, encoding="utf-8")
    return {
        "reference": str(reference),
        "status": "ok" if changed else "unchanged",
        "changed": changed,
    }


def references(lib: Path, values: list[str], limit: int | None) -> list[Path]:
    if values:
        refs: list[Path] = []
        for value in values:
            path = Path(value)
            if path.exists():
                refs.append(path)
                continue
            refs.extend(sorted((lib / "references").glob(f"*-{value}.md")))
        return refs[:limit] if limit is not None else refs
    refs = sorted((lib / "references").glob("*.md"))
    return refs[:limit] if limit is not None else refs


def main() -> int:
    parser = argparse.ArgumentParser(description="Backfill L3 reference sections required for reusable DesignStyle evidence.")
    parser.add_argument("--library", default=str(LIB))
    parser.add_argument("--reference", action="append", default=[])
    parser.add_argument("--limit", type=int)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    lib = Path(args.library).expanduser()
    refs = references(lib, args.reference, args.limit)
    results = [backfill_reference(ref, lib, args.dry_run) for ref in refs]
    changed = [row for row in results if row["changed"]]
    payload = {
        "mode": "dry-run" if args.dry_run else "write",
        "library": str(lib),
        "planned": len(refs),
        "changed": len(changed),
        "results": results,
    }
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"mode={payload['mode']} planned={len(refs)} changed={len(changed)}")
        for row in changed[:20]:
            print(f"- {Path(str(row['reference'])).name}: {', '.join(row['changed'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
