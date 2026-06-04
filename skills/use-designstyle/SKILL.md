---
name: use-designstyle
description: Use when designing or redesigning a webpage, app screen, landing page, prototype, visual system, or frontend UI and the work should draw from the local designstyle reference library.
---

# Use Designstyle

Use local references to preserve transferable design decisions, not to borrow mood words. A good use of references composes multiple evidence dimensions into implementation choices: scene fit, geometry, dimension ratios, typography roles, reference text grammar, style tokens, spacing rhythm, palette source, asset plan, motion logic, motion code evidence, component states, and anti-copy boundaries.

## Progressive Evidence Layers

Default to progressive disclosure:

- L1 cards: read `~/.codex/designstyle-library/indexes/cards/*.json` first for candidate ranking, evidence strength, and missing evidence.
- L2 dimensions: read only the needed `dimensions/<slug>/*.md` summaries for scene, layout/spacing, type/copy, color/surface, assets, motion/code, or components/states.
- Design systems: read `design-systems/<slug>/tokens.json`, `palette.md`, `moodboard.svg`, and `component-styles.md` when the task needs color systems, moodboards, component styling, or token-level reuse.
- Retained component systems: when implementation-grade component styling is needed, check the linked `assets/YYYY-MM-DD-<slug>-component-styles.json` evidence from the full reference or tokens before trusting a summarized component rule. Use exact computed styles for density, radius, border, shadow, padding, typography, and hover/focus deltas; keep missing states explicit.
- L3 full references: read `references/*.md` only when the L2 summary is insufficient, contradictory, contaminated, or implementation-grade detail is required.
- L4 on-demand evidence: retained screenshots and component-style JSON are checked only when visual/code evidence needs verification. Raw DOM is not kept in the default library; if L0-L3 plus retained components are insufficient, recapture the source URL into an external temp location and extract only the needed facts.

Do not jump straight to full references unless the task needs L3/L4 evidence. Do not claim typography, spacing, copy, motion, or code evidence exists if L1/L2 marks it missing.

## Library

Default location:

```text
~/.codex/designstyle-library/
```

If the library is empty or weak for the product scene, say so and either re-query or ask to run `add-designstyle`.

## Library Coverage Checks

Before using references for a design task, check whether the library covers the requested scene:

- Count candidate matches by `category_tags`, `page_scope`, `best_for`, and `avoid_for`, not only by style words.
- Prefer references with screenshots, page scope, code surface, motion evidence, and self-review. Demote references with explicit evidence limits.
- Prefer references that preserve reference text samples, style token grammar, and measured spacing/gap evidence when the target task asks for a complete visual system rather than mood only.
- Prefer references with retained design-system artifacts when the target task needs color palette, moodboard, component styling, or reusable tokens. Do not use a color mood adjective when exact palette evidence is available.
- If a category is underrepresented, say what is missing and run a narrower query. If the result is still weak, state that the library lacks implementation-grade references for that scene.
- For large or mixed libraries, use references by role: scene, structure, type/color, asset, motion/code, and component states. Do not let a high-scoring but wrong-category entry dominate.
- Treat page/category fit as the retrieval gate. Generic motion/code words such as `transition`, `hover`, `scroll`, `animation`, or `css` must not let an unrelated gallery, portfolio, or editorial page outrank a same-scene pricing/product/dashboard reference. Use motion/code evidence only after scene, page scope, and category fit are plausible.

## Workflow

1. **Understand The Design Need**
   - Product category and commerce/workflow context.
   - Page type and scope: homepage, product detail, pricing, docs, dashboard, portfolio, article, checkout, app screen, campaign, gallery, or listing.
   - User frequency: repeated task, one-time browsing, campaign launch, product inspection.
   - Desired feeling: name concrete mechanics, not just adjectives.
   - Content shape: narrative, product catalog, formula proof, media, forms, diagnostic flow.
   - Technical constraints: framework, devices, accessibility, performance, assets.
   - Required evidence level: visual-only mood, layout guidance, or implementation-grade motion/code guidance.

