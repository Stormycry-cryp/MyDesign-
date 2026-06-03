---
title: "La Mer"
source_url: "https://www.cremedelamer.com/"
captured_at: "2026-06-03"
tags: ["skincare", "luxury", "split-hero", "serif", "sea", "premium-commerce", "gift-campaign"]
style_tags: ["skincare", "luxury", "split-hero", "serif", "sea", "premium-commerce", "gift-campaign"]
structure_tags: ["split-hero", "full-bleed-media"]
motion_tags: ["source-video", "runtime-transform", "drawer-modal-overlay"]
code_tags: ["cdn-assets", "css-animation", "css-keyframes", "css-transition", "html-video", "request-animation-frame"]
best_for: ["premium skincare campaigns", "product ritual pages", "sea/mineral luxury positioning"]
avoid_for: ["indie natural brands", "clinical minimal formula pages", "playful DTC stores"]
evidence_screenshot: "screenshots/la-mer-split-luxury-product-story-desktop.png"
evidence_quality: "visual screenshot plus DOM/style/resource extraction"
---

# Style Reference: La Mer


## Essence
A classic luxury skincare system with a split hero: editorial serif story on one side and polished product still life on the other. The reusable idea is calm premium commerce where gift mechanics are present but visually subordinate to product aura.

## When To Use
- Premium skincare with strong product still-life and a sensory/sea/mineral origin story.
- Campaign pages that need product ritual, gifts, and luxury framing in one viewport.
- Brands with proprietary textures, jars, bottles, and reflective materials.

## When Not To Use
- Minimal science pages where big serif emotion would feel vague.
- Brands without premium product photography.
- Youthful social campaigns that need energy over composure.

## Evidence Snapshot
- Captured URL: https://www.cremedelamer.com/
- Page title: La Mer™ Official Site | Free Summer Skincare Gifts*
- Screenshot: screenshots/la-mer-split-luxury-product-story-desktop.png
- Viewport: 1440x1000
- H1 observed: not present in captured DOM
- H2 samples: SUMMERTIME SOOTHING, RESURFACEFOR RADIANCE, SUMMER SELECTS, The Broad Spectrum SPF 50 UV Protecting Fluid
- Navigation samples: Enjoy a complimentary mini duo with any purchase. Enter code: SUMMERDUO. Details., Claim your summer-ready gift with any eligible $375 purchase. Enter code: SOOTHE. Details., Account, Forgot Password?, Terms and Conditions, Privacy Policy, Sign In, Account Overview
- Images observed: 71; domains: www.cremedelamer.com, cdn.cookielaw.org
- Video observed: True; sources/domains recorded where available.
- Overlays or fixed elements: 14 fixed elements observed; treat cookie, cart, chat, region, and accessibility overlays as evidence limits, not style decisions.

## Visual System
- Layout: Top utility offer, left-aligned shop/discover/search, bag on right, split first viewport: copy panel left, image panel right. Oversized wordmark fragment anchors lower-left.
- Typography: Neue Haas Unica for retail; La Mer Headline/Text for luxury serif moments. Large serif display can use negative tracking, but should be checked for fit.
- Color: White, charcoal, soft gray, sea-glass greens from product imagery. Avoid broad beige monotony.
- Density: Spacious copy panel with retail utility around it; product grid below.
- Shape: Strict rectangular split; no cards.
- Shadow/depth: Reflections, marble/stone, glass bottle translucency.

## Typography And Reading Rhythm
- Observed font stack counts: "Neue Haas Unica Pro" (86); "Neue Haas Unica Pro", sans-serif (71); "La Mer Headline", serif (44); "La Mer Text" (17); sans-serif (2)
- Observed font sizes: 15px (118); 12px (36); 14px (23); 28px (17); 20px (15); 52px (5)
- Observed weights: 400 (194); 500 (10); 600 (10); 300 (5); 700 (1)
- Observed letter spacing: normal (106); 0.15px (69); 1px (13); 0.75px (12); -0.84px (7); -2.6px (5)
- Preserve the hierarchy relationship, not the exact proprietary typeface. Map brand display, retail UI, metadata, and CTA text separately.

