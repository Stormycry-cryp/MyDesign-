# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `System Font Enabled Bauhaus Clock for Mac Now on iPhone & iPad Turn waiting into watching. “An absolutely stunning screen saver for macOS.” Alexey Sekachov Founder of joi.software “This is absolutely stunning.” Chris Messina Inventor of #hashtag \"It's one of t`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 0, image count 40, document height 10226.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 10226}.
  - Media/card aspect stability: image natural sizes include 113x113; 113x113; 400x400; 320x320; 140x140; 400x400; 400x400; 400x400; 113x113; 213x213.
  - Observed border radii: 100px; 7.21272% / 94.2648%; 4px; 100px; 8px; 30px; 100%; 100%; 100%; 30px; 100%; 100%
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 10226}
  - Observed media ratios: 113:113; 113:113; 400:400; 320:320; 140:140; 400:400; 400:400; 400:400; 113:113; 213:213
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, keyframes, request_animation_frame
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
