---
title: "Flamingo Estate"
source_url: "https://flamingoestate.com/"
captured_at: "2026-06-03"
tags: ["botanical", "editorial-commerce", "surreal", "garden", "food-beauty", "rounded-media", "expressive"]
style_tags: ["botanical", "editorial-commerce", "surreal", "garden", "food-beauty", "rounded-media", "expressive"]
structure_tags: ["editorial-modules", "rounded-media-frame"]
motion_tags: ["runtime-transform", "carousel-swiper", "drawer-modal-overlay"]
code_tags: ["cdn-assets", "css-animation", "css-keyframes", "css-transition", "intersection-observer", "request-animation-frame", "shopify-runtime", "swiper-motion"]
best_for: ["editorial botanical brands", "garden-led commerce", "surreal seasonal campaigns"]
avoid_for: ["clinical skincare", "quiet luxury restraint", "dense product comparison"]
evidence_screenshot: "screenshots/flamingo-estate-surreal-garden-commerce-desktop.png"
evidence_quality: "visual screenshot plus DOM/style/resource extraction"
---

# Style Reference: Flamingo Estate


## Essence
A surreal garden-commerce style where product, food, membership, and culture merge into theatrical editorial scenes. The reusable idea is botanical luxury as a strange, memorable world rather than a clean lab or spa.

## When To Use
- Brands with a strong editorial voice and unusual seasonal product concepts.
- Garden/botanical commerce where storytelling and culture are as important as purchase.
- Landing pages that should be memorable, not merely refined.

## When Not To Use
- Clinical skincare or ingredient proof pages.
- Brands that need quiet high-end minimalism.
- Products with weak art direction; this style needs bold assets.

## Evidence Snapshot
- Captured URL: https://flamingoestate.com/
- Page title: Flamingo Estate
- Screenshot: screenshots/flamingo-estate-surreal-garden-commerce-desktop.png
- Viewport: 1440x1000
- H1 observed: No Slice Limit Needed, No Slice Limit Needed
- H2 samples: Our place in culture, Shop, Category, The Estate
- Navigation samples: SETS FOR THE PRINCESS, MOST LOVED CANDLES
- Images observed: 80; domains: flamingoestate.com
- Video observed: False; sources/domains recorded where available.
- Overlays or fixed elements: 14 fixed elements observed; treat cookie, cart, chat, region, and accessibility overlays as evidence limits, not style decisions.

## Visual System
- Layout: Mint membership strip, large centered wordmark, sparse nav, giant rounded hero media block with centered overlay text and CTA. Below, section labels continue editorial rhythm.
- Typography: Maison Neue for UI; expressive Exposure/Ortica serif for brand/editorial moments.
- Color: Cream, mint green, deep garden green, white. Color blocks are stronger and more playful than typical luxury skincare.
- Density: Hero dense in image content but sparse in text; commerce nav is quiet.
- Shape: Large rounded media corners, pill CTAs, round basket affordances.
- Shadow/depth: Theatrical photography depth, not UI elevation.

## Typography And Reading Rhythm
- Observed font stack counts: maison-neue, Helvetica, Arial, sans-serif (187); "Exposure VAR", serif (22); Ortica (5); exposure, sans-serif (2); maison-neue, sans-serif (2); maison-neue-medium, Helvetica, Arial, sans-serif (2)
- Observed font sizes: 14px (113); 11px (50); 19px (20); 13px (15); 15px (9); 18px (7)
- Observed weights: 400 (214); 300 (5); 500 (1)
- Observed letter spacing: normal (124); 0.5px (39); 0.35px (18); -0.285px (16); 0% (5); 0.11px (5)
- Preserve the hierarchy relationship, not the exact proprietary typeface. Map brand display, retail UI, metadata, and CTA text separately.

## Color, Material, And Contrast
- Observed text colors: rgb(69, 82, 62) (212); rgb(255, 255, 255) (7); rgb(28, 28, 28) (1)
- Observed backgrounds: rgba(0, 0, 0, 0) (171); rgb(252, 251, 246) (41); rgb(239, 242, 233) (4); rgb(163, 213, 177) (2); rgb(69, 82, 62) (2)
- Separate UI shell colors from asset-driven colors. If the palette comes from photography/video, recreate that through asset direction before choosing CSS colors.

