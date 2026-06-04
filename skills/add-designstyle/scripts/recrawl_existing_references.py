#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

from build_progressive_reference import parse_frontmatter


LIB = Path.home() / ".codex" / "designstyle-library"
CAPTURE = Path(__file__).with_name("capture_reference.py")


def csv(values: object) -> str:
    if isinstance(values, list):
        return ",".join(str(item) for item in values)
    return ""


def references(lib: Path) -> list[Path]:
    return sorted((lib / "references").glob("*.md"))


def command_for(reference: Path, lib: Path, timeout: int) -> list[str]:
    text = reference.read_text(encoding="utf-8", errors="ignore")
    meta = parse_frontmatter(text)
    missing = [key for key in ["title", "source_url", "community_signal", "page_scope"] if not str(meta.get(key) or "").strip()]
    if missing:
        raise ValueError(f"{reference.name} missing frontmatter fields: {', '.join(missing)}")
    return [
        sys.executable,
        str(CAPTURE),
        "--name",
        str(meta["title"]),
        "--url",
        str(meta["source_url"]),
        "--category-tags",
        csv(meta.get("category_tags")),
        "--style-tags",
        csv(meta.get("style_tags")),
        "--structure-tags",
        csv(meta.get("structure_tags")),
        "--motion-tags",
        csv(meta.get("motion_tags")),
        "--code-tags",
        csv(meta.get("code_tags")),
        "--best-for",
        csv(meta.get("best_for")),
        "--avoid-for",
        csv(meta.get("avoid_for")),
        "--community-signal",
        str(meta["community_signal"]),
        "--page-scope",
        str(meta["page_scope"]),
        "--library",
        str(lib),
        "--timeout",
        str(timeout),
        "--replace",
        "--output-reference",
        str(reference.resolve()),
        "--skip-secondary",
    ]


def write_report(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    ok = sum(1 for row in rows if row.get("status") == "ok")
    failed = sum(1 for row in rows if row.get("status") != "ok")
    lines = [
        "# DesignStyle Recrawl Report",
        "",
        f"Date: {date.today().isoformat()}",
        "",
        f"- Total: {len(rows)}",
        f"- OK: {ok}",
        f"- Failed: {failed}",
        "",
        "| # | Reference | Status | Component JSON | Note |",
        "|---:|---|---|---|---|",
    ]
    for index, row in enumerate(rows, 1):
        lines.append(
            "| {index} | `{reference}` | {status} | `{component_json}` | {note} |".format(
                index=index,
                reference=row.get("reference", ""),
                status=row.get("status", ""),
                component_json=row.get("component_json", ""),
                note=str(row.get("note", "")).replace("|", "\\|")[:260],
            )
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def component_sample_count(lib: Path, rel: str) -> int:
    path = lib / rel
    if not path.exists():
        return 0
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return 0
    evidence = payload.get("component_evidence", {})
    samples = evidence.get("samples", []) if isinstance(evidence, dict) else []
    return len(samples) if isinstance(samples, list) else 0


def component_blocked_reasons(lib: Path, rel: str) -> list[str]:
    path = lib / rel
    if not path.exists():
        return []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    reasons = payload.get("blocked_reasons", [])
    return reasons if isinstance(reasons, list) else []


def main() -> int:
    parser = argparse.ArgumentParser(description="Recrawl all existing designstyle references in place.")
    parser.add_argument("--library", default=str(LIB))
    parser.add_argument("--limit", type=int)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--timeout", type=int, default=14)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--report", default=f"reviews/{date.today().isoformat()}-recrawl-component-evidence.md")
    args = parser.parse_args()

    lib = Path(args.library).expanduser()
    selected = references(lib)[args.offset :]
    if args.limit is not None:
        selected = selected[: args.limit]
    rows: list[dict[str, object]] = []
    for reference in selected:
        try:
            command = command_for(reference, lib, args.timeout)
        except ValueError as exc:
            rows.append({"reference": reference.name, "status": "failed", "component_json": "", "note": str(exc)})
            continue
        if args.dry_run:
            rows.append({"reference": reference.name, "status": "planned", "component_json": "", "note": " ".join(command)})
            continue
        result = subprocess.run(command, text=True, capture_output=True)
        output_lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
        slug = reference.stem
        if slug[:10].count("-") == 2:
            slug = slug[11:]
        component_json = f"assets/{date.today().isoformat()}-{slug}-component-styles.json"
        sample_count = component_sample_count(lib, component_json)
        blocked_reasons = component_blocked_reasons(lib, component_json)
        status = "ok" if result.returncode == 0 and sample_count > 0 and not blocked_reasons else "failed"
        note = "; ".join(output_lines[-2:]) if output_lines else result.stderr.strip()
        if result.returncode == 0 and sample_count <= 0:
            note = f"component evidence empty; {note}"
        if blocked_reasons:
            note = f"blocked/security challenge captured: {', '.join(str(reason) for reason in blocked_reasons[:3])}; {note}"
        if sample_count > 0:
            note = f"component samples={sample_count}; {note}"
        rows.append({"reference": reference.name, "status": status, "component_json": component_json, "note": note})
        print(f"{status}: {reference.name}")
    write_report(lib / args.report, rows)
    print(lib / args.report)
    return 0 if all(row.get("status") in {"ok", "planned"} for row in rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