2. **Retrieve Candidate References By Dimension**
   Search with product scene plus mechanics:

   ```bash
   python ~/.codex/skills/use-designstyle/scripts/search_references.py "skincare clinical minimal formula product grid swiper transition" --matrix --explain-selection
   python ~/.codex/skills/use-designstyle/scripts/search_references.py "skincare clinical minimal formula product grid" --dimension type-copy
   python ~/.codex/skills/use-designstyle/scripts/search_references.py "dashboard analytics color system table components" --dimension color-surface --full
   ```

   Use 2-5 references maximum, selected by role rather than winner-takes-all ranking:
   - Scene/style reference: product category, audience, trust problem, tone.
   - Structure/ratio reference: first viewport geometry, page grid, media/product-card proportions.
   - Type/color reference: typography roles, color/material system, contrast.
   - Design-system reference: exact palette roles, moodboard, component style rules, and token evidence from `design-systems/<slug>/`.
   - Component-code reference: retained computed component samples from `assets/*-component-styles.json` when available.
   - Text grammar reference: H1/H2/eyebrow/CTA/body/meta copy rhythm, claim density, naming style, and tone mechanics.
   - Style/spacing reference: surface system, borders/radii/shadows, control density, header/hero/section gaps, grid gutters, card padding, and mobile compression.
   - Asset reference: photography/video/material production plan.
   - Motion/code reference: transition, animation, keyframes, exact duration/easing/transform parameters, runtime library, reduced-motion strategy.
   - Component/state reference: navigation, cards, forms, drawers, search, menus, pricing tables, dashboard tables, galleries, or feedback states.

   STOP: If top L1 cards are generic, contradictory, contaminated, or unrelated, re-query or say the library lacks a good match. Do not force a SaaS or culture reference onto beauty, retail, spa, or product pages just because tags include `product` or `motion`.
   STOP: If a result ranks mainly because of generic motion/code snippets while `category_tags`, `page_scope`, and `best_for` do not match the task, demote it manually and re-query with stronger scene/page terms.

3. **Build A Reference Element Matrix**
   Do not copy one reference wholesale. Make a matrix:
   - Requirement dimension.
   - Selected reference.
   - Category/page fit.
   - Evidence strength: screenshot/DOM/CSS/JS strong, runtime inference medium, visual-only weak.
   - Extracted element: the specific decision to borrow.
   - Adaptation rule: how it changes for the user's product/content/assets.
   - Anti-copy limit: what must not be copied.
   Include rows for reference text grammar and style/spacing whenever the output is a webpage, landing page, app screen, or visual system.

4. **Map Evidence To Requirements**
   For each selected reference, extract:
   - First viewport geometry: bars/header/nav/logo/hero/copy/CTA/next-section visibility.
   - Page scope and secondary pages inspected: whether the reference covers the same page type or only a neighboring one.
   - Dimension ratios: viewport, hero min-height, split ratios, product/media card ratios, header/drawer bounds.
   - Typography roles: display, UI, body, metadata, CTA, technical labels.
   - Reference text grammar: headline length and shape, eyebrow role, CTA verbs, claim density, technical vs editorial vocabulary, whether copy is terse, narrative, catalog-like, clinical, playful, or restrained.
   - Style tokens: background/surface layers, border/radius/shadow grammar, button/input density, icon stroke style, divider usage, hover/focus states.
   - Spacing rhythm: header height, hero top/bottom padding, section gaps, grid gutters, media margins, card padding, text measure, CTA spacing, mobile spacing compression.
   - Color source: shell palette vs asset-derived palette.
   - Design system: retained palette colors, color roles, moodboard direction, component style rules, source attribution, and missing evidence limits.
   - Asset plan: required photo/video/product/material quality.
   - Motion purpose: source video, reveal, drawer, hover, scroll, timing.
   - Motion code: CSS transition/animation/keyframes, exact duration/easing/delay/transform parameters, GSAP/Swiper/Slick/Owl/Framer evidence, `IntersectionObserver`, `requestAnimationFrame`, reduced-motion handling.
   - Code surface: CSS variables/tokens, layout primitives, framework/runtime hints, component naming clues, and media loading patterns.
   - Component grammar: nav, buttons, cards, forms, search, cart, overlays, feedback states.
   - Component raw evidence: computed component JSON sample path, sampled component categories, geometry, computed styles, and observed hover/focus deltas.
   - Implementation primitives: split hero, full-bleed media, product grid, sticky header, drawers, aspect ratios.
   - Community signal: why this reference was worth saving and what feedback theme it represents.
   - Evidence strength and contamination: screenshot/source/DOM strong, inference weak, cookie/region/modal ignored, and Cloudflare/security challenge pages excluded.
   - What not to copy: brand identity, proprietary assets, exact typefaces, product names, claims.

