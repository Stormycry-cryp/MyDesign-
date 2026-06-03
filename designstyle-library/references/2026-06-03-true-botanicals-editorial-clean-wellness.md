---
title: "True Botanicals"
source_url: "https://truebotanicals.com/"
captured_at: "2026-06-03"
tags: ["skincare", "clean-beauty", "clinical-natural", "editorial", "serif", "campaign-commerce", "warm-earth"]
style_tags: ["skincare", "clean-beauty", "clinical-natural", "editorial", "serif", "campaign-commerce", "warm-earth"]
structure_tags: ["full-bleed-media"]
motion_tags: ["source-video", "runtime-transform", "drawer-modal-overlay"]
code_tags: ["cdn-assets", "css-animation", "css-keyframes", "css-transition", "html-video", "reduced-motion-css", "request-animation-frame", "shopify-runtime"]
best_for: ["clean luxury skincare campaigns", "clinical-natural brands", "editorial sale launches"]
avoid_for: ["quiet spa minimalism", "strict clinical formula pages", "brands avoiding promotional energy"]
evidence_screenshot: "screenshots/true-botanicals-editorial-clean-wellness-desktop.png"
evidence_quality: "visual screenshot plus DOM/style/resource extraction"
---

# Style Reference: True Botanicals


## Essence
A clean-wellness editorial store that mixes clinical claims with human skin photography, warm brown identity, serif campaign headlines, and promotional retail mechanics. The reusable idea is natural performance as an editorial campaign, not a lab sheet.

## When To Use
- Natural skincare that still needs conversion, sale mechanics, and best-seller pathways.
- Campaign landing pages with face-forward photography and concern-based shopping.
- Brands that can support warm skin imagery and strong editorial serif headings.

## When Not To Use
- Brands needing very quiet high-luxury restraint.
- Ingredient-heavy formula education where sale banners would feel noisy.
- Products without human skin photography; the design relies on lived-in skin texture.

## Evidence Snapshot
- Captured URL: https://truebotanicals.com/
- Page title: True Botanicals - Clinical Skin Wellness
- Screenshot: screenshots/true-botanicals-editorial-clean-wellness-desktop.png
- Viewport: 1440x1000
- H1 observed: BIGGEST SALE OF THE YEAR, BIGGEST SALE OF THE YEAR, SIGN UP FOR 15% OFF YOUR FIRST ORDER + A FREE GIFT
- H2 samples: Your cart is empty, Your cart, Estimated total, Offers
- Navigation samples: Accessible Menu - Main Menu, Shop, Shop All, New Arrivals, Bestsellers, Sets, Pregnancy Safe, Limited Edition
- Images observed: 56; domains: truebotanicals.com, d3k81ch9hvuctc.cloudfront.net, cdnjs.cloudflare.com, action.dstillery.com, cdn.shopify.com
- Video observed: True; sources/domains recorded where available.
- Overlays or fixed elements: 14 fixed elements observed; treat cookie, cart, chat, region, and accessibility overlays as evidence limits, not style decisions.

## Visual System
- Layout: Promo bar plus dark warm header, hero split with text left and face close-up right, then campaign/product modules. Offers/drawers are part of the commerce system.
- Typography: PPObjectSans for retail and adobe-caslon-pro for editorial campaign headings. Letter spacing is used heavily in labels and nav.
- Color: Deep brown, warm off-white, occasional pale yellow promo highlight. Palette is distinctive but can become promotional if overused.
- Density: Hero is balanced; header and promo area are more retail-dense.
- Shape: Mostly flat rectangles; CTA is simple filled block, not pill-heavy.
- Shadow/depth: Depth through photography and editorial crop, not shadows.

## Typography And Reading Rhythm
- Observed font stack counts: PPObjectSans, sans-serif (167); adobe-caslon-pro, sans-serif (44); Arial, "Helvetica Neue", Helvetica, sans-serif (3); Arial (2); Wotfard, Arial, "Helvetica Neue", Helvetica, sans-serif (2); PPObjectSans (1)
- Observed font sizes: 14px (153); 20px (26); 12px (13); 24px (8); 40px (7); 16px (3)
- Observed weights: 400 (184); 300 (25); 500 (11)
- Observed letter spacing: normal (140); 1.5px (37); 2.6px (16); 1px (16); 0.2px (6); 0.6px (5)
- Preserve the hierarchy relationship, not the exact proprietary typeface. Map brand display, retail UI, metadata, and CTA text separately.

