---
title: "Typology"
source_url: "https://www.typology.com/"
captured_at: "2026-06-03"
tags: ["skincare", "clinical", "minimal", "ingredient-led", "french", "video-hero", "monochrome", "diagnostic"]
style_tags: ["skincare", "clinical", "minimal", "ingredient-led", "french", "video-hero", "monochrome", "diagnostic"]
structure_tags: ["full-bleed-media", "product-grid"]
motion_tags: ["source-video", "runtime-transform", "carousel-swiper", "drawer-modal-overlay"]
code_tags: ["css-transition", "html-video", "intersection-observer", "request-animation-frame", "swiper-motion"]
best_for: ["ingredient-led skincare", "formula transparency pages", "clinical-natural positioning", "routine diagnostics"]
avoid_for: ["warm botanical storytelling", "decorative luxury campaigns", "image-only brand pages"]
evidence_screenshot: "screenshots/typology-clinical-minimal-formulas-desktop.png"
evidence_quality: "visual screenshot plus DOM/style/resource extraction"
---

# Style Reference: Typology


## Essence
A formula-first skincare system that sells restraint through stark photography, compact claims, and product names that include active ingredients, concentrations, and prices. The reusable idea is clinical minimalism with commerce built directly into the wording.

## When To Use
- Skincare brands where short formulas, concentration, origin, and efficacy are the core trust signals.
- Sites that need product grids to read like an ingredient catalog without becoming a spreadsheet.
- Diagnostic/routine flows where users expect precision and low marketing fluff.

## When Not To Use
- Lifestyle-first brands where warmth and aspiration matter more than formula rigor.
- Ultra-luxury spa pages that should feel softer and less stark.
- Products with vague ingredient claims; the style exposes weak substance.

## Evidence Snapshot
- Captured URL: https://www.typology.com/
- Page title: Soins pour la peau naturels, végan et Made in France — Typology
- Screenshot: screenshots/typology-clinical-minimal-formulas-desktop.png
- Viewport: 1440x1000
- H1 observed: Nos formules sont :courtes,concentrées,fabriquées en France
- H2 samples: BIENTÔT, Sérum Teinté T10 — Vitamine C + Aloe vera — 29,90 €, Crème Visage à 9 Ingrédients D41 — 22,50 €, Sérum Éclat L32 — Complexe vitamine C 15% + Vitamine E 1% — à partir de 17,90 €
- Navigation samples: Produits, Nouveautés, Les iconiques, Duos, trios & kits, Coffrets cadeaux Nouveau, Dernière chance, Éclat du teint Nouveau, Soins purifiants
- Images observed: 51; domains: media.typology.com, www.typology.com, bat.bing.com, lantern.roeye.com
- Video observed: True; sources/domains recorded where available.
- Overlays or fixed elements: 4 fixed elements observed; treat cookie, cart, chat, region, and accessibility overlays as evidence limits, not style decisions.

## Visual System
- Layout: Announcement bars and symmetrical header over a full-bleed stark visual, followed by product rows where title, active ingredient, and price are one compact line.
- Typography: Post Grotesk dominates UI and body; Lettera mono appears as diagnostic/technical accent. Large hero type around 80px is balanced by many 13-15px labels.
- Color: Black/white and near-black text; occasional inverted black bar. The emotional color comes from close-up skin/formula imagery, not palette decoration.
- Density: Hero is sparse, product grid is medium-dense and exacting.
- Shape: Mostly square/rectangular; no rounded card softness.
- Shadow/depth: Flat, editorial, no UI shadow. Texture is photographic: skin, powder, serum.

## Typography And Reading Rhythm
- Observed font stack counts: "Post Grotesk", system-ui, sans-serif (198); Lettera, mono (18); "PingFang SC" (4)
- Observed font sizes: 15px (102); 14px (58); 13px (27); 16px (24); 80px (4); 30px (2)
- Observed weights: 400 (189); 500 (31)
- Observed letter spacing: normal (183); 0.26px (17); 0.28px (8); 0.35px (7); 0.65px (5)
- Preserve the hierarchy relationship, not the exact proprietary typeface. Map brand display, retail UI, metadata, and CTA text separately.

