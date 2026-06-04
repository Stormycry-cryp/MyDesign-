# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `ALL OF OUR PRODUCERS FARM LESS THAN 10 HECTARES OF VINEYARDS, HARVEST BY HAND AND ARE DRIVEN BY AN EARNEST DESIRE TO MAKE SERIOUS, COMPELLING WINES. FRIULI-VENEZIA GIULIA PIEDMONT SARDINIA SICILY SLOVENIA TUSCANY PRODUCERS DISTRIBUTORS A HISTORY OF THE FUTURE `.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 2, image count 22, document height 2604.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 2604}.
  - Media/card aspect stability: image natural sizes include 3456x2182; 1440x959; 1440x960; 0x0; 1440x1074; 1440x960; 1440x960; 0x0; 0x0; 0x0.
  - Observed border radii: none observed
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 2604}
  - Observed media ratios: 3456:2182; 1440:959; 1440:960; 1440:1074; 1440:960; 1440:960; 1440:959; 1440:960; 1440:1074
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, gsap, intersection, keyframes, request_animation_frame, swiper, transform, transition
  - Performance/accessibility concerns: heavy media count 22 and scripts 3; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