## Color, Material, And Contrast
- Observed text colors: rgb(44, 18, 3) (171); rgb(249, 244, 238) (39); rgb(255, 255, 255) (3); rgb(253, 253, 150) (3); rgb(42, 17, 3) (1); rgba(44, 18, 3, 0.85) (1)
- Observed backgrounds: rgba(0, 0, 0, 0) (211); rgb(249, 244, 238) (4); rgb(253, 253, 150) (2); rgb(255, 255, 255) (1); rgb(233, 228, 224) (1); rgb(239, 239, 239) (1)
- Separate UI shell colors from asset-driven colors. If the palette comes from photography/video, recreate that through asset direction before choosing CSS colors.

## Layout Geometry And Spacing
- Record first viewport structure before borrowing: promo/header/nav, hero media, copy location, CTA location, next-section visibility.
- Preserve macro geometry such as split hero, centered brand nav, large media frame, or object crop. Do not reduce it to a generic hero-card layout.
- Use stable aspect ratios for media/product cards so brand imagery does not jump during loading.
- Observed border radii: not observed

## Dimension And Ratio System
- Viewport and document: viewport 1440x1000; document 1425x5102; overflowX 0.
- Observed media ratios: image: 360x171 (2.11:1); image: 360x171 (2.11:1); image: 360x171 (2.11:1); True Botanicals: 367x28 (13.11:1); image: 1680x757 (2.22:1); image: 679x679 (1:1)
- Observed spacing samples: body 1425x5102, pt 0px, pb 0px, mt 0px, mb 0px; a 124x40, pt 0px, pb 0px, mt -1px, mb -1px; h2 369x146, pt 0px, pb 0px, mt 0px, mb 30px; a 259x40, pt 0px, pb 0px, mt 0px, mb 0px; p 369x62, pt 0px, pb 0px, mt 55px, mb 5px; p 369x24, pt 0px, pb 0px, mt 8px, mb 0px
- Preserve ratios as implementation constraints: hero min-height, split width, product-card aspect-ratio, section gaps, fixed header height, and drawer/modal bounds.
- Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.

## Assets
- Image style: Close-up faces, visible skin texture, patches/serum use, travel/lifestyle product scenes.
- Illustration/icon style: Minimal ecommerce utility icons.
- Texture/pattern: Skin texture, warm natural surfaces, outdoor lifestyle.
- Production: Shopify/CDN assets, campaign modules, promotional offer drawers.

## Motion
- Page transitions: Standard ecommerce.
- Micro-interactions: Offer drawers, cart, promo navigation, product modules.
- Scroll: Editorial sections can reveal but should not obscure promo clarity.
- Timing: Responsive retail timing; avoid slow cinematic pacing because sale mechanics are active.

