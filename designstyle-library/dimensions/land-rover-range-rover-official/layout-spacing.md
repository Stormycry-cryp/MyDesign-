# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `SKIP TO MAIN CONTENT VEHICLES OWNERS EXPLORE SHOP NOW OFFERS LOCATE A RETAILER BUILDS SUPPORT LEAD BY EXAMPLE EXPLORE European Model Shown. RANGE ROVER Starting at $113,300* New levels of luxury and refinement. EXPLORE BUILD AND RESERVE RANGE ROVER SPORT Start`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 8, image count 30, document height 8434.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 8434}.
  - Media/card aspect stability: image natural sizes include 300x16; 1280x720; 0x0; 1280x720; 0x0; 0x0; 0x0; 0x0; 0x0; 0x0.
  - Observed border radii: 100%; 50%; 50%; 50%; 50%; 50%; 50%
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 8434}
  - Observed media ratios: 300:16; 1280:720; 1280:720; 66:35
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, keyframes, reduced_motion, swiper, transform, transition
  - Performance/accessibility concerns: heavy media count 30 and scripts 36; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
