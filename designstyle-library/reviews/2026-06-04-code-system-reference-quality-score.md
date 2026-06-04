# Code/System Reference Quality Score

Date: 2026-06-04

Note: this is the first active-library aggregate scoring pass. The current stricter per-reference score report, with dimension-level point breakdown and post text-noise cleanup verification, is `designstyle-library/reviews/2026-06-04-per-reference-design-system-quality-scores.md`.

## Overall Score

Overall active-library code/design-system usefulness score: **93.8/100** across 76 active references.

Independent clean-context sub-agent score before blocked-page/raw-noise cleanup was **84/100**. A later clean-context sub-agent scored the state before final L2/L3 text-noise cleanup at **88/100**. The current per-reference report scores the cleaned active library at **91.3/100 average** and **93.0/100 median**, with 0 active blocked/challenge contamination and 0 scientific-notation px noise in active scored files.

| Metric | Value |
|---|---:|
| active_reference_count | 76 |
| excluded_blocked_references | 1 |
| active_component_json_count | 76 |
| non_empty_component_json | 76 |
| total_component_samples | 6226 |
| median_component_samples | 89.0 |
| min_component_samples | 6 |
| max_component_samples | 147 |
| total_hover_focus_state_samples | 641 |
| median_hover_focus_state_samples | 9.0 |
| average_score | 93.8 |
| median_score | 98.0 |
| min_score | 66 |
| max_score | 98 |
| below_80 | 8 |
| below_85 | 9 |
| scientific_px_noise_files | 0 |
| files_retaining_9999px | 10 |

## Rubric

- 30 pts: live browser component-code evidence is non-empty and broad enough for reuse.
- 20 pts: component categories cover nav/buttons/cards/forms/icons/sections rather than one narrow artifact.
- 15 pts: generated design systems expose computed geometry and CSS style facts in `component-styles.md` and `tokens.json`.
- 10 pts: hover/focus state deltas are captured where interactive elements exist.
- 10 pts: references remain practically reusable and are not dominated by challenge/captcha/security pages.
- 10 pts: progressive search/design-system retrieval and validators pass.
- 5 pts: evidence hygiene, including no scientific-notation CSS artifacts while preserving valid `9999px` pill radii.

## Findings

- Active library now excludes the blocked `arc-browser-product-site` capture because it represented a Cloudflare challenge page, not Arc UI.
- Every active reference has a non-empty live-DOM component JSON; active total captured component samples: 6226.
- Component systems now include rect geometry, computed color/background/border/radius/shadow/padding/gap/type/transition facts, and hover/focus deltas where observable.
- Raw JSON and generated design-system artifacts have 0 scientific-notation px values after cleanup. Valid `9999px` pill radii remain retained.
- Remaining low scores are mostly sparse/portfolio/editorial references with few exposed reusable components, not tool failures.

## Blocked Reference Exclusion

- `arc-browser-product-site` moved to `designstyle-library/references-excluded/blocked/` with evidence in `assets-excluded/blocked/`; it no longer counts toward active reference totals or design-system quality.

## All Active Reference Scores

