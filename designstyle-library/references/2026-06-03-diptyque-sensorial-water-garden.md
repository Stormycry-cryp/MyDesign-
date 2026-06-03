---
title: "Diptyque"
source_url: "https://www.diptyqueparis.com/en_hk/"
captured_at: "2026-06-03"
tags: ["beauty", "fragrance", "luxury", "sensorial", "video-hero", "editorial-commerce", "water", "serif-sans"]
style_tags: ["beauty", "fragrance", "luxury", "sensorial", "video-hero", "editorial-commerce", "water", "serif-sans"]
structure_tags: ["full-bleed-media", "editorial-modules"]
motion_tags: ["source-video", "runtime-transform", "drawer-modal-overlay"]
code_tags: ["cdn-assets", "css-animation", "css-keyframes", "css-transition", "html-video"]
best_for: ["fragrance and bath/body launch pages", "water/seasonal campaign storytelling", "luxury ecommerce with immersive media"]
avoid_for: ["clinical ingredient-heavy skincare", "dense catalog-first stores", "low-asset MVP pages"]
evidence_screenshot: "screenshots/diptyque-sensorial-water-garden-desktop.png"
evidence_quality: "visual screenshot plus DOM/style/resource extraction"
---

# Style Reference: Diptyque


## Essence
A sensorial fragrance-commerce page where a clean retail shell frames an immersive seasonal media world. The reusable idea is ceremonial navigation plus a single atmospheric hero that turns water, light, and texture into product desire.

## When To Use
- Seasonal luxury campaigns where the theme is a place or sensory environment, not just a product list.
- Beauty/fragrance pages that can support full-bleed video, precise navigation, and restrained product modules below.
- High-end natural skincare when the concept needs water, garden, spa, or ritual atmosphere.

## When Not To Use
- Ingredient education pages where users need comparison and proof before mood.
- Pages without strong video/photo assets; the structure becomes too generic without media.
- Brands that need earthy warmth more than polished Parisian retail order.

## Evidence Snapshot
- Captured URL: https://www.diptyqueparis.com/en_hk/
- Page title: Diptyque
- Screenshot: screenshots/diptyque-sensorial-water-garden-desktop.png
- Viewport: 1440x1000
- H1 observed: A sensorial stroll through the summer water garden
- H2 samples: Best sellers
- Navigation samples: do son, orpheon, rose, car, Discover, Discover, Discover, Discover
- Images observed: 80; domains: images.ctfassets.net, www.diptyqueparis.com
- Video observed: True; sources/domains recorded where available.
- Overlays or fixed elements: 4 fixed elements observed; treat cookie, cart, chat, region, and accessibility overlays as evidence limits, not style decisions.

## Visual System
- Layout: Thin promo bar, centered brand mark, horizontal category navigation, then a full-width video hero. Hero copy sits low and centered as a small framed CTA rather than a large headline block.
- Typography: Apercu Pro for retail UI and Diptyque Saint-Germain serif for brand/story moments. Most nav/body text is 12-16px; restraint makes the video and logo carry hierarchy.
- Color: Mostly white shell and black text; campaign color comes from pale aqua, gray stone, and water imagery. Avoid adding decorative color outside the media.
- Density: Low density above the fold, then product/best-seller modules below. Navigation is complete but visually light.
- Shape: Rectangular header and hero, small 3px radii only in controls. The design avoids card stacks.
- Shadow/depth: Depth comes from video footage and product photography, not UI shadows.

## Typography And Reading Rhythm
- Observed font stack counts: "Apercu Pro", sans-serif (174); "Diptyque Saint-Germain", serif (46)
- Observed font sizes: 14px (135); 16px (43); 12px (42)
- Observed weights: 400 (182); 300 (37); 600 (1)
- Observed letter spacing: normal (218); 0.1px (2)
- Preserve the hierarchy relationship, not the exact proprietary typeface. Map brand display, retail UI, metadata, and CTA text separately.

