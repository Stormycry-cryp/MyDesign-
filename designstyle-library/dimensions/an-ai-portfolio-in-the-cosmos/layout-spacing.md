# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `BLR 11:16:28 PVG 13:46:28 00:02 X 0.0000 Y 0.0000 ABOUT EXPERIENCE IMPACT WORK ▾ RECOMMENDATIONS STACK ARTICLES CONTACT Not what a model outputs - how the system decides, executes, and holds under load. Ashwin Gupta ROLE AI Systems Engineer COMPANY Coforge Jun`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 7, image count 40, document height 1000.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 1000}.
  - Media/card aspect stability: image natural sizes include 800x1734; 960x961; 529x302; 529x302; 1935x517; 1935x517; 150x150; 200x200; 150x150; 361x140.
  - Observed border radii: 3px; 3px; 3px; 3px; 3px; 3px; 3px; 3px; 50%; 50%; 50%; 999px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 1000}
  - Observed media ratios: 800:1734; 960:961; 529:302; 529:302; 1935:517; 1935:517; 150:150; 200:200; 150:150; 361:140
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, intersection, keyframes, reduced_motion, request_animation_frame, transform, transition
  - Performance/accessibility concerns: heavy media count 40 and scripts 3; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
