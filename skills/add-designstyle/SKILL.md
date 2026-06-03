---
name: add-designstyle
description: Use when the user provides an example website, product page, app screen, visual reference, or URL and wants its code/design/aesthetic style analyzed and added to a reusable local design reference library.
---

# Add Designstyle

Turn a concrete visual reference into a reusable designstyle entry in `~/.codex/designstyle-library/references/`.

The job is feature preservation, not praise. Capture enough evidence that a future build can reproduce the reference's transferable decisions: first viewport geometry, dimension ratios, typography roles, palette source, asset direction, motion logic, motion code evidence, interaction states, implementation clues, and anti-patterns.

## Library

```text
~/.codex/designstyle-library/
  references/
  screenshots/
  assets/
  reviews/
  indexes/
```

Create missing folders. Do not store secrets, private user data, full copied proprietary source, or proprietary brand assets beyond screenshots needed as evidence.

## Workflow

1. **Capture Evidence**
   - If given a URL, inspect the live page.
   - Capture at least one screenshot when visual fidelity matters. Prefer desktop first viewport; add mobile/product-detail screenshots when relevant.
   - Inspect visible UI before source. Then inspect public CSS/JS enough to identify implementation evidence for layout, style, and motion.
   - Record URL, final URL, date, viewport, screenshot path, page title, inaccessible parts, and overlay contamination.
   - For code evidence, prefer concrete clues: CSS variables, font declarations, layout primitives, transition/animation/keyframe snippets, animation libraries, framework/runtime hints, asset CDN patterns, component names, image/video sources.
   - Do not store full proprietary CSS/JS. Store resource URLs, fetch date, motion-relevant snippets, matched selectors/properties/library names, and implementation interpretation.
   - For motion, preserve exact useful parameters whenever available: duration, delay, easing, `cubic-bezier(...)`, animated properties, transform direction/axis, keyframe names, translate/scale/rotate values, carousel translate strategy, and reduced-motion overrides.

   STOP: If the reference cannot be viewed and there is no screenshot, HTML, or user-provided visual evidence, do not create a style reference from memory.

2. **Build The Evidence Matrix**
   Capture these dimensions before writing conclusions:
   - Product scene, audience, trust problem, and conversion context.
   - Layered tags: `style_tags`, `structure_tags`, `motion_tags`, and `code_tags`.
   - First viewport geometry: promo bars, header shape, nav density, logo position, hero media/copy/CTA placement, visible next section.
   - Dimension and ratio system: viewport/document size, hero height, split ratios, image/product-card ratios, header height, section gaps, fixed/drawer dimensions.
   - Typography roles: brand/display, retail UI, body, metadata, CTA, technical labels; include observed font stacks, sizes, weights, letter spacing.
   - Color source: shell palette vs asset-driven palette; include observed text/background colors and contrast behavior.
   - Media system: image/video style, crop, subject, material texture, aspect ratios, asset domains, production method.
   - Layout primitives: split hero, full-bleed media, product grid, editorial modules, drawers, modals, sticky/fixed headers.
   - Component grammar: nav, CTAs, cards, badges, forms, search, cart, menus, diagnostic flows, empty/loading/error states.
   - Motion: source video, hover, reveal, drawer/menu transitions, timing/easing, reduced-motion needs.
   - Motion code evidence: public CSS/JS resource URLs, `transition`, `animation`, `@keyframes`, `transform`, durations, easing curves, direction/axis values, `IntersectionObserver`, `requestAnimationFrame`, GSAP/Swiper/Framer/Slick/Owl hints, video play/pause code, and reduced-motion handling.
   - Contamination: cookie banners, region selectors, newsletter modals, carts, chat widgets, accessibility widgets, captcha/security pages.
   - Do-not-copy boundaries: wordmark, proprietary typefaces, campaign images, product names, claims, brand-specific mythology.

3. **Write The Reference**
   - Create one Markdown file in `references/` named `YYYY-MM-DD-site-or-style-name.md`.
   - Prefer transferable decisions over one-off descriptions.
   - Tags must include product scene and aesthetic mechanics, not only generic words like `luxury` or `motion`.
   - Use the required high-fidelity format below. `new_reference.py` generates this format.

