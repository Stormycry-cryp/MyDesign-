# Manifest

Version: v0.2.0
Date: 2026-06-04

## Skills

- `skills/designstyle`
- `skills/add-designstyle`
- `skills/use-designstyle`

## Library Contents

- `designstyle-library/references`: 53 validated Markdown references.
- `designstyle-library/screenshots`: 63 desktop evidence screenshots and supporting visual captures.
- `designstyle-library/assets`: DOM/resource evidence captures.
- `designstyle-library/reviews`: candidate reviews, batch reports, capture evidence JSON, motion code probe JSON.
- `designstyle-library/indexes`: manual indexes plus generated `manifest.json`, `facets.json`, and 53 L1 card JSON files.
- `designstyle-library/dimensions`: 371 L2 dimension summaries, 7 per reference.

## Highlights

- Progressive disclosure: L1 cards, L2 dimension summaries, L3 full references, and L4 raw evidence boundaries.
- Router skill: `designstyle` chooses add, use, or add-then-use and reports evidence layers read.
- Layered tags: `style_tags`, `structure_tags`, `motion_tags`, `code_tags`.
- Dimension/ratio preservation: viewport, document size, media ratios, spacing samples.
- Motion/code evidence: public CSS/JS probe keywords, motion snippets, exact motion parameters.
- Card-first retrieval: `use-designstyle` ranks by category, page scope, best_for, avoid_for penalties, then style/structure/motion/code evidence.

## Verification

Validated locally before release:

- `validate_references.py --library designstyle-library --json`: 53 total, 53 valid, 0 invalid.
- `build_progressive_reference.py --library designstyle-library --all --dry-run`: 53 cards and 371 dimensions planned.
- `build_progressive_reference.py --library designstyle-library --all`: 53 cards and 371 dimensions written idempotently.
- `validate_progressive_library.py --library designstyle-library --json`: 53 cards, 0 invalid, 0 errors.
- `search_references.py "hardware product minimal wearable landing page" --library designstyle-library --explain-selection`: hardware/product references rank above generic SaaS landing-page references.
