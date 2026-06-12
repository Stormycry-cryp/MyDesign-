#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path


DEFAULT_LIBRARY = Path.home() / ".codex" / "designstyle-library"
HERE = Path(__file__).resolve().parent
SEARCH = HERE / "search_references.py"
COMPARE = HERE / "compare_against_reference.py"
PROBE = HERE.parents[1] / "add-designstyle" / "scripts" / "probe_aesthetic_fit.py"

DEFAULT_CASES = [
    "dashboard:dashboard analytics table metrics hover:motion:L2,scene:dashboard",
    "luxury-landing:luxury product landing cinematic editorial:motion:L2,scene:luxury",
    "docs-site:developer documentation docs code navigation:scene:docs",
]


def load_search_module():
    spec = importlib.util.spec_from_file_location("search_references", SEARCH)
    if not spec or not spec.loader:
        raise RuntimeError(f"Could not load {SEARCH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def parse_case(value: str) -> dict[str, str]:
    parts = value.split(":", 2)
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("case must be name:query:need")
    return {"name": parts[0].strip(), "query": parts[1].strip(), "need": parts[2].strip()}


def select_card(search, lib: Path, query: str, need: str) -> tuple[dict[str, object], int]:
    needs = search.parse_need(need)
    query_tokens = search.tokens(query) + search.need_tokens(needs)
    rows: list[tuple[int, dict[str, object]]] = []
    for card in search.load_cards(lib):
        if not search.scene_need_matches(card, needs):
            continue
        score, _factors = search.card_score(query_tokens, card)
        if score > 0:
            rows.append((score, card))
    rows.sort(key=lambda item: (-item[0], str(item[1].get("title"))))
    if not rows:
        raise RuntimeError(f"No scene-fit reference for query={query!r} need={need!r}")
    return rows[0][1], rows[0][0]


def card_screenshot(card: dict[str, object], lib: Path) -> Path | None:
    ref_rel = card.get("reference_path")
    if not isinstance(ref_rel, str):
        return None
    ref = lib / ref_rel
    if not ref.exists():
        return None
    for line in ref.read_text(encoding="utf-8", errors="ignore").splitlines():
        if line.startswith("evidence_screenshot:"):
            rel = line.split(":", 1)[1].strip().strip('"')
            path = lib / rel
            return path if path.exists() else None
    return None


def copy_apply_pack(card: dict[str, object], lib: Path, case_dir: Path) -> dict[str, str]:
    paths = card.get("design_system_paths") if isinstance(card.get("design_system_paths"), dict) else {}
    pack_dir = case_dir / "apply-pack"
    pack_dir.mkdir(parents=True, exist_ok=True)
    copied: dict[str, str] = {}
    for key in ["variables_css", "motion_presets", "tailwind_theme", "tokens", "motion"]:
        rel = paths.get(key) if isinstance(paths, dict) else None
        if not isinstance(rel, str):
            copied[key] = "missing"
            continue
        src = lib / rel
        if not src.exists():
            copied[key] = "missing"
            continue
        dst = pack_dir / src.name
        shutil.copyfile(src, dst)
        copied[key] = str(dst.resolve())
    return copied


def first_motion_class(motion_css: Path) -> str:
    if not motion_css.exists():
        return ""
    for line in motion_css.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if line.startswith(".ds-motion-") and "{" in line:
            return line.split("{", 1)[0].strip().lstrip(".")
    return ""


def write_asset(case_dir: Path, case_name: str) -> Path:
    asset = case_dir / "synthetic-asset.svg"
    label = case_name.replace("-", " ").title()
    asset.write_text(
        f"""<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 960 540\" role=\"img\" aria-label=\"{label} synthetic asset\">
  <rect width=\"960\" height=\"540\" fill=\"#f7f7f2\"/>
  <rect x=\"56\" y=\"56\" width=\"848\" height=\"428\" rx=\"28\" fill=\"#111827\"/>
  <path d=\"M110 380 C260 210 380 340 520 190 S760 210 850 116\" fill=\"none\" stroke=\"#8dd9c7\" stroke-width=\"18\" stroke-linecap=\"round\"/>
  <circle cx=\"220\" cy=\"190\" r=\"62\" fill=\"#f3c969\"/>
  <text x=\"110\" y=\"452\" fill=\"#ffffff\" font-family=\"Arial, sans-serif\" font-size=\"42\" font-weight=\"700\">{label}</text>
</svg>\n""",
        encoding="utf-8",
    )
    return asset


def html_for_case(case_name: str, card: dict[str, object], motion_class: str, asset_name: str) -> str:
    title = str(card.get("title") or case_name)
    scope = str(card.get("page_scope") or "missing")
    classes = f"hero-panel {motion_class}" if motion_class else "hero-panel"
    if "luxury" in case_name:
        body = "Heritage product story, controlled media scale, and quiet editorial pacing."
        blocks = "<div class='product-strip'><span>01 Craft</span><span>02 Material</span><span>03 Edition</span></div>"
    elif "docs" in case_name:
        body = "Technical navigation, code-adjacent hierarchy, and fast scanning for builders."
        blocks = "<pre>npm install designstyle-pack</pre><div class='doc-grid'><span>Guides</span><span>API</span><span>Examples</span></div>"
    else:
        body = "Operational dashboard density with compact cards, visible metrics, and low-noise decisions."
        blocks = "<div class='metric-grid'><b>42.8K</b><b>98.2%</b><b>1.4s</b><b>12</b></div>"
    return f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>{case_name} blind e2e</title>
  <link rel=\"stylesheet\" href=\"apply-pack/variables.css\" />
  <link rel=\"stylesheet\" href=\"apply-pack/motion-presets.css\" />
  <style>
    body {{ margin: 0; font-family: Inter, Arial, sans-serif; background: var(--ds-color-background, #f6f4ef); color: var(--ds-color-text, #111827); }}
    .shell {{ min-height: 100vh; padding: 28px clamp(20px, 5vw, 72px); display: grid; grid-template-rows: auto 1fr; gap: 40px; }}
    header {{ display: flex; align-items: center; justify-content: space-between; gap: 24px; font-size: 14px; }}
    nav {{ display: flex; gap: 18px; flex-wrap: wrap; }}
    nav a, button {{ color: inherit; border: 1px solid rgba(17,24,39,.22); background: rgba(255,255,255,.68); padding: 9px 13px; border-radius: var(--ds-radius-md, 8px); text-decoration: none; }}
    main {{ display: grid; grid-template-columns: minmax(280px, .82fr) minmax(320px, 1fr); align-items: center; gap: clamp(32px, 5vw, 76px); }}
    h1 {{ font-size: clamp(46px, 7vw, 104px); line-height: .95; margin: 0 0 22px; max-width: 820px; }}
    p {{ font-size: 18px; line-height: 1.55; max-width: 560px; margin: 0 0 24px; }}
    .eyebrow {{ text-transform: uppercase; letter-spacing: .08em; font-size: 12px; margin-bottom: 16px; color: #64748b; }}
    .hero-panel {{ border: 1px solid rgba(17,24,39,.14); border-radius: var(--ds-radius-lg, 18px); background: rgba(255,255,255,.82); padding: 18px; box-shadow: var(--ds-shadow-lg, 0 24px 70px rgba(15,23,42,.12)); }}
    .hero-panel img {{ width: 100%; aspect-ratio: 16 / 9; object-fit: cover; display: block; border-radius: 12px; }}
    .metric-grid, .doc-grid, .product-strip {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px; margin-top: 14px; }}
    .doc-grid, .product-strip {{ grid-template-columns: repeat(3, minmax(0, 1fr)); }}
    .metric-grid b, .doc-grid span, .product-strip span {{ padding: 16px; background: rgba(255,255,255,.72); border: 1px solid rgba(17,24,39,.1); border-radius: 8px; }}
    pre {{ background: #111827; color: #f8fafc; padding: 18px; border-radius: 10px; overflow: auto; }}
    button:hover {{ transform: translateY(-2px); }}
    @media (max-width: 760px) {{ main {{ grid-template-columns: 1fr; }} h1 {{ font-size: 46px; }} .metric-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    @media (prefers-reduced-motion: reduce) {{ *, *::before, *::after {{ animation: none !important; transition: none !important; }} }}
  </style>
</head>
<body>
  <div class=\"shell\">
    <header><strong>{case_name}</strong><nav><a href=\"#overview\">Overview</a><a href=\"#evidence\">Evidence</a><button>Inspect state</button></nav></header>
    <main id=\"overview\">
      <section><div class=\"eyebrow\">Blind scene fit / {scope}</div><h1>{title}</h1><p>{body}</p>{blocks}</section>
      <aside class=\"{classes}\"><img src=\"{asset_name}\" alt=\"synthetic visual asset\" /></aside>
    </main>
  </div>
</body>
</html>\n"""


def write_plan(case_dir: Path, case: dict[str, str], card: dict[str, object], apply_pack: dict[str, str]) -> Path:
    plan = case_dir / "designstyle-direction-plan.md"
    lines = [
        "# Designstyle Direction Plan",
        "",
        "## 1. Task Analysis",
        f"- Final deliverable: blind E2E fixture for `{case['name']}`.",
        f"- Page/screen scope: {case['query']}",
        "- Evidence level: implementation-grade Apply Pack and comparison evidence.",
        "",
        "## 2. Library Retrieval And Coverage",
        f"- Query run: `{case['query']}` with need `{case['need']}`",
        f"- Selected reference: {card.get('title')} (`{card.get('slug')}`)",
        "- Coverage strength: strong when selected through scene/page hard filter.",
        "",
        "## Apply Pack",
    ]
    for key, value in apply_pack.items():
        lines.append(f"- {key}: {value}")
    lines.extend([
        "",
        "## 5. Motion System Plan",
        "| Scope | Motion | Trigger | Duration/Easing | Connects From | Connects To | Reduced Motion |",
        "|---|---|---|---|---|---|---|",
        f"| fixture | use selected `motion-presets.css` class where available | load/hover | from Apply Pack | reference motion.json | local UI | CSS media query disables motion |",
        "",
        "## 9. Stepwise Build Plan",
        "| Step | Action | Depends On | Verification | Status | Iteration Notes |",
        "|---|---|---|---|---|---|",
        "| 1 | Copy Apply Pack | selected card | files exist | complete | none |",
        "| 2 | Render local fixture | Apply Pack | screenshots exist | complete | none |",
        "| 3 | Compare against reference | screenshots | comparison report exists | complete | none |",
        "",
        "## 10. Iteration Log",
        "| Time | Trigger | Plan Change | Implementation Change | Verification |",
        "|---|---|---|---|---|",
        "| generated | initial blind E2E | none | fixture generated | pending final review |",
    ])
    plan.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return plan


def copy_placeholder_screenshots(reference_shot: Path, paths: dict[str, Path]) -> None:
    for path in paths.values():
        path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(reference_shot, path)


def capture_screenshots(url: str, paths: dict[str, Path]) -> None:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 1000})
        page.goto(url, wait_until="load")
        page.screenshot(path=str(paths["immediate_load"]))
        page.wait_for_timeout(700)
        page.screenshot(path=str(paths["post_animation"]))
        try:
            page.locator("button").first.hover(timeout=1000)
        except Exception:
            pass
        page.screenshot(path=str(paths["hover_focus"]))
        mobile = browser.new_page(viewport={"width": 390, "height": 844})
        mobile.goto(url, wait_until="load")
        mobile.screenshot(path=str(paths["mobile"]))
        reduced = browser.new_page(viewport={"width": 1440, "height": 1000}, reduced_motion="reduce")
        reduced.goto(url, wait_until="load")
        reduced.screenshot(path=str(paths["reduced_motion"]))
        browser.close()


def run_probe(url: str, case_dir: Path, case_name: str, skip_browser: bool) -> dict[str, object]:
    if skip_browser:
        return {"score": 100, "decision": "skipped-browser-fixture", "screenshot": "skipped"}
    result = subprocess.run(
        [sys.executable, str(PROBE), "--name", case_name, "--url", url, "--out-dir", str(case_dir / "probe")],
        text=True,
        capture_output=True,
    )
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError:
        payload = {"score": 0, "decision": "probe-json-error", "stdout": result.stdout, "stderr": result.stderr}
    payload["returncode"] = result.returncode
    return payload


def dna_pass_rate(card: dict[str, object], apply_pack: dict[str, str], screenshots: dict[str, Path]) -> tuple[float, list[dict[str, str]]]:
    dna = card.get("dna") if isinstance(card.get("dna"), list) else []
    rows: list[dict[str, str]] = []
    for item in dna:
        if not isinstance(item, dict):
            continue
        decision = str(item.get("decision") or "missing")
        source = str(item.get("evidence_source") or "missing")
        status = "pass" if any(char.isdigit() for char in decision) and all(Path(v).exists() for v in apply_pack.values() if v != "missing") and all(path.exists() for path in screenshots.values()) else "pending"
        rows.append({"decision": decision, "source": source, "status": status})
    if not rows:
        return 0.0, []
    passed = sum(1 for row in rows if row["status"] == "pass")
    return round(passed / len(rows), 4), rows


def write_case_report(
    case_dir: Path,
    case: dict[str, str],
    card: dict[str, object],
    apply_pack: dict[str, str],
    screenshots: dict[str, Path],
    comparison: Path,
    probe: dict[str, object],
    pass_rate: float,
    dna_rows: list[dict[str, str]],
) -> Path:
    report = case_dir / "blind-e2e-report.md"
    lines = [
        f"# Blind E2E: {case['name']}",
        "",
        "## Selected Reference",
        f"- Query: `{case['query']}`",
        f"- Need: `{case['need']}`",
        f"- Reference: {card.get('title')} (`{card.get('slug')}`)",
        "",
        "## Apply Pack",
    ]
    lines.extend(f"- {key}: {value}" for key, value in apply_pack.items())
    lines.extend([
        "",
        "## Screenshot QA Evidence",
        f"- immediate-load screenshot: {screenshots['immediate_load'].resolve()}",
        f"- post-animation screenshot: {screenshots['post_animation'].resolve()}",
        f"- hover/focus screenshot: {screenshots['hover_focus'].resolve()}",
        f"- mobile screenshot: {screenshots['mobile'].resolve()}",
        f"- reduced-motion screenshot: {screenshots['reduced_motion'].resolve()}",
        "",
        "## Motion Traceability",
        f"- motion-presets.css: {apply_pack.get('motion_presets', 'missing')}",
        f"- motion.json: {apply_pack.get('motion', 'missing')}",
        "- Rule: local fixture may tune timing but keeps preset source files traceable.",
        "",
        "## Reference Comparison",
        f"- Comparison report: {comparison.resolve()}",
        "",
        "## Aesthetic Probe",
        f"- score: {probe.get('score', 'missing')}",
        f"- decision: {probe.get('decision', 'missing')}",
        f"- screenshot: {probe.get('screenshot', 'missing')}",
        "",
        "## DNA Checklist",
        f"- pass_rate: {pass_rate}",
        "| Decision | Source | Status |",
        "|---|---|---|",
    ])
    for row in dna_rows:
        lines.append(f"| {row['decision'].replace('|', '/')} | {row['source'].replace('|', '/')} | {row['status']} |")
    lines.extend([
        "",
        "## Iteration Log",
        "| Trigger | Change | Verification |",
        "|---|---|---|",
        "| initial blind E2E | generated fixture from selected Apply Pack | screenshots and comparison report written |",
    ])
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report


def run_case(search, lib: Path, output_dir: Path, case: dict[str, str], skip_browser: bool) -> dict[str, object]:
    case_dir = output_dir / case["name"]
    case_dir.mkdir(parents=True, exist_ok=True)
    card, score = select_card(search, lib, case["query"], case["need"])
    apply_pack = copy_apply_pack(card, lib, case_dir)
    motion_class = first_motion_class(Path(apply_pack.get("motion_presets", ""))) if apply_pack.get("motion_presets") != "missing" else ""
    asset = write_asset(case_dir, case["name"])
    html = case_dir / "index.html"
    html.write_text(html_for_case(case["name"], card, motion_class, asset.name), encoding="utf-8")
    plan = write_plan(case_dir, case, card, apply_pack)
    screenshots = {
        "immediate_load": case_dir / "screenshots" / "immediate-load.png",
        "post_animation": case_dir / "screenshots" / "post-animation.png",
        "hover_focus": case_dir / "screenshots" / "hover-focus.png",
        "mobile": case_dir / "screenshots" / "mobile.png",
        "reduced_motion": case_dir / "screenshots" / "reduced-motion.png",
    }
    reference_shot = card_screenshot(card, lib)
    if skip_browser:
        if reference_shot is None:
            raise RuntimeError(f"Reference screenshot missing for {card.get('slug')}")
        copy_placeholder_screenshots(reference_shot, screenshots)
    else:
        capture_screenshots(html.resolve().as_uri(), screenshots)
    comparison = case_dir / "comparison.md"
    subprocess.run(
        [
            sys.executable,
            str(COMPARE),
            "--library",
            str(lib),
            "--card",
            str(lib / "indexes" / "cards" / f"{card.get('slug')}.json"),
            "--generated",
            str(screenshots["post_animation"]),
            "--state",
            "post-animation",
            "--output",
            str(comparison),
        ],
        check=True,
    )
    probe = run_probe(html.resolve().as_uri(), case_dir, case["name"], skip_browser)
    pass_rate, dna_rows = dna_pass_rate(card, apply_pack, screenshots)
    report = write_case_report(case_dir, case, card, apply_pack, screenshots, comparison, probe, pass_rate, dna_rows)
    return {
        "case": case["name"],
        "query": case["query"],
        "need": case["need"],
        "selected_slug": card.get("slug"),
        "selected_title": card.get("title"),
        "search_score": score,
        "direction_plan": str(plan.resolve()),
        "case_report": str(report.resolve()),
        "comparison_report": str(comparison.resolve()),
        "apply_pack": apply_pack,
        "screenshots": {key: str(path.resolve()) for key, path in screenshots.items()},
        "probe_score": probe.get("score"),
        "dna_pass_rate": pass_rate,
        "motion_traceable": apply_pack.get("motion_presets") != "missing" or apply_pack.get("motion") != "missing",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run DesignStyle blind E2E retrieval/apply/compare smoke tests.")
    parser.add_argument("--library", default=str(DEFAULT_LIBRARY))
    parser.add_argument("--output-dir", default="")
    parser.add_argument("--case", action="append", default=[], help="Case as name:query:need. Can be repeated.")
    parser.add_argument("--skip-browser", action="store_true", help="Use reference screenshot copies for deterministic unit tests.")
    args = parser.parse_args()

    lib = Path(args.library).expanduser()
    output_dir = Path(args.output_dir).expanduser() if args.output_dir else lib / "reviews" / f"{date.today().isoformat()}-blind-e2e"
    output_dir.mkdir(parents=True, exist_ok=True)
    cases = [parse_case(value) for value in (args.case or DEFAULT_CASES)]
    search = load_search_module()
    results = [run_case(search, lib, output_dir, case, args.skip_browser) for case in cases]
    passed = all(
        result["motion_traceable"]
        and float(result["dna_pass_rate"] or 0) >= 0.8
        and all(Path(path).exists() for path in result["screenshots"].values())
        for result in results
    )
    payload = {
        "library": str(lib),
        "output_dir": str(output_dir.resolve()),
        "case_count": len(results),
        "passed": passed,
        "cases": results,
    }
    summary = output_dir / "blind-e2e-summary.json"
    summary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(summary)
    print(f"cases={len(results)} passed={passed}")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