| # | Slug | Score | Grade | Samples | States | Categories | Computed Style Categories | Note |
|---:|---|---:|---|---:|---:|---:|---:|---|
| 1 | a24-culture-studio | 98 | A | 81 | 12 | 6 | 5 | computed component evidence useful |
| 2 | amie-productivity-calendar | 94 | A | 69 | 7 | 4 | 4 | computed component evidence useful |
| 3 | apple-vision-pro-product-story | 98 | A | 124 | 12 | 5 | 4 | computed component evidence useful |
| 4 | attio-crm-workspace | 98 | A | 94 | 4 | 5 | 4 | computed component evidence useful |
| 5 | bauhaus-clock-interactive-product | 77 | C+ | 32 | 0 | 3 | 2 | computed component evidence useful |
| 6 | benvenusa-food-wine | 85 | B+ | 51 | 1 | 4 | 3 | computed component evidence useful |
| 7 | better-stack-observability | 98 | A | 132 | 7 | 6 | 5 | computed component evidence useful |
| 8 | buffet-digital-agency | 92 | A- | 57 | 9 | 4 | 4 | computed component evidence useful |
| 9 | capital-finance-product | 89 | B+ | 26 | 10 | 5 | 4 | computed component evidence useful |
| 10 | clay-data-workspace | 98 | A | 127 | 9 | 5 | 4 | computed component evidence useful |
| 11 | cleo-ai-fintech-storytelling | 98 | A | 110 | 11 | 5 | 4 | computed component evidence useful |
| 12 | climate-trace-explore | 98 | A | 97 | 9 | 4 | 4 | computed component evidence useful |
| 13 | cosmos-creative-network | 97 | A | 69 | 4 | 6 | 5 | computed component evidence useful |
| 14 | counter-forms-typography-resource | 83 | B | 39 | 1 | 4 | 3 | computed component evidence useful |
| 15 | cron-calendar-interface | 72 | C+ | 18 | 8 | 3 | 3 | low sample coverage |
| 16 | developments-media-production | 96 | A | 85 | 9 | 4 | 3 | computed component evidence useful |
| 17 | eclipse-builders-software | 98 | A | 82 | 9 | 5 | 4 | computed component evidence useful |
| 18 | electricity-maps-app | 93 | A | 71 | 4 | 4 | 4 | computed component evidence useful |
| 19 | equals-spreadsheet-analytics | 98 | A | 74 | 12 | 5 | 5 | computed component evidence useful |
| 20 | figma-design-platform | 98 | A | 106 | 12 | 5 | 4 | computed component evidence useful |
| 21 | footer-design-gallery-resource | 98 | A | 102 | 12 | 5 | 4 | computed component evidence useful |
| 22 | glyphs-app-design-tool | 98 | A | 112 | 12 | 4 | 4 | computed component evidence useful |
| 23 | hex-data-workspace | 98 | A | 137 | 1 | 5 | 5 | computed component evidence useful |
| 24 | jacky-winter-gallery | 98 | A | 97 | 9 | 5 | 5 | computed component evidence useful |
| 25 | linear-product-saas | 98 | A | 119 | 11 | 6 | 5 | computed component evidence useful |
| 26 | livesurface-product-software | 96 | A | 77 | 12 | 4 | 3 | computed component evidence useful |
| 27 | lunchbox-restaurant-commerce-saas | 98 | A | 146 | 12 | 6 | 5 | computed component evidence useful |
| 28 | making-software-editorial-tooling | 94 | A | 63 | 5 | 5 | 4 | computed component evidence useful |
| 29 | mercury-financial-dashboard | 98 | A | 104 | 1 | 6 | 5 | computed component evidence useful |
| 30 | mezmo-observability-saas | 98 | A | 93 | 11 | 4 | 4 | computed component evidence useful |
| 31 | middle-name-agency-studio | 78 | C+ | 18 | 6 | 5 | 4 | low sample coverage |
| 32 | notion-workspace-product | 98 | A | 147 | 8 | 6 | 5 | computed component evidence useful |
| 33 | observable-data-platform | 94 | A | 70 | 6 | 4 | 4 | computed component evidence useful |
| 34 | ossa-wine-ecommerce | 98 | A | 85 | 12 | 6 | 5 | computed component evidence useful |
| 35 | overpass-software-platform | 98 | A | 126 | 12 | 6 | 5 | computed component evidence useful |
| 36 | patrick-mason-studio-portfolio | 66 | C | 6 | 1 | 3 | 3 | low sample coverage |
| 37 | pitch-interactive-data-studio | 87 | B+ | 44 | 7 | 4 | 3 | computed component evidence useful |
| 38 | pitch-presentation-workspace | 98 | A | 81 | 12 | 6 | 5 | computed component evidence useful |
| 39 | plausible-analytics-live-dashboard | 95 | A | 73 | 7 | 4 | 4 | computed component evidence useful |
| 40 | railway-developer-platform | 86 | B+ | 38 | 4 | 4 | 4 | computed component evidence useful |
| 41 | raycast-productivity | 79 | C+ | 24 | 4 | 3 | 3 | computed component evidence useful |
| 42 | reflect-notes-interface | 98 | A | 91 | 12 | 5 | 4 | computed component evidence useful |
| 43 | rekki-food-service-app | 95 | A | 42 | 11 | 6 | 5 | computed component evidence useful |
| 44 | render-cloud-platform | 98 | A | 73 | 12 | 5 | 4 | computed component evidence useful |
| 45 | retool-internal-tools | 98 | A | 117 | 4 | 5 | 4 | computed component evidence useful |
| 46 | rows-spreadsheet-dashboard | 97 | A | 60 | 12 | 5 | 4 | computed component evidence useful |
| 47 | snohetta-architecture-studio | 97 | A | 59 | 9 | 5 | 5 | computed component evidence useful |
| 48 | stripe-product-platform | 98 | A | 114 | 9 | 5 | 4 | computed component evidence useful |
| 49 | supabase-developer-platform | 95 | A | 63 | 2 | 5 | 5 | computed component evidence useful |
| 50 | teenage-engineering-hardware-brand | 98 | A | 62 | 12 | 5 | 5 | computed component evidence useful |
| 51 | the-pudding-data-stories | 98 | A | 70 | 11 | 6 | 5 | computed component evidence useful |
| 52 | tines-automation-platform | 98 | A | 126 | 9 | 6 | 5 | computed component evidence useful |
| 53 | tinybird-analytics-infrastructure | 97 | A | 98 | 6 | 4 | 3 | computed component evidence useful |
| 54 | typeform-product-forms-saas | 98 | A | 97 | 7 | 5 | 4 | computed component evidence useful |
| 55 | uncut-typography-resource | 77 | C+ | 16 | 5 | 5 | 4 | low sample coverage |
| 56 | usps-delivers-generational-report | 86 | B+ | 22 | 11 | 4 | 4 | computed component evidence useful |
| 57 | vercel-developer-platform | 98 | A | 131 | 2 | 6 | 5 | computed component evidence useful |
| 58 | viens-la-travel-hospitality | 98 | A | 87 | 9 | 5 | 4 | computed component evidence useful |
| 59 | visual-cinnamon-data-art | 96 | A | 55 | 12 | 5 | 4 | computed component evidence useful |
| 60 | visual-journal-editorial | 70 | C+ | 7 | 4 | 4 | 3 | low sample coverage |
| 61 | viviens-creative-talent | 66 | C | 21 | 0 | 2 | 2 | narrow component categories |
| 62 | wam-architecture-studio | 93 | A | 69 | 10 | 4 | 3 | computed component evidence useful |
| 63 | webinspoo-accessgrid-pricing-page | 98 | A | 99 | 12 | 6 | 5 | computed component evidence useful |
| 64 | webinspoo-airmee-landing-page | 98 | A | 97 | 12 | 6 | 5 | computed component evidence useful |
| 65 | webinspoo-bevel-landing-page | 98 | A | 99 | 12 | 6 | 5 | computed component evidence useful |
| 66 | webinspoo-braintrust-pricing-page | 98 | A | 103 | 12 | 6 | 5 | computed component evidence useful |
| 67 | webinspoo-browserbase-pricing-page | 98 | A | 103 | 12 | 6 | 5 | computed component evidence useful |
| 68 | webinspoo-cloudflare-pricing-pattern | 98 | A | 103 | 12 | 6 | 5 | computed component evidence useful |
| 69 | webinspoo-exa-ai-pricing-page | 98 | A | 103 | 12 | 6 | 5 | computed component evidence useful |
| 70 | webinspoo-expenseai-landing-page | 98 | A | 103 | 12 | 6 | 5 | computed component evidence useful |
| 71 | webinspoo-mistral-ai-landing-page | 98 | A | 103 | 12 | 6 | 5 | computed component evidence useful |
| 72 | webinspoo-poolside-ai-landing-page | 98 | A | 102 | 12 | 6 | 5 | computed component evidence useful |
| 73 | webinspoo-rerun-developer-landing-page | 98 | A | 99 | 12 | 6 | 5 | computed component evidence useful |
| 74 | webinspoo-unkey-pricing-page | 98 | A | 98 | 12 | 6 | 5 | computed component evidence useful |
| 75 | webinspoo-weav-saas-landing-page | 98 | A | 103 | 12 | 6 | 5 | computed component evidence useful |
| 76 | wiz-cybersecurity-saas | 98 | A | 125 | 1 | 6 | 5 | computed component evidence useful |

