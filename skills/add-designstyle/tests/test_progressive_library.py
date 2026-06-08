from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "scripts" / "build_progressive_reference.py"
VALIDATE = ROOT / "scripts" / "validate_progressive_library.py"
VALIDATE_REFERENCES = ROOT / "scripts" / "validate_references.py"
SKILL = ROOT / "SKILL.md"
DESIGNSTYLE_SKILL = ROOT.parent / "designstyle" / "SKILL.md"
USE_SKILL = ROOT.parent / "use-designstyle" / "SKILL.md"
SEARCH = ROOT.parent / "use-designstyle" / "scripts" / "search_references.py"
PROBE = ROOT / "scripts" / "probe_aesthetic_fit.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_reference(library: Path) -> Path:
    (library / "references").mkdir(parents=True)
    (library / "screenshots").mkdir(parents=True)
    (library / "screenshots" / "sample-hardware-desktop.png").write_bytes(
        bytes.fromhex(
            "89504e470d0a1a0a0000000d4948445200000004000000040802000000"
            "84e85ddc0000001549444154789c63606060f8ffff3f03031303c30300"
            "4f6507f91b5a4b7c0000000049454e44ae426082"
        )
    )
    (library / "assets").mkdir(parents=True)
    (library / "assets" / "2026-06-04-sample-hardware-component-styles.json").write_text(
        json.dumps(
            {
                "slug": "sample-hardware",
                "component_evidence": {
                    "samples": [
                        {
                            "sampleId": "button-0",
                            "category": "Button",
                            "tag": "a",
                            "text": "Buy now",
                            "rect": {"x": 1100, "y": 24, "width": 108, "height": 32},
                            "styles": {
                                "display": "inline-flex",
                                "backgroundColor": "rgb(17, 17, 17)",
                                "color": "rgb(255, 255, 255)",
                                "border": "1px solid rgb(17, 17, 17)",
                                "borderRadius": "9999px",
                                "fontSize": "13px",
                                "fontWeight": "600",
                                "padding": "0px 14px",
                                "transition": "transform 180ms ease",
                            },
                        },
                        {
                            "sampleId": "card-0",
                            "category": "Card",
                            "tag": "article",
                            "text": "Battery",
                            "rect": {"x": 80, "y": 520, "width": 280, "height": 180},
                            "styles": {
                                "backgroundColor": "rgb(255, 255, 255)",
                                "border": "1px solid rgb(229, 229, 229)",
                                "borderRadius": "3.35544e+07px",
                                "boxShadow": "rgba(0, 0, 0, 0.08) 0px 8px 24px",
                                "padding": "20px",
                            },
                        },
                    ],
                    "stateSamples": [
                        {
                            "sampleId": "button-0",
                            "category": "Button",
                            "text": "Buy now",
                            "hover_changed": {"transform": "matrix(1, 0, 0, 1, 0, -2)"},
                            "focus_changed": {"outlineColor": "rgb(17, 17, 17)"},
                        }
                    ],
                },
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    path = library / "references" / "2026-06-04-sample-hardware.md"
    path.write_text(
        """---
title: "Sample Hardware"
source_url: "https://example.com"
captured_at: "2026-06-04"
tags: ["hardware", "product"]
category_tags: ["hardware", "product"]
style_tags: ["minimal", "object-led"]
structure_tags: ["split hero", "product grid"]
motion_tags: ["hover lift"]
code_tags: ["css transitions"]
best_for: ["wearable product landing page"]
avoid_for: ["dashboard"]
community_signal: "selected for restrained hardware product hierarchy"
page_scope: "landing page"
evidence_screenshot: "screenshots/sample-hardware-desktop.png"
evidence_quality: "visual screenshot plus DOM/style/resource extraction"
---

# Style Reference: Sample Hardware

## Essence
Object-led hardware story with sparse copy and stable product media.

## When To Use
- Use for restrained product landing pages.

## When Not To Use
- Avoid for dashboards.

## Evidence Snapshot
- Captured URL: https://example.com
- Page title: Sample Hardware
- Screenshot: screenshots/sample-hardware-desktop.png
- Viewport: 1440x900
- Community signal: selected for restrained hardware product hierarchy
- Page scope: landing page
- Secondary pages inspected: product detail
- H1 observed: Wear the signal
- H2 samples: Designed for daily carry
- Navigation samples: Product, Specs, Buy
- Images observed: product renders
- Video observed: none
- Overlays or fixed elements: none

## Visual System
- Layout: split hero with product render
- Typography: large display headline, small metadata
- Color: white shell and charcoal text
- Density: sparse
- Shape: 8px cards
- Shadow/depth: soft product shadow

## Typography And Reading Rhythm
- Observed font stack counts: Inter-like sans
- Observed font sizes: 72px H1, 16px body
- Observed weights: 600 display, 400 body
- Observed letter spacing: 0
- Preserve role relationships: big headline, quiet specs

## Color, Material, And Contrast
- Observed text colors: #111111
- Observed backgrounds: #ffffff
- UI shell colors vs asset-driven colors: shell stays neutral

## Layout Geometry And Spacing
- First viewport structure: 72px header, 55/45 hero split
- Macro geometry: max-width 1180px
- Media/card aspect stability: 4:3 product render
- Header/hero/section spacing: 72px header, 96px hero padding
- Grid gutters and card padding: 24px gutters, 20px cards
- Mobile spacing behavior: stack hero, keep product first
- Observed border radii: 8px

## Dimension And Ratio System
- Viewport and document: 1440x900
- Observed media ratios: 4:3
- Observed spacing samples: 24px, 72px, 96px
- Preserve ratios as implementation constraints: keep product media stable

## Assets
- Image style: clean product render
- Illustration/icon style: thin line specs
- Texture/pattern: none
- Likely sources or production method: studio render

## Code Surface
- Framework/runtime hints: static HTML
- Public stylesheet/script URLs: /style.css
- CSS variables/tokens observed: --space-24
- Layout primitives observed: CSS grid
- Component or class naming clues: product-card
- Component computed-style evidence: `assets/2026-06-04-sample-hardware-component-styles.json`
- Asset CDN and media loading patterns: local images

## Motion
- Page transitions: none
- Micro-interactions: hover lift
- Scroll/entrance behavior: none
- Timing/easing: 180ms ease

## Motion Code And Runtime Evidence
- Motion source: CSS
- CSS animation/transition evidence: transition: transform 180ms ease
- Public CSS/JS probe keywords: transition transform
- Public CSS/JS motion snippets: transition: transform 180ms ease
- Exact motion parameters: 180ms ease, translateY(-2px)
- JavaScript/runtime motion evidence: none
- Stylesheet evidence: /style.css
- Interpreted motion tags: hover lift

## Interaction And Components
- Navigation: top nav
- Buttons/links: compact buy button
- Computed component styles: `assets/2026-06-04-sample-hardware-component-styles.json`
- Cards/sections: spec cards
- Forms/inputs: none
- Feedback states: hover focus visible

## Style Tokens And Surface Grammar
- Surface/background system: white shell, charcoal foreground, product render focal color
- Borders/dividers/radii: 1px neutral border, 8px card radius
- Shadow/depth/material: soft product shadow, no decorative blur
- Button/input/control density: compact buy button, 13px label, 32px height
- Icon/illustration stroke style: thin line spec icons

## Implementation Notes
- CSS/layout primitives: grid, max-width
- Token ideas: 24px gutter, 8px radius
- Libraries or techniques: CSS only
- Performance/accessibility concerns: reduced motion

## Borrow
- Stable media ratio and sparse product proof.

## Avoid Copying
- Exact product, claims, or renders.

## Evidence Limits
- No checkout page inspected.

## Self Review
- Evidence quality: strong visual and CSS clues
- Reuse value: good for hardware landing pages
- Missing pieces: mobile screenshot
- Revision made: tags tightened
""",
        encoding="utf-8",
    )
    return path


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, capture_output=True)


class ProgressiveLibraryTests(unittest.TestCase):
    def test_router_declares_shared_contract_and_handoff_rules(self) -> None:
        text = DESIGNSTYLE_SKILL.read_text(encoding="utf-8")

        for marker in [
            "## Shared Contract",
            "## Handoff Rules",
            "Required dimensions",
            "Reuse boundary",
            "Next handoff",
            "Add-Designstyle Backlog",
        ]:
            self.assertIn(marker, text)


    def test_add_skill_declares_use_readiness_gate(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        for marker in [
            "## Use-Readiness Gate",
            "A reference counts as active usable only when",
            "component_json_path",
            "Reference text grammar",
            "Style tokens",
            "Spacing rhythm",
            "## Use Readiness",
        ]:
            self.assertIn(marker, text)


    def test_use_skill_declares_coverage_strength_and_add_backlog(self) -> None:
        text = USE_SKILL.read_text(encoding="utf-8")

        for marker in [
            "## Coverage Strength",
            "strong: scene, page scope",
            "partial: enough for selected dimensions",
            "weak: only suitable as loose inspiration",
            "## Add-Designstyle Backlog",
            "Needed evidence level",
            "Candidate query direction",
        ]:
            self.assertIn(marker, text)


    def test_search_weights_page_scope_before_generic_style_or_motion(self) -> None:
        search = load_module(SEARCH, "search_references")
        weight_order = [field for field, _ in search.CARD_WEIGHTS]

        self.assertLess(weight_order.index("page_scope"), weight_order.index("category_tags"))
        self.assertLess(weight_order.index("page_scope"), weight_order.index("style_tags"))
        self.assertLess(weight_order.index("best_for"), weight_order.index("motion_tags"))

        query = search.tokens("skincare product detail formula hover transition")
        fit_card = {
            "title": "Clinical PDP",
            "page_scope": "product detail page",
            "category_tags": ["skincare", "commerce"],
            "best_for": ["clinical skincare product detail page"],
            "structure_tags": ["product grid"],
            "style_tags": ["clinical"],
            "motion_tags": [],
            "code_tags": [],
            "avoid_for": [],
        }
        wrong_motion_card = {
            "title": "Portfolio Motion",
            "page_scope": "portfolio",
            "category_tags": ["portfolio"],
            "best_for": ["portfolio gallery"],
            "structure_tags": [],
            "style_tags": [],
            "motion_tags": ["hover", "transition", "animation"],
            "code_tags": ["css", "js"],
            "avoid_for": ["product detail page", "skincare commerce"],
        }

        fit_score, fit_factors = search.card_score(query, fit_card)
        wrong_score, wrong_factors = search.card_score(query, wrong_motion_card)

        self.assertGreater(fit_score, wrong_score)
        self.assertGreaterEqual(fit_factors["scene_gate_percent"], 50)
        self.assertEqual(wrong_factors["gated_motion_code"], 0)


    def test_search_explain_output_names_selection_and_rejection_reasons(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            (library / "indexes" / "cards").mkdir(parents=True)
            (library / "references").mkdir(parents=True)
            (library / "references" / "clinical.md").write_text("# Clinical\n", encoding="utf-8")
            (library / "indexes" / "cards" / "clinical.json").write_text(
                json.dumps(
                    {
                        "slug": "clinical",
                        "title": "Clinical PDP",
                        "reference_path": "references/clinical.md",
                        "category_tags": ["skincare", "commerce"],
                        "style_tags": ["clinical"],
                        "structure_tags": ["product grid"],
                        "motion_tags": [],
                        "code_tags": [],
                        "page_scope": "product detail page",
                        "best_for": ["clinical skincare product detail page"],
                        "avoid_for": [],
                        "evidence_strength": {"screenshot": "strong"},
                        "dimension_paths": {},
                        "design_system_paths": {},
                        "selection_note": "same scene",
                        "evidence_limits": [],
                    }
                ),
                encoding="utf-8",
            )

            result = run([
                sys.executable,
                str(SEARCH),
                "skincare product detail formula hover transition",
                "--library",
                str(library),
                "--matrix",
                "--explain-selection",
            ])

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("selected_reason:", result.stdout)
            self.assertIn("rejected_reason:", result.stdout)
            self.assertIn("coverage_hint:", result.stdout)


    def test_skill_requires_aesthetic_gate_before_writing_reference(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        self.assertIn("Aesthetic Gate", text)
        self.assertIn("probe_aesthetic_fit.py", text)
        self.assertIn("minimum_score: 75", text)
        self.assertIn("Do not write the reference until the user confirms", text)


    def test_aesthetic_probe_blocks_failed_capture(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            result = run([
                sys.executable,
                str(PROBE),
                "--name",
                "Missing Local Site",
                "--url",
                "http://127.0.0.1:9/not-running",
                "--out-dir",
                td,
                "--timeout-ms",
                "1000",
            ])

            self.assertEqual(result.returncode, 2)
            payload = json.loads(result.stdout)
            self.assertFalse(payload["allowed_to_write"])
            self.assertEqual(payload["decision"], "warn_user_before_writing")
            self.assertIn("blocked", payload["flags"])


    def test_dry_run_does_not_write(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            write_reference(library)

            result = run([sys.executable, str(BUILD), "--all", "--library", str(library), "--dry-run"])

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("planned_cards=1", result.stdout)
            self.assertFalse((library / "indexes" / "cards").exists())
            self.assertFalse((library / "dimensions").exists())


    def test_single_reference_creates_card_and_seven_dimensions(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            reference = write_reference(library)

            result = run([sys.executable, str(BUILD), "--reference", str(reference), "--library", str(library)])

            self.assertEqual(result.returncode, 0, result.stderr)
            card = library / "indexes" / "cards" / "sample-hardware.json"
            self.assertTrue(card.exists())
            self.assertEqual(json.loads(card.read_text())["evidence_strength"]["layout_spacing"], "strong")
            payload = json.loads(card.read_text())
            self.assertIn("missing_evidence", payload)
            self.assertIn("component_json_path", payload)
            self.assertEqual(
                payload["component_json_path"],
                "assets/2026-06-04-sample-hardware-component-styles.json",
            )
            self.assertEqual(payload["evidence_strength"]["design_system"], "strong")
            self.assertEqual(payload["design_system_paths"]["tokens"], "design-systems/sample-hardware/tokens.json")
            dims = sorted((library / "dimensions" / "sample-hardware").glob("*.md"))
            self.assertEqual(len(dims), 7)
            system_dir = library / "design-systems" / "sample-hardware"
            self.assertTrue((system_dir / "tokens.json").exists())
            self.assertTrue((system_dir / "palette.md").exists())
            self.assertTrue((system_dir / "moodboard.svg").exists())
            self.assertTrue((system_dir / "component-styles.md").exists())
            tokens = json.loads((system_dir / "tokens.json").read_text())
            self.assertIn("palette", tokens)
            self.assertIn("component_styles", tokens)
            button_evidence = "\n".join(tokens["component_styles"]["Button"]["style_evidence"])
            card_evidence = "\n".join(tokens["component_styles"]["Card"]["style_evidence"])
            self.assertIn("9999px", button_evidence)
            self.assertNotIn("3.35544e+07px", card_evidence)
            self.assertIn("computed component style JSON", tokens["evidence"]["component_sources"])
            component_text = (system_dir / "component-styles.md").read_text(encoding="utf-8")
            self.assertIn("Buy now", component_text)
            self.assertIn("hover=", component_text)
            self.assertTrue(tokens["palette"]["colors"])
            self.assertIn("Button", tokens["component_styles"])
            component_text = (system_dir / "component-styles.md").read_text()
            self.assertIn("## Button", component_text)
            self.assertIn("### Style Evidence", component_text)
            self.assertIn("### Missing Evidence", component_text)
            self.assertTrue((library / "indexes" / "manifest.json").exists())
            self.assertTrue((library / "indexes" / "facets.json").exists())


    def test_reference_validator_requires_shared_mandatory_dimensions(self) -> None:
        validate_references = load_module(VALIDATE_REFERENCES, "validate_references")

        self.assertIn("Reference Text And Copy Grammar", validate_references.REQUIRED_SECTIONS)
        self.assertIn("Style Tokens And Surface Grammar", validate_references.REQUIRED_SECTIONS)
        self.assertIn("Layout Geometry And Spacing", validate_references.REQUIRED_SECTIONS)
        self.assertIn("- Component computed-style evidence:", validate_references.QUALITY_MARKERS)


    def test_validator_rejects_broken_card(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            (library / "indexes" / "cards").mkdir(parents=True)
            (library / "indexes" / "cards" / "broken.json").write_text('{"slug":"broken"}', encoding="utf-8")

            result = run([sys.executable, str(VALIDATE), "--library", str(library), "--json"])

            self.assertEqual(result.returncode, 1)
            payload = json.loads(result.stdout)
            self.assertFalse(payload["valid"])
            self.assertTrue(payload["errors"])


    def test_strength_missing_when_dimension_has_no_observed_values(self) -> None:
        build = load_module(BUILD, "build_progressive_reference")

        self.assertEqual(
            build.evidence_strength(
                "## Observed\n- First viewport structure:\n\n## Missing Evidence\n- layout missing\n",
                "layout_spacing",
            ),
            "missing",
        )


if __name__ == "__main__":
    unittest.main()