## Layout Geometry And Spacing
- Record first viewport structure before borrowing: promo/header/nav, hero media, copy location, CTA location, next-section visibility.
- Preserve macro geometry such as split hero, centered brand nav, large media frame, or object crop. Do not reduce it to a generic hero-card layout.
- Use stable aspect ratios for media/product cards so brand imagery does not jump during loading.
- Observed border radii: 100px (39); 50px (6); 30px (2); 20px (2)

## Dimension And Ratio System
- Viewport and document: viewport 1440x1000; document 1425x6062; overflowX 0.
- Observed media ratios: image: 600x600 (1:1); image: 600x605 (1:1); image: 600x600 (1:1); image: 600x605 (1:1); image: 600x600 (1:1); image: 600x605 (1:1)
- Observed spacing samples: body 1425x5453, pt 0px, pb 0px, mt 0px, mb 0px; a 167x42, pt 0px, pb 0px, mt 0px, mb 0px; a 84x33, pt 5px, pb 5px, mt 0px, mb 0px; a 113x33, pt 5px, pb 5px, mt 0px, mb 0px; a 121x56, pt 5px, pb 5px, mt 0px, mb 0px; a 121x56, pt 5px, pb 5px, mt 0px, mb 0px
- Preserve ratios as implementation constraints: hero min-height, split width, product-card aspect-ratio, section gaps, fixed header height, and drawer/modal bounds.
- Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.

## Assets
- Image style: Surreal still life, garden objects, food/product hybrids, dramatic editorial lighting.
- Illustration/icon style: Sparse line icons; the imagery is the illustration.
- Texture/pattern: Cake, soap, garden, swan, dark green sets.
- Production: Highly art-directed campaign photography; first-party images.

## Motion
- Page transitions: Can be expressive but must stay controllable.
- Micro-interactions: Mega menu, basket drawer, pill hover, screensaver-like brand details.
- Scroll: Editorial reveal and large image transitions work well.
- Timing: Slightly slower and more theatrical than utilitarian commerce.

