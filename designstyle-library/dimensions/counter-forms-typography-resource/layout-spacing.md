# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `COUNTER FORMS TEXTS TYPEFACES WORKROOM INFORMATION C O U N T E R F O R M S ACKNOWLEDGEMENT OF COUNTRY Counter Forms was made on/across/between the stolen lands of many Sovereign people including on Wurundjeri and Whadjuk lands. We recognise our practices are s`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 0, image count 9, document height 3217.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 3217}.
  - Media/card aspect stability: image natural sizes include 660x449; 660x414; 660x429; 660x445; 660x470; 920x506; 660x380; 567x567; 567x567.
  - Observed border radii: 50%; 2px; 2px; 2px; 2px; 2px; 2px; 2px; 2px; 2px; 2px; 2px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 3217}
  - Observed media ratios: 660:449; 660:414; 660:429; 660:445; 660:470; 920:506; 660:380; 567:567; 567:567
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: easing, intersection, transform, transition
  - Performance/accessibility concerns: heavy media count 9 and scripts 14; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
