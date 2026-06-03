---
title: "Monastery"
source_url: "https://monasterymade.com/"
captured_at: "2026-06-03"
tags: ["skincare", "botanical", "dark", "editorial", "split-hero", "spa", "handmade", "serif"]
style_tags: ["skincare", "botanical", "dark", "editorial", "split-hero", "spa", "handmade", "serif"]
structure_tags: ["split-hero", "editorial-modules"]
motion_tags: ["runtime-transform", "drawer-modal-overlay"]
code_tags: ["cdn-assets", "css-transition", "intersection-observer"]
best_for: ["dark luxury botanical skincare", "spa/editorial hybrids", "handmade premium brands"]
avoid_for: ["bright clean beauty", "clinical proof-heavy brands", "mass retail product grids"]
evidence_screenshot: "screenshots/monastery-dark-botanical-salon-desktop.png"
evidence_quality: "visual screenshot plus DOM/style/resource extraction"
---

# Style Reference: Monastery


## Essence
A dark botanical salon style that splits human editorial portraiture from floating formula textures, with fine borders and dramatic white serif copy. The reusable idea is handmade botanical luxury as intimate, mysterious, and tactile.

## When To Use
- Premium botanical skincare with rare ingredients, spa service, or handmade positioning.
- Sites that can support moody portraits, macro product textures, and minimal copy.
- Brands that want high editorial tension rather than sunny natural wellness.

## When Not To Use
- Approachable family/body-care shops.
- Clinical brands where darkness feels theatrical rather than trustworthy.
- Websites needing broad catalog scanning above the fold.

## Evidence Snapshot
- Captured URL: https://monasterymade.com/
- Page title: Home | Monastery
- Screenshot: screenshots/monastery-dark-botanical-salon-desktop.png
- Viewport: 1440x1000
- H1 observed: not present in captured DOM
- H2 samples: not present in captured DOM
- Navigation samples: SHOP NOW, SHOP NOW, SHOP NOW, Healing Botanical SkincareTM, Cart— 0, Shop, Spa, ABOUT
- Images observed: 80; domains: monasterymade.com, images.ctfassets.net, curator-assets.b-cdn.net
- Video observed: False; sources/domains recorded where available.
- Overlays or fixed elements: 10 fixed elements observed; treat cookie, cart, chat, region, and accessibility overlays as evidence limits, not style decisions.

## Visual System
- Layout: Red shipping strip, border-separated header, split hero with portrait left and black texture/product field right. Copy overlays the seam between halves.
- Typography: Garmond-like serif for brand/poetic copy, plainscribe-like uppercase sans for nav and CTAs. Strong contrast between elegant italics and tracked utility labels.
- Color: Black, off-white, muted red strip, dark botanical tones. Very high mood contrast.
- Density: Sparse above the fold, but fixed menu and back-in-stock affordance add commerce urgency.
- Shape: Thin lines, pill CTA, red pill notification.
- Shadow/depth: Deep photographic contrast and floating ingredient textures.

## Typography And Reading Rhythm
- Observed font stack counts: plainscribeFont, "plainscribeFont Fallback" (71); garmondFont, "garmondFont Fallback" (54)
- Observed font sizes: 12px (65); 16px (29); 24px (14); 36px (9); 14px (6); 13.3333px (2)
- Observed weights: 700 (71); 400 (54)
- Observed letter spacing: 1.8px (71); normal (24); -0.48px (19); 0.15008px (11)
- Preserve the hierarchy relationship, not the exact proprietary typeface. Map brand display, retail UI, metadata, and CTA text separately.

## Color, Material, And Contrast
- Observed text colors: rgb(241, 241, 241) (119); rgb(255, 255, 255) (6)
- Observed backgrounds: rgba(0, 0, 0, 0) (121); rgb(171, 6, 5) (2); rgb(6, 6, 6) (1); rgba(6, 6, 6, 0) (1)
- Separate UI shell colors from asset-driven colors. If the palette comes from photography/video, recreate that through asset direction before choosing CSS colors.

## Layout Geometry And Spacing
- Record first viewport structure before borrowing: promo/header/nav, hero media, copy location, CTA location, next-section visibility.
- Preserve macro geometry such as split hero, centered brand nav, large media frame, or object crop. Do not reduce it to a generic hero-card layout.
- Use stable aspect ratios for media/product cards so brand imagery does not jump during loading.
- Observed border radii: 36px (4); 20px (3); 88px (1)

