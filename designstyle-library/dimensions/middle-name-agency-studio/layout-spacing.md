# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `ABOUT TESTIMONIALS CONTACT INSTAGRAM Middle Name is a branding and design studio. With a strategic and collaborative approach, we create brands with intelligence, character, and clarity. GET IN TOUCH`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 4, image count 40, document height 1492.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 1492}.
  - Media/card aspect stability: image natural sizes include 384x512; 384x256; 384x512; 384x256; 300x375; 384x512; 384x512; 384x256; 384x288; 384x512.
  - Observed border radii: 12px; 12px; 12px; 12px; 12px; 12px; 12px; 12px; 12px; 12px; 12px; 12px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 1492}
  - Observed media ratios: 384:512; 384:256; 384:512; 384:256; 300:375; 384:512; 384:512; 384:256; 384:288; 384:512
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, gsap, keyframes, request_animation_frame, transform, transition
  - Performance/accessibility concerns: heavy media count 40 and scripts 2; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
