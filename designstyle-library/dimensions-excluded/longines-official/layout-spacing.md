# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `Skip to main content Accessibility settings Receive free two-day shipping and returns with your order. Close United States Customer Service Our Universe Longines Find my Longines Accessories Open Search Go to Store Go to My Account Go to Cart MASTER CONQUEST S`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 6, image count 34, document height 7037.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 7037}.
  - Media/card aspect stability: image natural sizes include 1440x810; 1440x810; 314x314; 314x314; 314x314; 314x314; 314x314; 314x314; 0x0; 1440x1310.
  - Observed border radii: 5px; 5px; 5px; 50%; 50%; 5px; 5px; 50%; 50%; 5px; 5px; 50%
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 7037}
  - Observed media ratios: 1440:810; 1440:810; 314:314; 314:314; 314:314; 314:314; 314:314; 314:314; 1440:1310; 1440:1800
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: none proven
  - Performance/accessibility concerns: heavy media count 34 and scripts 36; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
