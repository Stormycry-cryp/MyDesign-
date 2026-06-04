# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `EXPEDITED ONBOARDING FOR SVB CUSTOMERS CAPITAL CAPITAL HAS JOINED RHO • LEARN MORE Modern companies are built on Capital Earn 4% APY on all of your money Free, high-yield banking services with automated fundraising built right in. CAPITAL CUSTOMERS FOUNDERS IN`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 1, image count 25, document height 7402.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 7402}.
  - Media/card aspect stability: image natural sizes include 28x24; 152x152; 28x24; 1757x1483; 128x128; 128x128; 128x24; 128x82; 90x93; 0x0.
  - Observed border radii: 24px; 24px; 24px; 8px; 9px; 8px; 16px; 24px; 24px; 16px; 16px; 16px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 7402}
  - Observed media ratios: 28:24; 152:152; 28:24; 1757:1483; 128:128; 128:128; 128:24; 128:82; 90:93; 28:24
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, gsap, keyframes, request_animation_frame, transform, transition
  - Performance/accessibility concerns: heavy media count 25 and scripts 25; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