## Lowest-Scoring Active References

- `patrick-mason-studio-portfolio`: 66/100 — low sample coverage (samples=6, categories=3).
- `viviens-creative-talent`: 66/100 — narrow component categories (samples=21, categories=2).
- `visual-journal-editorial`: 70/100 — low sample coverage (samples=7, categories=4).
- `cron-calendar-interface`: 72/100 — low sample coverage (samples=18, categories=3).
- `bauhaus-clock-interactive-product`: 77/100 — computed component evidence useful (samples=32, categories=3).
- `uncut-typography-resource`: 77/100 — low sample coverage (samples=16, categories=5).
- `middle-name-agency-studio`: 78/100 — low sample coverage (samples=18, categories=5).
- `raycast-productivity`: 79/100 — computed component evidence useful (samples=24, categories=3).
- `counter-forms-typography-resource`: 83/100 — computed component evidence useful (samples=39, categories=4).
- `benvenusa-food-wine`: 85/100 — computed component evidence useful (samples=51, categories=4).

## Verdict

The active library is now strong as a code-informed reference system rather than only an aesthetic palette library. It is useful for borrowing component density, radii, borders, shadows, typography, spacing, transitions, and hover/focus behavior. The remaining gap is sparse component exposure on a few references and the need for replacement clean evidence for the excluded blocked Arc reference.
