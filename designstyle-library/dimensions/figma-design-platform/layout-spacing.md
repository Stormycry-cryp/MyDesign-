# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `Skip to main content Products Solutions Community Resources Pricing Log in Contact sales Get started for free Make anything possible, all in Figma Make anything possible, all in Figma Make anyth​ Get started SLIDE 1 OF 8 1 OF 8 Figma lets you turn big ideas in`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 4, image count 40, document height 9460.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 9460}.
  - Media/card aspect stability: image natural sizes include 1440x810; 1440x810; 71x22; 146x18; 92x18; 140x36; 67x18; 86x18; 100x48; 153x20.
  - Observed border radii: 8px; 8px; 18px; 16px; 8px; 50%; 50%; 50%; 50px; 50px; 50px; 50px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 9460}
  - Observed media ratios: 1440:810; 1440:810; 71:22; 146:18; 92:18; 140:36; 67:18; 86:18; 100:48; 153:20
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, intersection, request_animation_frame, transform, transition
  - Performance/accessibility concerns: heavy media count 40 and scripts 10; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
