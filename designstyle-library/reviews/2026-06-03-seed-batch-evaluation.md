# Seed Batch Evaluation

Created: 2026-06-03

## Scope

Seeded 10 reusable designstyle references:

- Stripe: product-led fintech/platform energy.
- Linear: quiet professional operational SaaS.
- Vercel: monochrome developer-platform rigor.
- Apple Vision Pro: cinematic product storytelling.
- Figma: collaborative creative-tool warmth.
- Framer: creator-tool template and motion language.
- Notion: warm modular productivity.
- A24: editorial cinematic culture/commerce.
- Teenage Engineering: object-led industrial ecommerce.
- Read.cv: quiet community/profile portfolio.

This seed set is intentionally broad, not an objective ranking. It gives `use-designstyle` a starting vocabulary across operational UI, cinematic narrative, developer platforms, creative collaboration, commerce, and community profiles.

## Per-Reference Self-Review Check

Each reference includes:

- `When To Use` and `When Not To Use`.
- `Visual System` with layout, typography, color, density, shape, and depth.
- `Assets` with image, illustration/icon, texture, and likely production method.
- `Motion` with transitions, micro-interactions, scroll behavior, and timing.
- `Interaction And Components`.
- `Code Evidence`, separating observed code/source clues from implementation inference and evidence limits.
- `Implementation Notes`.
- `Borrow` and `Avoid Copying`.
- `Self Review` with evidence quality, reuse value, missing pieces, and revision made.

No seeded reference should be treated as a pixel-copy source. The useful unit is a transferable decision: density, hierarchy, asset strategy, motion purpose, or component/state behavior.

## Retrieval Evaluation

Test queries after seeding:

- `dashboard quiet professional motion` returned Linear first.
- `cinematic AVG atmosphere film narrative` returned Apple Vision Pro and A24 first.
- `community profile portfolio social` returned Read.cv first.
- `hardware ecommerce object product grid` returned Teenage Engineering first.
- `developer platform technical monochrome` returned Vercel first.
- `warm productivity AI workspace docs` returned Notion first.

Initial issue: simple body word counts over-weighted generic words such as `product`, `motion`, and `storytelling`. This made some broad references rank too high for specific design intents.

Iteration made: `use-designstyle/scripts/search_references.py` now weights `tags`, `best_for`, and `title` above body text, and subtracts matches in `avoid_for`. This improved scene-fit retrieval without adding a complex indexing dependency.

## Skill Iteration Made

`add-designstyle` was tightened to require:

- Explicit code-level evidence when available: CSS variables, fonts, layout primitives, animation libraries, framework/runtime hints, asset CDN patterns, and public component clues.
- Separation between observed facts and inference.
- A batch evaluation note for future multi-reference additions.

`use-designstyle` was tightened to require:

- Reference-to-decision mapping.
- Explicit translation from product scene, audience trust need, content shape, interaction frequency, and technical constraints into design choices.
- Clear distinction between implementation-grade evidence and loose inspiration.

## Known Evidence Limits

Local screenshot capture was attempted but not completed because the local Playwright browser binary is missing. The references therefore rely on public page access, public brand/product language, prior visible design knowledge, and lightweight URL verification where available. Any future high-fidelity addition should capture screenshots after installing the browser binary or using another visual capture path.

## Outcome

The seed set is usable for future frontend work. It should help avoid generic AI-flavored pages by forcing scene-fit, asset realism, motion purpose, and component-state thinking before implementation.

Second iteration after completion audit: the seeded references were updated to include explicit `Code Evidence` sections. Stronger public-source evidence was recorded for Stripe, Linear, and Vercel; weaker evidence limits were explicitly marked for entries where no reliable source/render capture was completed. This keeps code-level decomposition honest instead of substituting aesthetic inference for observed implementation detail.
