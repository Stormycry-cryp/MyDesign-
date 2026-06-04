---
name: add-designstyle
description: Use when the user provides an example website, product page, app screen, visual reference, or URL and wants its code/design/aesthetic style analyzed and added to a reusable local design reference library.
---

# Add Designstyle

Turn a concrete visual reference into a reusable designstyle entry in `~/.codex/designstyle-library/references/`.

The job is feature preservation, not praise. Capture enough evidence that a future build can reproduce the reference's transferable decisions: first viewport geometry, dimension ratios, typography roles, palette source, reference text grammar, style tokens, spacing rhythm, asset direction, motion logic, motion code evidence, interaction states, implementation clues, and anti-patterns.

## Progressive Evidence Layers

After every full reference is written, update the progressive-disclosure layers:

- L1 card: `indexes/cards/<slug>.json` for fast retrieval and ranking.
- L2 dimensions: `dimensions/<slug>/*.md` for scene, layout/spacing, type/copy, color/surface, assets, motion/code, and components/states.
- L3 full reference: `references/YYYY-MM-DD-<slug>.md` remains the authoritative complete evidence record.
- L4 raw evidence: screenshots, DOM captures, and asset/resource clues remain supporting evidence.

L1/L2 are retrieval and selective-reading aids; they do not replace the L3 full reference. Missing typography, spacing, copy, motion, or code evidence must stay explicit as `missing` or `Missing Evidence`.

## Library

```text
~/.codex/designstyle-library/
  references/
  screenshots/
  assets/
  reviews/
  indexes/
    manifest.json
    facets.json
    cards/
  dimensions/
```

Create missing folders. Do not store secrets, private user data, full copied proprietary source, or proprietary brand assets beyond screenshots needed as evidence.

## Reference Counts And Quality Gates

A reference counts as usable only when all required evidence is present:

- It passes the **Aesthetic Gate** before any reference is written, or the user explicitly confirms adding it despite the warning.
- One unique site or one clearly scoped page style from a broad multi-style site.
- At least one screenshot or user-provided visual artifact.
- A specific page scope: home, product, pricing, docs, case study, portfolio, article, checkout, dashboard, app screen, gallery, campaign, or search/listing.
- Layered tags with `category_tags`, `style_tags`, `structure_tags`, `motion_tags`, and `code_tags`.
- First-viewport geometry, dimension/ratio system, typography roles, palette/material, assets, interaction components, motion, and evidence limits.
- Motion code evidence from public CSS/JS/DOM when available, or an explicit `no direct code evidence` limit.
- Community signal or selection reason for batch additions: source community, award/gallery list, repeated praise theme, or the user's stated reason.
- Self-review that names what was revised and what still limits reuse.

Do not count blocked, blank, overlay-dominated, visually ordinary, purely remembered, or single-sentence entries toward batch goals such as "50 websites".

## Aesthetic Gate

Run an aesthetic fit probe before writing any new reference. This is a blocking preflight, not a post-hoc review.

```bash
python ~/.codex/skills/add-designstyle/scripts/probe_aesthetic_fit.py --name "site name" --url "https://example.com"
```

Use `minimum_score: 75` unless the user gives a stricter standard. Score visible first-viewport UI quality, not brand fame. Penalize government-like layouts, generic templates, weak typography hierarchy, cluttered navigation, low visual distinctiveness, blocked/404/security pages, cookie/modal contamination, and screenshots that do not show the actual target UI.

Decision rule:

- `score >= 75` and no severe flags: proceed to capture/write the reference.
- `score < 75` or severe flags such as `blocked`, `404`, `overlay_dominated`, `blank`, `generic_template`, or `visually_ordinary`: stop and tell the user the score, screenshot path, and reasons. Do not write the reference until the user confirms.
- If the user confirms after a warning, record `community_signal` or `Evidence Limits` with `user explicitly approved low aesthetic score <score>` so future retrieval understands the weakness.
- For batches, probe all candidates first, save a candidate/rejection note in `reviews/YYYY-MM-DD-<batch>-candidates.md`, then write only approved candidates. Do not silently replace a failed candidate unless the user asked for a target count and equivalent replacements are available.

## Workflow

