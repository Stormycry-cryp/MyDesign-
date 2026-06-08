# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `SKIP TO CONTENT MODELS CULTURE COLLABORATIONS YOUR BENTLEY ABOUT BENTLEY REQUEST TEST DRIVE CONFIGURATOR LOCATE DEALER 1 / 8 New Flying Spur Breathtaking craftsmanship, unrivalled comfort and performance few cars can match. EXPLORE NOW CREATE YOUR OWN Bentley `.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 3, image count 40, document height 6028.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 6028}.
  - Media/card aspect stability: image natural sizes include 1000x500; 1000x500; 1343x671; 50x25; 1343x671; 50x25; 1343x671; 50x25; 1343x671; 50x25.
  - Observed border radii: none observed
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 6028}
  - Observed media ratios: 1000:500; 1000:500; 1343:671; 50:25; 1343:671; 50:25; 1343:671; 50:25; 1343:671; 50:25
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, intersection, keyframes, request_animation_frame, transform, transition
  - Performance/accessibility concerns: heavy media count 40 and scripts 11; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
