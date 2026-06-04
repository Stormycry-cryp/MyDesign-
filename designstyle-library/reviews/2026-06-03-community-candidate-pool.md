# Community Candidate Pool For 50+ UI References

Created: 2026-06-03 19:28 CST

## Goal

Build a broad, evidence-backed designstyle library from at least 50 different high-quality website UIs. This document is the candidate and community-feedback intake layer before using `add-designstyle` to create reference entries.

## Source Observations

- Awwwards `/websites/` was accessible and returned current submissions/winners. Useful signal: curated award/community recognition plus tags such as `Clean`, `Responsive Design`, `Transitions`, `Data Visualization`, `Storytelling`, `React`, `Next.js`, `Framer`, and `Interaction Design`.
- Awwwards detail pages expose external site URLs, tags, credits, highlight media, element titles, and collection context. Example inspected: Cleo AI links to `https://web.meetcleo.com/` and is tagged as business/corporate, technology, clean, transitions, data visualization, storytelling, React, Next.js, Framer.
- Httpster was accessible and provides explicit style categories: colourful, brutalist, dark, fullscreen, grid, illustrative, interactive, light, low-carbon, minimal, monotone, unusual layout, unusual navigation, photographic, print, responsive, retro, scrolling behaviour, typographic.
- Httpster also provides type categories: application/software, architecture/industrial design, art/photography, beauty, blog, craft, culture, education, event, fashion, finance, food/drink, fundraising, health, inspiration/resource, magazine, motion, music, news, ecommerce, product, production, property, service, showcase, sport, travel.
- WebInspoo was accessible and is useful for SaaS-specific feedback dimensions: landing pages, pricing pages, about pages, blog pages, testimonials, FAQ, contact pages, technologies, tags, fonts, and color families.
- Siteinspire returned a Vercel security checkpoint page during this run. It is not usable evidence until viewed through a clean browser session or alternate accessible path.

## Community Feedback Themes To Preserve

- Awwwards rewards visual polish, transitions, storytelling, responsive craft, data visualization, and interaction design. Use it for high-visual storytelling, motion, WebGL/immersive, campaigns, portfolios, and expressive brand sites.
- Awwwards alone is not enough UX proof. Do not treat award status as evidence that pricing, forms, dashboards, or repeated-use workflows are usable.
- Httpster is stronger for category/style coverage and for avoiding aesthetic monoculture. Use its style/type taxonomy to keep the 50-site batch diverse.
- WebInspoo is stronger for SaaS and page-type patterns. Use it for landing, pricing, about, testimonial, FAQ, contact, technology stack, typography, and color references.
- Product and SaaS references need practical UI signals: pricing clarity, navigation density, conversion sections, component states, trust proof, documentation, and page-to-page consistency.
- Immersive and campaign references need motion evidence: exact transitions, scroll behavior, 3D/video use, keyframes, library/runtime hints, and reduced-motion limitations.

## Selection Rules

- Target at least 60 candidates so that blocked or low-evidence pages can be excluded while still reaching 50 verified references.
- No single category may exceed 20% of the final 50 unless the user narrows scope later.
- Each accepted reference must pass `add-designstyle/scripts/validate_references.py`.
- A candidate can be replaced when it is blocked, visually ordinary, dominated by overlays, template-like, inaccessible, or lacks enough code/motion evidence.
- Each 10-reference batch must include a short review note with included entries, excluded entries, category coverage, community feedback theme, and retrieval risk.

## Candidate Pool V1

### Awwwards: Current Curated / High-Motion / Storytelling

1. `https://www.awwwards.com/sites/truckn-roll-r` — campaign/experience; inspect external URL from detail page.
2. `https://www.awwwards.com/sites/ref-digital` — agency/digital service.
3. `https://www.awwwards.com/sites/hashgraph-ventures` — venture/finance/technology.
4. `https://www.awwwards.com/sites/vaulk` — technology/product.
5. `https://www.awwwards.com/sites/zettajoule` — energy/industrial technology.
6. `https://www.awwwards.com/sites/sowieso-wero` — campaign/culture.
7. `https://www.awwwards.com/sites/cdiscount-jumping-max` — ecommerce/campaign.
8. `https://www.awwwards.com/sites/air-1` — product/experience.
9. `https://www.awwwards.com/sites/razorpay-sprint-26` — fintech/product/campaign.
10. `https://www.awwwards.com/sites/cartier-watches-wonders-2026` — luxury/product/campaign.
11. `https://www.awwwards.com/sites/aimees-papercraft-world` — craft/illustrative/interactive.
12. `https://www.awwwards.com/sites/cleo-ai` — AI/fintech/data storytelling; external URL observed: `https://web.meetcleo.com/`.
13. `https://www.awwwards.com/sites/sidewave` — agency/technology.
14. `https://www.awwwards.com/sites/la-revoltosa` — food/beverage/culture.
15. `https://www.awwwards.com/sites/aino-agency` — agency/studio.
16. `https://www.awwwards.com/sites/a-better-lou` — portfolio/editorial.
17. `https://www.awwwards.com/sites/danzan` — culture/experience.
18. `https://www.awwwards.com/sites/valentin-gassend-portfolio` — portfolio.
19. `https://www.awwwards.com/sites/tresmares-capital` — finance/capital.
20. `https://www.awwwards.com/sites/noxediem-creative-production` — production/studio.
21. `https://www.awwwards.com/sites/fauna-robotics` — robotics/hardware.
22. `https://www.awwwards.com/sites/apechain` — crypto/web3/product.