## Color, Material, And Contrast
- Observed text colors: rgb(20, 20, 20) (107); rgb(0, 0, 0) (104); rgb(255, 255, 255) (6); rgb(79, 79, 79) (3)
- Observed backgrounds: rgba(0, 0, 0, 0) (218); rgb(20, 20, 20) (2)
- Separate UI shell colors from asset-driven colors. If the palette comes from photography/video, recreate that through asset direction before choosing CSS colors.

## Layout Geometry And Spacing
- Record first viewport structure before borrowing: promo/header/nav, hero media, copy location, CTA location, next-section visibility.
- Preserve macro geometry such as split hero, centered brand nav, large media frame, or object crop. Do not reduce it to a generic hero-card layout.
- Use stable aspect ratios for media/product cards so brand imagery does not jump during loading.
- Observed border radii: not observed

## Dimension And Ratio System
- Viewport and document: viewport 1440x1000; document 1425x7842; overflowX 0.
- Observed media ratios: 08.06.26 : Le nouveau T30, noté 100/100 sur Yuka: 1200x1500 (4:5); Logo: 300x109 (2.75:1); Sérum Teinté Vitamine C + Aloe vera — Typology: 2500x2500 (1:1); Crème Visage à 9 Ingrédients — Typology: 1600x1600 (1:1); Sérum Éclat Complexe vitamine C 15% + Vitamine E: 1600x1600 (1:1)
- Observed spacing samples: body 1425x7842, pt 0px, pb 0px, mt 0px, mb 0px; a 356x14, pt 0px, pb 0px, mt 0px, mb 0px; a 374x14, pt 0px, pb 0px, mt 0px, mb 0px; a 356x14, pt 0px, pb 0px, mt 0px, mb 0px; header 1425x80, pt 0px, pb 0px, mt 0px, mb 0px; nav 205x80, pt 0px, pb 0px, mt 0px, mb 0px
- Preserve ratios as implementation constraints: hero min-height, split width, product-card aspect-ratio, section gaps, fixed header height, and drawer/modal bounds.
- Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.

## Assets
- Image style: Extreme close-ups, skin texture, formula materials, clinical product stills.
- Illustration/icon style: Sparse utility icons/search/cart only.
- Texture/pattern: Human skin and ingredient texture replace UI pattern.
- Production: Optimized media/video assets with query-transformed formats; product thumbnails from media CDN.

## Motion
- Page transitions: Immediate, utilitarian.
- Micro-interactions: Product hover and drawer/search transitions should be crisp.
- Scroll: Hero video can loop; product rows should remain stable.
- Timing: Use 150-250ms transitions; avoid luxury slow fades that dilute clinical precision.

