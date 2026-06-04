# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `Skip to main content A digital publication that... explains ideas with visual essays OUR FAVES POPULAR UPDATING YOUR INPUT VIDEO AUDIO #218 MAY 2026 k-pop generations Two friends tell the story of their friendship through every generation of K-pop. #217 MAY 20`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 0, image count 40, document height 6786.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 6786}.
  - Media/card aspect stability: image natural sizes include 450x240; 806x241; 454x240; 450x240; 806x241; 601x240; 516x240; 559x240; 590x240; 583x240.
  - Observed border radii: 2px; 2px; 2px; 2px; 2px; 2px; 2px; 2px; 2px; 2px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 6786}
  - Observed media ratios: 450:240; 806:241; 454:240; 450:240; 806:241; 601:240; 516:240; 559:240; 590:240; 583:240
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: easing, reduced_motion, transform, transition
  - Performance/accessibility concerns: heavy media count 40 and scripts 1; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
