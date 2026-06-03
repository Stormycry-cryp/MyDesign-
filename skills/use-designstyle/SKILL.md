---
name: use-designstyle
description: Use when designing or redesigning a webpage, app screen, landing page, prototype, visual system, or frontend UI and the work should draw from the local designstyle reference library.
---

# Use Designstyle

Use local references to preserve transferable design decisions, not to borrow mood words. A good use of references composes multiple evidence dimensions into implementation choices: scene fit, geometry, dimension ratios, typography roles, palette source, asset plan, motion logic, motion code evidence, component states, and anti-copy boundaries.

## Library

Default location:

```text
~/.codex/designstyle-library/references/
```

If the library is empty or weak for the product scene, say so and either re-query or ask to run `add-designstyle`.

## Workflow

1. **Understand The Design Need**
   - Product category and commerce/workflow context.
   - User frequency: repeated task, one-time browsing, campaign launch, product inspection.
   - Desired feeling: name concrete mechanics, not just adjectives.
   - Content shape: narrative, product catalog, formula proof, media, forms, diagnostic flow.
   - Technical constraints: framework, devices, accessibility, performance, assets.

2. **Retrieve Candidate References By Dimension**
   Search with product scene plus mechanics:

   ```bash
   python ~/.codex/skills/use-designstyle/scripts/search_references.py "skincare clinical minimal formula product grid swiper transition" --matrix
   ```

   Use 2-5 references maximum, selected by role rather than winner-takes-all ranking:
   - Scene/style reference: product category, audience, trust problem, tone.
   - Structure/ratio reference: first viewport geometry, page grid, media/product-card proportions.
   - Type/color reference: typography roles, color/material system, contrast.
   - Asset reference: photography/video/material production plan.
   - Motion/code reference: transition, animation, keyframes, exact duration/easing/transform parameters, runtime library, reduced-motion strategy.

   STOP: If top references are generic, contradictory, contaminated, or unrelated, re-query or say the library lacks a good match. Do not force a SaaS or culture reference onto beauty, retail, spa, or product pages just because tags include `product` or `motion`.

3. **Build A Reference Element Matrix**
   Do not copy one reference wholesale. Make a matrix:
   - Requirement dimension.
   - Selected reference.
   - Evidence strength: screenshot/DOM/CSS/JS strong, runtime inference medium, visual-only weak.
   - Extracted element: the specific decision to borrow.
   - Adaptation rule: how it changes for the user's product/content/assets.
   - Anti-copy limit: what must not be copied.

4. **Map Evidence To Requirements**
   For each selected reference, extract:
   - First viewport geometry: bars/header/nav/logo/hero/copy/CTA/next-section visibility.
   - Dimension ratios: viewport, hero min-height, split ratios, product/media card ratios, header/drawer bounds.
   - Typography roles: display, UI, body, metadata, CTA, technical labels.
   - Color source: shell palette vs asset-derived palette.
   - Asset plan: required photo/video/product/material quality.
   - Motion purpose: source video, reveal, drawer, hover, scroll, timing.
   - Motion code: CSS transition/animation/keyframes, exact duration/easing/delay/transform parameters, GSAP/Swiper/Slick/Owl/Framer evidence, `IntersectionObserver`, `requestAnimationFrame`, reduced-motion handling.
   - Component grammar: nav, buttons, cards, forms, search, cart, overlays, feedback states.
   - Implementation primitives: split hero, full-bleed media, product grid, sticky header, drawers, aspect ratios.
   - Evidence strength and contamination: screenshot/source/DOM strong, inference weak, cookie/region/captcha ignored.
   - What not to copy: brand identity, proprietary assets, exact typefaces, product names, claims.

5. **Derive The Design Direction**
   Produce a compact direction before implementation:
   - Scene and audience:
   - Visual stance:
   - First viewport geometry:
   - Dimension/ratio system:
   - Type roles:
   - Color/material:
   - Asset production plan:
   - Motion/code plan:
   - Components/states:
   - Anti-patterns and anti-copy limits:
   - Reference element matrix:

6. **Apply During Build**
   Keep checking:
   - Does the UI match the product scene, not merely the color palette?
   - Are real assets or asset placeholders strong enough for the borrowed style?
   - Did you preserve macro geometry, ratios, and typography roles?
   - Are motion and transitions causal and backed by the chosen motion/code reference?
   - Are text, spacing, contrast, responsive layout, and states robust?
   - Did you avoid copying protected brand identity and proprietary artwork?

7. **Final Design Audit**
   Before claiming completion, audit:
   - Which references were used and which exact dimensions were borrowed.
   - Which dimensions were intentionally not borrowed and why.
   - Whether screenshots/assets/text show the reference decisions in the final UI.
   - Interaction quality: hover, drawer/modal, loading/empty/error states.
   - Motion quality: purpose, timing, implementation technique, reduced-motion fallback.
   - Anti-patterns: generic gradients, decorative blobs, nested cards, stock filler, vague "premium" styling.

## Output Pattern

```markdown
## Selected References
- <reference>: use for <specific dimension>; evidence strength <strong/medium/weak>.

## Reference Element Matrix
| Need | Reference | Evidence | Borrow | Adapt | Do Not Copy |
|---|---|---|---|---|---|
| Scene/style |  |  |  |  |  |
| Structure/ratio |  |  |  |  |  |
| Type/color |  |  |  |  |  |
| Assets |  |  |  |  |  |
| Motion/code |  |  |  |  |  |

## Design Direction
- Scene:
- First viewport geometry:
- Dimension/ratio system:
- Type roles:
- Color/material:
- Assets:
- Motion/code:
- Components/states:
- Anti-copy limits:

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
| References conflict | Pick one primary and demote others by dimension | Do not blend incompatible aesthetics |
| One reference fits style but not layout/motion | Keep it only for the fitting dimension | Select separate structure or motion references |
| Assets are missing | Define an asset plan before layout polish | Use stable placeholders only as temporary scaffolding |
| Reference has contamination | Ignore cookie/region/captcha/modal as aesthetic evidence | Prefer clean screenshot or exclude reference |
| Implementation constraints conflict | Reduce media/motion first | Preserve hierarchy, typography roles, spacing, states |

## Do Not Do

- Do not copy a reference's brand identity, proprietary assets, exact layout, exact typefaces, or claims.
- Do not reduce references to adjectives like "luxury", "clean", "natural", or "premium".
- Do not use references with weak evidence as implementation-grade guidance.
- Do not treat the top search result as the whole answer. Use different references for different dimensions when that is more accurate.
- Do not implement before producing a reference element matrix when design direction is requested.
