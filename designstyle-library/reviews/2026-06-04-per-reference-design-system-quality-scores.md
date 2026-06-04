# Per-Reference Design-System Quality Scores

Date: 2026-06-04

This report scores each active reference individually for practical design-system and component-style reuse. It is not a pure aesthetic taste score; it measures how useful each reference is as implementation-grade evidence.

## Summary

- Active references scored: 76
- Average score: 91.3/100
- Median score: 93.0/100
- Score range: 66 to 100
- 90+: 52
- 80-89: 17
- 70-79: 5
- Below 70: 2
- Blocked/security contamination in active scored files: 0
- Scientific-notation px noise in active scored files: 0

## Rubric

| Dimension | Points | Meaning |
|---|---:|---|
| Retained component evidence | 30 | Component JSON exists, has broad live-browser samples, and comes from real rendered DOM without retaining raw DOM snapshots in the library. |
| Component coverage | 15 | Captures several useful categories such as nav, buttons, cards, forms, icons, and sections. |
| Design-system retention | 15 | Keeps tokens, palette, moodboard, component-styles, palette colors, and component system categories. |
| Component-style usefulness | 15 | `component-styles.md`/`tokens.json` contain reusable computed CSS, geometry, spacing, type, radii, borders, shadows, and transitions. |
| Interaction states | 10 | Hover/focus attempts and actual computed deltas are captured when observable. |
| Retrieval/validation | 10 | Reference has complete L1/L2/L3 paths, evidence limits, and design-system metadata. |
| Hygiene | 5 | No blocked/challenge text and no abnormal scientific-notation px noise in active evidence. |

## Score Table