## Motion Code And Runtime Evidence
- Motion source: video observed=True; video sources=https://media.typology.com/video-storyblok/x/a95b866ed4/homepage_teasing_16-9-1.mp4?twic=v1/cover=1920/output=vp9/quality=90; https://media.typology.com/video-storyblok/x/a95b866ed4/homepage_teasing_16-9-1.mp4?twic=v1/cover=1920/output=h265/quality=90; https://media.typology.com/video-storyblok/x/a95b866ed4/homepage_teasing_16-9-1.mp4?twic=v1/cover=1920/output=vp9/quality=90; https://media.typology.com/video-storyblok/x/a95b866ed4/homepage_teasing_16-9-1.mp4?twic=v1/cover=1920/output=h264/quality=90; https://media.typology.com/video-storyblok/x/8ef5797302/homepage-mobile_teasing-t30.mp4?twic=v1/cover=900/output=h265/quality=90.
- CSS animation/transition evidence: motion hints=div, class=transition-color duration-400 relative z-10 bg-black text-white; div, class=text-black md:text-black transition-color duration-400 menu self-stretch flex items-stretch justify-start w-full h-full mr-auto; svg, class=fill-current w-2 h-2 absolute z-20 left-1/2 bottom-0 transition duration-100 transform scale-0 -translate-x-1/2 group-hover:scale-75; svg, class=fill-current w-2 h-2 absolute z-20 left-1/2 bottom-0 transition duration-100 transform scale-0 -translate-x-1/2 group-hover:scale-75; svg, class=fill-current w-2 h-2 absolute z-20 left-1/2 bottom-0 transition duration-100 transform scale-0 -translate-x-1/2 group-hover:scale-75.
- Public CSS/JS probe keywords: duration, easing, intersection, request_animation_frame, swiper, transform, transform_function, transition.
- Public CSS/JS motion snippets: swiper: .carousel[data-v-ce07ea94] .swiper-slide{height:auto} | intersection: 1===i&&n&&Bt.push(t)}}function ir(t,e){!1===ue.has(t)&&(ue.set(t,e),(de=null===de&&se?new IntersectionObserver(ur,{threshold:[0,.05,.1,.2,.3,.4,.5,.6,.7,.8,.9,1]}):de)&&t&&t.nodeType===Node.ELEMENT_NODE&&de.observe(t))}function rr(t){return ue&&ue.ha | request_animation_frame: c=e.value,e.rating=c>r[1]?"poor":c>r[0]?"needs-improvement":"good",t(e))}},uE=function(t){requestAnimationFrame(function(){return requestAnimationFrame(function(){return t()})})},ub=function(t){var e=function(e){"pagehide"!==e.type&&"hidden"!==documen | duration: ver{-webkit-box-shadow:inset 0 0 0 1000px transparent;-webkit-transition:background-color 5000s ease-in-out 0s;transition:background-color 5000s ease-in-out 0s}input[data-v-63ee63c1]:disabled{-webkit-text-fill-color:#909090} | easing: ebkit-box-shadow:inset 0 0 0 1000px transparent;-webkit-transition:background-color 5000s ease-in-out 0s;transition:background-color 5000s ease-in-out 0s}input[data-v-63ee63c1]:disabled{-webkit-text-fill-color:#909090}.
- Exact motion parameters: transition: transition:background-color 5000s ease-in-out 0s | easing: ease-in-out | duration: 5000s | duration: 0s | transition: transition:background-color .218s,border-color .218s,box-shadow .218s | duration: 218s | transition: transition:opacity .218s | transform: transform:translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skew(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-s.
- JavaScript/runtime motion evidence: scripts=https://ct.pinterest.com/static/ct/token_create.js; https://wave.outbrain.com/mtWavesBundler/handler/005dc4e0684d80402f24415b669c52d5f8; https://www.clarity.ms/tag/uet/26111343; https://analytics.tiktok.com/i18n/pixel/enable_cookie; https://analytics.tiktok.com/i18n/pixel/static/identify_5cff1caf.js.
- Stylesheet evidence: css hrefs=https://www.typology.com/_nuxt/Checkout.BXMTpZcf.css; https://www.typology.com/_nuxt/FormText.MYcmWzZ-.css; https://www.typology.com/_nuxt/useForm.Cbc7hM6H.css; https://www.typology.com/_nuxt/FormRadio.7JrRPS0o.css; https://www.typology.com/_nuxt/DropdownPaymentMethodNetworks.Bj-0-MZa.css.
- Interpreted motion tags: source-video, runtime-transform, carousel-swiper, drawer-modal-overlay; code tags: css-transition, html-video, intersection-observer, request-animation-frame, swiper-motion.
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
- CSS/source clues observed: stylesheet links 20, scripts 29, motion hints 40. Treat minified/public-source details as weak evidence unless inspected directly.

## Borrow
- Encode proof in product names: active, percentage, purpose, price.
- Use one technical type layer for diagnostics and formula metadata.
- Let stark macro imagery create distinctiveness without adding UI decoration.

## Avoid Copying
- Do not imitate the exact French phrasing, logo, or image art direction.
- Do not overuse giant type if the formula/product text is not precise.
- Do not mix this with soft botanical illustration; it weakens the clinical stance.

## Evidence Limits
- This reference is based on a desktop capture and DOM/style/resource extraction, not a full multi-page audit.
- Cookie banners, region selectors, newsletter modals, carts, chat widgets, and accessibility widgets may appear in screenshots. They are cataloged as interaction states and should not be mistaken for the core aesthetic.
- Exact brand assets, campaign imagery, typefaces, product names, and proprietary claims must not be copied.

## Self Review
- Evidence quality: screenshot plus DOM/style/resource extraction is sufficient for visual and implementation direction; deeper source inspection remains optional.
- Reuse value: high for beauty/skincare/fragrance scene-fit because tags, best_for, visual geometry, typography, asset plan, motion, and interaction states are explicit.
- Missing pieces: mobile and product detail pages were not captured in this batch; add second-page/mobile captures for critical implementation work.
- Revision made: upgraded from broad style summary to high-dimensional evidence matrix with contamination notes and reference-to-implementation cues.