## Color, Material, And Contrast
- Observed text colors: rgb(0, 0, 0) (156); rgb(113, 113, 113) (33); rgb(128, 128, 128) (23); rgb(109, 109, 109) (8)
- Observed backgrounds: rgba(0, 0, 0, 0) (218); rgb(255, 255, 255) (2)
- Separate UI shell colors from asset-driven colors. If the palette comes from photography/video, recreate that through asset direction before choosing CSS colors.

## Layout Geometry And Spacing
- Record first viewport structure before borrowing: promo/header/nav, hero media, copy location, CTA location, next-section visibility.
- Preserve macro geometry such as split hero, centered brand nav, large media frame, or object crop. Do not reduce it to a generic hero-card layout.
- Use stable aspect ratios for media/product cards so brand imagery does not jump during loading.
- Observed border radii: 3px (8)

## Dimension And Ratio System
- Viewport and document: viewport 1440x1000; document 1425x4924; overflowX 0.
- Observed media ratios: Contact us: 160x161 (1:1); Track your order: 48x48 (1:1); Return an item: 160x161 (1:1); Find your nearest boutique: 40x40 (1:1)
- Observed spacing samples: body 1425x4864, pt 0px, pb 0px, mt 0px, mb 0px; a 769x12, pt 0px, pb 0px, mt 0px, mb 0px; header 1425x120, pt 0px, pb 0px, mt 0px, mb 0px; button 24x24, pt 0px, pb 0px, mt 0px, mb 0px; nav 1425x65, pt 0px, pb 0px, mt 0px, mb 0px; li 108x20, pt 0px, pb 0px, mt 0px, mb 0px
- Preserve ratios as implementation constraints: hero min-height, split width, product-card aspect-ratio, section gaps, fixed header height, and drawer/modal bounds.
- Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.

## Assets
- Image style: Macro seasonal video, mosaic/water texture, product packs as clean retail stills.
- Illustration/icon style: Tiny utility icons only; no decorative icon system.
- Texture/pattern: Real texture from tiles, water, droplets, and light refraction.
- Production: CMS-hosted images/video from Contentful domains; optimized campaign video variants.

## Motion
- Page transitions: Retail-stable; no theatrical page transition needed.
- Micro-interactions: Video pause/mute affordances, simple nav/CTA hover states.
- Scroll: Hero video is the motion event; below sections can use restrained reveal.
- Timing: Slow sensory motion from source video; UI timing should stay quiet at 180-250ms.

