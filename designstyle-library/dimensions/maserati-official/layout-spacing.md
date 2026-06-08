# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `MODELS PURCHASE EXPERIENCES BRAND CONFIGURE NOW BROWSE INVENTORY EN DRIVE AHEAD IN REFINED STYLE MASERATI VEHICLES A CENTURY OF A GLOBAL ICON THE YEAR OF THE TRIDENT BEST IN CLASS LEGROOM AND POWER. NOW ALSO AVAILABLE AS EV \"GRECALE FOLGORE\" GRECALE INTRODUCIN`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 0, image count 40, document height 8383.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1471, 'docH': 8383}.
  - Media/card aspect stability: image natural sizes include 1500x822; 1500x822; 1500x822; 1500x822; 1005x672; 1500x822; 1500x822; 1005x672; 1440x810; 1440x810.
  - Observed border radii: 50%; 50%; 50%; 2.5px; 2.5px; 2.5px; 2.5px; 2.5px; 2.5px; 2.5px; 2.5px; 2.5px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1471, 'docH': 8383}
  - Observed media ratios: 1500:822; 1500:822; 1500:822; 1500:822; 1005:672; 1500:822; 1500:822; 1005:672; 1440:810; 1440:810
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, intersection, keyframes, request_animation_frame, transform, transition
  - Performance/accessibility concerns: heavy media count 40 and scripts 12; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
