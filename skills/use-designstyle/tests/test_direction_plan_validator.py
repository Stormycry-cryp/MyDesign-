from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATE = ROOT / "scripts" / "validate_direction_plan.py"


COMPLETE_PLAN = """# Designstyle Direction Plan

## 0. Reference-Led Execution Contract
- Goal: preserve layout, motion, typography, page logic, hierarchy, fonts, surfaces, components, and states.
- Method: inspect original site, retained screenshots, L2 dimensions, design-system tokens, component JSON, and final screenshots.
- Reference workbench: keep a side-by-side reference workbench open while implementing.
- Acceptance criteria: screenshots prove borrowed reference mechanics are implemented.
- Required reference dimensions: layout, motion, typography, page logic, hierarchy, style tokens, components.
- Dimensions marked missing: none.
- Completion blocker if fidelity is weak: revise before final.

## 2.5 Original-Site Inspection Log
| Reference | Source URL | Live/Screenshot/Component Evidence | What Was Inspected | Key Observed Details | Missing/Blocked |
|---|---|---|---|---|---|
| Roope Rainisto | https://example.com | live original site plus screenshots/roope.png and assets/roope-component-styles.json | desktop, mobile, hover/focus, motion, font computed style | editorial image grid, sparse nav, image-first hierarchy | none |

## 4.5 Style Fidelity Contract
| Reference | Must Preserve | Implement As | Forbidden Drift | Verification |
|---|---|---|---|---|
| Roope Rainisto | archive gallery macro geometry, typography hierarchy, surface grammar, motion grammar, component states, spacing rhythm, page logic, image ratios | CSS grid, aspect-ratio, font scale, hover transition, screenshot QA | generic centered hero plus cards | compare final screenshot |

## 4.6 Implementation Mapping
| Reference Mechanic | Target Element/File | CSS/Layout/Motion Constraint | Token/Component Source | QA Evidence |
|---|---|---|---|---|
| Editorial archive grid | src/page.css | grid-template-columns, aspect-ratio, gap, max-width | design-systems/roope-rainisto/tokens.json | work/qa/desktop.png |
| Hover state | src/page.css | transition: transform 180ms ease | assets/roope-component-styles.json | work/qa/hover.png |

## 4.7 Page Logic And Information Hierarchy Mapping
| Reference Logic | Target Page Logic | Section Order | Hierarchy Rule | Acceptance |
|---|---|---|---|---|
| Viewer sees work first, then artist metadata | work gallery first, biography second, contact last | gallery, details, contact | images outrank copy, CTA is secondary | first viewport screenshot shows work first |

## 4.8 Typography And Font Mapping
| Reference Type Role | Evidence | Target Font/Scale | CSS Constraint | Acceptance |
|---|---|---|---|---|
| Display title | getComputedStyle and type-copy.md | Inter fallback, 64px, 600, 1.0 line-height, 0 letter-spacing | font-family, font-size, font-weight, line-height, letter-spacing, max-width | screenshot text hierarchy matches reference |

## 13. Final QA Checklist
- Immediate first viewport: work/qa/immediate.png
- Post-animation first viewport: work/qa/post-animation.png
- Desktop key sections: work/qa/desktop.png
- Mobile key sections: work/qa/mobile.png
- Hover/focus states: work/qa/hover.png
- Reduced motion: work/qa/reduced-motion.png
- Screenshot structural QA: 3 visible similarities, 2 intentional differences recorded.
- Overlap/misalignment check: passed.
- Aesthetic rating: 82.
"""


INCOMPLETE_PLAN = """# Designstyle Direction Plan

## 0. Reference-Led Execution Contract
- Goal: make it elegant.
- Method: use inspiration.
- Acceptance criteria: looks good.

## 4.5 Style Fidelity Contract
| Reference | Must Preserve | Implement As | Forbidden Drift | Verification |
|---|---|---|---|---|
| Example | clean style | CSS | generic | visual |
"""


class DirectionPlanValidatorTest(unittest.TestCase):
    def run_validator(self, text: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as tmp:
            plan = Path(tmp) / "designstyle-direction-plan.md"
            plan.write_text(text, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(VALIDATE), str(plan)],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

    def test_rejects_plan_without_reference_workbench_mapping_and_screenshot_qa(self) -> None:
        result = self.run_validator(INCOMPLETE_PLAN)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Original-Site Inspection Log", result.stdout)
        self.assertIn("Implementation Mapping", result.stdout)
        self.assertIn("Final QA Checklist", result.stdout)

    def test_accepts_plan_with_required_reference_fidelity_sections(self) -> None:
        result = self.run_validator(COMPLETE_PLAN)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("direction-plan-valid", result.stdout)


if __name__ == "__main__":
    unittest.main()
