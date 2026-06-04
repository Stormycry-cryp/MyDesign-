# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `Glyphs Get Glyphs Features Learn Forum Resources News Events EN Make things you love. Glyphs 3 is a Mac font editor that puts you in control: quickly draw high-precision vectors, efficiently reuse shapes, and easily manage any number of letters, figures and sy`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 24, image count 40, document height 6905.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 6905}.
  - Media/card aspect stability: image natural sizes include 576x576; 1152x1152; 576x576; 576x576; 91x91; 1440x1345; 1x1; 0x0; 1x1; 0x0.
  - Observed border radii: 5px; 5px; 5px; 5px; 5px; 5px; 5px; 5px; 10px; 5px; 10px; 5px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 6905}
  - Observed media ratios: 576:576; 1152:1152; 576:576; 576:576; 91:91; 1440:1345; 1:1; 1:1; 1:1; 1:1
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, gsap, request_animation_frame, transform, transition
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
