# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `Observable Notebooks 2.0 is here! Read the preview announcement Notebooks Resources Pricing Sign in Get started Not your typical notebook Observable’s reactive JavaScript notebooks are uniquely suited for interactive data visualization, animation, learning, an`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 2, image count 40, document height 7709.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 7709}.
  - Media/card aspect stability: image natural sizes include 600x400; 640x443; 600x300; 600x400; 600x250; 600x300; 600x510; 982x381; 600x300; 600x400.
  - Observed border radii: 2px; 2px; 2px; 4px; 4px; 4px; 4px; 4px; 4px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 7709}
  - Observed media ratios: 600:400; 640:443; 600:300; 600:400; 600:250; 600:300; 600:510; 982:381; 600:300; 600:400
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, gsap, intersection, keyframes, reduced_motion, request_animation_frame, transform, transition
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
