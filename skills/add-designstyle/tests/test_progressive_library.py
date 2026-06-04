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
SKILL = ROOT / "SKILL.md"
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
    (library / "screenshots" / "sample-hardware-desktop.png").write_bytes(b"png")
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
- Cards/sections: spec cards
- Forms/inputs: none
- Feedback states: hover focus visible

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
            dims = sorted((library / "dimensions" / "sample-hardware").glob("*.md"))
            self.assertEqual(len(dims), 7)
            self.assertTrue((library / "indexes" / "manifest.json").exists())
            self.assertTrue((library / "indexes" / "facets.json").exists())


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
