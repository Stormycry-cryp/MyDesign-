# Designstyle 50+ UI Library Final Report

Created: 2026-06-03

## Goal

Use `darwin-skill` to optimize `add-designstyle` and `use-designstyle`, observe design-community feedback, collect at least 50 different high-quality website UI references, dissect them with `add-designstyle`, update the designstyle aesthetic library, and produce a final report.

## What Changed

### Skills

- `add-designstyle` now requires layered tags, page scope, community signal, first-viewport geometry, dimension/ratio system, code surface, motion code evidence, exact motion parameters, interaction/components, evidence limits, and self-review.
- `add-designstyle/scripts/capture_reference.py` was repaired and extended:
  - Fixed the Playwright `arguments[0]` evaluation bug.
  - Improved cookie/banner dismissal.
  - Added failed-DOM fallback so blocked captures do not crash batch work.
  - Added same-domain secondary-page summaries while preserving the primary-page screenshot and DOM.
  - Captures public CSS/JS motion snippets, timing/easing, transforms, keyframes, runtime hints, fonts, colors, media, dimensions, buttons, navigation, and overlays.
- `add-designstyle/scripts/validate_references.py` enforces strict quality gates and refuses blank, weak, old-format, or screenshotless references.
- `use-designstyle` now explicitly gates retrieval by scene/page/category fit before using generic motion/code evidence.
- `use-designstyle/scripts/search_references.py` was reweighted so generic terms like `transition`, `hover`, `scroll`, `animation`, `css`, and `code` do not make unrelated visual sites outrank same-scene pricing/product/dashboard references.

### Community Intake

Community/candidate intake was recorded at:

- `~/.codex/designstyle-library/reviews/2026-06-03-community-candidate-pool.md`

Sources and signals used:

- Awwwards: curated award/community signal for high-polish, transitions, storytelling, interaction design, React/Next/Framer-style product/campaign work.
- Httpster: category and style taxonomy for broad diversity across software, architecture, art, food, media, typography, travel, agency, ecommerce, and product pages.
- WebInspoo: SaaS page-type patterns for landing pages, pricing pages, about/contact/resource patterns, typography, colors, and technology/site examples.
- Siteinspire was excluded as direct evidence in this run because it returned a security checkpoint.

## Library Result

Validation command:

```bash
python3 ~/.codex/skills/add-designstyle/scripts/validate_references.py
```

Result:

```text
references=53 valid=53 invalid=0
```

Active index:

- `~/.codex/designstyle-library/indexes/2026-06-03-53-valid-ui-reference-index.md`

Legacy/failed entries were not deleted. They were moved out of active retrieval:

- `~/.codex/designstyle-library/references-legacy-invalid/2026-06-03-pre-v2-and-failed-captures/`

Legacy manifest:

- `~/.codex/designstyle-library/references-legacy-invalid/2026-06-03-pre-v2-and-failed-captures/_manifest.json`

## Coverage Summary

- Active valid references: 53.
- Direct website/product/studio/report references: 40.
- WebInspoo inspiration/page-type references: 13.
- Old-format or failed-capture active references: 0.

Top categories by tag frequency:

- SaaS: 15
- Software: 13
- Inspiration/page-type: 13
- Culture: 11
- Product: 8
- Studio: 7
- Landing page: 7
- AI: 6
- Developer tool: 6
- Pricing: 6
- B2B: 5
- Developer platform: 5
- Productivity / consumer-app / portfolio: 4 each
- Media / agency / service / typography / design-resource / design-tool / editorial: 3 each

Representative category coverage:

- SaaS / developer platform: Vercel, Linear, Stripe, Wiz, Typeform, Mezmo, WebInspoo pricing/landing examples.
- Hardware/product: Apple Vision Pro, Teenage Engineering, Bauhaus Clock, LiveSurface.
- Culture/media/editorial: A24, Visual Journal, USPS report, Developments Media.
- Agency/studio/portfolio: Buffet, Middle Name, Patrick Mason, Snøhetta, WAM, Viviens.
- Design/typography resources: Counter Forms, Uncut, Footer Design, Glyphs.
- Food/wine/hospitality: Ossa Wine, Benvenusa, Lunchbox, Rekki, Viens La.
- Finance/AI: Cleo, Capital, Stripe, ExpenseAI/Mistral/Poolside/Exa references.

## Retrieval Regression

Commands run after reweighting `search_references.py`:

```bash
python3 ~/.codex/skills/use-designstyle/scripts/search_references.py \
  'developer platform pricing page transition comparison table' --matrix --limit 3
```

Top results were same-scene/page-type references:

- WebInspoo Browserbase Pricing Page
- WebInspoo Exa AI Pricing Page
- Vercel Developer Platform

```bash
python3 ~/.codex/skills/use-designstyle/scripts/search_references.py \
  'hardware product page cinematic media led scroll motion apple product story' --matrix --limit 3
```

Top results were product/hardware references:

- Apple Vision Pro Product Story
- Notion Workspace Product
- Linear Product SaaS

```bash
python3 ~/.codex/skills/use-designstyle/scripts/search_references.py \
  'agency studio portfolio typography project grid hover transition' --matrix --limit 3
```

Top results were studio/portfolio references:

- Patrick Mason Studio Portfolio
- WAM Architecture Studio
- Snøhetta Architecture Studio

## Important Use Notes

- WebInspoo references should be used as page-type/inspiration references, not as direct proof of an original brand site's full visual implementation.
- Motion code snippets are public CSS/JS evidence, often minified. Use exact durations/easing/transforms only when the reference section marks them as directly observed; otherwise treat library/framework attribution as weak.
- Secondary pages are summary evidence, not screenshots. They improve page-scope confidence but do not replace manual inspection when a final design depends on a secondary page.
- The active library is now intentionally stricter than the old seed library. Old weak entries were preserved outside active retrieval instead of being counted.

## Completion Evidence

- `add-designstyle` and `use-designstyle` were updated.
- Community candidate pool exists and records sources, feedback themes, candidates, exclusions, and batch rules.
- `capture_reference.py`, `validate_references.py`, and `search_references.py` pass `py_compile`.
- Active library has 53 valid references and 0 invalid references under the strict validator.
- Search regression now returns same-scene results for pricing, hardware product story, and studio/portfolio queries.

