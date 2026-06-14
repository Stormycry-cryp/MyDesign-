#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


REQUIRED_SECTIONS = [
    "Reference-Led Execution Contract",
    "Original-Site Inspection Log",
    "Style Fidelity Contract",
    "Implementation Mapping",
    "Page Logic And Information Hierarchy Mapping",
    "Typography And Font Mapping",
    "Final QA Checklist",
]

REQUIRED_DIMENSION_WORDS = [
    "layout",
    "motion",
    "typography",
    "page logic",
    "hierarchy",
    "fonts",
    "surfaces",
    "components",
    "states",
]

IMPLEMENTATION_CONSTRAINTS = [
    "grid-template-columns",
    "aspect-ratio",
    "max-width",
    "font-size",
    "font-weight",
    "line-height",
    "letter-spacing",
    "transition",
    "gap",
]

QA_STATES = [
    "Immediate first viewport",
    "Post-animation first viewport",
    "Desktop key sections",
    "Mobile key sections",
    "Hover/focus states",
    "Reduced motion",
    "Screenshot structural QA",
]


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def has_screenshot_path(text: str) -> bool:
    return bool(re.search(r"\b[\w./-]+\.(?:png|jpg|jpeg|webp)\b", text, re.I))


def validate(text: str) -> list[str]:
    lower = normalized(text)
    missing: list[str] = []

    for section in REQUIRED_SECTIONS:
        if section.lower() not in lower:
            missing.append(f"Missing section: {section}")

    for word in REQUIRED_DIMENSION_WORDS:
        if word not in lower:
            missing.append(f"Reference-led contract missing dimension: {word}")

    if not any(marker in lower for marker in ["source url", "live original site", "retained screenshot", "component json"]):
        missing.append("Original-Site Inspection Log lacks live/source/screenshot/component evidence.")

    if not any(term in lower for term in ["side-by-side", "reference workbench", "旁边对照"]):
        missing.append("Plan does not require a side-by-side reference workbench.")

    if not any(constraint in lower for constraint in IMPLEMENTATION_CONSTRAINTS):
        missing.append("Implementation Mapping lacks concrete CSS/layout/motion constraints.")

    if not any(term in lower for term in ["generic centered hero", "forbidden drift", "default pattern"]):
        missing.append("Style Fidelity Contract lacks forbidden drift/default-pattern guardrail.")

    for state in QA_STATES:
        if state.lower() not in lower:
            missing.append(f"Final QA Checklist missing state: {state}")

    if not has_screenshot_path(text):
        missing.append("Final QA lacks real screenshot paths.")

    if not re.search(r"\b3\b.*visible similarit", lower) and "3 visible similarities" not in lower:
        missing.append("Final QA must require at least 3 visible similarities.")

    if not re.search(r"\b2\b.*intentional difference", lower) and "2 intentional differences" not in lower:
        missing.append("Final QA must require at least 2 intentional differences.")

    return missing


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a use-designstyle direction plan for reference fidelity gates.")
    parser.add_argument("plan", help="Path to work/designstyle-direction-plan.md")
    args = parser.parse_args()

    path = Path(args.plan).expanduser()
    if not path.exists():
        print(f"Missing plan: {path}")
        return 2

    missing = validate(path.read_text(encoding="utf-8", errors="ignore"))
    if missing:
        print("direction-plan-invalid")
        for item in missing:
            print(f"- {item}")
        return 1

    print("direction-plan-valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
