---
title: "Augustinus Bader"
source_url: "https://augustinusbader.com/int/en/"
captured_at: "2026-06-03"
tags: ["skincare", "luxury", "science", "clinical-proof", "premium-commerce", "serif-sans", "black-white-copper"]
style_tags: ["skincare", "luxury", "science", "clinical-proof", "premium-commerce", "serif-sans", "black-white-copper"]
structure_tags: ["commerce-hero"]
motion_tags: ["runtime-transform", "drawer-modal-overlay"]
code_tags: ["cdn-assets", "css-animation", "css-keyframes", "css-transition", "gsap-motion", "request-animation-frame"]
best_for: ["science-backed luxury skincare", "clinical trial proof pages", "premium product category pages"]
avoid_for: ["small natural indie brands", "playful wellness shops", "pages without credible proof assets"]
evidence_screenshot: "screenshots/augustinus-bader-science-luxury-desktop.png"
evidence_quality: "visual screenshot plus DOM/style/resource extraction"
---

# Style Reference: Augustinus Bader


## Essence
A science-luxury commerce language that combines polished product/editorial imagery with formal proof, membership, trials, and founder authority. The reusable idea is premium clinical confidence: high commerce clarity plus research-backed prestige.

## When To Use
- High-price skincare where authority, trial metrics, and proprietary technology justify purchase.
- Product pages that need to balance beauty photography with founder/science sections.
- Brands with strong packaging and a credible research narrative.

## When Not To Use
- Brands without scientific proof or named technology.
- Warm botanical lifestyle pages where clinical authority would feel cold.
- Minimal one-product launches that cannot support the proof layer.

## Evidence Snapshot
- Captured URL: https://augustinusbader.com/int/en/
- Page title: Luxury Skin Creams & Serums | Augustinus Bader
- Screenshot: screenshots/augustinus-bader-science-luxury-desktop.png
- Viewport: 1440x1000
- H1 observed: Award-Winning, Skincare, Introducing, The Geranium Rose Body Cream
- H2 samples: My Bag, Trending Products, Trending Products, Trending Products
- Navigation samples: FAQ, Contact, Store Locator, English US ($), English UK (£), English EU (€), French (€), German (€)
- Images observed: 80; domains: static.augustinusbader.com, media.augustinusbader.com
- Video observed: False; sources/domains recorded where available.
- Overlays or fixed elements: 14 fixed elements observed; treat cookie, cart, chat, region, and accessibility overlays as evidence limits, not style decisions.

## Visual System
- Layout: Utility promo strip, category nav, large split campaign/product surfaces, then proof/trending sections. Drawers and cookie overlays are prominent in evidence, so modal behavior must be handled carefully.
- Typography: MaisonNeue/sans-serif majority, with refined serif-like campaign headings in screenshot. Font weights range 400/600/700; copy remains restrained.
- Color: White and black base with copper/rose-gold accent around rgb(207,156,135). Accent implies science-luxury warmth without turning into beige.
- Density: Medium-high navigation and commerce density; hero and proof sections stay spacious.
- Shape: Mostly rectangular modules; small radii in product chips and controls.
- Shadow/depth: Depth through glossy packaging, reflections, clinical/editorial photography.

## Typography And Reading Rhythm
- Observed font stack counts: sans-serif (156); MaisonNeue, Arial, Helvetica, sans-serif (64)
- Observed font sizes: 15px (156); 16px (44); 14px (20)
- Observed weights: 400 (126); 700 (57); 600 (37)
- Observed letter spacing: 0.1px (155); normal (64); 0.3px (1)
- Preserve the hierarchy relationship, not the exact proprietary typeface. Map brand display, retail UI, metadata, and CTA text separately.

## Color, Material, And Contrast
- Observed text colors: rgb(21, 21, 21) (126); rgb(0, 0, 0) (64); rgb(207, 156, 135) (29); rgb(255, 255, 255) (1)
- Observed backgrounds: rgba(0, 0, 0, 0) (215); rgb(255, 255, 255) (4); rgb(21, 21, 21) (1)
- Separate UI shell colors from asset-driven colors. If the palette comes from photography/video, recreate that through asset direction before choosing CSS colors.

