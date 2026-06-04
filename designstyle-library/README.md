# Designstyle Library

Local aesthetic reference library used by `add-designstyle` and `use-designstyle`.

- `references/`: one active Markdown style reference per website or design source.
- `references-excluded/blocked/`: blocked/challenge captures preserved outside active retrieval.
- `screenshots/`: optional screenshots captured during analysis.
- `assets/`: retained component style JSON and intentional lightweight assets. Raw DOM snapshots are not stored in the default library; recapture the source URL on demand when L0-L3 evidence is insufficient.
- `assets-excluded/blocked/`: blocked/challenge DOM or component evidence preserved outside active retrieval.
- `reviews/`: self-review notes and iteration records.
- `indexes/`: generated or manual index files for retrieval.
- `indexes/cards/`: L1 progressive cards for fast ranking.
- `dimensions/`: L2 summaries split by scene, layout/spacing, type/copy, color/surface, assets, motion/code, and components/states.
- `design-systems/`: per-reference design-system packs containing `tokens.json`, `palette.md`, `moodboard.svg`, and `component-styles.md`.

Default rule: references capture reusable design decisions, not praise. Each entry should state when to use it, when not to use it, what to borrow, and what to avoid.

Progressive summaries are aids, not replacements. If a card or dimension summary marks evidence as missing, future use must keep that missing evidence explicit instead of inferring typography, spacing, copy, motion, or code details.

Design-system packs retain exact color evidence from screenshot pixels and explicit DOM/reference colors, plus observed component style rules. Common CSS values such as `9999px` pill radii are preserved; abnormal browser-computed scientific-notation values are filtered.

Implementation-grade component evidence must come from a real browser capture, not static HTML fallback. Cloudflare/security challenge pages are excluded from active references and do not count as reusable component systems; normal product copy or scripts that mention CAPTCHA/recaptcha are not blocked-page evidence by themselves.