## Dimension And Ratio System
- Viewport and document: viewport 1440x1000; document 1432x6462; overflowX 7.
- Observed media ratios: image: 81x81 (1:1); image: 1440x822 (16:9); image: 1440x1625 (0.89:1); image: 130x60 (2.17:1); image: 196x33 (5.94:1); image: 196x33 (5.94:1)
- Observed spacing samples: body 1425x6463, pt 0px, pb 0px, mt 0px, mb 0px; header 1425x118, pt 0px, pb 0px, mt 0px, mb 0px; p 1425x20, pt 0px, pb 0px, mt 0px, mb 0px; a 81x14, pt 0px, pb 0px, mt 0px, mb 0px; a 140x31, pt 0px, pb 0px, mt 0px, mb 0px; a 110x79, pt 8px, pb 8px, mt 0px, mb 0px
- Preserve ratios as implementation constraints: hero min-height, split width, product-card aspect-ratio, section gaps, fixed header height, and drawer/modal bounds.
- Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.

## Assets
- Image style: Moody portrait crop, isolated serum/oil textures on black, editorial spa imagery.
- Illustration/icon style: Little to none; typography and photography carry identity.
- Texture/pattern: Oil droplets, creams, dark botanical extracts.
- Production: Large first-party/Contentful images and fixed editorial composition.

## Motion
- Page transitions: Dramatic but sparse.
- Micro-interactions: Fixed header, menu overlays, back-in-stock button, booking iframe.
- Scroll: Slow reveal can fit; avoid too many moving pieces.
- Timing: Use slower 300-500ms fades for editorial mood.

## Motion Code And Runtime Evidence
- Motion source: video observed=False; video sources=not observed.
- CSS animation/transition evidence: motion hints=div, class=slick-track, style=width: 1425px; opacity: 1; transform: translate3d(0px, 0px, 0px); transition: -webkit-transform 500ms;; div, class=MuiBox-root css-bx1hpa, style=opacity: 0; display: none; transform: translateY(-100%) translateZ(0px);; div, class=MuiBox-root css-xi606m, style=opacity: 1; transform: none;.
- Public CSS/JS probe keywords: duration, easing, intersection, transform, transform_function, transition.
- Public CSS/JS motion snippets: intersection: null)}let p="function"==typeof WeakMap?new WeakMap:new Map,y=new Set,g="function"==typeof IntersectionObserver?new IntersectionObserver(function(e){for(let t of e){let e=t.intersectionRatio>0;P(t.target,e)}},{rootMargin:"200px"}):null;function v(e,t) | duration: e;top:15px;right:15px;width:28px;height:28px;cursor:pointer;transition:-webkit-transform .2s;transition:transform .2s;transition:transform .2s,-webkit-transform .2s;fill:#fff}.blvd-close-button:hover{-webkit-transform:scale(1.25);-m | easing: ;left:0;width:100%;max-width:550px!important;height:100%;transition:-webkit-transform .5s ease-in-out;transition:transform .5s ease-in-out;transition:transform .5s ease-in-out,-webkit-transform .5s ease-in-out;-webkit-transform:translateX(-1 | transform_function: 0px;padding:0;font-size:0;line-height:0;display:block;position:absolute;top:50%;transform:translateY(-50%)}.slick-prev:hover,.slick-prev:focus,.slick-next:hover,.slick-next:focus{color:#0000;background:0 0;outline:none}.slick-prev:hover:before,.s | transition: -close-button{position:absolute;top:15px;right:15px;width:28px;height:28px;cursor:pointer;transition:-webkit-transform .2s;transition:transform .2s;transition:transform .2s,-webkit-transform .2s;fill:#fff}.blvd-close-button:hover{-webkit-transform:scale(1.25);.
- Exact motion parameters: transition: transition:-webkit-transform .2s | transition: transition:transform .2s | transition: transition:transform .2s,-webkit-transform .2s | transform: transform:scale(1.25) | transform_function: scale(1.25) | duration: 2s | transition: transition:opacity .2s | transition: transition:-webkit-transform .5s ease-in-out.
- JavaScript/runtime motion evidence: scripts=https://us-assets.i.posthog.com/static/array.js; https://static.joinboulevard.com/injector.min.js; https://consent.cookiebot.com/3b8c0be4-9578-432d-a69b-ef705734acf8/cc.js?renew=false&referer=monasterymade.com&dnt=false&init=false; https://consentcdn.cookiebot.com/consentconfig/3b8c0be4-9578-432d-a69b-ef705734acf8/monasterymade.com/configuration.js; https://monasterymade.com/_next/static/chunks/a4e9ade9f804e433.js?dpl=dpl_6DbCFjVSXAWcgtWmg4GTjq2SCvZT.
- Stylesheet evidence: css hrefs=https://monasterymade.com/_next/static/chunks/41d737c6ed5e3367.css?dpl=dpl_6DbCFjVSXAWcgtWmg4GTjq2SCvZT; https://monasterymade.com/_next/static/chunks/dd45105e86fa9005.css?dpl=dpl_6DbCFjVSXAWcgtWmg4GTjq2SCvZT; https://cdn-static.okendo.io/reviews-widget-plus/css/okendo-reviews-styles.6dbb2446.css; https://cdn-static.okendo.io/reviews-widget-plus/css/modules/okendo-star-rating.4cb378a8.css.
- Interpreted motion tags: runtime-transform, drawer-modal-overlay; code tags: cdn-assets, css-transition, intersection-observer.
- Use this as implementation guidance only where evidence is direct. If CSS/JS is minified or only CDN names are visible, mark library/framework attribution as weak.

