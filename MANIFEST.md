# Manifest

Version: v0.2.8-progressive-motion-apply-pack
Date: 2026-06-12

## Skills

- `skills/designstyle`
- `skills/add-designstyle`
- `skills/use-designstyle`

## Library Contents

- `designstyle-library/references`: 95 active Markdown references.
- `designstyle-library/references-excluded`: 10 excluded references preserved outside active retrieval.
- `designstyle-library/screenshots`: 95 active desktop evidence screenshots, one per active reference.
- `designstyle-library/screenshots-excluded`: 10 excluded screenshots preserved as exclusion evidence.
- `designstyle-library/assets`: 95 retained component-style JSON evidence files. Raw DOM snapshots are not stored in the default library.
- `designstyle-library/assets-excluded`: 12 excluded evidence captures preserved outside active retrieval, including 9 component-style JSON files and 3 blocked Arc Browser raw/challenge artifacts.
- `designstyle-library/reviews`: candidate reviews, batch reports, capture evidence JSON, scoring reports, motion code probe JSON.
- `designstyle-library/indexes`: manual indexes plus generated `manifest.json`, `facets.json`, and 95 L1 card JSON files.
- `designstyle-library/indexes/cards-excluded`: 9 excluded L1 cards.
- `designstyle-library/dimensions`: 665 L2 dimension summaries, 7 per active reference.
- `designstyle-library/dimensions-excluded`: 63 excluded L2 dimension summaries.
- `designstyle-library/design-systems`: 95 retained design-system packs, 1 per active reference, each with `tokens.json`, `palette.md`, `moodboard.svg`, `component-styles.md`, `motion.json`, `variables.css`, `tailwind.theme.json`, and `motion-presets.css`.
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
- Structured motion: `add-designstyle` now writes `motion.json` with selector role, trigger, property, duration, delay, easing, description, source, reduced-motion status, and missing markers instead of copying old CSS walls. Reusable `items` are complete-only; incomplete parsed evidence is retained under `omitted_incomplete` with `missing_fields`.
- Recapture sample: 14 of 16 recaptured references have reusable motion items with complete required fields and no active noise/truncation; Bauhaus and Hex remain explicit gaps.
- Apply Pack generation: every active design-system pack now includes `variables.css`, `tailwind.theme.json`, and `motion-presets.css` derived from the evidence/apply token layer.
- Style DNA: L1 cards include measurable DNA decisions for retrieval and comparison; unresolved values remain explicit rather than inferred.
- Use-side comparison: `compare_against_reference.py` writes an Apply Pack section, screenshot evidence paths, DNA checklist, and iteration log for generated-vs-reference review.
- Quality baseline restored: the 2026-06-12 final quality score average is 91.6/100, above the historical 91.3 target, after real low-score recapture, L3 backfill, and generated-layer backfill.
- Search regression: `run_search_regression.py` covers 15 structured queries, including motion-term cross-scene pollution cases; current result is 15/15 top3 hits and wrong top1 = 0.
- Blind E2E evidence: `run_blind_e2e.py` covers dashboard, luxury landing, and docs-site scenes; each case writes a direction plan, copied Apply Pack, generated fixture screenshots for immediate-load/post-animation/hover/mobile/reduced-motion, comparison report, aesthetic probe score, DNA checklist, and iteration log.

## Verification

Validated locally for this v0.2.8 snapshot:

- `python3 -m unittest skills.add-designstyle.tests.test_progressive_library -q`: 40 tests passed.
- `python3 -m py_compile skills/add-designstyle/scripts/*.py skills/use-designstyle/scripts/*.py`: passed.
- `backfill_progressive_library.py --library designstyle-library`: 95 planned, status ok, partial 0.
- `validate_progressive_library.py --library designstyle-library --json`: valid true, 95 cards, 0 invalid, 0 errors.
- `clean_reference_noise.py --library designstyle-library --check`: passed with no active truncated CSS, autofill/consent/cookie/captcha noise, or abnormal scientific-notation `px` values.
- `score_reference_quality.py --library designstyle-library --json-output designstyle-library/reviews/2026-06-12-final2-design-system-quality-scores.json --markdown-output designstyle-library/reviews/2026-06-12-final2-design-system-quality-scores.md`: 95 references, average 91.6, median 92, range 67-100, blocked/security 0, scientific-notation px 0.
- Recaptured motion sample audit: 16 sampled references, 14 with reusable complete motion items, 0 active noise/truncation in reusable items; Bauhaus and Hex preserve incomplete/missing motion evidence without fabricated values.
- Blank Vite/Tailwind Apply Pack smoke at `/tmp/designstyle-vite-tailwind-smoke.toJQNv`: imported Plausible's generated `variables.css` and `motion-presets.css`, loaded generated `tailwind.theme.json` from `tailwind.config.cjs`, and `npm run build` passed with `tailwind-theme-ok 12` plus Vite production assets.
- `search_references.py "dashboard analytics table components hover transition" --library designstyle-library --need "motion:L2,palette:dark,scene:dashboard" --matrix --explain-selection`: dashboard references ranked first and output borrowable/not-borrowable dimensions.
- `run_search_regression.py --library designstyle-library --json-output designstyle-library/reviews/2026-06-12-final2-search-regression.json`: 15 queries, top3 rate 1.0, wrong top1 0, passed true.
- `run_blind_e2e.py --library designstyle-library --output-dir designstyle-library/reviews/2026-06-12-final2-blind-e2e`: 3 cases passed; dashboard selected Plausible (probe 84), luxury selected Bentley (probe 78), docs selected Vercel (probe 84), each with DNA pass rate 1.0, motion traceability true, and five required QA screenshots.
- `compare_against_reference.py --library designstyle-library --card designstyle-library/indexes/cards/plausible-analytics-live-dashboard.json --generated designstyle-library/screenshots/plausible-analytics-live-dashboard-desktop.png --state first-viewport --output /tmp/designstyle-compare-smoke.md`: generated comparison report with screenshot evidence, Apply Pack paths, DNA checklist, and iteration log.
- `validate_references.py --library designstyle-library --json`: 95 total L3 references, 95 valid, 0 invalid under the stricter L3 validator.
- Blocked-page scan: Cloudflare/security challenge-page signatures are absent from active references, retained component JSON, active design-system artifacts, and active dimensions.
- Raw/reference/design-system noise scan: truncated CSS walls, autofill/consent/cookie/captcha style noise, and abnormal scientific-notation `px` values are not present in active retained artifacts.
