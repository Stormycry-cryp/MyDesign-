# DesignStyle

Reusable Codex designstyle skills and reference library.

This repository packages:

- `skills/designstyle`: route ambiguous designstyle work to add, use, or add-then-use workflows.
- `skills/add-designstyle`: capture concrete websites/screens into high-resolution local style references.
- `skills/use-designstyle`: retrieve and compose references by design dimension before building UI.
- `designstyle-library`: reusable design references, screenshots, progressive cards, dimension summaries, retained design-system packs, evidence reviews, and indexes.

## Install

Copy the packaged folders into your Codex home:

```bash
rsync -a skills/designstyle ~/.codex/skills/
rsync -a skills/add-designstyle ~/.codex/skills/
rsync -a skills/use-designstyle ~/.codex/skills/
rsync -a designstyle-library/ ~/.codex/designstyle-library/
```

## Current Library

The library includes 92 active UI references. Each reference preserves layered tags, first-viewport geometry, dimension ratios, typography, color/material source, retained color systems, component style systems, asset direction, interaction states, motion/code evidence, and explicit evidence limits. Nine excluded references are preserved outside active retrieval; they do not count toward active search, progressive validation, or design-system reuse.

The 2026-06-04 update adds a dashboard and information-display UI batch covering CRM workspaces, analytics dashboards, data platforms, developer platforms, observability tools, productivity interfaces, and data-storytelling references.

The 2026-06-05 library update adds 15 luxury official-site references covering automotive, fashion, jewelry, and watch brand systems, while preserving 9 rejected/blocked luxury candidates under excluded evidence folders.

The 2026-06-08 skill update turns Add and Use into a stricter evidence loop:

- `designstyle` requires routed child skills to report scene/page fit, required dimensions, missing evidence, reuse boundary, and next handoff.
- `add-designstyle` adds a Use-readiness gate so a reference is only active usable when L1/L2/L3, design-system artifacts, visual evidence, best/avoid use, required dimensions, and progressive validation are explicit.
- `use-designstyle` classifies coverage as strong, partial, or weak and emits an Add-Designstyle Backlog for partial/weak coverage.
- `search_references.py --explain-selection` now reports selected reasons, rejected reasons, category/page fit, and coverage hints so motion/code terms cannot bypass scene fit.

The progressive-disclosure layer lets `use-designstyle` search lightweight L1 cards first, read only needed L2 dimension summaries, and open L3 full references only when implementation-grade detail is needed:

- `designstyle-library/indexes/cards/*.json`: compact retrieval cards with evidence strength and missing-evidence limits.
- `designstyle-library/dimensions/<slug>/*.md`: scene, layout/spacing, type/copy, color/surface, assets, motion/code, and components/states summaries.
- `designstyle-library/design-systems/<slug>/`: per-reference `tokens.json`, `palette.md`, `moodboard.svg`, and `component-styles.md` for exact palette and reusable component-style retention.
- `designstyle-library/assets/*-component-styles.json`: retained component evidence with geometry, computed CSS, and hover/focus samples where observable. Raw DOM snapshots are not stored in the default library; L4 DOM inspection is recaptured from the source URL only when L0-L3 evidence is insufficient.
- `designstyle-library/references-excluded/blocked/`: blocked/challenge captures preserved outside active retrieval.
- `designstyle-library/references/*.md`: full evidence records.

## Design-System Retention

The 2026-06-04 design-system update promotes color reference from a loose color note into retained system artifacts. `add-designstyle` now generates a design-system pack for every active reference, using screenshot pixel samples and explicit DOM/reference color values for palettes. Component style evidence is extracted from live browser computed styles plus observed reference sections; common CSS values such as `9999px` pill radii are preserved, while abnormal browser-computed scientific-notation values are filtered from raw JSON and generated artifacts.

Code/component captures use Playwright with real Chrome rendering so references can retain `getComputedStyle`, geometry, and hover/focus evidence in structured component JSON. Static HTML fallback or Cloudflare/security challenge pages do not count as implementation-grade component evidence. Raw DOM belongs in external temp storage during capture and should not be committed.

`use-designstyle` can surface these artifacts directly:

```bash
python3 skills/use-designstyle/scripts/search_references.py "dashboard analytics color system table components" --library designstyle-library --matrix --design-system
```

The current per-reference design-system score report is saved at `designstyle-library/reviews/2026-06-04-per-reference-design-system-quality-scores.md`: it covers the pre-luxury 76-reference baseline, average 91.3/100, median 93.0/100, range 66-100, with 0 active blocked/challenge contamination and 0 active scientific-notation px noise. A clean-context independent sub-agent scored that state before the final text-noise cleanup at 88/100 and identified the remaining L2/L3 radius noise; that text layer was cleaned before v0.2.4 release. A fresh 92-reference quality score report has not been regenerated yet.

The v0.2.6 `use-designstyle` update adds upfront HITL and plan-led iteration. Before build work, the skill now collects style anchors, forbidden drift directions, motion richness level, asset boundaries, deliverable format, and required QA states. The direction plan is treated as an execution contract with a stepwise build plan, iteration log, and final QA checklist, so agents can build without repeatedly interrupting the user unless a hard blocker appears.

The v0.2.7 packaged library keeps 92 active screenshots, 92 component-style JSON files, and 92 design-system packs. The default `designstyle-library` is 135M after merging the 2026-06-05 luxury batch with the remote `bunkhouse` reference and excluded evidence preservation; raw DOM is still external/on-demand L4 evidence.

## Motion Evidence Boundary

The references intentionally do not store full proprietary CSS/JS. They keep resource URLs, short motion-relevant snippets, exact useful motion parameters, and implementation interpretation. This keeps references useful without turning the library into copied source.

## Verify

```bash
python3 skills/add-designstyle/scripts/validate_references.py --library designstyle-library --json
python3 skills/add-designstyle/scripts/clean_reference_noise.py --library designstyle-library --check
python3 skills/add-designstyle/scripts/score_reference_quality.py --library designstyle-library --markdown-output designstyle-library/reviews/2026-06-04-per-reference-design-system-quality-scores.md --json-output designstyle-library/reviews/2026-06-04-per-reference-design-system-quality-scores.json
python3 skills/add-designstyle/scripts/build_progressive_reference.py --library designstyle-library --all --dry-run
python3 skills/add-designstyle/scripts/validate_progressive_library.py --library designstyle-library --json
python3 skills/use-designstyle/scripts/search_references.py "dashboard analytics color system table components" --library designstyle-library --matrix --design-system
```

Note: `validate_references.py` is intentionally stricter in v0.2.7. Existing L3 references fail until they are backfilled with the new `Reference Text And Copy Grammar` and `Style Tokens And Surface Grammar` sections. `validate_progressive_library.py` is the active readiness check for the generated L1/L2/design-system layer.