## Motion Code And Runtime Evidence
- Motion source: video observed=True; video sources=not observed.
- CSS animation/transition evidence: motion hints=body, class=animate--hover-default page-index title--true-botanicals---clinical-skin-wellness smart-cart--enabled; img, class=header__heading-logo motion-reduce; div, class=mega-menu__content color-background-1 gradient motion-reduce global-settings-popup; div, class=gradient menu-drawer motion-reduce color-background-1; div, class=block-carousel_item_kbatHw hero-slider slideWrapper splide__slide banner banner--content-align-center banner--content-align-mobile-center ba, style=width: calc(100%); transform: translateX(0%);.
- Public CSS/JS probe keywords: animation, duration, easing, keyframes, reduced_motion, request_animation_frame, transform, transform_function, transition.
- Public CSS/JS motion snippets: request_animation_frame: n(){clearTimeout(r),dp&&cancelAnimationFrame(t),setTimeout(e)},r=setTimeout(o,100);dp&&(t=requestAnimationFrame(o))}function Rn(e){var t=Le,o=e.__c;typeof o=="function"&&(e.__c=void 0,o()),Le=t}function yi(e){var t=Le;e.__c=e.__(),Le=t}function bi(e,t | reduced_motion: izing:border-box}.break{word-break:break-word}.visibility-hidden{visibility:hidden}@media(prefers-reduced-motion){.motion-reduce{transition:none!important;animation:none!important}}:root{--duration-short: .1s;--duration-default: .2s;--duration-announce | duration: lative}.splide__slide img{vertical-align:bottom}.splide__spinner{animation:splide-loading 1s linear infinite;border:2px solid #999;border-left-color:transparent;border-radius:50%;bottom:0;contain:strict;display:inline-block;height:2 | easing: ive}.splide__slide img{vertical-align:bottom}.splide__spinner{animation:splide-loading 1s linear infinite;border:2px solid #999;border-left-color:transparent;border-radius:50%;bottom:0;contain:strict;display:inline-block;height:20px;lef | transform_function: _track{overflow:hidden;position:relative;z-index:0}@keyframes splide-loading{0%{transform:rotate(0)}to{transform:rotate(1turn)}}.splide__track--draggable{-webkit-touch-callout:none;-webkit-user-select:none;-ms-user-select:none;user-select:.
- Exact motion parameters: transition: transition:transform .2s linear | easing: linear | transform: transform:scale(1.4) | transform_function: scale(1.4) | duration: 2s | transition: transition:background .2s ease-in-out | easing: ease-in-out | transition: transition:none!important.
- JavaScript/runtime motion evidence: scripts=https://static.hotjar.com/c/hotjar-1381889.js?sv=7; https://bat.bing.com/bat.js; https://www.googletagmanager.com/gtag/destination?id=AW-892764911&cx=c&gtm=4e6611; https://onetext.com/sdk/onetext.min.js?onetext-account-token=onetext_account_production_019b0509-866b-733e-ad43-0dd87aba641a&timestamp=1780383620544&shop=tnbotanicals.myshopify.com; https://shopify-extension.getredo.com/main.js?widget_id=2b4trmoc0hitlk4&shop=tnbotanicals.myshopify.com.
- Stylesheet evidence: css hrefs=https://use.typekit.net/mmb7oxv.css; https://truebotanicals.com/cdn/shop/t/1560/assets/splide.min.css?v=44329677166622589231777939588; https://truebotanicals.com/cdn/shopifycloud/portable-wallets/latest/accelerated-checkout-backwards-compat.css; https://truebotanicals.com/cdn/shop/t/1560/assets/base.css?v=87176164045751999561777939480; https://truebotanicals.com/cdn/shop/t/1560/assets/component-localization-form.css?v=155603600527820746741777939498.
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
- CSS/source clues observed: stylesheet links 20, scripts 28, motion hints 18. Treat minified/public-source details as weak evidence unless inspected directly.

## Borrow
- Use editorial serif only for campaign headline and keep nav/product text sans.
- Let real skin texture replace generic nature imagery.
- Separate proof/clinical language from promotional offer mechanics so neither muddies the other.

## Avoid Copying
- Do not copy the sale wording, exact brown/yellow identity, or face imagery.
- Do not overload a premium brand with too many offer bars unless conversion is the goal.
- Do not call natural claims clinical unless evidence is present.

## Evidence Limits
- This reference is based on a desktop capture and DOM/style/resource extraction, not a full multi-page audit.
- Cookie banners, region selectors, newsletter modals, carts, chat widgets, and accessibility widgets may appear in screenshots. They are cataloged as interaction states and should not be mistaken for the core aesthetic.
- Exact brand assets, campaign imagery, typefaces, product names, and proprietary claims must not be copied.

## Self Review
- Evidence quality: screenshot plus DOM/style/resource extraction is sufficient for visual and implementation direction; deeper source inspection remains optional.
- Reuse value: high for beauty/skincare/fragrance scene-fit because tags, best_for, visual geometry, typography, asset plan, motion, and interaction states are explicit.
- Missing pieces: mobile and product detail pages were not captured in this batch; add second-page/mobile captures for critical implementation work.
- Revision made: upgraded from broad style summary to high-dimensional evidence matrix with contamination notes and reference-to-implementation cues.