## Color, Material, And Contrast
- Observed text colors: rgb(48, 48, 48) (78); rgb(102, 102, 102) (68); rgb(27, 27, 27) (44); rgb(255, 255, 255) (23); rgb(125, 125, 125) (3); rgb(255, 0, 0) (2)
- Observed backgrounds: rgba(0, 0, 0, 0) (205); rgb(255, 255, 255) (11); rgb(27, 27, 27) (4)
- Separate UI shell colors from asset-driven colors. If the palette comes from photography/video, recreate that through asset direction before choosing CSS colors.

## Layout Geometry And Spacing
- Record first viewport structure before borrowing: promo/header/nav, hero media, copy location, CTA location, next-section visibility.
- Preserve macro geometry such as split hero, centered brand nav, large media frame, or object crop. Do not reduce it to a generic hero-card layout.
- Use stable aspect ratios for media/product cards so brand imagery does not jump during loading.
- Observed border radii: not observed

## Dimension And Ratio System
- Viewport and document: viewport 1440x1000; document 1425x4271; overflowX 0.
- Observed media ratios: image: 1440x1800 (4:5); The Lip Balm: 340x340 (1:1); The Resurfacing Treatment: 340x340 (1:1); The Hand Treatment: 340x340 (1:1); The Body Crème: 340x340 (1:1); Crème de la Mer: 340x340 (1:1)
- Observed spacing samples: body 1425x4271, pt 0px, pb 0px, mt 0px, mb 0px; header 1425x130, pt 0px, pb 0px, mt 0px, mb 0px; a 465x18, pt 0px, pb 0px, mt 0px, mb 0px; a 45x21, pt 0px, pb 3px, mt 0px, mb 0px; a 61x18, pt 0px, pb 0px, mt 0px, mb 0px; header 1425x80, pt 0px, pb 0px, mt 0px, mb 0px
- Preserve ratios as implementation constraints: hero min-height, split width, product-card aspect-ratio, section gaps, fixed header height, and drawer/modal bounds.
- Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.

## Assets
- Image style: Polished product still-life on stone/water-reflective surfaces, premium jars and bottles.
- Illustration/icon style: Thin line utility icons.
- Texture/pattern: Stone, water, reflection, glass, cream jar surfaces.
- Production: Brand-hosted product assets and campaign imagery.

## Motion
- Page transitions: Luxury commerce standard.
- Micro-interactions: Header drawers, account forms, product carousel, bag.
- Scroll: Split hero can transition into product ritual sections; keep motion slow and stable.
- Timing: Premium 220-400ms; no springy motion.

## Motion Code And Runtime Evidence
- Motion source: video observed=True; video sources=not observed.
- CSS animation/transition evidence: motion hints=div, class=esearch-nav__animation-wrapper js-end-esearch-animation; section, class=content-block content-block-formatter js-animating-block js-animating-block--active content-container js-animate container-vertical-default; div, class=js-animating-content content-block-formatter__items animate animating done; div, class=hero content-block js-analytics-tag-content-module js-animate max-width-1440px
 js-contentmodule-analytics-processed scroll-animation js-ani; div, class=slick-track, style=opacity: 1; width: 6840px; transform: translate3d(-1368px, 0px, 0px);.