## Layout Geometry And Spacing
- Record first viewport structure before borrowing: promo/header/nav, hero media, copy location, CTA location, next-section visibility.
- Preserve macro geometry such as split hero, centered brand nav, large media frame, or object crop. Do not reduce it to a generic hero-card layout.
- Use stable aspect ratios for media/product cards so brand imagery does not jump during loading.
- Observed border radii: 7.5px (49); 3.75px (4)

## Dimension And Ratio System
- Viewport and document: viewport 1440x1000; document 1432x7245; overflowX -8.
- Observed media ratios: logo: 61x46 (1.33:1); opens in a new window: 18x18 (1:1); opens in a new window: 18x18 (1:1); opens in a new window: 18x18 (1:1); opens in a new window: 18x18 (1:1); opens in a new window: 18x18 (1:1)
- Observed spacing samples: body 1432x7245, pt 0px, pb 0px, mt 0px, mb 0px; li 300x60, pt 0px, pb 0px, mt 0px, mb 0px; a 300x60, pt 15px, pb 15px, mt 0px, mb 0px; li 300x60, pt 0px, pb 0px, mt 0px, mb 0px; a 300x60, pt 15px, pb 15px, mt 0px, mb 0px; li 300x60, pt 0px, pb 0px, mt 0px, mb 0px
- Preserve ratios as implementation constraints: hero min-height, split width, product-card aspect-ratio, section gaps, fixed header height, and drawer/modal bounds.
- Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.

## Assets
- Image style: Premium product stills, campaign lifestyle, founder/science imagery, clinical trial proof graphics.
- Illustration/icon style: Fine line utility icons and science badges.
- Texture/pattern: Gloss, serum smear, lab/skin-care surfaces.
- Production: Dedicated media/static asset domains; heavy product imagery.

## Motion
- Page transitions: Commerce-stable.
- Micro-interactions: Drawers, cart, mega-menu, product hover, membership CTAs.
- Scroll: Proof stats can reveal sequentially; avoid over-animated science claims.
- Timing: Sober 180-300ms interactions; proof should feel reliable.

