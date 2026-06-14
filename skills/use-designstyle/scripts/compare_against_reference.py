#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
import os


LIB = Path(os.environ.get("DESIGNSTYLE_LIBRARY", str(Path.home() / ".codex" / "designstyle-library")))


def read_json(path: Path) -> dict[str, object]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def screenshot_path(card: dict[str, object], lib: Path) -> str:
    reference_path = card.get("reference_path")
    if not isinstance(reference_path, str):
        return "missing"
    ref = lib / reference_path
    if not ref.exists():
        return "missing"
    text = ref.read_text(encoding="utf-8", errors="ignore")
    for line in text.splitlines():
        if line.startswith("evidence_screenshot:"):
            value = line.split(":", 1)[1].strip().strip('"')
            return str((lib / value).resolve()) if value else "missing"
    return "missing"


def list_value(value: object) -> str:
    if isinstance(value, list):
        return ", ".join(str(item) for item in value) or "missing"
    if isinstance(value, dict):
        return ", ".join(value.keys()) or "missing"
    return str(value or "missing")


def dna_rows(card: dict[str, object]) -> str:
    dna = card.get("dna")
    if not isinstance(dna, list) or not dna:
        return "| missing | missing | pending manual check | missing |"
    rows: list[str] = []
    for item in dna:
        if not isinstance(item, dict):
            continue
        decision = str(item.get("decision") or "missing").replace("|", "/")
        source = str(item.get("evidence_source") or "missing").replace("|", "/")
        rows.append(f"| {decision} | {source} | pending manual check against generated screenshot | pending |")
    return "\n".join(rows) or "| missing | missing | pending manual check | missing |"


def dimensions(card: dict[str, object]) -> tuple[list[str], list[str]]:
    strength = card.get("evidence_strength") if isinstance(card.get("evidence_strength"), dict) else {}
    borrow = []
    not_borrow = []
    for key, value in strength.items():
        if value in {"strong", "medium"}:
            borrow.append(str(key))
        else:
            not_borrow.append(str(key))
    paths = card.get("design_system_paths") if isinstance(card.get("design_system_paths"), dict) else {}
    for key in ["variables_css", "tailwind_theme", "motion_presets", "motion"]:
        if paths.get(key):
            borrow.append(key)
        else:
            not_borrow.append(key)
    return sorted(set(borrow)), sorted(set(not_borrow))


def report(card: dict[str, object], lib: Path, generated: Path, state: str) -> str:
    reference_shot = screenshot_path(card, lib)
    borrow, not_borrow = dimensions(card)
    now = datetime.now().isoformat(timespec="seconds")
    return f"""# Reference Comparison

Generated at: {now}

## Reference
- Title: {card.get("title", "missing")}
- Slug: {card.get("slug", "missing")}
- Card: {card.get("_card_path", "provided card path")}
- Reference path: {card.get("reference_path", "missing")}
- State compared: {state}

## Screenshot Evidence
- Reference screenshot: {reference_shot}
- Generated screenshot: {generated.resolve()}
- screenshot path required: satisfied for generated state `{state}`

## Apply Pack
- variables.css: {card.get("design_system_paths", {}).get("variables_css", "missing") if isinstance(card.get("design_system_paths"), dict) else "missing"}
- motion-presets.css: {card.get("design_system_paths", {}).get("motion_presets", "missing") if isinstance(card.get("design_system_paths"), dict) else "missing"}
- tailwind.theme.json: {card.get("design_system_paths", {}).get("tailwind_theme", "missing") if isinstance(card.get("design_system_paths"), dict) else "missing"}
- tokens.json: {card.get("design_system_paths", {}).get("tokens", "missing") if isinstance(card.get("design_system_paths"), dict) else "missing"}
- motion.json: {card.get("design_system_paths", {}).get("motion", "missing") if isinstance(card.get("design_system_paths"), dict) else "missing"}

## Borrowed Dimensions
- Borrowable: {list_value(borrow)}
- Not borrowed / weak: {list_value(not_borrow)}

## DNA Checklist
| DNA Decision | Evidence Source | Generated Check | Status |
|---|---|---|---|
{dna_rows(card)}

## Aesthetic Probe
- probe_aesthetic_fit.py score: pending
- Threshold: 75

## Iteration Log
| Time | Trigger | Plan Change | Implementation Change | Verification |
|---|---|---|---|---|
| {now} | initial comparison | none yet | none yet | pending DNA and probe checks |
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a DesignStyle generated-vs-reference comparison report.")
    parser.add_argument("--library", default=str(LIB))
    parser.add_argument("--card", required=True)
    parser.add_argument("--generated", required=True)
    parser.add_argument("--state", default="first-viewport")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    lib = Path(args.library).expanduser()
    card_path = Path(args.card).expanduser()
    generated = Path(args.generated).expanduser()
    output = Path(args.output).expanduser()
    card = read_json(card_path)
    if not card:
        raise SystemExit(f"Card JSON missing or invalid: {card_path}")
    if not generated.exists():
        raise SystemExit(f"Generated screenshot missing: {generated}")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report(card, lib, generated, args.state), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