### Httpster: Type And Style Diversity

23. `https://www.makingsoftware.com/` — software/editorial.
24. `https://www.footer.design/` — design resource/gallery.
25. `https://wam.studio/` — architecture/studio.
26. `https://www.jackywinter.gallery/` — art/gallery.
27. `https://drams.framer.website/` — app/software/framer.
28. `https://bauhausclock.com/` — product/interactive/retro.
29. `https://visualjournal.it/` — editorial/visual journal.
30. `https://benvenusa.com/` — food/beverage/wine.
31. `https://developments.media/` — media/production.
32. `https://patrickmason.studio/` — portfolio/studio.
33. `https://www.cosmos.so/` — community/social/creative tool.
34. `https://www.overpass.com/` — application/software.
35. `https://www.snohetta.com/` — architecture/global studio.
36. `https://www.wiz.io/` — cybersecurity/SaaS.
37. `https://viens-la.com/` — travel/hospitality.
38. `https://middlename.co.uk/` — agency/studio.
39. `https://ossa.wine/` — wine/ecommerce.
40. `https://vivienscreative.com.au/` — creative/talent.
41. `https://www.uspsdelivers.com/2020-2021-generational-research-report/` — report/data/editorial.
42. `https://counter-forms.com/` — typography/resource.
43. `https://uncut.wtf/` — typography/resource.
44. `https://www.livesurface.com/` — product/software.
45. `https://www.buffet.digital/` — agency/studio.
46. `https://www.eclipse.builders/` — product/software.
47. `https://uno.app/` — application/software.
48. `https://amie.so/` — productivity/calendar app.
49. `https://capital.xyz/` — finance/product.
50. `https://arc.net/` — browser/software/product.
51. `https://www.mezmo.com/` — observability/SaaS.
52. `https://www.lunchbox.io/` — food/commerce SaaS.
53. `https://glyphsapp.com/` — design tool/software.
54. `https://rekki.com/` — food/service/app.
55. `https://radix.bio/` — health/biotech.
56. `https://consider.co/` — software/product.
57. `https://www.typeform.com/` — forms/SaaS/product.

### WebInspoo: SaaS Page-Type Patterns

58. `https://www.webinspoo.com/inspiration/airmee-landing-page` — landing page.
59. `https://www.webinspoo.com/inspiration/bevel-landing-page` — landing page.
60. `https://www.webinspoo.com/inspiration/cloudflare-landing-page-2` — landing page.
61. `https://www.webinspoo.com/inspiration/expenseai-landing-page` — AI/finance landing.
62. `https://www.webinspoo.com/inspiration/mistral-landing-page-e2` — AI landing.
63. `https://www.webinspoo.com/inspiration/poolside-landing-page` — AI/dev landing.
64. `https://www.webinspoo.com/inspiration/rerun-landing-page` — developer tool landing.
65. `https://www.webinspoo.com/inspiration/weav-landing-page` — SaaS landing.
66. `https://www.webinspoo.com/inspiration/weave-landing-page` — SaaS landing.
67. `https://www.webinspoo.com/inspiration/accessgrid-pricing-page` — pricing page.
68. `https://www.webinspoo.com/inspiration/braintrust-pricing-pricing-page` — pricing page.
69. `https://www.webinspoo.com/inspiration/browserbase-pricing-page-e2` — pricing page.
70. `https://www.webinspoo.com/inspiration/cloudflare-pricing-page` — pricing page.
71. `https://www.webinspoo.com/inspiration/exa-ai-pricing-page` — AI pricing.
72. `https://www.webinspoo.com/inspiration/unkey-pricing-page` — developer pricing.

## First Batch Plan

Batch 01 should mix high-signal, accessible candidates from different categories:

1. Cleo AI — AI/fintech storytelling; Awwwards tags and external URL available.
2. Wiz — cybersecurity SaaS; Httpster app/software.
3. Cosmos — community/creative tool; Httpster.
4. Arc — browser/product; Httpster.
5. Typeform — forms/SaaS; Httpster.
6. Amie — productivity app; Httpster.
7. Snøhetta — architecture/studio; Httpster.
8. Ossa Wine — food/beverage/ecommerce; Httpster.
9. Counter Forms — typography/resource; Httpster.
10. WebInspoo Cloudflare pricing page — SaaS pricing pattern; WebInspoo page-type reference.

## Current Completion Status

- Candidate pool: complete enough to start Batch 01.
- Verified references under new quality gate: 0.
- Target remaining: 50 verified references.
