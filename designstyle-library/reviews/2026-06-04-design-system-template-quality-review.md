# Design-System Template Quality Review

Date: 2026-06-04

## Score

Overall template quality score: **86.3/100** across 77 references.

| Metric | Value |
|---|---:|
| count | 77 |
| average | 86.3 |
| median | 88 |
| min | 76 |
| max | 88 |
| below_80 | 1 |
| below_85 | 6 |
| scientific_noise | 0 |
| cookie_noise | 0 |
| files_with_9999px | 8 |

## Rubric

- 20 pts: required artifact structure exists (`tokens.json`, `palette.md`, `moodboard.svg`, `component-styles.md`).
- 20 pts: palette breadth and exact source grounding from screenshot pixels or explicit color evidence.
- 16 pts: observed component style sections contain reusable style evidence.
- 8 pts: component content samples are present where the reference exposed them.
- 8 pts: missing evidence is explicit and bounded.
- 8 pts: no scientific-notation radius, cookie/banner, or modal contamination remains.
- 20 pts: cards, token schema, paths, and `use-designstyle --design-system` retrieval are validator-backed.
- Up to 12 pts deducted for generic carryover such as manual-refinement warnings or unmeasured component fields.

## Findings

- Color-system retention is strong: every reference has exact palette values from screenshot pixels and/or explicit DOM/reference colors.
- Retrieval quality is strong: `design_system_paths` are present on all 77 cards, and `use-designstyle` can expose palette and component-style summaries.
- Component-style retention is useful but not uniformly implementation-grade. It captures observed navigation density, radii/surface grammar, buttons/links text, and state clues, while keeping missing button sizing, form styling, icon stroke, and feedback-state gaps explicit.
- Noise handling is acceptable: scientific-notation radius artifacts and cookie/banner/modal contamination are absent. Common `9999px` pill radii are retained as valid CSS evidence.

## All Reference Scores