| # | Slug | Score | Grade | Component evidence /30 | Coverage /15 | Design system /15 | Component styles /15 | States /10 | Retrieval /10 | Hygiene /5 | Samples | Cats | State attempts | Changed states | Palette colors | Penalties |
|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | a24-culture-studio | 100 | A | 30 | 15 | 15 | 15 | 10 | 10 | 5 | 81 | 6 | 12 | 7 | 13 | none |
| 2 | amie-productivity-calendar | 88 | B+ | 29 | 11 | 15 | 14 | 4 | 10 | 5 | 69 | 4 | 7 | 0 | 13 | -1 retained browser component evidence; -4 component category coverage; -1 reusable computed component styles; -6 hover/focus state evidence |
| 3 | apple-vision-pro-product-story | 97 | A | 30 | 13 | 15 | 14 | 10 | 10 | 5 | 124 | 5 | 12 | 11 | 14 | -2 component category coverage; -1 reusable computed component styles |
| 4 | attio-crm-workspace | 89 | B+ | 30 | 13 | 15 | 14 | 2 | 10 | 5 | 94 | 5 | 4 | 0 | 15 | -2 component category coverage; -1 reusable computed component styles; -8 hover/focus state evidence |
| 5 | bauhaus-clock-interactive-product | 71 | C+ | 25 | 8 | 14 | 9 | 0 | 10 | 5 | 32 | 3 | 0 | 0 | 16 | -5 retained browser component evidence; -7 component category coverage; -1 design-system file completeness; -6 reusable computed component styles; -10 hover/focus state evidence |
| 6 | benvenusa-food-wine | 79 | C+ | 27 | 11 | 14 | 12 | 0 | 10 | 5 | 51 | 4 | 1 | 0 | 12 | -3 retained browser component evidence; -4 component category coverage; -1 design-system file completeness; -3 reusable computed component styles; -10 hover/focus state evidence |
| 7 | better-stack-observability | 95 | A | 30 | 15 | 15 | 15 | 5 | 10 | 5 | 132 | 6 | 7 | 1 | 15 | -5 hover/focus state evidence |
| 8 | buffet-digital-agency | 88 | B+ | 28 | 11 | 15 | 15 | 4 | 10 | 5 | 57 | 4 | 9 | 0 | 11 | -2 retained browser component evidence; -4 component category coverage; -6 hover/focus state evidence |
| 9 | capital-finance-product | 85 | B+ | 25 | 13 | 15 | 12 | 5 | 10 | 5 | 26 | 5 | 10 | 0 | 15 | -5 retained browser component evidence; -2 component category coverage; -3 reusable computed component styles; -5 hover/focus state evidence |
| 10 | clay-data-workspace | 95 | A | 30 | 13 | 15 | 14 | 8 | 10 | 5 | 127 | 5 | 9 | 6 | 11 | -2 component category coverage; -1 reusable computed component styles; -2 hover/focus state evidence |
| 11 | cleo-ai-fintech-storytelling | 94 | A- | 30 | 13 | 15 | 14 | 7 | 10 | 5 | 110 | 5 | 11 | 2 | 14 | -2 component category coverage; -1 reusable computed component styles; -3 hover/focus state evidence |
| 12 | climate-trace-explore | 91 | A- | 30 | 11 | 15 | 15 | 5 | 10 | 5 | 97 | 4 | 9 | 1 | 16 | -4 component category coverage; -5 hover/focus state evidence |
| 13 | cosmos-creative-network | 92 | A- | 29 | 15 | 15 | 15 | 3 | 10 | 5 | 69 | 6 | 4 | 2 | 12 | -1 retained browser component evidence; -7 hover/focus state evidence |
| 14 | counter-forms-typography-resource | 80 | B | 26 | 11 | 15 | 12 | 1 | 10 | 5 | 39 | 4 | 1 | 1 | 15 | -4 retained browser component evidence; -4 component category coverage; -3 reusable computed component styles; -9 hover/focus state evidence |
| 15 | cron-calendar-interface | 76 | C+ | 24 | 8 | 14 | 10 | 5 | 10 | 5 | 18 | 3 | 8 | 1 | 16 | -6 retained browser component evidence; -7 component category coverage; -1 design-system file completeness; -5 reusable computed component styles; -5 hover/focus state evidence |
| 16 | developments-media-production | 93 | A- | 30 | 11 | 15 | 14 | 8 | 10 | 5 | 85 | 4 | 9 | 6 | 8 | -4 component category coverage; -1 reusable computed component styles; -2 hover/focus state evidence |
| 17 | eclipse-builders-software | 95 | A | 30 | 13 | 15 | 14 | 8 | 10 | 5 | 82 | 5 | 9 | 6 | 11 | -2 component category coverage; -1 reusable computed component styles; -2 hover/focus state evidence |
| 18 | electricity-maps-app | 87 | B+ | 29 | 11 | 15 | 15 | 2 | 10 | 5 | 71 | 4 | 4 | 0 | 15 | -1 retained browser component evidence; -4 component category coverage; -8 hover/focus state evidence |
| 19 | equals-spreadsheet-analytics | 93 | A- | 29 | 13 | 15 | 15 | 6 | 10 | 5 | 74 | 5 | 12 | 0 | 13 | -1 retained browser component evidence; -2 component category coverage; -4 hover/focus state evidence |
| 20 | figma-design-platform | 94 | A- | 30 | 13 | 15 | 14 | 7 | 10 | 5 | 106 | 5 | 12 | 2 | 11 | -2 component category coverage; -1 reusable computed component styles; -3 hover/focus state evidence |
| 21 | footer-design-gallery-resource | 97 | A | 30 | 13 | 15 | 14 | 10 | 10 | 5 | 102 | 5 | 12 | 10 | 15 | -2 component category coverage; -1 reusable computed component styles |
| 22 | glyphs-app-design-tool | 91 | A- | 30 | 11 | 15 | 14 | 6 | 10 | 5 | 112 | 4 | 12 | 0 | 14 | -4 component category coverage; -1 reusable computed component styles; -4 hover/focus state evidence |
| 23 | hex-data-workspace | 88 | B+ | 30 | 13 | 15 | 15 | 0 | 10 | 5 | 137 | 5 | 1 | 0 | 15 | -2 component category coverage; -10 hover/focus state evidence |
| 24 | jacky-winter-gallery | 95 | A | 30 | 13 | 15 | 15 | 7 | 10 | 5 | 97 | 5 | 9 | 5 | 11 | -2 component category coverage; -3 hover/focus state evidence |
| 25 | linear-product-saas | 99 | A | 30 | 15 | 15 | 15 | 9 | 10 | 5 | 119 | 6 | 11 | 5 | 16 | -1 hover/focus state evidence |
| 26 | livesurface-product-software | 93 | A- | 30 | 11 | 14 | 13 | 10 | 10 | 5 | 77 | 4 | 12 | 8 | 9 | -4 component category coverage; -1 design-system file completeness; -2 reusable computed component styles |
| 27 | lunchbox-restaurant-commerce-saas | 96 | A | 30 | 15 | 15 | 15 | 6 | 10 | 5 | 146 | 6 | 12 | 0 | 12 | -4 hover/focus state evidence |
| 28 | making-software-editorial-tooling | 90 | A- | 29 | 13 | 15 | 14 | 4 | 10 | 5 | 63 | 5 | 5 | 3 | 11 | -1 retained browser component evidence; -2 component category coverage; -1 reusable computed component styles; -6 hover/focus state evidence |
| 29 | mercury-financial-dashboard | 91 | A- | 30 | 15 | 15 | 15 | 1 | 10 | 5 | 104 | 6 | 1 | 1 | 16 | -9 hover/focus state evidence |
| 30 | mezmo-observability-saas | 92 | A- | 30 | 11 | 15 | 14 | 7 | 10 | 5 | 93 | 4 | 11 | 1 | 16 | -4 component category coverage; -1 reusable computed component styles; -3 hover/focus state evidence |
| 31 | middle-name-agency-studio | 85 | B+ | 25 | 13 | 15 | 11 | 6 | 10 | 5 | 18 | 5 | 6 | 4 | 15 | -5 retained browser component evidence; -2 component category coverage; -4 reusable computed component styles; -4 hover/focus state evidence |
| 32 | notion-workspace-product | 98 | A | 30 | 15 | 15 | 15 | 8 | 10 | 5 | 147 | 6 | 8 | 6 | 14 | -2 hover/focus state evidence |
| 33 | observable-data-platform | 89 | B+ | 29 | 11 | 15 | 14 | 5 | 10 | 5 | 70 | 4 | 6 | 3 | 16 | -1 retained browser component evidence; -4 component category coverage; -1 reusable computed component styles; -5 hover/focus state evidence |
| 34 | ossa-wine-ecommerce | 96 | A | 30 | 15 | 15 | 15 | 6 | 10 | 5 | 85 | 6 | 12 | 0 | 12 | -4 hover/focus state evidence |
| 35 | overpass-software-platform | 96 | A | 30 | 15 | 15 | 15 | 6 | 10 | 5 | 126 | 6 | 12 | 0 | 15 | -4 hover/focus state evidence |
| 36 | patrick-mason-studio-portfolio | 69 | C | 23 | 8 | 15 | 8 | 0 | 10 | 5 | 6 | 3 | 1 | 0 | 12 | -7 retained browser component evidence; -7 component category coverage; -7 reusable computed component styles; -10 hover/focus state evidence |
| 37 | pitch-interactive-data-studio | 83 | B | 27 | 11 | 14 | 12 | 4 | 10 | 5 | 44 | 4 | 7 | 0 | 15 | -3 retained browser component evidence; -4 component category coverage; -1 design-system file completeness; -3 reusable computed component styles; -6 hover/focus state evidence |
| 38 | pitch-presentation-workspace | 99 | A | 30 | 15 | 15 | 15 | 9 | 10 | 5 | 81 | 6 | 12 | 5 | 13 | -1 hover/focus state evidence |
| 39 | plausible-analytics-live-dashboard | 92 | A- | 29 | 11 | 15 | 14 | 8 | 10 | 5 | 73 | 4 | 7 | 6 | 15 | -1 retained browser component evidence; -4 component category coverage; -1 reusable computed component styles; -2 hover/focus state evidence |
| 40 | railway-developer-platform | 84 | B | 26 | 11 | 15 | 13 | 4 | 10 | 5 | 38 | 4 | 4 | 3 | 13 | -4 retained browser component evidence; -4 component category coverage; -2 reusable computed component styles; -6 hover/focus state evidence |
| 41 | raycast-productivity | 78 | C+ | 24 | 8 | 15 | 12 | 4 | 10 | 5 | 24 | 3 | 4 | 3 | 15 | -6 retained browser component evidence; -7 component category coverage; -3 reusable computed component styles; -6 hover/focus state evidence |
| 42 | reflect-notes-interface | 94 | A- | 30 | 13 | 15 | 15 | 6 | 10 | 5 | 91 | 5 | 12 | 0 | 15 | -2 component category coverage; -4 hover/focus state evidence |
| 43 | rekki-food-service-app | 94 | A- | 27 | 15 | 15 | 14 | 8 | 10 | 5 | 42 | 6 | 11 | 3 | 12 | -3 retained browser component evidence; -1 reusable computed component styles; -2 hover/focus state evidence |
| 44 | render-cloud-platform | 93 | A- | 29 | 13 | 15 | 14 | 7 | 10 | 5 | 73 | 5 | 12 | 2 | 11 | -1 retained browser component evidence; -2 component category coverage; -1 reusable computed component styles; -3 hover/focus state evidence |
| 45 | retool-internal-tools | 89 | B+ | 30 | 13 | 15 | 14 | 2 | 10 | 5 | 117 | 5 | 4 | 0 | 15 | -2 component category coverage; -1 reusable computed component styles; -8 hover/focus state evidence |
| 46 | rows-spreadsheet-dashboard | 92 | A- | 28 | 13 | 15 | 14 | 7 | 10 | 5 | 60 | 5 | 12 | 1 | 15 | -2 retained browser component evidence; -2 component category coverage; -1 reusable computed component styles; -3 hover/focus state evidence |
| 47 | snohetta-architecture-studio | 93 | A- | 28 | 13 | 15 | 15 | 7 | 10 | 5 | 59 | 5 | 9 | 4 | 12 | -2 retained browser component evidence; -2 component category coverage; -3 hover/focus state evidence |
| 48 | stripe-product-platform | 94 | A- | 30 | 13 | 15 | 14 | 7 | 10 | 5 | 114 | 5 | 9 | 4 | 15 | -2 component category coverage; -1 reusable computed component styles; -3 hover/focus state evidence |
| 49 | supabase-developer-platform | 88 | B+ | 29 | 13 | 15 | 15 | 1 | 10 | 5 | 63 | 5 | 2 | 0 | 16 | -1 retained browser component evidence; -2 component category coverage; -9 hover/focus state evidence |
| 50 | teenage-engineering-hardware-brand | 92 | A- | 28 | 13 | 15 | 15 | 6 | 10 | 5 | 62 | 5 | 12 | 0 | 11 | -2 retained browser component evidence; -2 component category coverage; -4 hover/focus state evidence |
| 51 | the-pudding-data-stories | 95 | A | 29 | 15 | 15 | 15 | 6 | 10 | 5 | 70 | 6 | 11 | 0 | 14 | -1 retained browser component evidence; -4 hover/focus state evidence |
| 52 | tines-automation-platform | 94 | A- | 30 | 15 | 15 | 15 | 4 | 10 | 5 | 126 | 6 | 9 | 0 | 15 | -6 hover/focus state evidence |
| 53 | tinybird-analytics-infrastructure | 89 | B+ | 30 | 11 | 15 | 14 | 4 | 10 | 5 | 98 | 4 | 6 | 2 | 15 | -4 component category coverage; -1 reusable computed component styles; -6 hover/focus state evidence |
| 54 | typeform-product-forms-saas | 92 | A- | 30 | 13 | 15 | 14 | 5 | 10 | 5 | 97 | 5 | 7 | 2 | 16 | -2 component category coverage; -1 reusable computed component styles; -5 hover/focus state evidence |
| 55 | uncut-typography-resource | 80 | B | 24 | 13 | 15 | 10 | 3 | 10 | 5 | 16 | 5 | 5 | 2 | 11 | -6 retained browser component evidence; -2 component category coverage; -5 reusable computed component styles; -7 hover/focus state evidence |
| 56 | usps-delivers-generational-report | 84 | B | 25 | 11 | 15 | 11 | 7 | 10 | 5 | 22 | 4 | 11 | 1 | 13 | -5 retained browser component evidence; -4 component category coverage; -4 reusable computed component styles; -3 hover/focus state evidence |
| 57 | vercel-developer-platform | 91 | A- | 30 | 15 | 15 | 15 | 1 | 10 | 5 | 131 | 6 | 2 | 0 | 15 | -9 hover/focus state evidence |
| 58 | viens-la-travel-hospitality | 93 | A- | 30 | 13 | 15 | 15 | 5 | 10 | 5 | 87 | 5 | 9 | 2 | 16 | -2 component category coverage; -5 hover/focus state evidence |
| 59 | visual-cinnamon-data-art | 95 | A | 28 | 13 | 15 | 14 | 10 | 10 | 5 | 55 | 5 | 12 | 9 | 16 | -2 retained browser component evidence; -2 component category coverage; -1 reusable computed component styles |
| 60 | visual-journal-editorial | 73 | C+ | 24 | 11 | 14 | 7 | 2 | 10 | 5 | 7 | 4 | 4 | 0 | 11 | -6 retained browser component evidence; -4 component category coverage; -1 design-system file completeness; -8 reusable computed component styles; -8 hover/focus state evidence |
| 61 | viviens-creative-talent | 66 | C | 24 | 5 | 14 | 8 | 0 | 10 | 5 | 21 | 2 | 0 | 0 | 11 | -6 retained browser component evidence; -10 component category coverage; -1 design-system file completeness; -7 reusable computed component styles; -10 hover/focus state evidence |
| 62 | wam-architecture-studio | 87 | B+ | 29 | 11 | 14 | 12 | 6 | 10 | 5 | 69 | 4 | 10 | 2 | 11 | -1 retained browser component evidence; -4 component category coverage; -1 design-system file completeness; -3 reusable computed component styles; -4 hover/focus state evidence |
| 63 | webinspoo-accessgrid-pricing-page | 100 | A | 30 | 15 | 15 | 15 | 10 | 10 | 5 | 99 | 6 | 12 | 9 | 12 | none |
| 64 | webinspoo-airmee-landing-page | 100 | A | 30 | 15 | 15 | 15 | 10 | 10 | 5 | 97 | 6 | 12 | 9 | 12 | none |
| 65 | webinspoo-bevel-landing-page | 100 | A | 30 | 15 | 15 | 15 | 10 | 10 | 5 | 99 | 6 | 12 | 9 | 12 | none |
| 66 | webinspoo-braintrust-pricing-page | 100 | A | 30 | 15 | 15 | 15 | 10 | 10 | 5 | 103 | 6 | 12 | 9 | 12 | none |
| 67 | webinspoo-browserbase-pricing-page | 100 | A | 30 | 15 | 15 | 15 | 10 | 10 | 5 | 103 | 6 | 12 | 9 | 13 | none |
| 68 | webinspoo-cloudflare-pricing-pattern | 100 | A | 30 | 15 | 15 | 15 | 10 | 10 | 5 | 103 | 6 | 12 | 9 | 12 | none |
| 69 | webinspoo-exa-ai-pricing-page | 100 | A | 30 | 15 | 15 | 15 | 10 | 10 | 5 | 103 | 6 | 12 | 9 | 12 | none |
| 70 | webinspoo-expenseai-landing-page | 100 | A | 30 | 15 | 15 | 15 | 10 | 10 | 5 | 103 | 6 | 12 | 9 | 12 | none |
| 71 | webinspoo-mistral-ai-landing-page | 100 | A | 30 | 15 | 15 | 15 | 10 | 10 | 5 | 103 | 6 | 12 | 9 | 13 | none |
| 72 | webinspoo-poolside-ai-landing-page | 100 | A | 30 | 15 | 15 | 15 | 10 | 10 | 5 | 102 | 6 | 12 | 9 | 12 | none |
| 73 | webinspoo-rerun-developer-landing-page | 100 | A | 30 | 15 | 15 | 15 | 10 | 10 | 5 | 99 | 6 | 12 | 9 | 12 | none |
| 74 | webinspoo-unkey-pricing-page | 100 | A | 30 | 15 | 15 | 15 | 10 | 10 | 5 | 98 | 6 | 12 | 9 | 12 | none |
| 75 | webinspoo-weav-saas-landing-page | 100 | A | 30 | 15 | 15 | 15 | 10 | 10 | 5 | 103 | 6 | 12 | 9 | 13 | none |
| 76 | wiz-cybersecurity-saas | 90 | A- | 30 | 15 | 15 | 15 | 0 | 10 | 5 | 125 | 6 | 1 | 0 | 15 | -10 hover/focus state evidence |

