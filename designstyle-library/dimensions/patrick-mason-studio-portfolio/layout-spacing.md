# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `P A T R I C K M A S O N Add Project Lauren Bamford Banduch The Global Studio Threadgate UTS 2020 Photography Grad UTS 2021 Photography Grad LoveArt UTS 2022 Photography Grad →`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 0, image count 16, document height 1000.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 1000}.
  - Media/card aspect stability: image natural sizes include 512x512; 512x512; 128x128; 128x128; 96x96; 96x96; 428x426; 428x426; 256x256; 256x256.
  - Observed border radii: 25px; 50%; 25px; 9999px; 9999px; 9999px; 9999px; 9999px; 9999px; 9999px; 9999px; 9999px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 1000}
  - Observed media ratios: 512:512; 512:512; 128:128; 128:128; 96:96; 96:96; 428:426; 428:426; 256:256; 256:256
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, framer, intersection, reduced_motion, request_animation_frame, transform, transition
  - Performance/accessibility concerns: heavy media count 16 and scripts 5; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
