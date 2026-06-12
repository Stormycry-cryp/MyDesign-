#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import capture_reference as capture


LIB = Path.home() / ".codex" / "designstyle-library"


def frontmatter_value(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.*?)\s*$", text, re.M)
    if not match:
        return ""
    return match.group(1).strip().strip('"')


def slug_from_reference(path: Path, text: str) -> str:
    title = frontmatter_value(text, "title")
    if title:
        return capture.slugify(title)
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)


def replace_or_append_line(text: str, prefix: str, replacement: str) -> str:
    pattern = re.compile(rf"^{re.escape(prefix)}.*$", re.M)
    if pattern.search(text):
        return pattern.sub(replacement, text)
    return text.rstrip() + "\n" + replacement + "\n"


def update_reference_evidence_paths(text: str, screenshot_rel: str, component_rel: str, motion_rel: str) -> str:
    text = replace_or_append_line(text, "evidence_screenshot:", f'evidence_screenshot: "{screenshot_rel}"')
    text = replace_or_append_line(
        text,
        "- Screenshot:",
        f"- Screenshot: {screenshot_rel}",
    )
    text = replace_or_append_line(
        text,
        "- Component computed-style evidence:",
        f"- Component computed-style evidence: `{component_rel}`",
    )
    text = replace_or_append_line(
        text,
        "- Computed component styles:",
        f"- Computed component styles: `{component_rel}`",
    )
    text = replace_or_append_line(
        text,
        "- Structured motion evidence:",
        f"- Structured motion evidence: `{motion_rel}`",
    )
    return text