| # | Slug | Score | Grade | Colors | Style sections | Content sections | Missing sections | Weak hits | Note |
|---:|---|---:|---|---:|---:|---:|---:|---:|---|
| 1 | uncut-typography-resource | 76 | C+ | 9 | 3 | 0 | 3 | 16 | color adequate; component samples weak; manual refinement needed |
| 2 | bauhaus-clock-interactive-product | 80 | B | 16 | 3 | 0 | 3 | 16 | color strong; component samples weak; manual refinement needed |
| 3 | buffet-digital-agency | 80 | B | 11 | 3 | 0 | 3 | 16 | color strong; component samples weak; manual refinement needed |
| 4 | viviens-creative-talent | 80 | B | 11 | 3 | 0 | 3 | 16 | color strong; component samples weak; manual refinement needed |
| 5 | developments-media-production | 81 | B | 8 | 3 | 1 | 3 | 15 | color adequate; component samples partial |
| 6 | livesurface-product-software | 81 | B | 9 | 3 | 1 | 3 | 15 | color adequate; component samples partial |
| 7 | a24-culture-studio | 85 | B+ | 14 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 8 | arc-browser-product-site | 85 | B+ | 16 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 9 | benvenusa-food-wine | 85 | B+ | 12 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 10 | climate-trace-explore | 85 | B+ | 16 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 11 | counter-forms-typography-resource | 85 | B+ | 14 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 12 | eclipse-builders-software | 85 | B+ | 11 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 13 | electricity-maps-app | 85 | B+ | 15 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 14 | glyphs-app-design-tool | 85 | B+ | 13 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 15 | hex-data-workspace | 85 | B+ | 15 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 16 | lunchbox-restaurant-commerce-saas | 85 | B+ | 12 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 17 | making-software-editorial-tooling | 85 | B+ | 11 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 18 | mezmo-observability-saas | 85 | B+ | 16 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 19 | middle-name-agency-studio | 85 | B+ | 10 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 20 | notion-workspace-product | 85 | B+ | 14 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 21 | patrick-mason-studio-portfolio | 85 | B+ | 12 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 22 | pitch-interactive-data-studio | 85 | B+ | 15 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 23 | railway-developer-platform | 85 | B+ | 12 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 24 | raycast-productivity | 85 | B+ | 15 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 25 | reflect-notes-interface | 85 | B+ | 14 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 26 | rekki-food-service-app | 85 | B+ | 12 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 27 | render-cloud-platform | 85 | B+ | 12 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 28 | retool-internal-tools | 85 | B+ | 15 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 29 | the-pudding-data-stories | 85 | B+ | 14 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 30 | tinybird-analytics-infrastructure | 85 | B+ | 15 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 31 | vercel-developer-platform | 85 | B+ | 15 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 32 | viens-la-travel-hospitality | 85 | B+ | 16 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 33 | visual-cinnamon-data-art | 85 | B+ | 16 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 34 | wam-architecture-studio | 85 | B+ | 12 | 3 | 1 | 3 | 15 | color strong; component samples partial |
| 35 | amie-productivity-calendar | 88 | B+ | 13 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 36 | apple-vision-pro-product-story | 88 | B+ | 14 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 37 | attio-crm-workspace | 88 | B+ | 15 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 38 | better-stack-observability | 88 | B+ | 15 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 39 | capital-finance-product | 88 | B+ | 15 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 40 | clay-data-workspace | 88 | B+ | 11 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 41 | cleo-ai-fintech-storytelling | 88 | B+ | 12 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 42 | cosmos-creative-network | 88 | B+ | 12 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 43 | cron-calendar-interface | 88 | B+ | 16 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 44 | equals-spreadsheet-analytics | 88 | B+ | 13 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 45 | figma-design-platform | 88 | B+ | 10 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 46 | footer-design-gallery-resource | 88 | B+ | 15 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 47 | jacky-winter-gallery | 88 | B+ | 11 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 48 | linear-product-saas | 88 | B+ | 16 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 49 | mercury-financial-dashboard | 88 | B+ | 16 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 50 | observable-data-platform | 88 | B+ | 14 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 51 | ossa-wine-ecommerce | 88 | B+ | 12 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 52 | overpass-software-platform | 88 | B+ | 15 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 53 | pitch-presentation-workspace | 88 | B+ | 13 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 54 | plausible-analytics-live-dashboard | 88 | B+ | 15 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 55 | rows-spreadsheet-dashboard | 88 | B+ | 16 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 56 | snohetta-architecture-studio | 88 | B+ | 12 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 57 | stripe-product-platform | 88 | B+ | 15 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 58 | supabase-developer-platform | 88 | B+ | 16 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 59 | teenage-engineering-hardware-brand | 88 | B+ | 11 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 60 | tines-automation-platform | 88 | B+ | 14 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 61 | typeform-product-forms-saas | 88 | B+ | 16 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 62 | usps-delivers-generational-report | 88 | B+ | 13 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 63 | visual-journal-editorial | 88 | B+ | 11 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 64 | webinspoo-accessgrid-pricing-page | 88 | B+ | 12 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 65 | webinspoo-airmee-landing-page | 88 | B+ | 12 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 66 | webinspoo-bevel-landing-page | 88 | B+ | 12 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 67 | webinspoo-braintrust-pricing-page | 88 | B+ | 12 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 68 | webinspoo-browserbase-pricing-page | 88 | B+ | 13 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 69 | webinspoo-cloudflare-pricing-pattern | 88 | B+ | 12 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 70 | webinspoo-exa-ai-pricing-page | 88 | B+ | 12 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 71 | webinspoo-expenseai-landing-page | 88 | B+ | 12 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 72 | webinspoo-mistral-ai-landing-page | 88 | B+ | 13 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 73 | webinspoo-poolside-ai-landing-page | 88 | B+ | 12 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 74 | webinspoo-rerun-developer-landing-page | 88 | B+ | 12 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 75 | webinspoo-unkey-pricing-page | 88 | B+ | 12 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 76 | webinspoo-weav-saas-landing-page | 88 | B+ | 13 | 3 | 2 | 3 | 14 | color strong; component samples good |
| 77 | wiz-cybersecurity-saas | 88 | B+ | 15 | 3 | 2 | 3 | 14 | color strong; component samples good |

## Verdict

The template is production-useful as a retained reference layer and retrieval aid. It should not be presented as a fully measured design-system spec for every reference yet; manual refinement is still needed before directly implementing exact component dimensions or interaction states from weaker entries.
