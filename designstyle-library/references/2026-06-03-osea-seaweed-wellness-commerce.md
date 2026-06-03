---
title: "Osea Malibu"
source_url: "https://oseamalibu.com/"
captured_at: "2026-06-03"
tags: ["skincare", "sea", "wellness", "natural", "green", "friendly-commerce", "routine-builder"]
style_tags: ["skincare", "sea", "wellness", "natural", "green", "friendly-commerce", "routine-builder"]
structure_tags: ["full-bleed-media"]
motion_tags: ["source-video", "runtime-transform", "drawer-modal-overlay"]
code_tags: ["cdn-assets", "css-animation", "css-keyframes", "css-transition", "html-video", "reduced-motion-css", "request-animation-frame", "shopify-runtime"]
best_for: ["ocean/seaweed skincare", "warm natural wellness commerce", "routine-builder stores"]
avoid_for: ["ultra-minimal monochrome brands", "high-fashion fragrance", "hard clinical pages"]
evidence_screenshot: "screenshots/osea-seaweed-wellness-commerce-desktop.png"
evidence_quality: "visual screenshot plus DOM/style/resource extraction"
---

# Style Reference: Osea Malibu


## Essence
A sea-powered wellness store using fresh photography, rounded controls, green identity, and friendly category navigation. The reusable idea is natural efficacy made approachable through ocean light, human use, and routine-building commerce.

## When To Use
- Natural skincare/body care where ingredients connect to sea, minerals, hydration, or summer skin.
- Stores that need approachable routine navigation and product recommendations.
- Brands that want warmth without losing product clarity.

## When Not To Use
- Ultra-luxury pages that need silence and restraint.
- Clinical formula brands where rounded friendliness reduces seriousness.
- Dark moody spa pages.

## Evidence Snapshot
- Captured URL: https://oseamalibu.com/
- Page title: OSEA® Malibu - Skincare from the Sea | Vegan Skincare Brand & Products
- Screenshot: screenshots/osea-seaweed-wellness-commerce-desktop.png
- Viewport: 1440x1000
- H1 observed: Skincare from the Sea®
- H2 samples: Your cart: 0 items, Your cart is empty, Category, Concern
- Navigation samples: Shop All, Bestsellers, New, Body, Body Oil & Moisturizers, Cleanse & Exfoliate, Face, Mineral SunscreenNEW!
- Images observed: 80; domains: adresults-39-adswizz.attribution.adswizz.com, cdn.shopify.com, oseamalibu.com, osea.imgix.net, cdnjs.cloudflare.com
- Video observed: True; sources/domains recorded where available.
- Overlays or fixed elements: 14 fixed elements observed; treat cookie, cart, chat, region, and accessibility overlays as evidence limits, not style decisions.

## Visual System
- Layout: Thin green promo bar, centered logo, category nav, large framed hero image with centered headline and CTA, then bestseller grid.
- Typography: Circular sans for most UI; Canela serif appears as high-touch display accent. 72px hero headline in green.
- Color: Seaweed green text, white shell, sea/sky photography, light badges. Green is identity, not just accent.
- Density: Header medium-density; hero spacious; product grid with badges below.
- Shape: Soft rounded CTA and product badges around 6px; friendly but not bubbly.
- Shadow/depth: Photography depth and product cards; minimal UI shadow.

## Typography And Reading Rhythm
- Observed font stack counts: Circular, sans-serif (219); Canela, serif (1)
- Observed font sizes: 16px (171); 14px (32); 18px (14); 12px (2); 72px (1)
- Observed weights: 400 (161); 450 (48); 700 (6); 600 (5)
- Observed letter spacing: normal (161); 0.4px (21); 0.45px (13); 0.7px (9); 0.35px (9); 1.4px (6)
- Preserve the hierarchy relationship, not the exact proprietary typeface. Map brand display, retail UI, metadata, and CTA text separately.