1. **Capture Evidence**
   - First run the **Aesthetic Gate**. If it fails, stop before writing files and ask for user confirmation.
   - If given a URL, inspect the live page.
   - Capture at least one screenshot when visual fidelity matters. Prefer desktop first viewport; add mobile/product-detail screenshots when relevant.
   - For a website rather than one screen, inspect at least two meaningful page states when available: home plus one product/pricing/docs/case-study/detail/listing page. If only one page is accessible, record `page_scope` and the missing states.
   - Inspect visible UI before source. Then inspect public CSS/JS enough to identify implementation evidence for layout, style, and motion.
   - Record URL, final URL, date, viewport, screenshot path, page title, inaccessible parts, and overlay contamination.
   - For code evidence, prefer concrete clues: CSS variables, font declarations, layout primitives, spacing declarations, transition/animation/keyframe snippets, animation libraries, framework/runtime hints, asset CDN patterns, component names, image/video sources.
   - Do not store full proprietary CSS/JS. Store resource URLs, fetch date, motion-relevant snippets, matched selectors/properties/library names, and implementation interpretation.
   - For motion, preserve exact useful parameters whenever available: duration, delay, easing, `cubic-bezier(...)`, animated properties, transform direction/axis, keyframe names, translate/scale/rotate values, carousel translate strategy, and reduced-motion overrides.

   STOP: If the reference cannot be viewed and there is no screenshot, HTML, or user-provided visual evidence, do not create a style reference from memory.

2. **Build The Evidence Matrix**
   Capture these dimensions before writing conclusions:
   - Product scene, audience, trust problem, and conversion context.
   - Community signal: source community/list, signal type, visible praise/critique theme, and why it was selected.
   - Layered tags: `category_tags`, `style_tags`, `structure_tags`, `motion_tags`, and `code_tags`.
   - Page scope: page type, secondary pages inspected, and whether the entry represents the whole site or one pattern.
   - First viewport geometry: promo bars, header shape, nav density, logo position, hero media/copy/CTA placement, visible next section.
   - Dimension and ratio system: viewport/document size, hero height, split ratios, image/product-card ratios, header height, section gaps, fixed/drawer dimensions.
   - Reference text system: H1/H2/eyebrow/CTA/body/meta text samples; sentence length; verb style; claim density; naming patterns; whether copy is technical, editorial, retail, clinical, playful, or restrained.
   - Typography roles: brand/display, retail UI, body, metadata, CTA, technical labels; include observed font stacks, sizes, weights, letter spacing.
   - Style token system: dominant surfaces, border/radius/shadow grammar, icon/stroke style, dividers, focus/hover states, button density, form density, and whether the system feels product-led, editorial, dashboard-like, catalog-like, or campaign-like.
   - Spacing rhythm: header height, hero padding, section vertical gaps, grid gutters, card padding, text block width, CTA spacing, media margins, mobile compression behavior, and any CSS variables such as `--spacing-*`, `gap`, `padding`, `margin`, or `grid-template-*`.
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
   - Generate and validate progressive files after the L3 reference is written:

     ```bash
     python ~/.codex/skills/add-designstyle/scripts/build_progressive_reference.py --reference ~/.codex/designstyle-library/references/YYYY-MM-DD-slug.md
     python ~/.codex/skills/add-designstyle/scripts/validate_progressive_library.py --json
     ```

   - Report the generated L1 card path and L2 dimension folder. If generation or validation fails, report the exact failing command and do not count the reference as progressive-ready.

4. **Self-Review And Revise**
   Before reporting completion, verify:
   - Grounded in visible evidence and screenshot paths.
   - Observed facts are separated from inference.
   - Overlay/security/modal contamination is called out.
   - Typography, color, layout geometry, assets, motion, components, and implementation notes are specific.
   - `When Not To Use`, `Avoid Copying`, `Evidence Limits`, and `Self Review` are present.
   - The entry would retrieve for the right future task and not for the wrong one.

## Community-Driven Batch Workflow

Use this workflow for large library expansion tasks.

1. **Observe Design Community Feedback**
   - Search or browse focused sources such as Awwwards, Godly, Siteinspire, Httpster, Land-book, Landingfolio, Mobbin, Layers, Muzli, FWA, Webflow showcase, Framer gallery, Vercel gallery, Product Hunt launches, indie maker showcases, design Twitter/X threads, and respected studio portfolios.
   - Record feedback themes, not just URLs: what people praise or criticize, such as scroll storytelling, typography restraint, bold 3D, density, pricing clarity, conversion polish, dark-mode depth, editorial rhythm, motion restraint, or overused effects.
   - Ignore popularity when the site is visually ordinary, inaccessible, mostly template noise, or dominated by ads/overlays.