## Motion Code And Runtime Evidence
- Motion source: video observed=False; video sources=not observed.
- CSS animation/transition evidence: motion hints=div, class=flex flex-row justify-center items-center w-full h-full fixed select-none z-[1000] bg-white/70, style=left: 50%; top: 50%; transform: translateX(-50%) translateY(-50%); display: none;; button, class=p-2 text-gray-300 transition duration-150 ease-in-out hover:text-black; li, class=tab-title !list-none uppercase cursor-pointer font-medium pb-1 !pl-0 !ml-0 !indent-0 transition-all border-b-2 border-black; li, class=tab-title !list-none uppercase cursor-pointer font-medium pb-1 !pl-0 !ml-0 !indent-0 transition-all; li, class=tab-title !list-none uppercase cursor-pointer font-medium pb-1 !pl-0 !ml-0 !indent-0 transition-all.
- Public CSS/JS probe keywords: animation, duration, easing, gsap, keyframes, request_animation_frame, scroll_snap, transform, transform_function, transition, video.
- Public CSS/JS motion snippets: gsap: =n.Quart=n.Cubic=n.Quad=n.Linear=n.Power4=n.Power3=n.Power2=n.Power1=n.Power0=n.default=n.gsap=n.PropTween=n.TweenLite=n.TweenMax=n.Tween=n.TimelineLite=n.TimelineMax=n.Timeline=n.Animation=n.GSCache=void 0;var o,s,a,u,l,_,c,h,$,p,f,d | request_animation_frame: ions||(v.gsapVersions=[])).push(eG.version),tt(J||v.GreenSockGlobals||!v.gsap&&v||{}),a=v.requestAnimationFrame),o&&u.sleep(),s=a||function(t){return setTimeout(t,1e3*(f-u.time)+1|0)},w=1,g(2))},sleep:function(){(a?v.cancelAnimationFrame:clearTimeout) | duration: ackdrop-filter,-webkit-backdrop-filter;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.2s}.button-raw:hover{border-style:none;opacity:.9}@media (min-width:768px){.button-raw{max-width:272px}}.arrow-button-raw{position:absolute;to | easing: r,fill,stroke,opacity,box-shadow,transform,filter,backdrop-filter,-webkit-backdrop-filter;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.2s}.button-raw:hover{border-style:none;opacity:.9}@media (min-width:768px){.button-raw{max-width:2 | transform_function: ],.-translate-y-\[50\%\]{transform:translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))}.-translate-y-\[50\%\]{--tw-translate-.
- Exact motion parameters: transition: transition-property:color,background-color,border-color,text-decoration-color,fill,stroke,opacity,box-shadow,transform,filter,-webkit-backdrop-filter | transition: transition-property:color,background-color,border-color,text-decoration-color,fill,stroke,opacity,box-shadow,transform,filter,backdrop-filt | transition: transition-property:color,background-color,border-color,text-decoration-color,fill,stroke,opacity,box-shadow,transform,filter,backdrop-filter | transition: transition-property:color,background-color,border-color,text-decoration-color,fill,stroke,opacity,box-shadow,transform,filter,backdrop-filter,-webkit-backdrop-filter | transition: transition-timing-function:cubic-bezier(.4,0,.2,1) | transition: transition-duration:.2s | easing: cubic-bezier(.4,0,.2,1) | duration: 2s.
- JavaScript/runtime motion evidence: scripts=https://widget.intercom.io/widget/n1u129wp; https://www.googletagmanager.com/gtag/js?id=G-NJ8F0BS45K&cx=c&gtm=4e6611h1; https://www.googletagmanager.com/gtag/js?id=AW-792719427&cx=c&gtm=4e6611h1; https://consent.cookiebot.com/88ed2949-00f2-4dc7-b672-4e3943d3dee2/cc.js?renew=false&referer=augustinusbader.com&dnt=false&init=false; https://analytics-api.augustinusbader.com/js/exponea.min.js.
- Stylesheet evidence: css hrefs=https://static.augustinusbader.com/version1779958417/frontend/AugustinusBader/hyva2025/en_US/Ab_ContentComponents/css/components.css; https://static.augustinusbader.com/version1779958417/frontend/AugustinusBader/hyva2025/en_US/css/styles.css; https://static.augustinusbader.com/version1779958417/frontend/AugustinusBader/hyva2025/en_US/Afterpay_Afterpay/css/afterpay-express-checkout.css; https://static.augustinusbader.com/version1779958417/frontend/AugustinusBader/hyva2025/en_US/Hyva_PayPalBraintree/css/apple-pay.css; https://static.augustinusbader.com/version1779958417/frontend/AugustinusBader/hyva2025/en_US/Hyva_PayPalBraintree/css/google-pay.css.
- Interpreted motion tags: runtime-transform, drawer-modal-overlay; code tags: cdn-assets, css-animation, css-keyframes, css-transition, gsap-motion, request-animation-frame.
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
- CSS/source clues observed: stylesheet links 5, scripts 13, motion hints 21. Treat minified/public-source details as weak evidence unless inspected directly.

## Borrow
- Add a proof architecture: founder/science, trial metrics, product technology, membership rewards.
- Use one restrained metallic accent only where it signals premium science.
- Keep cart/category/search affordances obvious even on luxury pages.

## Avoid Copying
- Do not copy TFC8, founder imagery, product names, or copper brand marks.
- Do not invent trial metrics; this style requires real evidence.
- Do not let cookie/modals cover the core capture when adding future references.

## Evidence Limits
- This reference is based on a desktop capture and DOM/style/resource extraction, not a full multi-page audit.
- Cookie banners, region selectors, newsletter modals, carts, chat widgets, and accessibility widgets may appear in screenshots. They are cataloged as interaction states and should not be mistaken for the core aesthetic.
- Exact brand assets, campaign imagery, typefaces, product names, and proprietary claims must not be copied.

## Self Review
- Evidence quality: screenshot plus DOM/style/resource extraction is sufficient for visual and implementation direction; deeper source inspection remains optional.
- Reuse value: high for beauty/skincare/fragrance scene-fit because tags, best_for, visual geometry, typography, asset plan, motion, and interaction states are explicit.
- Missing pieces: mobile and product detail pages were not captured in this batch; add second-page/mobile captures for critical implementation work.
- Revision made: upgraded from broad style summary to high-dimensional evidence matrix with contamination notes and reference-to-implementation cues.
