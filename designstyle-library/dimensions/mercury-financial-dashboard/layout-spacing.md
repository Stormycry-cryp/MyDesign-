# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `Products Solutions Resources About Pricing Log in Open account Radically different banking Apply online in 10 minutes to experience banking1 unlike anything that’s come before. Enter your email Open account Mercury will occasionally send you emails with offers`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 4, image count 35, document height 13147.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 13147}.
  - Media/card aspect stability: image natural sizes include 3840x1440; 3840x1440; 3840x1440; 0x0; 0x0; 0x0; 0x0; 0x0; 0x0; 0x0.
  - Observed border radii: 4px; 40px; 40px; 40px; 40px; 40px; 40px; 32px; 32px; 32px; 12px; 4px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 13147}
  - Observed media ratios: 3840:1440; 3840:1440; 3840:1440; 24:16; 24:16; 24:24; 19:24; 24:24; 19:24; 24:16
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, keyframes, reduced_motion, request_animation_frame, transform, transition
  - Performance/accessibility concerns: heavy media count 35 and scripts 36; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