## Lowest Scores

- `viviens-creative-talent`: 66/100 (C) — weak active reference; consider replacement or manual enrichment; penalties: -6 retained browser component evidence; -10 component category coverage; -1 design-system file completeness; -7 reusable computed component styles; -10 hover/focus state evidence.
- `patrick-mason-studio-portfolio`: 69/100 (C) — weak active reference; consider replacement or manual enrichment; penalties: -7 retained browser component evidence; -7 component category coverage; -7 reusable computed component styles; -10 hover/focus state evidence.
- `bauhaus-clock-interactive-product`: 71/100 (C+) — usable mainly for aesthetic or narrow component cues; penalties: -5 retained browser component evidence; -7 component category coverage; -1 design-system file completeness; -6 reusable computed component styles; -10 hover/focus state evidence.
- `visual-journal-editorial`: 73/100 (C+) — usable mainly for aesthetic or narrow component cues; penalties: -6 retained browser component evidence; -4 component category coverage; -1 design-system file completeness; -8 reusable computed component styles; -8 hover/focus state evidence.
- `cron-calendar-interface`: 76/100 (C+) — usable mainly for aesthetic or narrow component cues; penalties: -6 retained browser component evidence; -7 component category coverage; -1 design-system file completeness; -5 reusable computed component styles; -5 hover/focus state evidence.
- `raycast-productivity`: 78/100 (C+) — usable mainly for aesthetic or narrow component cues; penalties: -6 retained browser component evidence; -7 component category coverage; -3 reusable computed component styles; -6 hover/focus state evidence.
- `benvenusa-food-wine`: 79/100 (C+) — usable mainly for aesthetic or narrow component cues; penalties: -3 retained browser component evidence; -4 component category coverage; -1 design-system file completeness; -3 reusable computed component styles; -10 hover/focus state evidence.
- `counter-forms-typography-resource`: 80/100 (B) — usable with selective follow-up; penalties: -4 retained browser component evidence; -4 component category coverage; -3 reusable computed component styles; -9 hover/focus state evidence.
- `uncut-typography-resource`: 80/100 (B) — usable with selective follow-up; penalties: -6 retained browser component evidence; -2 component category coverage; -5 reusable computed component styles; -7 hover/focus state evidence.
- `pitch-interactive-data-studio`: 83/100 (B) — usable with selective follow-up; penalties: -3 retained browser component evidence; -4 component category coverage; -1 design-system file completeness; -3 reusable computed component styles; -6 hover/focus state evidence.
- `railway-developer-platform`: 84/100 (B) — usable with selective follow-up; penalties: -4 retained browser component evidence; -4 component category coverage; -2 reusable computed component styles; -6 hover/focus state evidence.
- `usps-delivers-generational-report`: 84/100 (B) — usable with selective follow-up; penalties: -5 retained browser component evidence; -4 component category coverage; -4 reusable computed component styles; -3 hover/focus state evidence.

