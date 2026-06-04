# DesignStyle

Reusable Codex designstyle skills and reference library.

This repository packages:

- `skills/designstyle`: route ambiguous designstyle work to add, use, or add-then-use workflows.
- `skills/add-designstyle`: capture concrete websites/screens into high-resolution local style references.
- `skills/use-designstyle`: retrieve and compose references by design dimension before building UI.
- `designstyle-library`: reusable design references, screenshots, progressive cards, dimension summaries, evidence reviews, and indexes.

## Install

Copy the packaged folders into your Codex home:

```bash
rsync -a skills/designstyle ~/.codex/skills/
rsync -a skills/add-designstyle ~/.codex/skills/
rsync -a skills/use-designstyle ~/.codex/skills/
rsync -a designstyle-library/ ~/.codex/designstyle-library/
```

## Current Library

The library includes 77 validated UI references. Each reference preserves layered tags, first-viewport geometry, dimension ratios, typography, color/material source, asset direction, interaction states, motion/code evidence, and explicit evidence limits.

The 2026-06-04 update adds a dashboard and information-display UI batch covering CRM workspaces, analytics dashboards, data platforms, developer platforms, observability tools, productivity interfaces, and data-storytelling references.

The progressive-disclosure layer lets `use-designstyle` search lightweight L1 cards first, read only needed L2 dimension summaries, and open L3 full references only when implementation-grade detail is needed:

- `designstyle-library/indexes/cards/*.json`: compact retrieval cards with evidence strength and missing-evidence limits.
- `designstyle-library/dimensions/<slug>/*.md`: scene, layout/spacing, type/copy, color/surface, assets, motion/code, and components/states summaries.
- `designstyle-library/references/*.md`: full evidence records.

## Motion Evidence Boundary

The references intentionally do not store full proprietary CSS/JS. They keep resource URLs, short motion-relevant snippets, exact useful motion parameters, and implementation interpretation. This keeps references useful without turning the library into copied source.

## Verify

```bash
python3 skills/add-designstyle/scripts/validate_references.py --library designstyle-library --json
python3 skills/add-designstyle/scripts/build_progressive_reference.py --library designstyle-library --all --dry-run
python3 skills/add-designstyle/scripts/validate_progressive_library.py --library designstyle-library --json
python3 skills/use-designstyle/scripts/search_references.py "hardware product minimal wearable landing page" --library designstyle-library --explain-selection
```