## Interaction And Components
- Navigation: capture exact density, category depth, logo position, and whether search/account/cart are visible.
- Buttons/links: note whether CTAs are text links, outlined rectangles, pills, filled blocks, or media overlays.
- Cards/sections: preserve product-card image ratio, badge strategy, price/title density, and whether cards are framed or unframed.
- Forms/inputs: region selectors, newsletter modals, diagnostic flows, account/cart drawers, and search overlays are common in beauty commerce.
- Feedback states: cart empty, waitlist, sale/offer drawer, cookie/region modals, loading placeholders, and accessibility widgets should be recorded as states, not ignored.

## Implementation Notes
- CSS/layout primitives: full-bleed media, split panels, sticky/fixed header, product grid, media aspect ratios, drawers/modals, and responsive nav.
- Token ideas: keep tokens for shell background, ink, accent, display font, UI font, section gap, hero min-height, media radius, CTA shape, badge treatment, overlay opacity.
- Libraries or techniques: ecommerce sites often use Shopify/headless CMS/CDN image transforms; do not assume framework unless public evidence shows it.
- Performance/accessibility: lazy-load product grids, preserve image dimensions, expose video pause/mute where video is central, and avoid hiding nav behind inaccessible overlays.
- CSS/source clues observed: stylesheet links 4, scripts 30, motion hints 3. Treat minified/public-source details as weak evidence unless inspected directly.

## Borrow
- Use split hero to contrast human skin and formula material.
- Let one strong line of poetic claim sit over the image seam.
- Use dark botanical texture when the brand has handmade/rare ingredient credibility.

## Avoid Copying
- Do not copy Monastery's exact split image, wording, or red strip.
- Do not use this for cheerful natural brands.
- Do not let dark mood hide navigation or purchase controls.

## Evidence Limits
- This reference is based on a desktop capture and DOM/style/resource extraction, not a full multi-page audit.
- Cookie banners, region selectors, newsletter modals, carts, chat widgets, and accessibility widgets may appear in screenshots. They are cataloged as interaction states and should not be mistaken for the core aesthetic.
- Exact brand assets, campaign imagery, typefaces, product names, and proprietary claims must not be copied.

## Self Review
- Evidence quality: screenshot plus DOM/style/resource extraction is sufficient for visual and implementation direction; deeper source inspection remains optional.
- Reuse value: high for beauty/skincare/fragrance scene-fit because tags, best_for, visual geometry, typography, asset plan, motion, and interaction states are explicit.
- Missing pieces: mobile and product detail pages were not captured in this batch; add second-page/mobile captures for critical implementation work.
- Revision made: upgraded from broad style summary to high-dimensional evidence matrix with contamination notes and reference-to-implementation cues.