## Motion Code And Runtime Evidence
- Motion source: video observed=True; video sources=https://videos.ctfassets.net/4sg0zck18nfj/1a3BOkoNEmLNo7TxXG4JQt/9d8c5cc26882af9d1497d8d2a1942bd9/Summer_2026_Video_10Sec_Secondaire_Medicis-Vase-Blue-Small_1920X1080-16-9_Desktop_Diptyque_opt.mp4#t=0.1; https://videos.ctfassets.net/4sg0zck18nfj/1a3BOkoNEmLNo7TxXG4JQt/9d8c5cc26882af9d1497d8d2a1942bd9/Summer_2026_Video_10Sec_Secondaire_Medicis-Vase-Blue-Small_1920X1080-16-9_Desktop_Diptyque_opt.mp4#t=0.1.
- CSS animation/transition evidence: motion hints=span, class=vaimo-icon__inner, style=width: 48px; height: 48px; background-position: -962px 0px; transform: scale(0.5);; span, class=vaimo-icon__inner, style=width: 96px; height: 96px; background-position: -5448px 0px; transform: scale(0.25);; span, class=vaimo-icon__inner, style=width: 48px; height: 48px; background-position: -1538px 0px; transform: scale(0.25);; span, class=vaimo-icon__inner, style=width: 48px; height: 48px; background-position: -1394px 0px; transform: scale(0.25);; span, class=vaimo-icon__inner, style=width: 48px; height: 48px; background-position: -1874px 0px; transform: scale(0.25);.
- Public CSS/JS probe keywords: animation, duration, easing, keyframes, scroll_snap, transform, transform_function, transition.
- Public CSS/JS motion snippets: duration: :var(--button-background,var(--c-primary));transition:var(--button-transition,background .8s);background-position:50%;text-transform:var(--button-text-transform,uppercase);-webkit-text-decoration:var(--button-text-decoration);text-d | easing: lid;content:"";position:absolute;opacity:.5;height:11px;width:1px;transition:opacity .15s ease}.promo-banner__button .icon-close:before{transform:rotate(45deg)}.promo-banner__button .icon-close:after{transform:rotate(-45deg)}.promo-ba | transform_function: -border-width,0);--button-box-shadow-opacity:0}.promo-banner{background:#f8f8f8;transform:translateY(-102%);opacity:1;visibility:visible;max-height:52px;overflow:hidden;will-change:transform}.promo-banner__countdown{padding-right:var(--spacer-base | keyframes: ltiselect__clear{right:auto;left:12px}[dir=rtl] .multiselect__spinner{right:auto;left:1px}@keyframes spinning{0%{transform:rotate(0)}to{transform:rotate(2turn)}} | transition: button-color,var(--c-light-variant));background:var(--button-background,var(--c-primary));transition:var(--button-transition,background .8s);background-position:50%;text-transform:var(--button-text-transform,uppercase);-webkit-text-decoration:var(--button-text.
- Exact motion parameters: transition: transition:var(--button-transition,background .8s) | transform: transform:var(--button-text-transform,uppercase) | duration: 8s | transition: transition:opacity .15s ease | easing: ease | transform: transform:rotate(45deg) | transform: transform:rotate(-45deg) | transform_function: rotate(45deg).
- JavaScript/runtime motion evidence: scripts=https://snap.licdn.com/li.lms-analytics/insight.old.min.js; https://stapecdn.com/dtag/v8.js; https://tk.diptyqueparis.com/50297/tag_50297_1.js; https://www.googletagmanager.com/gtag/destination?id=AW-501283105&cx=c&gtm=4e6611; https://www.googletagmanager.com/gtag/destination?id=DC-12289031&cx=c&gtm=4e6611.
- Stylesheet evidence: css hrefs=https://www.diptyqueparis.com/criticalCSS/critical.css; https://www.diptyqueparis.com/criticalCSS/critical.css; https://www.diptyqueparis.com/_nuxt/css/582124c.css; https://www.diptyqueparis.com/_nuxt/css/eaa1c98.css; https://www.diptyqueparis.com/_nuxt/css/5391d3e.css.
- Interpreted motion tags: source-video, runtime-transform, drawer-modal-overlay; code tags: cdn-assets, css-animation, css-keyframes, css-transition, html-video.
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
- CSS/source clues observed: stylesheet links 20, scripts 28, motion hints 40. Treat minified/public-source details as weak evidence unless inspected directly.

## Borrow
- Use a complete retail header but make it visually quiet so the campaign world leads.
- Let one sensory material system set the palette for the whole page.
- Use a small framed CTA over media instead of large button treatments when the image is strong.

## Avoid Copying
- Do not copy Diptyque's wordmark, Saint-Germain brand typography, or campaign artwork.
- Do not use water/tiles as decoration if the product concept is not sensorially tied to water.
- Do not bury commerce affordances; keep categories and cart visible.

## Evidence Limits
- This reference is based on a desktop capture and DOM/style/resource extraction, not a full multi-page audit.
- Cookie banners, region selectors, newsletter modals, carts, chat widgets, and accessibility widgets may appear in screenshots. They are cataloged as interaction states and should not be mistaken for the core aesthetic.
- Exact brand assets, campaign imagery, typefaces, product names, and proprietary claims must not be copied.

## Self Review
- Evidence quality: screenshot plus DOM/style/resource extraction is sufficient for visual and implementation direction; deeper source inspection remains optional.
- Reuse value: high for beauty/skincare/fragrance scene-fit because tags, best_for, visual geometry, typography, asset plan, motion, and interaction states are explicit.
- Missing pieces: mobile and product detail pages were not captured in this batch; add second-page/mobile captures for critical implementation work.
- Revision made: upgraded from broad style summary to high-dimensional evidence matrix with contamination notes and reference-to-implementation cues.