## Color, Material, And Contrast
- Observed text colors: rgb(29, 77, 65) (199); rgb(255, 255, 255) (9); rgb(11, 46, 37) (6); rgb(73, 116, 105) (5); rgb(128, 155, 165) (1)
- Observed backgrounds: rgba(0, 0, 0, 0) (213); rgb(255, 255, 255) (7)
- Separate UI shell colors from asset-driven colors. If the palette comes from photography/video, recreate that through asset direction before choosing CSS colors.

## Layout Geometry And Spacing
- Record first viewport structure before borrowing: promo/header/nav, hero media, copy location, CTA location, next-section visibility.
- Preserve macro geometry such as split hero, centered brand nav, large media frame, or object crop. Do not reduce it to a generic hero-card layout.
- Use stable aspect ratios for media/product cards so brand imagery does not jump during loading.
- Observed border radii: 6px (49)

## Dimension And Ratio System
- Viewport and document: viewport 1440x1000; document 1425x6330; overflowX 0.
- Observed media ratios: Model with product from the Body Oil collection: 400x400 (1:1); Model with product from the Body Moisturizers co: 400x400 (1:1); Model with product from the Cleansers collection: 400x400 (1:1); Model with product from the Body Scrubs collecti: 400x400 (1:1); Model with product from the Face Moisturizers co: 400x400 (1:1); Model with product from the Travel & Sets collec: 400x400 (1:1)
- Observed spacing samples: body 1425x6235, pt 0px, pb 0px, mt 0px, mb 0px; a 34x10, pt 4px, pb 4px, mt -1px, mb -1px; a 34x10, pt 4px, pb 4px, mt -1px, mb -1px; h3 448x20, pt 0px, pb 0px, mt 0px, mb 0px; li 448x18, pt 0px, pb 0px, mt 0px, mb 4px; li 448x18, pt 0px, pb 0px, mt 0px, mb 4px
- Preserve ratios as implementation constraints: hero min-height, split width, product-card aspect-ratio, section gaps, fixed header height, and drawer/modal bounds.
- Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.

## Assets
- Image style: Sunlit skin, ocean background, product in hand, seaweed/hydration cues.
- Illustration/icon style: Simple utility icons and certification badges.
- Texture/pattern: Sea, skin, serum, sand; no artificial blobs.
- Production: Shopify/imgix/CDN product and lifestyle images.

## Motion
- Page transitions: Commerce-stable.
- Micro-interactions: Mega menu, cart drawer, predictive search, chat, product badges.
- Scroll: Product grid reveal is enough; hero image can stay still.
- Timing: Friendly 180-300ms; no cinematic drag.

