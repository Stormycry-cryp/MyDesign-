# DesignStyle

Reusable Codex designstyle skills and reference library.

This repository packages:

- `skills/add-designstyle`: capture concrete websites/screens into high-resolution local style references.
- `skills/use-designstyle`: retrieve and compose references by design dimension before building UI.
- `designstyle-library`: reusable design references, screenshots, evidence reviews, and indexes.

## Install

Copy the packaged folders into your Codex home:

```bash
rsync -a skills/add-designstyle ~/.codex/skills/
rsync -a skills/use-designstyle ~/.codex/skills/
rsync -a designstyle-library/ ~/.codex/designstyle-library/
```

## Current Library

The library includes the original seed references plus a 2026-06-03 beauty/skincare cold-start batch. Newer references preserve layered tags, first-viewport geometry, dimension ratios, typography, color/material source, asset direction, interaction states, and motion/code evidence.

## Motion Evidence Boundary

The references intentionally do not store full proprietary CSS/JS. They keep resource URLs, short motion-relevant snippets, exact useful motion parameters, and implementation interpretation. This keeps references useful without turning the library into copied source.