## Evidence Paths

| Slug | Component JSON | Tokens | Component styles | Full reference |
|---|---|---|---|---|
| a24-culture-studio | assets/2026-06-04-a24-culture-studio-component-styles.json | design-systems/a24-culture-studio/tokens.json | design-systems/a24-culture-studio/component-styles.md | references/2026-06-03-a24-culture-studio.md |
| amie-productivity-calendar | assets/2026-06-04-amie-productivity-calendar-component-styles.json | design-systems/amie-productivity-calendar/tokens.json | design-systems/amie-productivity-calendar/component-styles.md | references/2026-06-03-amie-productivity-calendar.md |
| apple-vision-pro-product-story | assets/2026-06-04-apple-vision-pro-product-story-component-styles.json | design-systems/apple-vision-pro-product-story/tokens.json | design-systems/apple-vision-pro-product-story/component-styles.md | references/2026-06-03-apple-vision-pro-product-story.md |
| attio-crm-workspace | assets/2026-06-04-attio-crm-workspace-component-styles.json | design-systems/attio-crm-workspace/tokens.json | design-systems/attio-crm-workspace/component-styles.md | references/2026-06-04-attio-crm-workspace.md |
| bauhaus-clock-interactive-product | assets/2026-06-04-bauhaus-clock-interactive-product-component-styles.json | design-systems/bauhaus-clock-interactive-product/tokens.json | design-systems/bauhaus-clock-interactive-product/component-styles.md | references/2026-06-03-bauhaus-clock-interactive-product.md |
| benvenusa-food-wine | assets/2026-06-04-benvenusa-food-wine-component-styles.json | design-systems/benvenusa-food-wine/tokens.json | design-systems/benvenusa-food-wine/component-styles.md | references/2026-06-03-benvenusa-food-wine.md |
| better-stack-observability | assets/2026-06-04-better-stack-observability-component-styles.json | design-systems/better-stack-observability/tokens.json | design-systems/better-stack-observability/component-styles.md | references/2026-06-04-better-stack-observability.md |
| buffet-digital-agency | assets/2026-06-04-buffet-digital-agency-component-styles.json | design-systems/buffet-digital-agency/tokens.json | design-systems/buffet-digital-agency/component-styles.md | references/2026-06-03-buffet-digital-agency.md |
| capital-finance-product | assets/2026-06-04-capital-finance-product-component-styles.json | design-systems/capital-finance-product/tokens.json | design-systems/capital-finance-product/component-styles.md | references/2026-06-03-capital-finance-product.md |
| clay-data-workspace | assets/2026-06-04-clay-data-workspace-component-styles.json | design-systems/clay-data-workspace/tokens.json | design-systems/clay-data-workspace/component-styles.md | references/2026-06-04-clay-data-workspace.md |
| cleo-ai-fintech-storytelling | assets/2026-06-04-cleo-ai-fintech-storytelling-component-styles.json | design-systems/cleo-ai-fintech-storytelling/tokens.json | design-systems/cleo-ai-fintech-storytelling/component-styles.md | references/2026-06-03-cleo-ai-fintech-storytelling.md |
| climate-trace-explore | assets/2026-06-04-climate-trace-explore-component-styles.json | design-systems/climate-trace-explore/tokens.json | design-systems/climate-trace-explore/component-styles.md | references/2026-06-04-climate-trace-explore.md |
| cosmos-creative-network | assets/2026-06-04-cosmos-creative-network-component-styles.json | design-systems/cosmos-creative-network/tokens.json | design-systems/cosmos-creative-network/component-styles.md | references/2026-06-03-cosmos-creative-network.md |
| counter-forms-typography-resource | assets/2026-06-04-counter-forms-typography-resource-component-styles.json | design-systems/counter-forms-typography-resource/tokens.json | design-systems/counter-forms-typography-resource/component-styles.md | references/2026-06-03-counter-forms-typography-resource.md |
| cron-calendar-interface | assets/2026-06-04-cron-calendar-interface-component-styles.json | design-systems/cron-calendar-interface/tokens.json | design-systems/cron-calendar-interface/component-styles.md | references/2026-06-04-cron-calendar-interface.md |
| developments-media-production | assets/2026-06-04-developments-media-production-component-styles.json | design-systems/developments-media-production/tokens.json | design-systems/developments-media-production/component-styles.md | references/2026-06-03-developments-media-production.md |
| eclipse-builders-software | assets/2026-06-04-eclipse-builders-software-component-styles.json | design-systems/eclipse-builders-software/tokens.json | design-systems/eclipse-builders-software/component-styles.md | references/2026-06-03-eclipse-builders-software.md |
| electricity-maps-app | assets/2026-06-04-electricity-maps-app-component-styles.json | design-systems/electricity-maps-app/tokens.json | design-systems/electricity-maps-app/component-styles.md | references/2026-06-04-electricity-maps-app.md |
| equals-spreadsheet-analytics | assets/2026-06-04-equals-spreadsheet-analytics-component-styles.json | design-systems/equals-spreadsheet-analytics/tokens.json | design-systems/equals-spreadsheet-analytics/component-styles.md | references/2026-06-04-equals-spreadsheet-analytics.md |
| figma-design-platform | assets/2026-06-04-figma-design-platform-component-styles.json | design-systems/figma-design-platform/tokens.json | design-systems/figma-design-platform/component-styles.md | references/2026-06-03-figma-design-platform.md |
| footer-design-gallery-resource | assets/2026-06-04-footer-design-gallery-resource-component-styles.json | design-systems/footer-design-gallery-resource/tokens.json | design-systems/footer-design-gallery-resource/component-styles.md | references/2026-06-03-footer-design-gallery-resource.md |
| glyphs-app-design-tool | assets/2026-06-04-glyphs-app-design-tool-component-styles.json | design-systems/glyphs-app-design-tool/tokens.json | design-systems/glyphs-app-design-tool/component-styles.md | references/2026-06-03-glyphs-app-design-tool.md |
| hex-data-workspace | assets/2026-06-04-hex-data-workspace-component-styles.json | design-systems/hex-data-workspace/tokens.json | design-systems/hex-data-workspace/component-styles.md | references/2026-06-04-hex-data-workspace.md |
| jacky-winter-gallery | assets/2026-06-04-jacky-winter-gallery-component-styles.json | design-systems/jacky-winter-gallery/tokens.json | design-systems/jacky-winter-gallery/component-styles.md | references/2026-06-03-jacky-winter-gallery.md |
| linear-product-saas | assets/2026-06-04-linear-product-saas-component-styles.json | design-systems/linear-product-saas/tokens.json | design-systems/linear-product-saas/component-styles.md | references/2026-06-03-linear-product-saas.md |
| livesurface-product-software | assets/2026-06-04-livesurface-product-software-component-styles.json | design-systems/livesurface-product-software/tokens.json | design-systems/livesurface-product-software/component-styles.md | references/2026-06-03-livesurface-product-software.md |
| lunchbox-restaurant-commerce-saas | assets/2026-06-04-lunchbox-restaurant-commerce-saas-component-styles.json | design-systems/lunchbox-restaurant-commerce-saas/tokens.json | design-systems/lunchbox-restaurant-commerce-saas/component-styles.md | references/2026-06-03-lunchbox-restaurant-commerce-saas.md |
| making-software-editorial-tooling | assets/2026-06-04-making-software-editorial-tooling-component-styles.json | design-systems/making-software-editorial-tooling/tokens.json | design-systems/making-software-editorial-tooling/component-styles.md | references/2026-06-03-making-software-editorial-tooling.md |
| mercury-financial-dashboard | assets/2026-06-04-mercury-financial-dashboard-component-styles.json | design-systems/mercury-financial-dashboard/tokens.json | design-systems/mercury-financial-dashboard/component-styles.md | references/2026-06-04-mercury-financial-dashboard.md |
| mezmo-observability-saas | assets/2026-06-04-mezmo-observability-saas-component-styles.json | design-systems/mezmo-observability-saas/tokens.json | design-systems/mezmo-observability-saas/component-styles.md | references/2026-06-03-mezmo-observability-saas.md |
| middle-name-agency-studio | assets/2026-06-04-middle-name-agency-studio-component-styles.json | design-systems/middle-name-agency-studio/tokens.json | design-systems/middle-name-agency-studio/component-styles.md | references/2026-06-03-middle-name-agency-studio.md |
| notion-workspace-product | assets/2026-06-04-notion-workspace-product-component-styles.json | design-systems/notion-workspace-product/tokens.json | design-systems/notion-workspace-product/component-styles.md | references/2026-06-03-notion-workspace-product.md |
| observable-data-platform | assets/2026-06-04-observable-data-platform-component-styles.json | design-systems/observable-data-platform/tokens.json | design-systems/observable-data-platform/component-styles.md | references/2026-06-04-observable-data-platform.md |
| ossa-wine-ecommerce | assets/2026-06-04-ossa-wine-ecommerce-component-styles.json | design-systems/ossa-wine-ecommerce/tokens.json | design-systems/ossa-wine-ecommerce/component-styles.md | references/2026-06-03-ossa-wine-ecommerce.md |
| overpass-software-platform | assets/2026-06-04-overpass-software-platform-component-styles.json | design-systems/overpass-software-platform/tokens.json | design-systems/overpass-software-platform/component-styles.md | references/2026-06-03-overpass-software-platform.md |
| patrick-mason-studio-portfolio | assets/2026-06-04-patrick-mason-studio-portfolio-component-styles.json | design-systems/patrick-mason-studio-portfolio/tokens.json | design-systems/patrick-mason-studio-portfolio/component-styles.md | references/2026-06-03-patrick-mason-studio-portfolio.md |
| pitch-interactive-data-studio | assets/2026-06-04-pitch-interactive-data-studio-component-styles.json | design-systems/pitch-interactive-data-studio/tokens.json | design-systems/pitch-interactive-data-studio/component-styles.md | references/2026-06-04-pitch-interactive-data-studio.md |
| pitch-presentation-workspace | assets/2026-06-04-pitch-presentation-workspace-component-styles.json | design-systems/pitch-presentation-workspace/tokens.json | design-systems/pitch-presentation-workspace/component-styles.md | references/2026-06-04-pitch-presentation-workspace.md |
| plausible-analytics-live-dashboard | assets/2026-06-04-plausible-analytics-live-dashboard-component-styles.json | design-systems/plausible-analytics-live-dashboard/tokens.json | design-systems/plausible-analytics-live-dashboard/component-styles.md | references/2026-06-04-plausible-analytics-live-dashboard.md |
| railway-developer-platform | assets/2026-06-04-railway-developer-platform-component-styles.json | design-systems/railway-developer-platform/tokens.json | design-systems/railway-developer-platform/component-styles.md | references/2026-06-04-railway-developer-platform.md |
| raycast-productivity | assets/2026-06-04-raycast-productivity-component-styles.json | design-systems/raycast-productivity/tokens.json | design-systems/raycast-productivity/component-styles.md | references/2026-06-04-raycast-productivity.md |
| reflect-notes-interface | assets/2026-06-04-reflect-notes-interface-component-styles.json | design-systems/reflect-notes-interface/tokens.json | design-systems/reflect-notes-interface/component-styles.md | references/2026-06-04-reflect-notes-interface.md |
| rekki-food-service-app | assets/2026-06-04-rekki-food-service-app-component-styles.json | design-systems/rekki-food-service-app/tokens.json | design-systems/rekki-food-service-app/component-styles.md | references/2026-06-03-rekki-food-service-app.md |
| render-cloud-platform | assets/2026-06-04-render-cloud-platform-component-styles.json | design-systems/render-cloud-platform/tokens.json | design-systems/render-cloud-platform/component-styles.md | references/2026-06-04-render-cloud-platform.md |
| retool-internal-tools | assets/2026-06-04-retool-internal-tools-component-styles.json | design-systems/retool-internal-tools/tokens.json | design-systems/retool-internal-tools/component-styles.md | references/2026-06-04-retool-internal-tools.md |
| rows-spreadsheet-dashboard | assets/2026-06-04-rows-spreadsheet-dashboard-component-styles.json | design-systems/rows-spreadsheet-dashboard/tokens.json | design-systems/rows-spreadsheet-dashboard/component-styles.md | references/2026-06-04-rows-spreadsheet-dashboard.md |
| snohetta-architecture-studio | assets/2026-06-04-snohetta-architecture-studio-component-styles.json | design-systems/snohetta-architecture-studio/tokens.json | design-systems/snohetta-architecture-studio/component-styles.md | references/2026-06-03-snohetta-architecture-studio.md |
| stripe-product-platform | assets/2026-06-04-stripe-product-platform-component-styles.json | design-systems/stripe-product-platform/tokens.json | design-systems/stripe-product-platform/component-styles.md | references/2026-06-03-stripe-product-platform.md |
| supabase-developer-platform | assets/2026-06-04-supabase-developer-platform-component-styles.json | design-systems/supabase-developer-platform/tokens.json | design-systems/supabase-developer-platform/component-styles.md | references/2026-06-04-supabase-developer-platform.md |
| teenage-engineering-hardware-brand | assets/2026-06-04-teenage-engineering-hardware-brand-component-styles.json | design-systems/teenage-engineering-hardware-brand/tokens.json | design-systems/teenage-engineering-hardware-brand/component-styles.md | references/2026-06-03-teenage-engineering-hardware-brand.md |
| the-pudding-data-stories | assets/2026-06-04-the-pudding-data-stories-component-styles.json | design-systems/the-pudding-data-stories/tokens.json | design-systems/the-pudding-data-stories/component-styles.md | references/2026-06-04-the-pudding-data-stories.md |
| tines-automation-platform | assets/2026-06-04-tines-automation-platform-component-styles.json | design-systems/tines-automation-platform/tokens.json | design-systems/tines-automation-platform/component-styles.md | references/2026-06-04-tines-automation-platform.md |
| tinybird-analytics-infrastructure | assets/2026-06-04-tinybird-analytics-infrastructure-component-styles.json | design-systems/tinybird-analytics-infrastructure/tokens.json | design-systems/tinybird-analytics-infrastructure/component-styles.md | references/2026-06-04-tinybird-analytics-infrastructure.md |
| typeform-product-forms-saas | assets/2026-06-04-typeform-product-forms-saas-component-styles.json | design-systems/typeform-product-forms-saas/tokens.json | design-systems/typeform-product-forms-saas/component-styles.md | references/2026-06-03-typeform-product-forms-saas.md |
| uncut-typography-resource | assets/2026-06-04-uncut-typography-resource-component-styles.json | design-systems/uncut-typography-resource/tokens.json | design-systems/uncut-typography-resource/component-styles.md | references/2026-06-03-uncut-typography-resource.md |
| usps-delivers-generational-report | assets/2026-06-04-usps-delivers-generational-report-component-styles.json | design-systems/usps-delivers-generational-report/tokens.json | design-systems/usps-delivers-generational-report/component-styles.md | references/2026-06-03-usps-delivers-generational-report.md |
| vercel-developer-platform | assets/2026-06-04-vercel-developer-platform-component-styles.json | design-systems/vercel-developer-platform/tokens.json | design-systems/vercel-developer-platform/component-styles.md | references/2026-06-03-vercel-developer-platform.md |
| viens-la-travel-hospitality | assets/2026-06-04-viens-la-travel-hospitality-component-styles.json | design-systems/viens-la-travel-hospitality/tokens.json | design-systems/viens-la-travel-hospitality/component-styles.md | references/2026-06-03-viens-la-travel-hospitality.md |
| visual-cinnamon-data-art | assets/2026-06-04-visual-cinnamon-data-art-component-styles.json | design-systems/visual-cinnamon-data-art/tokens.json | design-systems/visual-cinnamon-data-art/component-styles.md | references/2026-06-04-visual-cinnamon-data-art.md |
| visual-journal-editorial | assets/2026-06-04-visual-journal-editorial-component-styles.json | design-systems/visual-journal-editorial/tokens.json | design-systems/visual-journal-editorial/component-styles.md | references/2026-06-03-visual-journal-editorial.md |
| viviens-creative-talent | assets/2026-06-04-viviens-creative-talent-component-styles.json | design-systems/viviens-creative-talent/tokens.json | design-systems/viviens-creative-talent/component-styles.md | references/2026-06-03-viviens-creative-talent.md |
| wam-architecture-studio | assets/2026-06-04-wam-architecture-studio-component-styles.json | design-systems/wam-architecture-studio/tokens.json | design-systems/wam-architecture-studio/component-styles.md | references/2026-06-03-wam-architecture-studio.md |
| webinspoo-accessgrid-pricing-page | assets/2026-06-04-webinspoo-accessgrid-pricing-page-component-styles.json | design-systems/webinspoo-accessgrid-pricing-page/tokens.json | design-systems/webinspoo-accessgrid-pricing-page/component-styles.md | references/2026-06-03-webinspoo-accessgrid-pricing-page.md |
| webinspoo-airmee-landing-page | assets/2026-06-04-webinspoo-airmee-landing-page-component-styles.json | design-systems/webinspoo-airmee-landing-page/tokens.json | design-systems/webinspoo-airmee-landing-page/component-styles.md | references/2026-06-03-webinspoo-airmee-landing-page.md |
| webinspoo-bevel-landing-page | assets/2026-06-04-webinspoo-bevel-landing-page-component-styles.json | design-systems/webinspoo-bevel-landing-page/tokens.json | design-systems/webinspoo-bevel-landing-page/component-styles.md | references/2026-06-03-webinspoo-bevel-landing-page.md |
| webinspoo-braintrust-pricing-page | assets/2026-06-04-webinspoo-braintrust-pricing-page-component-styles.json | design-systems/webinspoo-braintrust-pricing-page/tokens.json | design-systems/webinspoo-braintrust-pricing-page/component-styles.md | references/2026-06-03-webinspoo-braintrust-pricing-page.md |
| webinspoo-browserbase-pricing-page | assets/2026-06-04-webinspoo-browserbase-pricing-page-component-styles.json | design-systems/webinspoo-browserbase-pricing-page/tokens.json | design-systems/webinspoo-browserbase-pricing-page/component-styles.md | references/2026-06-03-webinspoo-browserbase-pricing-page.md |
| webinspoo-cloudflare-pricing-pattern | assets/2026-06-04-webinspoo-cloudflare-pricing-pattern-component-styles.json | design-systems/webinspoo-cloudflare-pricing-pattern/tokens.json | design-systems/webinspoo-cloudflare-pricing-pattern/component-styles.md | references/2026-06-03-webinspoo-cloudflare-pricing-pattern.md |
| webinspoo-exa-ai-pricing-page | assets/2026-06-04-webinspoo-exa-ai-pricing-page-component-styles.json | design-systems/webinspoo-exa-ai-pricing-page/tokens.json | design-systems/webinspoo-exa-ai-pricing-page/component-styles.md | references/2026-06-03-webinspoo-exa-ai-pricing-page.md |
| webinspoo-expenseai-landing-page | assets/2026-06-04-webinspoo-expenseai-landing-page-component-styles.json | design-systems/webinspoo-expenseai-landing-page/tokens.json | design-systems/webinspoo-expenseai-landing-page/component-styles.md | references/2026-06-03-webinspoo-expenseai-landing-page.md |
| webinspoo-mistral-ai-landing-page | assets/2026-06-04-webinspoo-mistral-ai-landing-page-component-styles.json | design-systems/webinspoo-mistral-ai-landing-page/tokens.json | design-systems/webinspoo-mistral-ai-landing-page/component-styles.md | references/2026-06-03-webinspoo-mistral-ai-landing-page.md |
| webinspoo-poolside-ai-landing-page | assets/2026-06-04-webinspoo-poolside-ai-landing-page-component-styles.json | design-systems/webinspoo-poolside-ai-landing-page/tokens.json | design-systems/webinspoo-poolside-ai-landing-page/component-styles.md | references/2026-06-03-webinspoo-poolside-ai-landing-page.md |
| webinspoo-rerun-developer-landing-page | assets/2026-06-04-webinspoo-rerun-developer-landing-page-component-styles.json | design-systems/webinspoo-rerun-developer-landing-page/tokens.json | design-systems/webinspoo-rerun-developer-landing-page/component-styles.md | references/2026-06-03-webinspoo-rerun-developer-landing-page.md |
| webinspoo-unkey-pricing-page | assets/2026-06-04-webinspoo-unkey-pricing-page-component-styles.json | design-systems/webinspoo-unkey-pricing-page/tokens.json | design-systems/webinspoo-unkey-pricing-page/component-styles.md | references/2026-06-03-webinspoo-unkey-pricing-page.md |
| webinspoo-weav-saas-landing-page | assets/2026-06-04-webinspoo-weav-saas-landing-page-component-styles.json | design-systems/webinspoo-weav-saas-landing-page/tokens.json | design-systems/webinspoo-weav-saas-landing-page/component-styles.md | references/2026-06-03-webinspoo-weav-saas-landing-page.md |
| wiz-cybersecurity-saas | assets/2026-06-04-wiz-cybersecurity-saas-component-styles.json | design-systems/wiz-cybersecurity-saas/tokens.json | design-systems/wiz-cybersecurity-saas/component-styles.md | references/2026-06-03-wiz-cybersecurity-saas.md |