## Motion Code And Runtime Evidence
- Motion source: video observed=True; video sources=not observed.
- CSS animation/transition evidence: motion hints=progress, class=progress-bar-alt block motion-safe:transition-all absolute inset-x-0 top-2.5; label, class=-rotate-90 peer-checked:rotate-90 transition-transform; div, class=w-full peer-checked:max-h-80 max-h-0 transition-max-height overflow-hidden; div, class=sticky top-0 z-40 motion-safe:transition-colors border-b border-transparent duration-300; ul, class=glide__slides pb-0, style=transition: transform 400ms cubic-bezier(0.165, 0.84, 0.44, 1); width: 3456px; transform: translate3d(-1728px, 0px, 0px);.
- Public CSS/JS probe keywords: animation, duration, easing, keyframes, reduced_motion, request_animation_frame, scroll_snap, transform, transform_function, transition.
- Public CSS/JS motion snippets: request_animation_frame: n(t){fetch(e,{method:"HEAD",mode:"no-cors"}).then(function(){o(),t(!1)}).catch(function(){requestAnimationFrame(function(){o(),t(!n)})})})}function r(t){var e=getComputedStyle(t);return null===t.offsetParent||0===t.offsetHeight||0===t.offsetWidth||"no | reduced_motion: mary::marker{content:""}menu-drawer .menu-scrim,cart-drawer .cart-scrim{opacity:0}@media (prefers-reduced-motion:no-preference){menu-drawer .menu-scrim,cart-drawer .cart-scrim{transition-property:opacity;transition-timing-function:var(--ease-in-out);tr | duration: lock;font-size:1em;font-weight:500;line-height:1;text-align:center;transition:background .2s ease-in-out}.shopify-payment-button__button[disabled]{opacity:.6;cursor:default}.shopify-payment-button__button--unbranded{background-color | easing: k;font-size:1em;font-weight:500;line-height:1;text-align:center;transition:background .2s ease-in-out}.shopify-payment-button__button[disabled]{opacity:.6;cursor:default}.shopify-payment-button__button--unbranded{background-color:#1990c6;pad | transform_function: er{animation:shopify-rotator 1.4s linear infinite}@keyframes shopify-rotator{0%{transform:rotate(0)}to{transform:rotate(270deg)}}.shopify-payment-button__button .path{stroke-dasharray:280;stroke-dashoffset:0;transform-origin:center;stroke:.
- Exact motion parameters: transition: transition:background .2s ease-in-out | easing: ease-in-out | duration: 2s | transition: transition-duration:.15s | transition: transition-timing-function:cubic-bezier(.4,0,.2,1) | easing: cubic-bezier(.4,0,.2,1) | easing: linear | duration: 1s.
- JavaScript/runtime motion evidence: scripts=https://www.googletagmanager.com/gtag/destination?id=AW-AW-873848209&cx=c&gtm=4e6611h1; https://www.dwin1.com/101463.js; https://load.sgtm.oseamalibu.com/gtm.js?id=GTM-K8TVH9&gtg_health=1; https://sgtm.oseamalibu.com/vciobdrtu/1s?004fdee5=L2d0YWcvanM%2FaWQ9Ry1QNllDRjFYMFFGJmN4PWMmZ3RtPTRlNjYxMWgx; https://www.googletagmanager.com/gtag/js?id=AW-873848209&cx=c&gtm=4e6611.
- Stylesheet evidence: css hrefs=https://oseamalibu.com/cdn/shopifycloud/portable-wallets/latest/accelerated-checkout-backwards-compat.css; https://oseamalibu.com/cdn/shop/t/189/assets/application.css?v=147911141018695544561780444083; https://cdn-static.okendo.io/reviews-widget-plus/css/modules/okendo-star-rating.4cb378a8.css; https://accounts.google.com/gsi/style; https://static.klaviyo.com/onsite/js/build-preview/commit-d0f8559f647289d8fce26053317653b678aa8994/532.0e7e190ea756de832333.css.
- Interpreted motion tags: source-video, runtime-transform, drawer-modal-overlay; code tags: cdn-assets, css-animation, css-keyframes, css-transition, html-video, reduced-motion-css, request-animation-frame, shopify-runtime.
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
- CSS/source clues observed: stylesheet links 6, scripts 18, motion hints 40. Treat minified/public-source details as weak evidence unless inspected directly.

## Borrow
- Use natural ingredient origin as a navigation/category system, not just hero copy.
- Balance serif display warmth with sans product clarity.
- Let real outdoor light carry freshness.

## Avoid Copying
- Do not copy the OSEA logo, seaweed claims, or exact green.
- Do not let chat/badges clutter a refined luxury variant.
- Do not use ocean imagery unless the product story genuinely supports it.

## Evidence Limits
- This reference is based on a desktop capture and DOM/style/resource extraction, not a full multi-page audit.
- Cookie banners, region selectors, newsletter modals, carts, chat widgets, and accessibility widgets may appear in screenshots. They are cataloged as interaction states and should not be mistaken for the core aesthetic.
- Exact brand assets, campaign imagery, typefaces, product names, and proprietary claims must not be copied.

## Self Review
- Evidence quality: screenshot plus DOM/style/resource extraction is sufficient for visual and implementation direction; deeper source inspection remains optional.
- Reuse value: high for beauty/skincare/fragrance scene-fit because tags, best_for, visual geometry, typography, asset plan, motion, and interaction states are explicit.
- Missing pieces: mobile and product detail pages were not captured in this batch; add second-page/mobile captures for critical implementation work.
- Revision made: upgraded from broad style summary to high-dimensional evidence matrix with contamination notes and reference-to-implementation cues.
