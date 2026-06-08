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
- Design system: `design-systems/<slug>/` stores reusable color systems, moodboards, component style rules, and machine-readable tokens.
- L3 full reference: `references/YYYY-MM-DD-<slug>.md` remains the authoritative complete evidence record.
- L4 on-demand evidence: keep one screenshot per active reference and retain structured component-style JSON, but do not store raw DOM snapshots in the default library. If L0-L3 evidence is insufficient, recapture the source URL into an external temp location and extract only the needed facts back into L2/L3/design-system files.

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
  design-systems/
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
- A complete design-system retention pack with `tokens.json`, `palette.md`, `moodboard.svg`, and `component-styles.md`.
- Motion code evidence from public CSS/JS/DOM when available, or an explicit `no direct code evidence` limit.
- Community signal or selection reason for batch additions: source community, award/gallery list, repeated praise theme, or the user's stated reason.
- Self-review that names what was revised and what still limits reuse.

Do not count blocked, blank, overlay-dominated, visually ordinary, purely remembered, or single-sentence entries toward batch goals such as "50 websites".

Do not count Cloudflare/security challenge pages as references. If the screenshot, title, DOM, or component samples show challenge-page signatures such as `Attention Required | Cloudflare`, `Cloudflare Ray ID`, `Performance & security by Cloudflare`, `checking your browser`, `verify you are human`, `cf-chl`, or `challenge-platform`, exclude the candidate or move it to a blocked/excluded record until clean visual evidence is available. Do not automatically exclude a legitimate product page merely because its normal product copy or scripts mention CAPTCHA/recaptcha.

## Use-Readiness Gate

A reference counts as active usable only when:

- L3 full reference is written.
- L1 card is generated.
- L2 dimensions are generated.
- `design-systems/<slug>/tokens.json` exists.
- `design-systems/<slug>/palette.md` exists.
- `design-systems/<slug>/moodboard.svg` exists.
- `design-systems/<slug>/component-styles.md` exists.
- At least one screenshot or user-provided visual artifact exists.
- `component_json_path` points to non-empty component-style JSON, or missing component evidence is explicitly recorded.
- `best_for` and `avoid_for` can guide `use-designstyle` retrieval.
- Reference text grammar, Style tokens, and Spacing rhythm have evidence or explicit `missing` markers.
- Progressive library validation passes.

If any condition fails, mark the entry partial or blocked instead of counting it as active usable.

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
   - For high-quality code/component evidence, use a real browser runtime with Playwright and the system Chrome executable. Static HTML fetches are not enough for implementation-grade component styles because modern sites hydrate components, inject CSS variables, and compute hover/focus states after load.
   - Required component-code capture toolchain:
     - Python Playwright or an equivalent browser automation runtime that can call `getComputedStyle`, `getBoundingClientRect`, `locator.hover()`, and `locator.focus()`.
     - Real Chromium/Chrome rendering, not plain HTTP scraping.
     - Screenshot plus structured component JSON evidence in `assets/YYYY-MM-DD-<slug>-component-styles.json`; raw DOM snapshots belong in an external temp path such as `/tmp/designstyle-raw-evidence/`, not in the project or library.
     - Public CSS/JS resource sampling for motion/code snippets, while avoiding full proprietary source dumps.
   - High-quality component evidence must include sampled category, selector/class hint, visible text, geometry, computed typography/color/background/border/radius/shadow/padding/gap/transition/transform/cursor/backdrop styles, and hover/focus deltas where observable.
   - Treat capture as failed for component-code quality if Playwright is missing or `component-styles.json` has zero samples. Do not mark fallback HTML extraction as successful component evidence.
   - Treat capture as failed for component-code quality if component samples are from Cloudflare/security challenge UI. Do not retain challenge-page buttons, ray IDs, bot checks, or security vendor footers as component style evidence. Normal product copy that mentions CAPTCHA/recaptcha is not a blocked-page signal by itself.
   - Clean abnormal browser-computed style artifacts before storing raw JSON. Values like `3.35544e+07px` are noise and must be filtered; valid common CSS such as `9999px` pill radii should remain.
   - Before release or batch completion, run `clean_reference_noise.py --library <library> --check` so active references, dimensions, indexes, and design-system artifacts fail fast if abnormal scientific-notation `px` values remain.
   - For large recrawls where the goal is component/code quality, prefer first-page computed component evidence over slow secondary-page summaries. Secondary pages are useful context but must not block code-style retention.

   STOP: If the reference cannot be viewed and there is no screenshot, HTML, or user-provided visual evidence, do not create a style reference from memory.
   STOP: If implementation-grade component styles are requested and the browser runtime cannot produce computed component samples, report the tooling gap instead of claiming the design system has been refreshed.
   STOP: If the captured page is a Cloudflare/security challenge, do not write or update the active reference. Preserve it only as excluded evidence and ask for a clean URL/screenshot or replacement reference.

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
   - Design system retention: save the reference's color system as a reusable palette/moodboard, component style rules, token roles, evidence source, and missing-evidence limits. Color values must come from screenshot pixels or explicit DOM/CSS/reference values; component styles must come from observed component evidence. Do not invent palettes or component states.
   - For live webpage captures, retain computed component evidence in `assets/YYYY-MM-DD-<slug>-component-styles.json`, including sampled navigation/buttons/cards/forms/icons/sections, geometry, computed styles, and hover/focus deltas when observable. Treat this JSON as retained L4 component evidence that feeds `design-systems/<slug>/component-styles.md`.
   - Spacing rhythm: header height, hero padding, section vertical gaps, grid gutters, card padding, text block width, CTA spacing, media margins, mobile compression behavior, and any CSS variables such as `--spacing-*`, `gap`, `padding`, `margin`, or `grid-template-*`.
   - Color source: shell palette vs asset-driven palette; include observed text/background colors and contrast behavior.
   - Media system: image/video style, crop, subject, material texture, aspect ratios, asset domains, production method.
   - Layout primitives: split hero, full-bleed media, product grid, editorial modules, drawers, modals, sticky/fixed headers.
   - Component grammar: nav, CTAs, cards, badges, forms, search, cart, menus, diagnostic flows, empty/loading/error states.
   - Motion: source video, hover, reveal, drawer/menu transitions, timing/easing, reduced-motion needs.
   - Motion code evidence: public CSS/JS resource URLs, `transition`, `animation`, `@keyframes`, `transform`, durations, easing curves, direction/axis values, `IntersectionObserver`, `requestAnimationFrame`, GSAP/Swiper/Framer/Slick/Owl hints, video play/pause code, and reduced-motion handling.
   - Contamination: cookie banners, region selectors, newsletter modals, carts, chat widgets, accessibility widgets, Cloudflare/security challenge pages.
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
   - Report the generated design-system folder:

     ```text
     design-systems/<slug>/tokens.json
     design-systems/<slug>/palette.md
     design-systems/<slug>/moodboard.svg
     design-systems/<slug>/component-styles.md
     ```