def recapture_reference(reference: Path, lib: Path, width: int, height: int, timeout: int, dry_run: bool) -> dict[str, object]:
    text = reference.read_text(encoding="utf-8")
    url = frontmatter_value(text, "source_url")
    if not url:
        return {"reference": str(reference), "status": "partial", "reason": "missing source_url"}
    slug = slug_from_reference(reference, text)
    today = date.today().isoformat()
    screenshot_rel = f"screenshots/{slug}-desktop.png"
    component_rel = f"assets/{today}-{slug}-component-styles.json"
    motion_rel = f"assets/{today}-{slug}-motion.json"
    if dry_run:
        return {
            "reference": str(reference),
            "slug": slug,
            "url": url,
            "status": "planned",
            "screenshot": screenshot_rel,
            "component": component_rel,
            "motion": motion_rel,
        }

    screenshot = lib / screenshot_rel
    component_path = lib / component_rel
    motion_path = lib / motion_rel
    raw_dir = Path(tempfile.gettempdir()) / "designstyle-raw-evidence" / today
    raw_dir.mkdir(parents=True, exist_ok=True)
    dom_path = raw_dir / f"{today}-{slug}-recapture-dom.html"

    ok, browser_log, captured_data = capture.capture_with_playwright(
        url,
        screenshot,
        dom_path,
        width,
        height,
        timeout,
        inspect_secondary=False,
    )
    if not dom_path.exists():
        dom_path.write_text(
            f"<!doctype html><title>{slug}</title><body>capture failed: {browser_log}</body>",
            encoding="utf-8",
        )
    dom = dom_path.read_text(encoding="utf-8", errors="ignore")
    data = captured_data or capture.extract_json(dom) or capture.fallback_extract(dom, url)
    component_evidence = data.get("componentEvidence") if isinstance(data.get("componentEvidence"), dict) else {}
    component_evidence = capture.sanitize_computed_value(component_evidence)
    blocked_reasons = capture.blocked_evidence_reasons(data)
    component_payload = {
        "slug": slug,
        "name": frontmatter_value(text, "title") or slug,
        "source_url": url,
        "final_url": data.get("url") or url,
        "captured_at": today,
        "screenshot": screenshot_rel,
        "evidence_quality": "blocked/security challenge captured" if blocked_reasons else "recaptured computed component styles from live DOM" if component_evidence else "component style recapture unavailable",
        "blocked_reasons": blocked_reasons,
        "component_evidence": component_evidence,
    }
    component_path.parent.mkdir(parents=True, exist_ok=True)
    component_path.write_text(json.dumps(component_payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    final_url = data.get("url") or url
    resource_urls = (data.get("stylesheets") or []) + (data.get("scripts") or [])
    checked_urls, _motion, structured_motion = capture.collect_motion(resource_urls, final_url, slug)
    interaction_motion = capture.motion_items_from_interaction_states(component_evidence, slug, "playwright computed-style interaction diff")
    if interaction_motion:
        existing = {
            (
                item.get("selector"),
                item.get("trigger"),
                item.get("property"),
                item.get("duration_ms"),
                item.get("easing"),
                item.get("to"),
            )
            for item in structured_motion.get("items", [])
            if isinstance(item, dict)
        }
        for item in interaction_motion:
            key = (
                item.get("selector"),
                item.get("trigger"),
                item.get("property"),
                item.get("duration_ms"),
                item.get("easing"),
                item.get("to"),
            )
            if key not in existing:
                structured_motion.setdefault("items", []).append(item)
                existing.add(key)
    structured_motion["checked_urls"] = checked_urls
    structured_motion["missing"] = [] if structured_motion.get("items") else structured_motion.get("missing", [])
    motion_path.parent.mkdir(parents=True, exist_ok=True)
    motion_path.write_text(json.dumps(structured_motion, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    updated = update_reference_evidence_paths(text, screenshot_rel, component_rel, motion_rel)
    reference.write_text(updated, encoding="utf-8")
    samples = component_evidence.get("samples") if isinstance(component_evidence, dict) else []
    states = component_evidence.get("stateSamples") if isinstance(component_evidence, dict) else []
    return {
        "reference": str(reference),
        "slug": slug,
        "url": url,
        "status": "ok" if ok and not blocked_reasons else "partial",
        "reason": browser_log,
        "screenshot": screenshot_rel,
        "component": component_rel,
        "motion": motion_rel,
        "component_samples": len(samples) if isinstance(samples, list) else 0,
        "state_samples": len(states) if isinstance(states, list) else 0,
        "motion_items": len(structured_motion.get("items", [])) if isinstance(structured_motion.get("items"), list) else 0,
        "blocked_reasons": blocked_reasons,
    }


def resolve_references(lib: Path, values: list[str]) -> list[Path]:
    refs: list[Path] = []
    for value in values:
        path = Path(value)
        if path.exists():
            refs.append(path)
            continue
        matches = sorted((lib / "references").glob(f"*-{value}.md"))
        if matches:
            refs.append(matches[-1])
    return refs


def main() -> int:
    parser = argparse.ArgumentParser(description="Safely recapture component and motion assets for existing DesignStyle references.")
    parser.add_argument("--library", default=str(LIB))
    parser.add_argument("--reference", action="append", default=[], help="Reference path or slug. Can be repeated.")
    parser.add_argument("--slugs", default="", help="Comma-separated reference slugs.")
    parser.add_argument("--width", type=int, default=1440)
    parser.add_argument("--height", type=int, default=1000)
    parser.add_argument("--timeout", type=int, default=12)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--report", default=f"reviews/{date.today().isoformat()}-recapture-assets.json")
    args = parser.parse_args()

    lib = Path(args.library).expanduser()
    values = list(args.reference)
    values.extend(slug.strip() for slug in args.slugs.split(",") if slug.strip())
    refs = resolve_references(lib, values)
    if not refs:
        raise SystemExit("No references matched.")
    results = [recapture_reference(ref, lib, args.width, args.height, args.timeout, args.dry_run) for ref in refs]
    payload = {
        "mode": "dry-run" if args.dry_run else "write",
        "library": str(lib),
        "planned": len(refs),
        "ok": sum(1 for result in results if result.get("status") == "ok"),
        "partial": sum(1 for result in results if result.get("status") == "partial"),
        "results": results,
    }
    if not args.dry_run:
        report = lib / args.report
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(report)
    print(f"mode={payload['mode']} planned={payload['planned']} ok={payload['ok']} partial={payload['partial']}")
    for result in results:
        print(f"{result.get('status')}: {result.get('slug')} motion={result.get('motion_items', 0)} samples={result.get('component_samples', 0)} states={result.get('state_samples', 0)}")
    return 0 if payload["partial"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
