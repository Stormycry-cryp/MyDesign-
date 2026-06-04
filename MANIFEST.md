# Manifest

Version: v0.2.4
Date: 2026-06-04

## Skills

- `skills/designstyle`
- `skills/add-designstyle`
- `skills/use-designstyle`

## Library Contents

- `designstyle-library/references`: 76 active validated Markdown references.
- `designstyle-library/references-excluded/blocked`: 1 blocked reference excluded from active retrieval because the live page captured a Cloudflare/security challenge.
- `designstyle-library/screenshots`: 86 active desktop evidence screenshots and supporting visual captures.
- `designstyle-library/screenshots-excluded/blocked`: 1 blocked screenshot preserved as exclusion evidence.
- `designstyle-library/assets`: 207 active DOM/resource/component evidence captures.
- `designstyle-library/assets-excluded/blocked`: 3 blocked evidence captures preserved outside active retrieval.
- `designstyle-library/reviews`: candidate reviews, batch reports, capture evidence JSON, scoring reports, motion code probe JSON.
- `designstyle-library/indexes`: manual indexes plus generated `manifest.json`, `facets.json`, and 76 L1 card JSON files.
- `designstyle-library/dimensions`: 532 L2 dimension summaries, 7 per active reference.
- `designstyle-library/design-systems`: 76 retained design-system packs, 1 per active reference, each with `tokens.json`, `palette.md`, `moodboard.svg`, and `component-styles.md`.

## Highlights

- Progressive disclosure: L1 cards, L2 dimension summaries, L3 full references, and L4 raw evidence boundaries.
- Router skill: `designstyle` chooses add, use, or add-then-use and reports evidence layers read.
- Aesthetic gate: `add-designstyle` can reject visually ordinary candidates before they count as library references.
- Layered tags: `style_tags`, `structure_tags`, `motion_tags`, `code_tags`.
- Dimension/ratio preservation: viewport, document size, media ratios, spacing samples.
- Motion/code evidence: public CSS/JS probe keywords, motion snippets, exact motion parameters.
- Card-first retrieval: `use-designstyle` ranks by category, page scope, best_for, avoid_for penalties, then style/structure/motion/code evidence.
- Design-system retention: `add-designstyle` stores exact color palettes from screenshot pixels and explicit color evidence, moodboard SVGs, token JSON, and component style systems.
- Code/component retention: active references retain non-empty live-DOM computed component JSON with geometry, computed CSS, and hover/focus samples where observable.
- Blocked-page hygiene: Cloudflare/security challenge captures are excluded from active references and preserved under blocked evidence folders.
- Use-side retrieval: `use-designstyle` search can print design-system paths and excerpts with `--design-system`; `--matrix` shows retained design-system paths.
- Component hygiene: common CSS values such as `9999px` pill radii are preserved, while abnormal browser-computed scientific-notation values are filtered from raw JSON, references, dimensions, and generated design-system artifacts.

## Verification

Validated locally before release:

- `validate_references.py --library designstyle-library --json`: 76 total, 76 valid, 0 invalid.
- `clean_reference_noise.py --library designstyle-library --check`: no abnormal scientific-notation `px` values remain in active reference text artifacts.
- `score_reference_quality.py --library designstyle-library --markdown-output designstyle-library/reviews/2026-06-04-per-reference-design-system-quality-scores.md --json-output designstyle-library/reviews/2026-06-04-per-reference-design-system-quality-scores.json`: 76 references scored with per-dimension breakdown.
- `build_progressive_reference.py --library designstyle-library --all --dry-run`: 76 cards and 532 dimensions planned.
- `build_progressive_reference.py --library designstyle-library --all`: 76 cards and 532 dimensions written idempotently.
- `validate_progressive_library.py --library designstyle-library --json`: 76 cards, 0 invalid, 0 errors.
- `search_references.py "dashboard analytics color system table components" --library designstyle-library --matrix --design-system`: search output includes retained design-system paths, palette colors, and component style sections.
- Blocked-page scan: Cloudflare/security challenge-page signatures are absent from active references, active raw component JSON, active design-system artifacts, and active dimensions.
- Raw/reference/design-system noise scan: abnormal scientific-notation `px` values are not present in active retained artifacts.
- `designstyle-library/reviews/2026-06-04-per-reference-design-system-quality-scores.md`: per-reference design-system quality report with 76 active score rows, average 91.3/100, median 93.0/100, range 66-100, and explicit dimension-level point breakdown.