4. **Self-Review And Revise**
   Before reporting completion, verify:
   - Grounded in visible evidence and screenshot paths.
   - Observed facts are separated from inference.
   - Overlay/security/modal contamination is called out.
   - Typography, color, layout geometry, assets, motion, components, and implementation notes are specific.
   - Color systems and component styles are retained as design-system artifacts, with exact source attribution and missing evidence called out.
   - Live captures include computed component-style JSON when the browser can inspect the page, while raw DOM remains external/on-demand.
   - `component-styles.json` is non-empty and includes sampled computed styles; empty fallback JSON does not count.
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

## Curated Website UI Candidate Workflow

Use this stricter workflow when the user asks for high-quality websites, brand
official sites, luxury/high-end official sites, or daily candidate discovery.

1. **Build a style-coherent candidate set first**
   - Pick one style theme for the batch, such as refined luxury commerce,
     editorial culture, precise dashboard, calm wellness, expressive product
     launch, or immersive portfolio.
   - All candidates in a confirmation batch must share that style theme. Do not
     mix unrelated aesthetics just to hit the requested count.
   - Prefer brand/official/product/studio sites and strong original UI sources.
     Do not use marketplace, aggregator, template, or generic independent-store
     pages unless the user explicitly approves that weaker source type.

2. **Probe before counting**
   - Run the Aesthetic Gate for every candidate.
   - Record rejected candidates and reasons in a review file. Rejection reasons
     must distinguish at least: `anti_bot_or_security`, `blank_or_error`,
     `cookie_or_region_overlay`, `screenshot_contamination`,
     `generic_independent_store_feel`, `marketplace_or_aggregator`,
     `ordinary_visual_quality`, and `insufficient_component_evidence`.
   - A candidate is not counted only because the brand is famous. The visible
     UI must be clean, distinctive, and captureable.

3. **Show confirmation screenshots before full add**
   - For daily or exploratory discovery, stop after a clean screenshot/contact
     sheet of the proposed candidates.
   - Present the unified style theme, candidate names, URLs, scores, and one
     contact sheet. Do not write active references until the user confirms.
   - If the user confirms, run the normal full capture/write/progressive
     workflow for exactly the confirmed sites or approved replacements.

4. **Clean screenshot QA for official/brand sites**
   - Before claiming a batch is ready, visually inspect the contact sheet.
   - Do not accept Cloudflare pages, blank/near-blank pages, menus accidentally
     opened by hover, footer/detail miscaptures, large cookie/region dialogs, or
     pages navigated away by overly broad button-click rules.
   - If a site is unstable after reasonable exact dismiss rules, replace it or
     report the shortfall. Do not keep unstable screenshots to satisfy count.

5. **Active-library hygiene**
   - Move failed, unstable, or user-rejected attempts to an excluded/blocked
     location or review note; do not leave them in active references, indexes,
     dimensions, or design-system retrieval.
   - After replacements, rerun progressive generation and validators for the
     final active set only.

## Failure Handling

| Trigger | First response | Fallback |
|---|---|---|
| URL blocked by Cloudflare/security challenge | Record as unusable evidence; do not infer style | Ask for screenshot or replace with a cleaner reference |
| Cloudflare/security challenge appears in component JSON | Fail the component-code capture; exclude from active references | Move evidence to blocked/excluded records and recrawl only with clean access |
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
- Design system: design-systems/<slug>/
- L3 reference: references/YYYY-MM-DD-<slug>.md
- Validation: <command + result>
Missing evidence: <explicit limits or "none beyond recorded Evidence Limits">
```

## Use Readiness

When a reference or batch is added, also include:

```markdown
## Use Readiness
- Status: active usable | partial | blocked
- Best for:
- Avoid for:
- Strong dimensions:
- Weak or missing dimensions:
- Suggested Use roles:
- Retrieval tags to strengthen:
- Validator result:
```