5. **Derive The Design Direction**
   Produce a compact direction before implementation:
   - Scene and audience:
   - Visual stance:
   - First viewport geometry:
   - Dimension/ratio system:
   - Type roles:
   - Reference text grammar:
   - Style tokens:
   - Spacing rhythm:
   - Color/material:
   - Asset production plan:
   - Motion/code plan:
   - Components/states:
   - Anti-patterns and anti-copy limits:
   - Reference element matrix:
   - Missing-reference warning:

6. **Apply During Build**
   Keep checking:
   - Does the UI match the product scene, not merely the color palette?
   - Are real assets or asset placeholders strong enough for the borrowed style?
   - Did you preserve macro geometry, ratios, and typography roles?
   - Are motion and transitions causal and backed by the chosen motion/code reference?
   - Are the selected references category-fit, page-fit, and evidence-fit?
   - Are text, spacing, contrast, responsive layout, and states robust?
   - Did you avoid copying protected brand identity and proprietary artwork?

7. **Final Design Audit**
   Before claiming completion, audit:
   - Which references were used and which exact dimensions were borrowed.
   - Which dimensions were intentionally not borrowed and why.
   - Whether screenshots/assets/text show the reference decisions in the final UI.
   - Interaction quality: hover, drawer/modal, loading/empty/error states.
   - Motion quality: purpose, timing, implementation technique, reduced-motion fallback.
   - Reference fit quality: scene, page scope, category diversity, evidence strength, and contamination.
   - Anti-patterns: generic gradients, decorative blobs, nested cards, stock filler, vague "premium" styling.

## Output Pattern

```markdown
## Selected References
- Evidence layers read: L1 cards -> L2 dimensions -> L3 full references if needed.
- <reference>: use for <specific dimension>; evidence strength <strong/medium/weak>.

## Reference Element Matrix
| Need | Reference | Category/Page Fit | Evidence | Borrow | Adapt | Do Not Copy |
|---|---|---|---|---|---|---|
| Scene/style |  |  |  |  |  |  |
| Structure/ratio |  |  |  |  |  |  |
| Type/color |  |  |  |  |  |  |
| Text grammar |  |  |  |  |  |  |
| Style/spacing |  |  |  |  |  |  |
| Assets |  |  |  |  |  |  |
| Motion/code |  |  |  |  |  |  |
| Components/states |  |  |  |  |  |  |

## Design Direction
- Scene:
- First viewport geometry:
- Dimension/ratio system:
- Type roles:
- Reference text grammar:
- Style tokens:
- Design system:
- Spacing rhythm:
- Color/material:
- Assets:
- Motion/code:
- Components/states:
- Anti-copy limits:
- Missing references:

## Do Not Do
- ...

## Build Checks
- ...
```

## Failure Handling

| Trigger | First response | Fallback |
|---|---|---|
| Library lacks scene-fit references | Say so and run/add references first | Use general design judgment with uncertainty |
| Search returns generic matches | Re-query with scene + mechanics | Manually inspect fewer references |
| Search returns wrong-category matches | Re-query with category/page scope and `avoid_for` terms | State the gap and use only weak inspiration |
| References conflict | Pick one primary and demote others by dimension | Do not blend incompatible aesthetics |
| One reference fits style but not layout/motion | Keep it only for the fitting dimension | Select separate structure or motion references |
| Assets are missing | Define an asset plan before layout polish | Use stable placeholders only as temporary scaffolding |
| Reference has contamination | Ignore cookie/region/modal as aesthetic evidence; exclude Cloudflare/security challenge pages | Prefer clean screenshot or exclude reference |
| Motion/code evidence is weak | Use it only as motion intention | Do not copy exact timing or claim implementation backing |
| 50+ library has near-duplicates | Pick the most evidence-rich entry and one contrasting reference | Do not use five same-category references to justify one design |
| Implementation constraints conflict | Reduce media/motion first | Preserve hierarchy, typography roles, spacing, states |

## Do Not Do

- Do not copy a reference's brand identity, proprietary assets, exact layout, exact typefaces, or claims.
- Do not reduce references to adjectives like "luxury", "clean", "natural", or "premium".
- Do not use references with weak evidence as implementation-grade guidance.
- Do not treat the top search result as the whole answer. Use different references for different dimensions when that is more accurate.
- Do not implement before producing a reference element matrix when design direction is requested.
