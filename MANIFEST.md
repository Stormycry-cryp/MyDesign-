# Manifest

Version: v0.2.3
Date: 2026-06-04

## Skills

- `skills/designstyle`
- `skills/add-designstyle`
- `skills/use-designstyle`

## Library Contents

- `designstyle-library/references`: 77 validated Markdown references.
- `designstyle-library/screenshots`: 87 desktop evidence screenshots and supporting visual captures.
- `designstyle-library/assets`: 80 DOM/resource evidence captures.
- `designstyle-library/reviews`: candidate reviews, batch reports, capture evidence JSON, motion code probe JSON.
- `designstyle-library/indexes`: manual indexes plus generated `manifest.json`, `facets.json`, and 77 L1 card JSON files.
- `designstyle-library/dimensions`: 539 L2 dimension summaries, 7 per reference.
- `designstyle-library/design-systems`: 77 retained design-system packs, 1 per reference, each with `tokens.json`, `palette.md`, `moodboard.svg`, and `component-styles.md`.

## Highlights

- Progressive disclosure: L1 cards, L2 dimension summaries, L3 full references, and L4 raw evidence boundaries.
- Router skill: `designstyle` chooses add, use, or add-then-use and reports evidence layers read.
- Aesthetic gate: `add-designstyle` can reject visually ordinary candidates before they count as library references.
- Layered tags: `style_tags`, `structure_tags`, `motion_tags`, `code_tags`.
- Dimension/ratio preservation: viewport, document size, media ratios, spacing samples.
- Motion/code evidence: public CSS/JS probe keywords, motion snippets, exact motion parameters.
- Card-first retrieval: `use-designstyle` ranks by category, page scope, best_for, avoid_for penalties, then style/structure/motion/code evidence.
- Design-system retention: `add-designstyle` stores exact color palettes from screenshot pixels and explicit color evidence, moodboard SVGs, token JSON, and component style systems.
- Use-side retrieval: `use-designstyle` search can print design-system paths and excerpts with `--design-system`; `--matrix` shows retained design-system paths.
- Component hygiene: common CSS values such as `9999px` pill radii are preserved, while abnormal browser-computed scientific-notation values are filtered.

## Verification

Validated locally before release:

- `validate_references.py --library designstyle-library --json`: 77 total, 77 valid, 0 invalid.
- `build_progressive_reference.py --library designstyle-library --all --dry-run`: 77 cards and 539 dimensions planned.
- `build_progressive_reference.py --library designstyle-library --all`: 77 cards and 539 dimensions written idempotently.
- `validate_progressive_library.py --library designstyle-library --json`: 77 cards, 0 invalid, 0 errors.
- `search_references.py "dashboard analytics color system table components" --library designstyle-library --matrix --design-system`: search output includes retained design-system paths, palette colors, and component style sections.
- Design-system noise scan: abnormal `3.35544e+07` / `e+07` component-style values are not present in retained artifacts.
- `designstyle-library/reviews/2026-06-04-design-system-template-quality-review.md`: strict template quality score 86.3/100 with 77 per-reference score rows; color retention is strong, component-style retention is useful but not uniformly implementation-grade.
