# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `ABOUT BUILDERS CAREERS ECOSYSTEM START BUILDING ECLIPSE IS SOLANA ON ETHEREUM Ethereum’s First SVM L2 ECLIPSE IS SOLANA ON ETHEREUM ETHEREUM’S FIRST SVM L2 BRIDGE TO ECLIPSE BUILD ON ECLIPSE ETHEREUM’S FASTEST LAYER 2 POWERED BY SVM ETHEREUM’S FASTEST LAYER 2 `.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 5, image count 9, document height 8157.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 28016, 'docH': 8157}.
  - Media/card aspect stability: image natural sizes include 1440x632; 1440x368; 1134x876; 1440x382; 1440x462; 1440x810; 720x720; 720x720; 1439x1772.
  - Observed border radii: 100px; 100px; 100px; 100px; 100px; 100px; 25px; 25px; 50%; 25px; 25px; 50%
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 28016, 'docH': 8157}
  - Observed media ratios: 1440:632; 1440:368; 1134:876; 1440:382; 1440:462; 1440:810; 720:720; 720:720; 1439:1772
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, gsap, keyframes, request_animation_frame, swiper, transform, transition
  - Performance/accessibility concerns: heavy media count 9 and scripts 16; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
