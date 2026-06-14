from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "scripts" / "build_progressive_reference.py"
CAPTURE = ROOT / "scripts" / "capture_reference.py"
CLEAN = ROOT / "scripts" / "clean_reference_noise.py"
BACKFILL = ROOT / "scripts" / "backfill_progressive_library.py"
BACKFILL_L3 = ROOT / "scripts" / "backfill_reference_l3.py"
RECAPTURE = ROOT / "scripts" / "recapture_reference_assets.py"
SCORE = ROOT / "scripts" / "score_reference_quality.py"
VALIDATE = ROOT / "scripts" / "validate_progressive_library.py"
VALIDATE_REFERENCES = ROOT / "scripts" / "validate_references.py"
SKILL = ROOT / "SKILL.md"
DESIGNSTYLE_SKILL = ROOT.parent / "designstyle" / "SKILL.md"
USE_SKILL = ROOT.parent / "use-designstyle" / "SKILL.md"
SEARCH = ROOT.parent / "use-designstyle" / "scripts" / "search_references.py"
COMPARE = ROOT.parent / "use-designstyle" / "scripts" / "compare_against_reference.py"
BLIND_E2E = ROOT.parent / "use-designstyle" / "scripts" / "run_blind_e2e.py"
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
    (library / "assets" / "2026-06-04-sample-hardware-motion.json").write_text(
        json.dumps(
            {
                "slug": "sample-hardware",
                "source": "public CSS/JS resource sampling",
                "items": [
                    {
                        "id": "motion-card-hover-transform-180ms-ease",
                        "selector": ".product-card:hover",
                        "selector_role": "card",
                        "trigger": "hover",
                        "property": "transform",
                        "from": "missing",
                        "to": "translateY(-2px)",
                        "duration_ms": 180,
                        "delay_ms": 0,
                        "easing": "ease",
                        "keyframes": [],
                        "reduced_motion": "missing",
                        "source": "/style.css",
                        "description": "卡片悬停：transform -> translateY(-2px)，180ms ease，hover 触发",
                        "snippet": ".product-card:hover { transform: translateY(-2px); transition: transform 180ms ease; }",
                    },
                    {
                        "id": "motion-incomplete-opacity",
                        "selector": ".toast",
                        "selector_role": "component",
                        "trigger": "state-change",
                        "property": "opacity",
                        "from": "missing",
                        "to": "missing",
                        "duration_ms": "missing",
                        "delay_ms": 0,
                        "easing": "missing",
                        "keyframes": [],
                        "reduced_motion": "missing",
                        "source": "/style.css",
                        "description": "Opacity transition was mentioned but timing/easing were not captured.",
                        "snippet": ".toast { transition-property: opacity; }",
                    }
                ],
                "noise_filtered": ["autofill", "consent"],
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

## Style DNA
- First viewport uses a 72px header and 55/45 hero split; source: Layout Geometry And Spacing
- Product media keeps a 4:3 ratio; source: Dimension And Ratio System
- Hover lift uses 180ms ease; source: Motion Code And Runtime Evidence

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

## Reference Text And Copy Grammar
- H1/H2/eyebrow/CTA samples: Wear the signal; Designed for daily carry; Buy now
- Sentence rhythm: short product claims under 6 words
- Claim density: 0 numeric marketing claims in captured copy
- Voice and naming: restrained product naming
- Copy boundaries: do not reuse exact product claims

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
- Structured motion evidence: `assets/2026-06-04-sample-hardware-motion.json`
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
    def test_capture_parses_motion_json_and_filters_noise(self) -> None:
        capture = load_module(CAPTURE, "capture_reference")
        css = """
        input:-webkit-autofill { transition: background-color 9999s ease-in-out; }
        .consent-banner { animation: consentSlide 400ms ease; }
        .product-card:hover {
          transform: translateY(-2px);
          transition: transform 180ms ease;
        }
        .reveal {
          animation: cardIn 250ms cubic-bezier(0, 1, .25, 1) 80ms both;
        }
        @keyframes cardIn {
          from { opacity: 0; transform: translateY(24px); }
          to { opacity: 1; transform: translateY(0); }
        }
        @media (prefers-reduced-motion: reduce) {
          .reveal { animation: none; transition: none; }
        }
        """

        payload = capture.parse_motion_stylesheet(css, "https://example.com/style.css", slug="sample")

        self.assertEqual(payload["slug"], "sample")
        self.assertTrue(payload["items"])
        joined = json.dumps(payload, ensure_ascii=False)
        self.assertNotIn("autofill", joined.lower())
        self.assertNotIn("consent", joined.lower())
        hover = next(item for item in payload["items"] if item["trigger"] == "hover")
        self.assertEqual(hover["selector"], ".product-card:hover")
        self.assertEqual(hover["selector_role"], "card")
        self.assertEqual(hover["property"], "transform")
        self.assertEqual(hover["duration_ms"], 180)
        self.assertEqual(hover["easing"], "ease")
        reveal = next(item for item in payload["items"] if item["property"] == "animation")
        self.assertEqual(reveal["duration_ms"], 250)
        self.assertEqual(reveal["delay_ms"], 80)
        self.assertIn("translateY(24px)", json.dumps(reveal["keyframes"], ensure_ascii=False))
        self.assertEqual(reveal["reduced_motion"], "reduce disables animation/transition")
        self.assertIn("触发", reveal["description"])

    def test_capture_filters_noise_inside_keyframe_values(self) -> None:
        capture = load_module(CAPTURE, "capture_reference")
        css = """
        .footer-tray {
          animation: trayIn 1000ms linear;
        }
        @keyframes trayIn {
          0% { padding-bottom: calc(var(--s12) + var(--consent-banner-height)); translate: 0 0; }
          to { padding-bottom: var(--s12); translate: 0 100%; }
        }
        .card:hover {
          transform: translateY(-2px);
          transition: transform 180ms ease;
        }
        """

        payload = capture.parse_motion_stylesheet(css, "https://example.com/style.css", slug="sample")
        joined = json.dumps(payload, ensure_ascii=False).lower()

        self.assertNotIn("consent", joined)
        self.assertEqual(len(payload["items"]), 1)
        self.assertEqual(payload["items"][0]["selector"], ".card:hover")

    def test_capture_converts_interaction_deltas_to_motion_items(self) -> None:
        capture = load_module(CAPTURE, "capture_reference")
        component_evidence = {
            "stateSamples": [
                {
                    "sampleId": "button-0",
                    "category": "Button",
                    "text": "Buy now",
                    "before": {
                        "transitionDuration": "180ms",
                        "transitionTimingFunction": "ease",
                    },
                    "hover_changed": {
                        "transform": "matrix(1, 0, 0, 1, 0, -2)",
                    },
                    "focus_changed": {},
                }
            ]
        }

        items = capture.motion_items_from_interaction_states(component_evidence, "sample", "playwright")

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["selector_role"], "button")
        self.assertEqual(items[0]["trigger"], "hover")
        self.assertEqual(items[0]["property"], "transform")
        self.assertEqual(items[0]["duration_ms"], 180)
        self.assertEqual(items[0]["easing"], "ease")
        self.assertEqual(items[0]["to"], "matrix(1, 0, 0, 1, 0, -2)")
        self.assertIn("Buy now", items[0]["description"])

    def test_capture_does_not_promote_cookie_interaction_deltas_to_motion(self) -> None:
        capture = load_module(CAPTURE, "capture_reference")
        component_evidence = {
            "stateSamples": [
                {
                    "sampleId": "button-6",
                    "category": "Button",
                    "text": "Cookie preferences",
                    "before": {"transitionDuration": "0ms"},
                    "hover_changed": {"color": "rgb(247, 247, 248)"},
                    "focus_changed": {"color": "rgb(247, 247, 248)"},
                }
            ]
        }

        items = capture.motion_items_from_interaction_states(component_evidence, "sample", "playwright")

        self.assertEqual(items, [])

    def test_collect_motion_does_not_parse_javascript_as_css(self) -> None:
        capture = load_module(CAPTURE, "capture_reference")
        with tempfile.TemporaryDirectory() as td:
            script = Path(td) / "app.js"
            script.write_text(
                "const bad = 'transition: null===(n=e.options.initialPromotionConfig)||void 0';",
                encoding="utf-8",
            )
            stylesheet = Path(td) / "style.css"
            stylesheet.write_text(
                ".card:hover { transform: translateY(-2px); transition: transform 180ms ease; }",
                encoding="utf-8",
            )

            checked, evidence, structured = capture.collect_motion(
                [script.as_uri(), stylesheet.as_uri()],
                "https://example.com/",
                "sample",
            )

            self.assertEqual(len(checked), 2)
            self.assertIn("transition", evidence)
            self.assertEqual(len(structured["items"]), 1)
            self.assertEqual(structured["items"][0]["selector"], ".card:hover")
            self.assertEqual(structured["items"][0]["property"], "transform")

    def test_collect_motion_omits_noise_resource_urls(self) -> None:
        capture = load_module(CAPTURE, "capture_reference")
        with tempfile.TemporaryDirectory() as td:
            noisy = Path(td) / "otSDKStub.js"
            noisy.write_text("requestAnimationFrame(() => document.cookie)", encoding="utf-8")
            stylesheet = Path(td) / "style.css"
            stylesheet.write_text(
                ".card:hover { transform: translateY(-2px); transition: transform 180ms ease; }",
                encoding="utf-8",
            )

            checked, evidence, structured = capture.collect_motion(
                [noisy.as_uri(), stylesheet.as_uri()],
                "https://example.com/",
                "sample",
            )

            joined = json.dumps({"checked": checked, "evidence": evidence, "structured": structured}, ensure_ascii=False).lower()
            self.assertNotIn("otsdkstub", joined)
            self.assertNotIn("cookie", joined)
            self.assertEqual(checked, [stylesheet.as_uri()])
            self.assertEqual(structured["source_urls"], [stylesheet.as_uri()])

    def test_collect_motion_omits_analytics_key_urls(self) -> None:
        capture = load_module(CAPTURE, "capture_reference")
        with tempfile.TemporaryDirectory() as td:
            analytics = Path(td) / "config.js"
            analytics.write_text("requestAnimationFrame(() => {})", encoding="utf-8")
            replay = Path(td) / "replay.js"
            replay.write_text("requestAnimationFrame(() => {})", encoding="utf-8")
            stylesheet = Path(td) / "style.css"
            stylesheet.write_text(
                ".card:hover { transform: translateY(-2px); transition: transform 180ms ease; }",
                encoding="utf-8",
            )

            checked, evidence, structured = capture.collect_motion(
                [
                    f"{analytics.as_uri()}?project={'ph' + 'c_'}abc123",
                    f"{replay.as_uri()}?{'replay' + 'ApiKey'}=abc-123",
                    stylesheet.as_uri(),
                ],
                "https://example.com/",
                "sample",
            )

            joined = json.dumps({"checked": checked, "evidence": evidence, "structured": structured}, ensure_ascii=False).lower()
            self.assertNotIn("ph" + "c_", joined)
            self.assertNotIn(("replay" + "ApiKey").lower(), joined)
            self.assertEqual(checked, [stylesheet.as_uri()])
            self.assertEqual(structured["source_urls"], [stylesheet.as_uri()])

    def test_capture_resolves_css_variables_and_transition_longhands(self) -> None:
        capture = load_module(CAPTURE, "capture_reference")
        css = """
        :root {
          --hover-transition-duration: 220ms;
          --hover-transition-timing: cubic-bezier(.4, 0, .2, 1);
        }
        .product-card {
          transition: transform var(--hover-transition-duration) var(--hover-transition-timing),
            box-shadow var(--hover-transition-duration) var(--hover-transition-timing);
        }
        .swiper-wrapper {
          transition-property: transform, height;
          transition-duration: 300ms, 450ms;
          transition-timing-function: ease-out, linear;
        }
        .loader {
          animation-name: spin;
          animation-duration: 1s;
          animation-timing-function: steps(12);
        }
        @keyframes spin {
          from { transform: rotate(0deg); }
          to { transform: rotate(360deg); }
        }
        """

        payload = capture.parse_motion_stylesheet(css, "https://example.com/style.css", slug="sample")

        card = next(item for item in payload["items"] if item["selector"] == ".product-card" and item["property"] == "transform")
        self.assertEqual(card["duration_ms"], 220)
        self.assertEqual(card["easing"], "cubic-bezier(.4, 0, .2, 1)")
        wrapper = next(item for item in payload["items"] if item["selector"] == ".swiper-wrapper" and item["property"] == "height")
        self.assertEqual(wrapper["duration_ms"], 450)
        self.assertEqual(wrapper["easing"], "linear")
        loader = next(item for item in payload["items"] if item["selector"] == ".loader")
        self.assertEqual(loader["duration_ms"], 1000)
        self.assertEqual(loader["easing"], "steps(12)")
        self.assertIn("rotate(360deg)", json.dumps(loader["keyframes"], ensure_ascii=False))

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

    def test_use_skill_requires_apply_pack_compare_loop_and_screenshot_qa(self) -> None:
        text = USE_SKILL.read_text(encoding="utf-8")

        for marker in [
            "## Apply Pack",
            "variables.css",
            "motion-presets.css",
            "tailwind.theme.json",
            "compare_against_reference",
            "DNA checklist",
            "probe_aesthetic_fit.py",
            "screenshot path required",
            "immediate-load screenshot",
            "post-animation screenshot",
            "hover/focus screenshot",
            "mobile screenshot",
            "reduced-motion screenshot",
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
            self.assertEqual(payload["design_system_paths"]["motion"], "design-systems/sample-hardware/motion.json")
            self.assertEqual(payload["design_system_paths"]["variables_css"], "design-systems/sample-hardware/variables.css")
            self.assertEqual(payload["design_system_paths"]["tailwind_theme"], "design-systems/sample-hardware/tailwind.theme.json")
            self.assertEqual(payload["design_system_paths"]["motion_presets"], "design-systems/sample-hardware/motion-presets.css")
            dims = sorted((library / "dimensions" / "sample-hardware").glob("*.md"))
            self.assertEqual(len(dims), 7)
            system_dir = library / "design-systems" / "sample-hardware"
            self.assertTrue((system_dir / "tokens.json").exists())
            self.assertTrue((system_dir / "motion.json").exists())
            self.assertTrue((system_dir / "variables.css").exists())
            self.assertTrue((system_dir / "tailwind.theme.json").exists())
            self.assertTrue((system_dir / "motion-presets.css").exists())
            self.assertTrue((system_dir / "palette.md").exists())
            self.assertTrue((system_dir / "moodboard.svg").exists())
            self.assertTrue((system_dir / "component-styles.md").exists())
            tokens = json.loads((system_dir / "tokens.json").read_text())
            self.assertIn("evidence", tokens)
            self.assertIn("apply", tokens)
            self.assertIn("palette", tokens)
            self.assertIn("component_styles", tokens)
            self.assertIn("color", tokens["apply"])
            self.assertIn("motion", tokens["apply"])
            self.assertEqual(tokens["apply"]["motion"]["motion-card-hover-transform-180ms-ease"]["duration"]["$value"], "180ms")
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
            motion = json.loads((system_dir / "motion.json").read_text())
            self.assertEqual(len(motion["items"]), 1)
            self.assertEqual(motion["items"][0]["selector_role"], "card")
            self.assertEqual(motion["omitted_incomplete"][0]["id"], "motion-incomplete-opacity")
            self.assertIn("duration_ms", motion["omitted_incomplete"][0]["missing_fields"])
            motion_text = (library / "dimensions" / "sample-hardware" / "motion-code.md").read_text(encoding="utf-8")
            self.assertIn("| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |", motion_text)
            self.assertIn("card", motion_text)
            self.assertIn("180ms", motion_text)
            self.assertIn("motion-incomplete-opacity lacks duration_ms", motion_text)
            self.assertIn("## Snippet Appendix", motion_text)
            variables = (system_dir / "variables.css").read_text(encoding="utf-8")
            self.assertIn(":root", variables)
            self.assertIn("--ds-motion-motion-card-hover-transform-180ms-ease-duration: 180ms;", variables)
            tailwind = json.loads((system_dir / "tailwind.theme.json").read_text())
            self.assertIn("theme", tailwind)
            self.assertIn("colors", tailwind["theme"]["extend"])
            presets = (system_dir / "motion-presets.css").read_text(encoding="utf-8")
            self.assertIn(".ds-motion-motion-card-hover-transform-180ms-ease", presets)
            component_text = (system_dir / "component-styles.md").read_text()
            self.assertIn("## Button", component_text)
            self.assertIn("### Style Evidence", component_text)
            self.assertIn("### Missing Evidence", component_text)
            self.assertTrue((library / "indexes" / "manifest.json").exists())
            self.assertTrue((library / "indexes" / "facets.json").exists())

    def test_validator_rejects_invalid_motion_json(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            reference = write_reference(library)

            build_result = run([sys.executable, str(BUILD), "--reference", str(reference), "--library", str(library)])
            self.assertEqual(build_result.returncode, 0, build_result.stderr)

            motion_path = library / "design-systems" / "sample-hardware" / "motion.json"
            motion_path.write_text(
                json.dumps(
                    {
                        "slug": "sample-hardware",
                        "items": [
                            {
                                "selector_role": "card",
                                "trigger": "hover",
                                "property": "transform",
                                "duration_ms": "fast",
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )

            result = run([sys.executable, str(VALIDATE), "--library", str(library), "--json"])

            self.assertEqual(result.returncode, 1)
            payload = json.loads(result.stdout)
            self.assertFalse(payload["valid"])
            self.assertIn("invalid motion duration", "\n".join(payload["errors"]))

    def test_validator_requires_apply_tokens_and_apply_pack_files(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            reference = write_reference(library)

            build_result = run([sys.executable, str(BUILD), "--reference", str(reference), "--library", str(library)])
            self.assertEqual(build_result.returncode, 0, build_result.stderr)

            tokens_path = library / "design-systems" / "sample-hardware" / "tokens.json"
            tokens = json.loads(tokens_path.read_text())
            tokens.pop("apply", None)
            tokens_path.write_text(json.dumps(tokens), encoding="utf-8")
            (library / "design-systems" / "sample-hardware" / "variables.css").unlink()

            result = run([sys.executable, str(VALIDATE), "--library", str(library), "--json"])

            self.assertEqual(result.returncode, 1)
            payload = json.loads(result.stdout)
            errors = "\n".join(payload["errors"])
            self.assertIn("design system lacks apply tokens", errors)
            self.assertIn("design system file missing: design-systems/sample-hardware/variables.css", errors)

    def test_clean_reference_noise_flags_truncated_css_and_consent_noise(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            motion_dir = library / "dimensions" / "noisy"
            motion_dir.mkdir(parents=True)
            (motion_dir / "motion-code.md").write_text(
                """
# Motion And Code

## Observed
- Public CSS/JS motion snippets: input:-webkit-autofill { transition: background-color 9999s ease; } .consent-banner { animation: slide 400ms ease; } .card { transition
""",
                encoding="utf-8",
            )

            result = run([sys.executable, str(CLEAN), "--library", str(library), "--check"])

            self.assertEqual(result.returncode, 1)
            self.assertIn("autofill/consent noise", result.stdout)
            self.assertIn("truncated css declaration", result.stdout)

    def test_clean_reference_noise_flags_analytics_keys(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            motion_dir = library / "dimensions" / "noisy"
            motion_dir.mkdir(parents=True)
            (motion_dir / "assets.md").write_text(
                f"""
# Assets

- Public stylesheet/script URLs: https://example.com/array/{'ph' + 'c_'}abc123/config.js; https://example.com/replay.js?{'replay' + 'ApiKey'}=abc-123
""",
                encoding="utf-8",
            )

            result = run([sys.executable, str(CLEAN), "--library", str(library), "--check"])

            self.assertEqual(result.returncode, 1)
            self.assertIn("third-party analytics/replay key", result.stdout)

    def test_clean_reference_noise_removes_truncated_css_lines(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            motion_dir = library / "dimensions" / "noisy"
            motion_dir.mkdir(parents=True)
            motion_path = motion_dir / "motion-code.md"
            motion_path.write_text(
                """
# Motion And Code

## Observed
- Public CSS/JS motion snippets: .card { transition
- Motion purpose: retain summary text.
""",
                encoding="utf-8",
            )

            clean_result = run([sys.executable, str(CLEAN), "--library", str(library)])
            check_result = run([sys.executable, str(CLEAN), "--library", str(library), "--check"])

            self.assertEqual(clean_result.returncode, 0, clean_result.stderr)
            self.assertEqual(check_result.returncode, 0, check_result.stdout)
            cleaned = motion_path.read_text(encoding="utf-8")
            self.assertNotIn(".card { transition", cleaned)
            self.assertIn("retain summary text", cleaned)

    def test_build_does_not_copy_fallback_motion_css_wall(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            reference = write_reference(library)
            (library / "assets" / "2026-06-04-sample-hardware-motion.json").unlink()
            (library / "assets" / "2026-06-04-sample-hardware-component-styles.json").unlink()
            text = reference.read_text(encoding="utf-8")
            text = text.replace(
                "- Structured motion evidence: `assets/2026-06-04-sample-hardware-motion.json`\n",
                "",
            )
            text = text.replace(
                "- Public CSS/JS motion snippets: transition: transform 180ms ease",
                "- Public CSS/JS motion snippets: .card { transition",
            )
            reference.write_text(text, encoding="utf-8")

            result = run([sys.executable, str(BUILD), "--reference", str(reference), "--library", str(library)])

            self.assertEqual(result.returncode, 0, result.stderr)
            motion_path = library / "design-systems" / "sample-hardware" / "motion.json"
            motion = json.loads(motion_path.read_text(encoding="utf-8"))
            motion_text = (library / "dimensions" / "sample-hardware" / "motion-code.md").read_text(encoding="utf-8")
            self.assertEqual(motion["items"], [])
            self.assertEqual(motion["omitted_incomplete"][0]["snippet"], "")
            self.assertNotIn(".card { transition", motion_text)
            self.assertIn("No direct snippet appendix available.", motion_text)

    def test_build_promotes_component_transition_states_to_motion_items(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            reference = write_reference(library)
            (library / "assets" / "2026-06-04-sample-hardware-motion.json").unlink()
            text = reference.read_text(encoding="utf-8")
            text = text.replace(
                "- Structured motion evidence: `assets/2026-06-04-sample-hardware-motion.json`\n",
                "",
            )
            reference.write_text(text, encoding="utf-8")

            result = run([sys.executable, str(BUILD), "--reference", str(reference), "--library", str(library)])

            self.assertEqual(result.returncode, 0, result.stderr)
            motion = json.loads((library / "design-systems" / "sample-hardware" / "motion.json").read_text(encoding="utf-8"))
            self.assertEqual(motion["items"][0]["selector_role"], "button")
            self.assertEqual(motion["items"][0]["trigger"], "hover")
            self.assertEqual(motion["items"][0]["property"], "transform")
            self.assertEqual(motion["items"][0]["duration_ms"], 180)
            self.assertEqual(motion["items"][0]["easing"], "ease")
            self.assertEqual(motion["items"][0]["source"], "component-styles interaction evidence")
            self.assertIn("Buy now", motion["items"][0]["description"])

    def test_build_promotes_component_transition_declarations_without_state_diff(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            reference = write_reference(library)
            (library / "assets" / "2026-06-04-sample-hardware-motion.json").unlink()
            component_path = library / "assets" / "2026-06-04-sample-hardware-component-styles.json"
            payload = json.loads(component_path.read_text(encoding="utf-8"))
            payload["component_evidence"]["stateSamples"] = []
            payload["component_evidence"]["samples"][0]["styles"]["transition"] = "opacity 240ms ease-out"
            payload["component_evidence"]["samples"][0]["styles"]["opacity"] = "0.88"
            payload["component_evidence"]["samples"][1]["styles"]["transition"] = "all 0s ease"
            component_path.write_text(json.dumps(payload), encoding="utf-8")
            text = reference.read_text(encoding="utf-8")
            text = text.replace(
                "- Structured motion evidence: `assets/2026-06-04-sample-hardware-motion.json`\n",
                "",
            )
            reference.write_text(text, encoding="utf-8")

            result = run([sys.executable, str(BUILD), "--reference", str(reference), "--library", str(library)])

            self.assertEqual(result.returncode, 0, result.stderr)
            motion = json.loads((library / "design-systems" / "sample-hardware" / "motion.json").read_text(encoding="utf-8"))
            self.assertEqual(len(motion["items"]), 1)
            self.assertEqual(motion["items"][0]["trigger"], "state-change")
            self.assertEqual(motion["items"][0]["property"], "opacity")
            self.assertEqual(motion["items"][0]["duration_ms"], 240)
            self.assertEqual(motion["items"][0]["easing"], "ease-out")
            self.assertEqual(motion["items"][0]["source"], "component-styles transition declaration")

    def test_component_noise_samples_are_not_promoted(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            reference = write_reference(library)
            component_path = library / "assets" / "2026-06-04-sample-hardware-component-styles.json"
            payload = json.loads(component_path.read_text(encoding="utf-8"))
            payload["component_evidence"]["samples"].append(
                {
                    "sampleId": "form-0",
                    "category": "Form",
                    "tag": "input",
                    "classHint": "size-full autofill:shadow-[0_0_0px_1000px_var(--background)_inset]",
                    "rect": {"x": 10, "y": 10, "width": 180, "height": 24},
                    "styles": {
                        "display": "block",
                        "fontSize": "14px",
                        "transition": "color 150ms ease",
                    },
                }
            )
            component_path.write_text(json.dumps(payload), encoding="utf-8")

            result = run([sys.executable, str(BUILD), "--reference", str(reference), "--library", str(library)])

            self.assertEqual(result.returncode, 0, result.stderr)
            tokens_text = (library / "design-systems" / "sample-hardware" / "tokens.json").read_text(encoding="utf-8")
            component_text = (library / "design-systems" / "sample-hardware" / "component-styles.md").read_text(encoding="utf-8")
            self.assertNotIn("autofill", tokens_text)
            self.assertNotIn("autofill", component_text)

    def test_backfill_dry_run_reports_partial_without_writing(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            write_reference(library)

            result = run([sys.executable, str(BACKFILL), "--library", str(library), "--dry-run", "--limit", "1"])

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("mode=dry-run", result.stdout)
            self.assertIn("planned=1", result.stdout)
            self.assertFalse((library / "indexes" / "cards" / "sample-hardware.json").exists())

    def test_l3_backfill_inserts_dna_and_required_sections(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            reference = write_reference(library)
            build_result = run([sys.executable, str(BUILD), "--reference", str(reference), "--library", str(library)])
            self.assertEqual(build_result.returncode, 0, build_result.stderr)

            text = reference.read_text(encoding="utf-8")
            for section in ["Style DNA", "Reference Text And Copy Grammar", "Style Tokens And Surface Grammar"]:
                text = re.sub(rf"\n## {re.escape(section)}\n[\s\S]*?(?=\n## |\Z)", "", text)
            text = re.sub(r"^- Public stylesheet/script URLs:.*\n", "", text, flags=re.M)
            text = re.sub(r"^- Exact motion parameters:.*\n", "", text, flags=re.M)
            reference.write_text(text, encoding="utf-8")

            result = run([sys.executable, str(BACKFILL_L3), "--library", str(library), "--reference", str(reference)])

            self.assertEqual(result.returncode, 0, result.stderr)
            updated = reference.read_text(encoding="utf-8")
            self.assertIn("## Style DNA", updated)
            self.assertIn("source:", updated)
            self.assertIn("## Reference Text And Copy Grammar", updated)
            self.assertIn("## Style Tokens And Surface Grammar", updated)
            self.assertIn("- Public stylesheet/script URLs:", updated)
            self.assertIn("- Exact motion parameters:", updated)

    def test_reference_validator_rejects_non_measurable_l3_style_dna(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            reference = write_reference(library)
            text = reference.read_text(encoding="utf-8")
            text = re.sub(
                r"\n## Style DNA\n[\s\S]*?(?=\n## |\Z)",
                "\n## Style DNA\n- quiet premium whitespace; source: manual note\n",
                text,
            )
            reference.write_text(text, encoding="utf-8")

            result = run([sys.executable, str(VALIDATE_REFERENCES), "--library", str(library), "--json"])

            self.assertEqual(result.returncode, 1)
            self.assertIn("Style DNA decision is not measurable", result.stdout)

    def test_recapture_updates_evidence_paths_without_replacing_body(self) -> None:
        recapture = load_module(RECAPTURE, "recapture_reference_assets")
        original = """---
title: "Sample Hardware"
source_url: "https://example.com"
evidence_screenshot: "screenshots/old.png"
---

# Style Reference: Sample Hardware

## Essence
Keep this hand-written body.

## Code Surface
- Component computed-style evidence: `assets/old-component-styles.json`

## Motion
- Existing motion note stays.

## Interaction And Components
- Computed component styles: `assets/old-component-styles.json`
"""

        updated = recapture.update_reference_evidence_paths(
            original,
            "screenshots/sample-hardware-desktop.png",
            "assets/2026-06-11-sample-hardware-component-styles.json",
            "assets/2026-06-11-sample-hardware-motion.json",
        )

        self.assertIn("Keep this hand-written body.", updated)
        self.assertIn("- Existing motion note stays.", updated)
        self.assertIn('evidence_screenshot: "screenshots/sample-hardware-desktop.png"', updated)
        self.assertIn("assets/2026-06-11-sample-hardware-component-styles.json", updated)
        self.assertIn("- Structured motion evidence: `assets/2026-06-11-sample-hardware-motion.json`", updated)
        self.assertNotIn("assets/old-component-styles.json", updated)

    def test_recapture_dry_run_resolves_slug_without_writing(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            write_reference(library)

            result = run([sys.executable, str(RECAPTURE), "--library", str(library), "--slugs", "sample-hardware", "--dry-run"])

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("mode=dry-run", result.stdout)
            self.assertIn("planned=1", result.stdout)
            self.assertFalse((library / "assets" / "2026-06-11-sample-hardware-motion.json").exists())

    def test_quality_score_includes_motion_and_apply_pack_dimensions(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            reference = write_reference(library)
            build_result = run([sys.executable, str(BUILD), "--reference", str(reference), "--library", str(library)])
            self.assertEqual(build_result.returncode, 0, build_result.stderr)

            result = run([sys.executable, str(SCORE), "--library", str(library)])

            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertIn("motion_structure", payload["rubric"])
            self.assertIn("apply_pack", payload["rubric"])
            row = payload["references"][0]
            self.assertGreater(row["parts"]["motion_structure"], 0)
            self.assertGreater(row["parts"]["apply_pack"], 0)

    def test_progressive_card_includes_measurable_style_dna(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            reference = write_reference(library)

            result = run([sys.executable, str(BUILD), "--reference", str(reference), "--library", str(library)])

            self.assertEqual(result.returncode, 0, result.stderr)
            card = json.loads((library / "indexes" / "cards" / "sample-hardware.json").read_text())
            self.assertIn("dna", card)
            self.assertLessEqual(len(card["dna"]), 12)
            self.assertTrue(card["dna"])
            for item in card["dna"]:
                self.assertRegex(item["decision"], r"\d")
                self.assertTrue(item["evidence_source"])

    def test_validator_rejects_non_measurable_style_dna(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            reference = write_reference(library)
            build_result = run([sys.executable, str(BUILD), "--reference", str(reference), "--library", str(library)])
            self.assertEqual(build_result.returncode, 0, build_result.stderr)

            card_path = library / "indexes" / "cards" / "sample-hardware.json"
            card = json.loads(card_path.read_text())
            card["dna"] = [{"decision": "quiet premium whitespace", "evidence_source": "manual"}]
            card_path.write_text(json.dumps(card), encoding="utf-8")

            result = run([sys.executable, str(VALIDATE), "--library", str(library), "--json"])

            self.assertEqual(result.returncode, 1)
            self.assertIn("dna decision is not measurable", result.stdout)

    def test_search_need_hard_filters_scene_and_outputs_borrow_dimensions(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            (library / "indexes" / "cards").mkdir(parents=True)
            (library / "references").mkdir(parents=True)
            (library / "references" / "dashboard.md").write_text("# Dashboard\n", encoding="utf-8")
            (library / "references" / "portfolio.md").write_text("# Portfolio\n", encoding="utf-8")
            for slug, title, category, page_scope, best_for, motion in [
                ("dashboard", "Analytics Dashboard", ["dashboard", "analytics"], "dashboard", ["analytics dashboard"], ["table hover"]),
                ("portfolio", "Motion Portfolio", ["portfolio"], "portfolio", ["portfolio gallery"], ["hover", "scroll", "transition"]),
            ]:
                (library / "indexes" / "cards" / f"{slug}.json").write_text(
                    json.dumps(
                        {
                            "slug": slug,
                            "title": title,
                            "reference_path": f"references/{slug}.md",
                            "category_tags": category,
                            "style_tags": ["dark"],
                            "structure_tags": [],
                            "motion_tags": motion,
                            "code_tags": ["css"],
                            "page_scope": page_scope,
                            "best_for": best_for,
                            "avoid_for": ["dashboard"] if slug == "portfolio" else [],
                            "evidence_strength": {"screenshot": "strong", "motion_code": "strong", "design_system": "strong"},
                            "dimension_paths": {},
                            "design_system_paths": {},
                            "selection_note": title,
                            "evidence_limits": [],
                            "missing_evidence": [],
                            "component_json_path": "",
                            "dna": [{"decision": "grid gap 24px", "evidence_source": "layout-spacing.md"}],
                        }
                    ),
                    encoding="utf-8",
                )

            result = run([
                sys.executable,
                str(SEARCH),
                "hover transition dark",
                "--library",
                str(library),
                "--need",
                "motion:L2,palette:dark,scene:dashboard",
                "--explain-selection",
            ])

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Analytics Dashboard", result.stdout)
            self.assertNotIn("Motion Portfolio", result.stdout)
            self.assertIn("borrowable_dimensions:", result.stdout)
            self.assertIn("not_borrowable_dimensions:", result.stdout)

    def test_search_scene_need_matches_docs_aliases(self) -> None:
        search = load_module(SEARCH, "search_references")
        docs_card = {
            "category_tags": ["software", "editorial", "developer-tooling", "education"],
            "page_scope": "homepage software editorial resource",
            "best_for": ["software editorial homepages", "developer resource sites", "technical writing indexes"],
        }
        dashboard_card = {
            "category_tags": ["analytics", "dashboard"],
            "page_scope": "public analytics dashboard",
            "best_for": ["web analytics dashboards"],
        }

        self.assertTrue(search.scene_need_matches(docs_card, {"scene": "docs"}))
        self.assertTrue(search.scene_need_matches(docs_card, {"scene": "documentation"}))
        self.assertFalse(search.scene_need_matches(dashboard_card, {"scene": "docs"}))

    def test_compare_against_reference_writes_table_and_iteration_log(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            reference = write_reference(library)
            build_result = run([sys.executable, str(BUILD), "--reference", str(reference), "--library", str(library)])
            self.assertEqual(build_result.returncode, 0, build_result.stderr)
            out = Path(td) / "comparison.md"
            generated = Path(td) / "generated-first-viewport.png"
            generated.write_bytes((library / "screenshots" / "sample-hardware-desktop.png").read_bytes())

            result = run([
                sys.executable,
                str(COMPARE),
                "--library",
                str(library),
                "--card",
                str(library / "indexes" / "cards" / "sample-hardware.json"),
                "--generated",
                str(generated),
                "--state",
                "first-viewport",
                "--output",
                str(out),
            ])

            self.assertEqual(result.returncode, 0, result.stderr)
            text = out.read_text(encoding="utf-8")
            self.assertIn("# Reference Comparison", text)
            self.assertIn("| DNA Decision | Evidence Source | Generated Check | Status |", text)
            self.assertIn("## Screenshot Evidence", text)
            self.assertIn("## Iteration Log", text)
            self.assertIn(str(generated), text)

    def test_blind_e2e_writes_plan_apply_pack_comparison_and_qa_paths(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            library = Path(td) / "library"
            reference = write_reference(library)
            build_result = run([sys.executable, str(BUILD), "--reference", str(reference), "--library", str(library)])
            self.assertEqual(build_result.returncode, 0, build_result.stderr)
            out = Path(td) / "blind-e2e"

            result = run([
                sys.executable,
                str(BLIND_E2E),
                "--library",
                str(library),
                "--case",
                "dashboard:hardware product dashboard:motion:L2",
                "--output-dir",
                str(out),
                "--skip-browser",
            ])

            self.assertEqual(result.returncode, 0, result.stderr)
            summary = json.loads((out / "blind-e2e-summary.json").read_text(encoding="utf-8"))
            self.assertEqual(summary["case_count"], 1)
            case = summary["cases"][0]
            self.assertTrue(Path(case["direction_plan"]).exists())
            self.assertTrue(Path(case["comparison_report"]).exists())
            self.assertEqual(case["dna_pass_rate"], 1.0)
            self.assertIn("variables.css", Path(case["direction_plan"]).read_text(encoding="utf-8"))
            report_text = Path(case["case_report"]).read_text(encoding="utf-8")
            for marker in [
                "## Apply Pack",
                "## Screenshot QA Evidence",
                "immediate-load screenshot",
                "post-animation screenshot",
                "hover/focus screenshot",
                "mobile screenshot",
                "reduced-motion screenshot",
                "## Motion Traceability",
            ]:
                self.assertIn(marker, report_text)


    def test_reference_validator_requires_shared_mandatory_dimensions(self) -> None:
        validate_references = load_module(VALIDATE_REFERENCES, "validate_references")

        self.assertIn("Reference Text And Copy Grammar", validate_references.REQUIRED_SECTIONS)
        self.assertIn("Style Tokens And Surface Grammar", validate_references.REQUIRED_SECTIONS)
        self.assertIn("Style DNA", validate_references.REQUIRED_SECTIONS)
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
