# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `Explore Careers Try 'vitsoe shelving' Login Sign up Your space for inspiration Sign up Get the app Watch our new film (ft. Odessa A’zion) Every search opens a new world. future home Your collections, your references, your taste. Connected, searchable, yours. S`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 5, image count 40, document height 6422.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 6422}.
  - Media/card aspect stability: image natural sizes include 600x875; 600x751; 600x900; 600x1291; 600x1103; 600x484; 600x1111; 600x658; 600x1009; 600x780.
  - Observed border radii: 3.35544e+07px; 3.35544e+07px; 3.35544e+07px; 3.35544e+07px; 3.35544e+07px; 3.35544e+07px; 3.35544e+07px; 3.35544e+07px; 3.35544e+07px; 3.35544e+07px; 3.35544e+07px; 3.35544e+07px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 6422}
  - Observed media ratios: 600:875; 600:751; 600:900; 600:1291; 600:1103; 600:484; 600:1111; 600:658; 600:1009; 600:780
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, intersection, keyframes, reduced_motion, request_animation_frame, transform, transition
  - Performance/accessibility concerns: heavy media count 40 and scripts 36; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
