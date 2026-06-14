#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
import os


LIB = Path(os.environ.get("DESIGNSTYLE_LIBRARY", str(Path.home() / ".codex" / "designstyle-library")))

REQUIRED_FRONTMATTER = [
    "title",
    "source_url",
    "captured_at",
    "tags",
    "category_tags",
    "style_tags",
    "structure_tags",
    "motion_tags",
    "code_tags",
    "best_for",
    "avoid_for",
    "community_signal",
    "page_scope",
    "evidence_screenshot",
    "evidence_quality",
]

REQUIRED_SECTIONS = [
    "Essence",
    "When To Use",
    "When Not To Use",
    "Style DNA",
    "Evidence Snapshot",
    "Visual System",
    "Typography And Reading Rhythm",
    "Reference Text And Copy Grammar",
    "Color, Material, And Contrast",
    "Layout Geometry And Spacing",
    "Style Tokens And Surface Grammar",
    "Dimension And Ratio System",
    "Assets",
    "Code Surface",
    "Motion",
    "Motion Code And Runtime Evidence",
    "Interaction And Components",
    "Implementation Notes",
    "Borrow",
    "Avoid Copying",
    "Evidence Limits",
    "Self Review",
]

QUALITY_MARKERS = [
    "- Screenshot:",
    "- Viewport:",
    "- Community signal:",
    "- Page scope:",
    "- Secondary pages inspected:",
    "- Exact motion parameters:",
    "- Framework/runtime hints:",
    "- Public stylesheet/script URLs:",
    "- CSS variables/tokens observed:",
    "- Preserve ratios as implementation constraints:",
    "- Component computed-style evidence:",
    "- Evidence quality:",
    "- Reuse value:",
]
MANDATORY_DIMENSION_SECTIONS = [
    "Reference Text And Copy Grammar",
    "Style Tokens And Surface Grammar",
    "Layout Geometry And Spacing",
]
MISSING_MARKERS = {"missing", "missing evidence", "not observed", "no direct", "unavailable"}
MEASURABLE_DNA = re.compile(r"\d")


def field(text: str, name: str) -> str:
    match = re.search(rf"^{re.escape(name)}:\s*(.*?)\s*$", text, re.M)
    return match.group(1).strip() if match else ""


def has_section(text: str, name: str) -> bool:
    return bool(re.search(rf"^## {re.escape(name)}\s*$", text, re.M))


def section_text(text: str, name: str) -> str:
    match = re.search(rf"^## {re.escape(name)}\s*$([\s\S]*?)(?=^## |\Z)", text, re.M)
    return match.group(1).strip() if match else ""


def is_todo_heavy(text: str) -> bool:
    todo_count = len(re.findall(r"\bTODO\b", text, re.I))
    return todo_count > 4


def has_evidence_or_missing_marker(content: str) -> bool:
    cleaned_lines = []
    for line in content.splitlines():
        cleaned = line.strip().lstrip("- ").strip()
        if not cleaned or cleaned.endswith(":"):
            continue
        cleaned_lines.append(cleaned)
    if not cleaned_lines:
        return False
    blob = "\n".join(cleaned_lines).lower()
    if any(marker in blob for marker in MISSING_MARKERS):
        return True
    return any(not re.search(r"\btodo\b", line, re.I) for line in cleaned_lines)


def validate_style_dna(content: str) -> list[str]:
    issues: list[str] = []
    lines = [line.strip().lstrip("- ").strip() for line in content.splitlines() if line.strip().startswith("-")]
    if not lines:
        return ["Style DNA lacks measurable decisions or explicit missing marker"]
    if len(lines) > 12:
        issues.append("Style DNA has more than 12 decisions")
    for index, line in enumerate(lines, 1):
        lowered = line.lower()
        if any(marker in lowered for marker in MISSING_MARKERS):
            continue
        if not MEASURABLE_DNA.search(line):
            issues.append(f"Style DNA decision is not measurable: item {index}")
        if "source:" not in lowered and "evidence" not in lowered:
            issues.append(f"Style DNA decision lacks evidence source: item {index}")
    return issues


def validate(path: Path, lib: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    issues: list[str] = []

    for name in REQUIRED_FRONTMATTER:
        value = field(text, name)
        if not value or value in {"[]", '""'}:
            issues.append(f"missing frontmatter: {name}")

    for name in REQUIRED_SECTIONS:
        if not has_section(text, name):
            issues.append(f"missing section: {name}")

    for marker in QUALITY_MARKERS:
        if marker not in text:
            issues.append(f"missing marker: {marker}")

    for name in MANDATORY_DIMENSION_SECTIONS:
        content = section_text(text, name)
        if not has_evidence_or_missing_marker(content):
            issues.append(f"mandatory dimension lacks evidence or explicit missing marker: {name}")

    issues.extend(validate_style_dna(section_text(text, "Style DNA")))

    screenshot = field(text, "evidence_screenshot").strip('"')
    if screenshot:
        screenshot_path = lib / screenshot
        if not screenshot_path.exists():
            issues.append(f"screenshot not found: {screenshot}")
    elif "user-provided visual evidence" not in text.lower():
        issues.append("screenshot missing without explicit user-provided visual evidence")

    component_evidence = f"{section_text(text, 'Code Surface')}\n{section_text(text, 'Interaction And Components')}".lower()
    if "component-styles.json" not in component_evidence and "component evidence missing" not in text.lower():
        issues.append("component JSON missing without explicit component evidence missing marker")

    if "no direct code evidence" not in text.lower():
        motion_evidence = section_text(text, "Motion Code And Runtime Evidence")
        code_surface = section_text(text, "Code Surface")
        combined = f"{motion_evidence}\n{code_surface}".lower()
        if not any(token in combined for token in ["transition", "animation", "keyframes", "transform", "gsap", "framer", "swiper", "intersectionobserver", "requestanimationframe", "css variables", "public stylesheet"]):
            issues.append("weak code/motion evidence without explicit limit")

    if is_todo_heavy(text):
        issues.append("too many TODO placeholders")

    return {
        "path": str(path),
        "title": field(text, "title").strip('"') or path.stem,
        "valid": not issues,
        "issues": issues,
        "category_tags": field(text, "category_tags"),
        "page_scope": field(text, "page_scope").strip('"'),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate designstyle reference quality gates.")
    parser.add_argument("--library", default=str(LIB))
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    lib = Path(args.library).expanduser()
    refs = sorted((lib / "references").glob("*.md"))
    results = [validate(path, lib) for path in refs]
    valid = [row for row in results if row["valid"]]

    if args.json:
        print(json.dumps({"total": len(results), "valid": len(valid), "invalid": len(results) - len(valid), "results": results}, ensure_ascii=False, indent=2))
        return 0 if len(valid) == len(results) else 1

    print(f"references={len(results)} valid={len(valid)} invalid={len(results) - len(valid)}")
    for row in results:
        status = "OK" if row["valid"] else "FAIL"
        print(f"{status}\t{row['title']}\t{Path(row['path']).name}")
        for issue in row["issues"][:8]:
            print(f"  - {issue}")
    return 0 if len(valid) == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
