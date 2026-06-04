# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `📈 No more QPS limits on Developer Plans We're removing QPS limits from Developer Plans and switching to vCPU-based billing. Pay for the compute you use, not the number of requests you make. Read the announcement Read the announcement Product [ ] Pricing Docs R`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 0, image count 18, document height 9556.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1425, 'docH': 9556}.
  - Media/card aspect stability: image natural sizes include 717x1200; 96x97; 111x111; 0x0; 0x0; 0x0; 0x0; 0x0; 0x0; 0x0.
  - Observed border radii: 4px; 4px; 4px; 4px; 4px; 4px; 8px; 3.35544e+07px; 8px; 4px; 4px; 4px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1425, 'docH': 9556}
  - Observed media ratios: 717:1200; 96:97; 111:111
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, intersection, keyframes, reduced_motion, request_animation_frame, swiper, transform, transition
  - Performance/accessibility concerns: heavy media count 18 and scripts 36; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
