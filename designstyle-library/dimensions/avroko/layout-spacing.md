# Layout And Spacing

## Observed
- Visual layout:
  - Layout: slim top nav, two-column text band, full-width project image strip beneath
  - Typography: high-contrast serif display paired with small restrained sans navigation and metadata
  - Color: warm ivory background, dark charcoal type, muted gold quote text, black-and-gold hospitality imagery
  - Density: low to medium; the composition is airy despite multiple navigation categories
  - Shape: flat rectangles and underlines; little visible rounding except in deeper component samples
  - Shadow/depth: little explicit shadow; depth is created through layered interior photography and warm lighting
- Layout geometry:
  - First viewport structure: nav at top, text split left/right, underline CTA below headline, then a wide hero image band
  - Macro geometry: roughly 60/40 headline-to-quote balance across the top text field
  - Media/card aspect stability: hero image is a wide horizontal band cropped shallowly in the first viewport
  - Header/hero/section spacing: large top whitespace around the headline, then a hard transition into the image strip
  - Grid gutters and card padding: generous lateral margins; content breathes rather than stacking tightly
  - Mobile spacing behavior: missing evidence
  - Observed border radii: component samples show some rounded assets deeper in the page, but not as a first-viewport signature
- Dimension ratios:
  - Viewport and document: 1440x1000 visible state, document height captured around 1000px for the accepted screenshot state
  - Observed media ratios: the project image band reads as a panoramic crop; the headline block occupies about the left half of the upper field
  - Observed spacing samples: top nav padding around 28.8px vertically and 57.6px horizontally surfaced in component evidence; headline field uses expansive whitespace
  - Preserve ratios as implementation constraints: preserve the balance of broad white top field to shallow image band underneath
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: leverage broad padding, top-anchored nav, two-column intro copy, and panoramic media bands
  - Token ideas: ivory background, charcoal text, muted gold accent, literary serif plus disciplined sans
  - Libraries or techniques: Webflow stack, Locomotive Scroll, Finsweet CMS Slider, requestAnimationFrame-driven behavior
  - Performance/accessibility concerns: heavy media payload and scroll libraries mean reduced-motion and image-loading policies need active review

## Inference
- Borrow:
  - Borrow the split of declarative headline and validation quote.
  - Borrow the combination of soft shell, luxury-material imagery, and restrained nav.
  - Borrow the practice of proving the narrative with a single strong project image immediately below the fold line.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy AvroKO’s hospitality positioning, exact testimonial, or project imagery.
- Do not blindly import all Webflow/scroll behaviors into a simpler product context.
- Do not over-expand the typography system; its power comes from restraint.
