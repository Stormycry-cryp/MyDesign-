# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `Back Product Product Use Cases Use Cases Solutions Solutions Resources Resources Company Company Pricing Pricing ⌘ K Log in Get a demo Start free trial FEATURES Claygents Research target companies and people with AI Waterfall Combine multiple data providers fo`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 24, image count 40, document height 9326.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 9326}.
  - Media/card aspect stability: image natural sizes include 0x0; 509x163; 300x300; 300x300; 150x150; 300x300; 361x380; 88x88; 88x88; 150x150.
  - Observed border radii: 0px 0px 24px 24px; 10px; 4px; 4px; 8px; 12px; 12px; 0px 0px 24px 24px; 8px; 8px; 8px; 8px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 9326}
  - Observed media ratios: 509:163; 300:300; 300:300; 150:150; 300:300; 361:380; 88:88; 88:88; 150:150; 300:300
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, keyframes, request_animation_frame, swiper, transform, transition
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
