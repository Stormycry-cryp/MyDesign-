# Motion And Code

## Observed
- Motion:
  - Page transitions: no direct code evidence
  - Micro-interactions: likely hover emphasis on top-row navigation, but not proven
  - Scroll/entrance behavior: missing evidence
  - Timing/easing: missing evidence
- Motion code:
  - Motion source: probe-only visual evidence
  - CSS animation/transition evidence: no direct code evidence
  - Public CSS/JS probe keywords: missing evidence
  - Public CSS/JS motion snippets: missing evidence
  - Exact motion parameters: no direct code evidence
  - JavaScript/runtime motion evidence: missing evidence
  - Stylesheet evidence: missing evidence
  - Interpreted motion tags: minimal-motion, hover-reveal
  - Use this as implementation guidance only where evidence is direct. If CSS/JS is minified or only CDN names are visible, mark library/framework attribution as weak.
- Code surface:
  - Framework/runtime hints: missing evidence from the successful probe beyond rendered DOM output
  - Public stylesheet/script URLs: missing evidence; formal capture timed out before resource sampling became reliable
  - CSS variables/tokens observed: missing evidence
  - Layout primitives observed: image-first hero with overlayed absolute-position slabs inferred from the screenshot
  - Component or class naming clues: missing evidence
  - Component computed-style evidence: `assets/2026-06-08-oma-component-styles.json`
  - Asset CDN and media loading patterns: missing evidence
- Implementation notes:
  - CSS/layout primitives: absolute overlays on a full-bleed image, hard rectangles, overscaled top navigation
  - Token ideas: white shell, black text, one alert red accent, restrained neutral fallback surfaces
  - Libraries or techniques: no direct code evidence
  - Performance/accessibility concerns: giant text over imagery needs careful contrast checks and responsive collapse behavior

## Inference
- Borrow:
  - Borrow the confidence of giant shell typography and the discipline of showing one project at a time.
  - Borrow the editorial use of date + headline inside a bordered information slab.
  - Borrow the image-led hierarchy where navigation feels like part of the art direction.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the exact OMA navigation treatment, project names, or red/white alert framing verbatim.
- Do not copy the photographic subject matter or city-scene composition.
- Do not imply motion behavior that was not directly evidenced.