4. **Self-Review And Revise**
   Before reporting completion, verify:
   - Grounded in visible evidence and screenshot paths.
   - Observed facts are separated from inference.
   - Overlay/security/modal contamination is called out.
   - Typography, color, layout geometry, assets, motion, components, and implementation notes are specific.
   - `When Not To Use`, `Avoid Copying`, `Evidence Limits`, and `Self Review` are present.
   - The entry would retrieve for the right future task and not for the wrong one.

For a batch, add a review note under `reviews/` describing included references, excluded/weak samples, retrieval implications, and skill/search-helper lessons.

## Failure Handling

| Trigger | First response | Fallback |
|---|---|---|
| URL blocked by captcha/security | Record as unusable evidence; do not infer style | Ask for screenshot or replace with a cleaner reference |
| Cookie/region/newsletter overlay dominates | Try dismissing once if safe; recapture | Mark contamination and do not use overlay as aesthetic evidence |
| Blank/minimal capture | Retry once with longer wait or alternate URL | Exclude or create an evidence-unavailable stub only |
| Public source unavailable | Use visible UI, screenshots, asset domains, computed styles | Mark implementation details as inference |
| Public CSS/JS is large or minified | Probe for motion/layout keywords and save motion-relevant snippets with exact parameters | Record URLs and hash/keywords; do not paste full source |
| Broad multi-style site | Scope to one page/style | Split into separate entries if needed |
| Batch retrieves poorly | Fix tags/frontmatter and add index/review notes | Revise search helper weighting |

## Required Reference Format

```markdown
---
title: ""
source_url: ""
captured_at: "YYYY-MM-DD"
tags: []
style_tags: []
structure_tags: []
motion_tags: []
code_tags: []
best_for: []
avoid_for: []
evidence_screenshot: "screenshots/<slug>-desktop.png"
evidence_quality: "visual screenshot plus DOM/style/resource extraction"
---

# Style Reference: <name>

## Essence

## When To Use

## When Not To Use

## Evidence Snapshot
- Captured URL:
- Page title:
- Screenshot:
- Viewport:
- H1 observed:
- H2 samples:
- Navigation samples:
- Images observed:
- Video observed:
- Overlays or fixed elements:

## Visual System
- Layout:
- Typography:
- Color:
- Density:
- Shape:
- Shadow/depth:

## Typography And Reading Rhythm
- Observed font stack counts:
- Observed font sizes:
- Observed weights:
- Observed letter spacing:
- Preserve role relationships:

## Color, Material, And Contrast
- Observed text colors:
- Observed backgrounds:
- UI shell colors vs asset-driven colors:

## Layout Geometry And Spacing
- First viewport structure:
- Macro geometry:
- Media/card aspect stability:
- Observed border radii:

## Dimension And Ratio System
- Viewport and document:
- Observed media ratios:
- Observed spacing samples:
- Preserve ratios as implementation constraints:
- Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.

## Assets
- Image style:
- Illustration/icon style:
- Texture/pattern:
- Likely sources or production method:

## Motion
- Page transitions:
- Micro-interactions:
- Scroll/entrance behavior:
- Timing/easing:

## Motion Code And Runtime Evidence
- Motion source:
- CSS animation/transition evidence:
- Public CSS/JS probe keywords:
- Public CSS/JS motion snippets:
- Exact motion parameters:
- JavaScript/runtime motion evidence:
- Stylesheet evidence:
- Interpreted motion tags:
- Use this as implementation guidance only where evidence is direct. If CSS/JS is minified or only CDN names are visible, mark library/framework attribution as weak.

## Interaction And Components
- Navigation:
- Buttons/links:
- Cards/sections:
- Forms/inputs:
- Feedback states:

## Implementation Notes
- CSS/layout primitives:
- Token ideas:
- Libraries or techniques:
- Performance/accessibility concerns:

## Borrow

## Avoid Copying

## Evidence Limits

## Self Review
- Evidence quality:
- Reuse value:
- Missing pieces:
- Revision made:
```

## Helper

```bash
python ~/.codex/skills/add-designstyle/scripts/new_reference.py "site name" --url "https://example.com" --tags "skincare,luxury,split-hero"
```

Probe public motion/style code when possible:

```bash
python ~/.codex/skills/add-designstyle/scripts/probe_motion_code.py
```

Fill every section and self-review it before reporting completion. A reference that only says "premium", "clean", "natural", or "high-end" has failed the skill. A reference that claims motion without code/runtime evidence or explicitly marked evidence limits has also failed.