- Public CSS/JS probe keywords: animation, duration, easing, keyframes, request_animation_frame, transform, transform_function, transition.
- Public CSS/JS motion snippets: request_animation_frame: c=e.value,e.rating=c>r[1]?"poor":c>r[0]?"needs-improvement":"good",t(e))}},uE=function(t){requestAnimationFrame(function(){return requestAnimationFrame(function(){return t()})})},ub=function(t){var e=function(e){"pagehide"!==e.type&&"hidden"!==documen | duration: een{background-color:#16a085;box-shadow:0 0 5px 5px #70d2bf;animation:pulse_poa_recording 2s infinite;}@keyframes pulse_poa_recording{0%{box-shadow:0 0 0 0 rgba(112,210,91,0.8);}70%{box-shadow:0 0 0 10px rgba(112,210,91,0);}100%{box | easing: .scroll-animation{transition:all .5s ease-in-out;transform:translateY(120px);opacity:0}.scroll-animation.transition{transform:translateY(0);opacity:1}.animate{transition:all .5s ease-in-ou | transform_function: ick-slide{margin:0}.offer-banner-formatter .slick-arrow{z-index:10;margin-top:0;transform:translateY(-50%)}.offer-banner-formatter .slick-arrow::before{font-size:16px}.offer-banner-item{text-align:center;padding:10px 20px 14px 20px;width:85%;marg | keyframes: d-color:#16a085;box-shadow:0 0 5px 5px #70d2bf;animation:pulse_poa_recording 2s infinite;}@keyframes pulse_poa_recording{0%{box-shadow:0 0 0 0 rgba(112,210,91,0.8);}70%{box-shadow:0 0 0 10px rgba(112,210,91,0);}100%{box-shadow:0 0 0 0 rgba(112,210,91,0);}}.
- Exact motion parameters: transition: transition:all .5s ease-in-out | transition: transition:all .5s ease-in-ou | easing: ease-in-out | easing: ease-in | transform: transform:translateY(120px) | transform: transform:translateY(0) | transform_function: translateY(120px) | transform_function: translateY(0).
- JavaScript/runtime motion evidence: scripts=https://www.googletagmanager.com/gtag/js?id=G-FZSHM1QRCP&cx=c&gtm=4e6611h1; https://www.googletagmanager.com/gtag/js?id=AW-881094102&cx=c&gtm=4e6611h1; https://insights.bizrate.com/js/init.js; https://assets.pixlee.com/assets/pixlee_events.js; https://tr.snapchat.com/config/com/88e89d45-1ef3-46f9-81c1-4ea5e230370a.js?v=3.56.1-2604231811.
- Stylesheet evidence: css hrefs=https://www.cremedelamer.com/sites/cremedelamer2/files/css/css_Ciwm6LXnVFiL-IBAzSXeW-gOCm-8pCVvSaG0a-xsUk02.css; https://www.cremedelamer.com/sites/cremedelamer2/files/css/css_vBq6nIguIN-mlDqt_oPWeU6cYWqKmcvZQ-btLv7PtQA2.css; https://www.cremedelamer.com/sites/cremedelamer2/files/css/css_FF127INyMVSYFqOC6IQml0Ael7BvhK7Mwpd4C3d5FiI2.css; https://www.cremedelamer.com/sites/cremedelamer2/files/css/css_7u30SErbqHSkl-mGJP7QCNg1vSoud50b45Njru9jAzQ2.css; https://www.cremedelamer.com/sites/cremedelamer2/files/css/css_qftzPCDyfX8IpZxpCZ8YH1xLjRGWnYC0C3a2_EdwJdw2.css.
- Interpreted motion tags: source-video, runtime-transform, drawer-modal-overlay; code tags: cdn-assets, css-animation, css-keyframes, css-transition, html-video, request-animation-frame.
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
- CSS/source clues observed: stylesheet links 10, scripts 27, motion hints 14. Treat minified/public-source details as weak evidence unless inspected directly.

## Borrow
- Use split hero when you need both story and product inspection above the fold.
- Anchor luxury with material surfaces rather than gradients.
- Use a restrained offer strip; do not let promo mechanics dominate the hero.

## Avoid Copying
- Do not copy La Mer wordmark, sea-origin claims, or product stills.
- Do not use huge serif fragments if the brand name is not typographically strong.
- Do not overdo negative letter spacing; it can break mobile text.

## Evidence Limits
- This reference is based on a desktop capture and DOM/style/resource extraction, not a full multi-page audit.
- Cookie banners, region selectors, newsletter modals, carts, chat widgets, and accessibility widgets may appear in screenshots. They are cataloged as interaction states and should not be mistaken for the core aesthetic.
- Exact brand assets, campaign imagery, typefaces, product names, and proprietary claims must not be copied.

## Self Review
- Evidence quality: screenshot plus DOM/style/resource extraction is sufficient for visual and implementation direction; deeper source inspection remains optional.
- Reuse value: high for beauty/skincare/fragrance scene-fit because tags, best_for, visual geometry, typography, asset plan, motion, and interaction states are explicit.
- Missing pieces: mobile and product detail pages were not captured in this batch; add second-page/mobile captures for critical implementation work.
- Revision made: upgraded from broad style summary to high-dimensional evidence matrix with contamination notes and reference-to-implementation cues.
