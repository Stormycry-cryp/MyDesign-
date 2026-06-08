# Manifest

Version: v0.2.7
Date: 2026-06-08

## Skills

- `skills/designstyle`
- `skills/add-designstyle`
- `skills/use-designstyle`

## Library Contents

- `designstyle-library/references`: 92 active Markdown references.
- `designstyle-library/references-excluded`: 9 excluded references preserved outside active retrieval.
- `designstyle-library/screenshots`: 92 active desktop evidence screenshots, one per active reference.
- `designstyle-library/screenshots-excluded`: 9 excluded screenshots preserved as exclusion evidence.
- `designstyle-library/assets`: 92 retained component-style JSON evidence files. Raw DOM snapshots are not stored in the default library.
- `designstyle-library/assets-excluded`: 12 excluded evidence captures preserved outside active retrieval, including 9 component-style JSON files and 3 blocked Arc Browser raw/challenge artifacts.
- `designstyle-library/reviews`: candidate reviews, batch reports, capture evidence JSON, scoring reports, motion code probe JSON.
- `designstyle-library/indexes`: manual indexes plus generated `manifest.json`, `facets.json`, and 92 L1 card JSON files.
- `designstyle-library/indexes/cards-excluded`: 9 excluded L1 cards.
- `designstyle-library/dimensions`: 644 L2 dimension summaries, 7 per active reference.
- `designstyle-library/dimensions-excluded`: 63 excluded L2 dimension summaries.
- `designstyle-library/design-systems`: 92 retained design-system packs, 1 per active reference, each with `tokens.json`, `palette.md`, `moodboard.svg`, and `component-styles.md`.
- `designstyle-library/design-systems-excluded`: 9 excluded design-system packs.

## Highlights

- `use-designstyle` now requires an upfront HITL gate before build work when user-provided assets, premium visual direction, or rich motion are involved. The gate collects style anchors, forbidden drift directions, motion richness level, asset boundaries, deliverable format, and required QA states.
- `use-designstyle` now treats `work/designstyle-direction-plan.md` as an execution contract with upfront assumptions, a stepwise build plan, an iteration log, and a final QA checklist.
- Build flow is now plan-led: agents should update the plan after each step and avoid repeatedly asking the user for confirmation during build unless a hard blocker appears.
- Use-side QA now explicitly covers hover/focus states, immediate-load first viewport, post-animation state, mobile sections, reduced motion, and asset usage against the confirmed plan.
- Progressive disclosure: L1 cards, L2 dimension summaries, L3 full references, and L4 on-demand evidence boundaries.
- Router skill: `designstyle` chooses add, use, or add-then-use and reports evidence layers read.
- Shared evidence contract: `designstyle` now requires routed child skills to report scene/page fit, required dimensions, missing evidence, reuse boundary, and next handoff.
- Aesthetic gate: `add-designstyle` can reject visually ordinary candidates before they count as library references.
- Use-readiness gate: `add-designstyle` now marks whether a reference is active usable, partial, or blocked, with best/avoid use, strong dimensions, weak/missing dimensions, suggested Use roles, and validator result.
- Layered tags: `style_tags`, `structure_tags`, `motion_tags`, `code_tags`.
- Dimension/ratio preservation: viewport, document size, media ratios, spacing samples.
- Motion/code evidence: public CSS/JS probe keywords, motion snippets, exact motion parameters.
- Card-first retrieval: `use-designstyle` ranks by category, page scope, best_for, avoid_for penalties, then style/structure/motion/code evidence.
- Coverage/backlog loop: `use-designstyle` classifies coverage as strong, partial, or weak; partial/weak coverage must produce an Add-Designstyle Backlog.
- Search explainability: `search_references.py --explain-selection` reports selected reason, rejected reason, category/page fit, evidence strength, missing evidence, and coverage hints.
- Design-system retention: `add-designstyle` stores exact color palettes from screenshot pixels and explicit color evidence, moodboard SVGs, token JSON, and component style systems.
- Code/component retention: active references retain non-empty computed component JSON with geometry, computed CSS, and hover/focus samples where observable.
- Blocked-page hygiene: Cloudflare/security challenge captures are excluded from active references and preserved under blocked evidence folders.
- Use-side retrieval: `use-designstyle` search can print design-system paths and excerpts with `--design-system`; `--matrix` shows retained design-system paths.
- Component hygiene: common CSS values such as `9999px` pill radii are preserved, while abnormal browser-computed scientific-notation values are filtered from raw JSON, references, dimensions, and generated design-system artifacts.
- Raw-evidence hygiene: raw DOM is captured only to external temp storage during add/refresh workflows; it is recaptured from the source URL when L0-L3 plus retained screenshots/component JSON are insufficient.

## Verification

Validated locally before release:

- `python3 -m unittest test_progressive_library.py`: 12 tests passed.
- `build_progressive_reference.py --library designstyle-library --all`: 92 cards and 644 dimensions written.
- `validate_progressive_library.py --library designstyle-library --json`: 92 cards, 0 invalid, 0 errors.
- `clean_reference_noise.py --library designstyle-library --check`: no abnormal scientific-notation `px` values remain in active reference text artifacts.
- `search_references.py "skincare product detail clinical formula product grid" --library designstyle-library --matrix --explain-selection`: search output includes selected reasons, rejected reasons, category/page fit, coverage hints, dimension paths, and design-system paths.
- `validate_references.py --library designstyle-library --json`: 92 invalid under the new stricter L3 reference validator because historical references do not yet contain the new `Reference Text And Copy Grammar` and `Style Tokens And Surface Grammar` sections. The L1/L2/design-system derived layers are valid; L3 backfill remains a known follow-up.
- Blocked-page scan: Cloudflare/security challenge-page signatures are absent from active references, retained component JSON, active design-system artifacts, and active dimensions.
- Raw/reference/design-system noise scan: abnormal scientific-notation `px` values are not present in active retained artifacts.
- `designstyle-library/reviews/2026-06-04-per-reference-design-system-quality-scores.md`: historical per-reference design-system quality report for the pre-luxury baseline; a fresh 92-reference score report has not been regenerated.