## Motion Code And Runtime Evidence
- Motion source: video observed=False; video sources=not observed.
- CSS animation/transition evidence: motion hints=div, class=swiper-wrapper fe-swiperjs-items ts-carousel-items, style=transition-duration: 0ms; transition-delay: 0ms; transform: translate3d(49.7093px, 0px, 0px);; div, class=swiper-wrapper fe-swiperjs-items ts-carousel-items, style=transition-duration: 0ms; transition-delay: 0ms; transform: translate3d(49.7093px, 0px, 0px);; div, class=testimonial-excerpt swiper-slide swiper-slide-prev, style=width: 1215px; opacity: 1; transform: translate3d(0px, 0px, 0px); transition-duration: 0ms;; div, class=testimonial-excerpt swiper-slide swiper-slide-visible swiper-slide-fully-visible swiper-slide-active, style=width: 1215px; opacity: 1; transform: translate3d(-1215px, 0px, 0px); transition-duration: 0ms;; div, class=testimonial-excerpt swiper-slide swiper-slide-next, style=width: 1215px; opacity: 0; transform: translate3d(-2430px, 0px, 0px); transition-duration: 0ms;.
- Public CSS/JS probe keywords: animation, duration, easing, intersection, keyframes, request_animation_frame, scroll_snap, swiper, transform, transform_function, transition, video.
- Public CSS/JS motion snippets: swiper: ransition:all .25s ease;visibility:visible;width:100%;z-index:1000}@font-face{font-family:swiper-icons;font-style:normal;font-weight:400;src:url(data:application/font-woff;charset=utf-8;base64,\ d09GRgABAAAAAAZgABAAAAAADAAAAAAAAAAAAAAAA | intersection: usTrap.deactivate()}},mounted(){if(Ft)return;const{popupBlockRef:t}=this.$refs;t&&(Ft=new IntersectionObserver((e=>{const n=e[0],r=n.intersectionRatio;0<r&&r<1&&n.boundingClientRect.right>window.innerWidth&&(t.style.left="50%",t.style.transform="tran | request_animation_frame: ssList.remove(e)));const{_vtc:n}=t;n&&(n.delete(e),n.size||(t._vtc=void 0))}function I(t){requestAnimationFrame((()=>{requestAnimationFrame(t)}))}let D=0;function N(t,e,n,r){const o=t._endId=++D,i=()=>{o===t._endId&&r()};if(n)return setTimeout(i,n);co | duration: :3px;content:"";height:1px;left:0;opacity:1;position:absolute;-webkit-transition:opacity .1s ease;transition:opacity .1s ease;width:100%}.link-underline:hover{color:#45523e}.link-underline:hover:after{opacity:0}body.noscroll{height: | easing: x;content:"";height:1px;left:0;opacity:1;position:absolute;-webkit-transition:opacity .1s ease;transition:opacity .1s ease;width:100%}.link-underline:hover{color:#45523e}.link-underline:hover:after{opacity:0}body.noscroll{height:100%;.
- Exact motion parameters: transition: transition:opacity .1s ease | easing: ease | duration: 1s | transition: transition:color .2s ease-in-out,opacity .2s ease-in-out | easing: ease-in-out | duration: 2s | transition: transition:-webkit-transform .2s ease-in-out | transition: transition:transform .2s ease-in-out.
- JavaScript/runtime motion evidence: scripts=https://cdn.pushowl.com/latest/sdks/pushowl-shopify.js?subdomain=flamingo-estate-organics&environment=production&guid=179a9e82-7d71-4f60-a10e-ba67b1cbed56&shop=flamingo-estate-organics.myshopify.com; https://cdn.attn.tv/flamingoestate/dtag.js?shop=flamingo-estate-organics.myshopify.com; https://app.electricsms.com/cart-widget/widget.min.js?shop=flamingo-estate-organics.myshopify.com; https://assets.dailykarma.io/prod/init-v3.js?v2&shop=flamingo-estate-organics.myshopify.com; https://static.rechargecdn.com/assets/js/widget.min.js?shop=flamingo-estate-organics.myshopify.com.
- Stylesheet evidence: css hrefs=https://flamingoestate.com/cdn/shop/t/232/assets/main.bundle.css?v=163086077477102552971779227859; https://flamingoestate.com/cdn/shop/t/232/assets/owl.carousel.min.css?v=70516089817612781961725383549; https://flamingoestate.com/cdn/shop/t/232/assets/ia-custom-utils.css?v=98383545916839652291776099623; https://flamingoestate.com/cdn/shop/t/232/assets/swiper-bundle.min.css?v=127803016596819466191778189135; https://flamingoestate.com/cdn/shop/t/232/assets/index.bundle.css?v=54839946892358751241762545246.
- Interpreted motion tags: runtime-transform, carousel-swiper, drawer-modal-overlay; code tags: cdn-assets, css-animation, css-keyframes, css-transition, intersection-observer, request-animation-frame, shopify-runtime, swiper-motion.
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
- CSS/source clues observed: stylesheet links 17, scripts 21, motion hints 9. Treat minified/public-source details as weak evidence unless inspected directly.

## Borrow
- Make one surreal product metaphor the hero, then keep UI simple around it.
- Use large rounded media frames to soften dramatic imagery.
- Let editorial voice appear in product naming and section labels.

## Avoid Copying
- Do not copy the exact surreal art direction, product names, or garden mythology.
- Do not force this on a brand without a strong voice.
- Do not confuse expressive with cluttered; the nav remains sparse.

## Evidence Limits
- This reference is based on a desktop capture and DOM/style/resource extraction, not a full multi-page audit.
- Cookie banners, region selectors, newsletter modals, carts, chat widgets, and accessibility widgets may appear in screenshots. They are cataloged as interaction states and should not be mistaken for the core aesthetic.
- Exact brand assets, campaign imagery, typefaces, product names, and proprietary claims must not be copied.

## Self Review
- Evidence quality: screenshot plus DOM/style/resource extraction is sufficient for visual and implementation direction; deeper source inspection remains optional.
- Reuse value: high for beauty/skincare/fragrance scene-fit because tags, best_for, visual geometry, typography, asset plan, motion, and interaction states are explicit.
- Missing pieces: mobile and product detail pages were not captured in this batch; add second-page/mobile captures for critical implementation work.
- Revision made: upgraded from broad style summary to high-dimensional evidence matrix with contamination notes and reference-to-implementation cues.