2. **Build A Diverse Candidate List**
   Use category coverage before capture. A 50-reference batch must include multiple kinds, for example:
   - SaaS/productivity, AI/developer tools, fintech, ecommerce, fashion/beauty, hardware, health/wellness, media/culture, editorial/news, agency/studio, portfolio, education, gaming/entertainment, nonprofit/civic, documentation/devrel, data/analytics, community/social, travel/hospitality, food/beverage, and immersive/WebGL.
   - No single category should exceed 20% of the batch unless the user explicitly asks for that category.
   - Save candidate and exclusion notes in `reviews/YYYY-MM-DD-<batch>-candidates.md`.

3. **Capture In Batches Of 10**
   - Process 10 references at a time, then run retrieval checks before continuing.
   - For each set, write `reviews/YYYY-MM-DD-<batch>-review.md` with included entries, excluded entries, category coverage, recurring community feedback, and retrieval risks.
   - If a batch over-produces the same aesthetic, stop and replace the weakest references with underrepresented categories.

4. **Count Only Verified Entries**
   - Count entries by files in `references/` that pass the quality gates above.
   - Do not count candidate notes, blocked pages, screenshots without references, or TODO-filled templates.
   - Run the validator before claiming a batch count:

     ```bash
     python ~/.codex/skills/add-designstyle/scripts/validate_references.py
     ```
   - For progressive batches, also run:

     ```bash
     python ~/.codex/skills/add-designstyle/scripts/build_progressive_reference.py --all
     python ~/.codex/skills/add-designstyle/scripts/validate_progressive_library.py --json
     ```

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
| Batch lacks category diversity | Stop adding near-duplicates | Replace weak same-category entries before continuing |
| Community feedback is unavailable | Record selection reason from visible quality and comparable references | Do not invent praise or pretend a community signal exists |

## Required Reference Format

```markdown
---
title: ""
source_url: ""
captured_at: "YYYY-MM-DD"
tags: []
category_tags: []
style_tags: []
structure_tags: []
motion_tags: []
code_tags: []
best_for: []
avoid_for: []
community_signal: ""
page_scope: ""
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
- Community signal:
- Page scope:
- Secondary pages inspected:
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

## Reference Text And Copy Grammar
- H1/H2/eyebrow/CTA samples:
- Sentence rhythm:
- Claim density:
- Voice and naming:
- Copy boundaries:

## Color, Material, And Contrast
- Observed text colors:
- Observed backgrounds:
- UI shell colors vs asset-driven colors:

## Layout Geometry And Spacing
- First viewport structure:
- Macro geometry:
- Media/card aspect stability:
- Header/hero/section spacing:
- Grid gutters and card padding:
- Mobile spacing behavior:
- Observed border radii:

## Style Tokens And Surface Grammar
- Surface/background system:
- Borders/dividers/radii:
- Shadow/depth/material:
- Button/input/control density:
- Icon/illustration stroke style:

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

## Code Surface
- Framework/runtime hints:
- Public stylesheet/script URLs:
- CSS variables/tokens observed:
- Layout primitives observed:
- Component or class naming clues:
- Asset CDN and media loading patterns:

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

Validate whether references count toward a batch target:

```bash
python ~/.codex/skills/add-designstyle/scripts/validate_references.py
```

Validate progressive cards and dimensions:

```bash
python ~/.codex/skills/add-designstyle/scripts/build_progressive_reference.py --all --dry-run
python ~/.codex/skills/add-designstyle/scripts/validate_progressive_library.py --json
```

Fill every section and self-review it before reporting completion. A reference that only says "premium", "clean", "natural", or "high-end" has failed the skill. A reference that claims motion without code/runtime evidence or explicitly marked evidence limits has also failed.

## Output Addendum

When a reference or batch is added, include:

```markdown
Generated progressive evidence:
- L1 card: indexes/cards/<slug>.json
- L2 dimensions: dimensions/<slug>/
- L3 reference: references/YYYY-MM-DD-<slug>.md
- Validation: <command + result>
Missing evidence: <explicit limits or "none beyond recorded Evidence Limits">
```
