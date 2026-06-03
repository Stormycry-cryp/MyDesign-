# Manifest

Version: v0.1.0
Date: 2026-06-03

## Skills

- `skills/add-designstyle`
- `skills/use-designstyle`

## Library Contents

- `designstyle-library/references`: 20 Markdown references.
- `designstyle-library/screenshots`: 10 beauty/skincare evidence screenshots.
- `designstyle-library/reviews`: seed review, beauty batch review, capture evidence JSON, motion code probe JSON.
- `designstyle-library/indexes`: seed and beauty indexes.

## Highlights

- Layered tags: `style_tags`, `structure_tags`, `motion_tags`, `code_tags`.
- Dimension/ratio preservation: viewport, document size, media ratios, spacing samples.
- Motion/code evidence: public CSS/JS probe keywords, motion snippets, exact motion parameters.
- Multi-reference retrieval: `use-designstyle` can compose scene/style, structure/ratio, type/color, assets, and motion/code references.

## Verification

Validated locally before release:

- Formal skill scripts parsed successfully with Python AST.
- Ten beauty/skincare references passed the strict schema validator.
- Formal `use-designstyle` search returned dimension leaders and exact motion parameters.
