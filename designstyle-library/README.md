# Designstyle Library

Local aesthetic reference library used by `add-designstyle` and `use-designstyle`. The library path is configurable via `DESIGNSTYLE_LIBRARY`; if unset, it defaults to `~/.codex/designstyle-library`.

- `references/`: one active Markdown style reference per website or design source.
- `references-excluded/`: blocked, rejected, or otherwise excluded captures preserved outside active retrieval.
- `screenshots/`: optional screenshots captured during analysis.
- `assets/`: retained component style JSON and intentional lightweight assets. Raw DOM snapshots are not stored in the default library; recapture the source URL on demand when L0-L3 evidence is insufficient.
- `assets-excluded/`: blocked/challenge or rejected component evidence preserved outside active retrieval.
- `reviews/`: self-review notes and iteration records.
- `indexes/`: generated or manual index files for retrieval.
- `indexes/cards/`: L1 progressive cards for fast ranking.
- `indexes/cards-excluded/`: excluded cards that must not participate in active retrieval.
- `dimensions/`: L2 summaries split by scene, layout/spacing, type/copy, color/surface, assets, motion/code, and components/states.
- `dimensions-excluded/`: excluded L2 summaries.
- `design-systems/`: per-reference design-system packs containing `tokens.json`, `palette.md`, `moodboard.svg`, `component-styles.md`, `motion.json`, `variables.css`, `tailwind.theme.json`, and `motion-presets.css`.
- `design-systems-excluded/`: excluded design-system packs.

Default rule: references capture reusable design decisions, not praise. Each entry should state when to use it, when not to use it, what to borrow, and what to avoid.

Progressive summaries are aids, not replacements. If a card or dimension summary marks evidence as missing, future use must keep that missing evidence explicit instead of inferring typography, spacing, copy, motion, or code details.

Active readiness is evaluated through both the L3 Markdown validator and the generated L1/L2/design-system validator. In the current 2026-06-12 worktree snapshot, the active library has 95 valid L3 references, 95 cards, 665 L2 dimension summaries, 95 component-style JSON files, 95 structured `motion.json` files, 95 design-system packs, and 285 generated Apply Pack files. `validate_references.py` and `validate_progressive_library.py` both pass for the active library.

Design-system packs retain exact color evidence from screenshot pixels and explicit DOM/reference colors, plus observed component style rules, structured motion evidence, and apply-layer tokens. Common CSS values such as `9999px` pill radii are preserved; abnormal browser-computed scientific-notation values, old truncated CSS walls, autofill/consent/cookie/captcha style noise, and third-party analytics/replay key shapes are filtered from active generated artifacts. Reusable `motion.json.items` are complete-only; incomplete parsed motion evidence stays visible under `omitted_incomplete` with explicit missing fields.

Implementation-grade component evidence must come from a real browser capture, not static HTML fallback. Cloudflare/security challenge pages are excluded from active references and do not count as reusable component systems; normal product copy or scripts that mention CAPTCHA/recaptcha are not blocked-page evidence by themselves.

Current status: `designstyle-library/reviews/2026-06-12-final2-design-system-quality-scores.md` scores the active generated layer at 91.6/100 average, above the historical 91.3 target. The score was raised through real low-score recapture, L3 backfill, and generated-layer backfill; missing source values remain explicit instead of being inferred. Use-side blind E2E evidence is saved under `reviews/2026-06-12-final2-blind-e2e/` for dashboard, luxury landing, and docs-site scenes.

Apply Pack compile smoke also passed in a blank Vite/Tailwind project at `/tmp/designstyle-vite-tailwind-smoke.toJQNv`: generated `variables.css` and `motion-presets.css` were imported by Vite, Plausible's generated `tailwind.theme.json` was loaded by `tailwind.config.cjs`, and `npm run build` exited 0.
