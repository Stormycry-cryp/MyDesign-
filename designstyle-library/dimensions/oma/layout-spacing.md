# Layout And Spacing

## Observed
- Visual layout:
  - Layout: edge-to-edge hero image, extra-large wordmark/navigation row pinned across the top, centered white project pill, lower-left editorial story card
  - Typography: bold condensed-looking all-caps sans for navigation and announcement, with scale doing more work than weight variation
  - Color: powder-blue city dusk image, white slabs, black type, and sharp red accent for the story card border/text
  - Density: very sparse; only a handful of text elements are visible in the first viewport
  - Shape: almost entirely rectangular, no ornamental rounding
  - Shadow/depth: no visible shadow grammar; depth comes from photography rather than UI effects
- Layout geometry:
  - First viewport structure: giant top row from left to right, hero image filling almost all height, centered white pill above a lower-left text card
  - Macro geometry: one main image plane with two overlay rectangles; no visible grid of secondary modules in the first screen
  - Media/card aspect stability: hero image reads nearly full-width landscape; story card is a wide shallow rectangle
  - Header/hero/section spacing: the top row hugs the upper edge; major overlays are generously separated and rely on large dead space
  - Grid gutters and card padding: broad outer margins; the story card uses thick inner padding relative to its text
  - Mobile spacing behavior: missing evidence
  - Observed border radii: none observed
- Dimension ratios:
  - Viewport and document: 1440x1000 visible probe viewport; probe document height reported about 13861px
  - Observed media ratios: hero image reads like a full-width cinematic landscape; the centered pill is about one-third page width and much shallower than the lower story card
  - Observed spacing samples: top row to hero edge is tight; centered pill floats well above the lower card; generous whitespace separates the two overlays
  - Preserve ratios as implementation constraints: if adapted, preserve one dominant image plane plus two overlay layers rather than decomposing into cards
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
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
