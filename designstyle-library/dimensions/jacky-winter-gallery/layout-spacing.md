# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `Exhibitions About Jacky Winter Gallery Contact Best Before Karan Singh 15 May – 20 Jun, 2026 NOW SHOWING PAST SHOW ALL PAST SHOWS NOW SHOWING PAST SHOW ALL PAST SHOWS We are currently open To receive show catalogues or get updates on our openings and events, s`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 4, image count 19, document height 11796.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 11796}.
  - Media/card aspect stability: image natural sizes include 1500x2000; 1500x2338; 1500x1960; 1500x2000; 1500x2338; 1500x1960; 200x267; 200x312; 200x261; 2000x1500.
  - Observed border radii: 17.5px; 17.5px; 17.5px; 17.5px; 17.5px; 17.5px; 17.5px; 17.5px; 17.5px; 17.5px; 17.5px; 17.5px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 11796}
  - Observed media ratios: 1500:2000; 1500:2338; 1500:1960; 1500:2000; 1500:2338; 1500:1960; 200:267; 200:312; 200:261; 2000:1500
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, intersection, keyframes, reduced_motion, transform, transition
  - Performance/accessibility concerns: heavy media count 19 and scripts 12; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
