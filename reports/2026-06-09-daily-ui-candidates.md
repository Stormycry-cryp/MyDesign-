Routing: add-designstyle
Reason: daily DesignStyle candidate discovery for a coherent theme; stop after preflight and ask for confirmation before any ingestion.
Evidence layers read: L0 router; prior daily candidate reports; L4 live aesthetic probe screenshots
Missing evidence, if any: none for preflight; no active references were written

# Daily UI Candidates - 2026-06-09

## Theme

Design-led consumer audio and hardware product homepages

This stays different from the recent hospitality, watch/jewelry, and architecture/interior-studio batches while keeping one coherent official-brand theme.

## Preflight status

- Started with two rejected theme explorations before landing the final set:
  - High-end fragrance/beauty brand sites: too many Cloudflare, region-switch, or ecommerce-heavy first viewports.
  - Contemporary furniture/home brands: too many cookie-dominated or catalog-heavy first viewports.
- Used the local `probe_aesthetic_fit.py` preflight on official brand/product sites only.
- Manually reviewed the generated screenshots and removed candidates with region-picker contamination, Cloudflare/security pages, large cookie layers, or visually weak first viewports.
- Kept one borderline candidate below `75` only because the screenshot was still clean and theme-fit after manual QA.
- Did not run full `add-designstyle`.
- Did not write any active references, cards, dimensions, or design-system artifacts.

## Contact sheet

- Contact sheet: [2026-06-09-daily-ui-candidates-contact-sheet.png](/Users/chenyunzhe/Documents/Codex/2026-06-04/files-mentioned-by-the-user-designstyle/work/DesignStyle/reports/2026-06-09-daily-ui-candidates-contact-sheet.png)

## Candidate table

| Name | URL | Theme | Score | Notes |
| --- | --- | --- | ---: | --- |
| ROLI | https://roli.com/ | Design-led consumer audio and hardware product homepages | 90 | Strong product-learning hero, soft neutral surface, clean capture after overlay dismissal. |
| Devialet | https://www.devialet.com/ | Design-led consumer audio and hardware product homepages | 78 | Minimal premium audio framing, sparse navigation, stable first viewport. |
| Marshall | https://www.marshall.com/ | Design-led consumer audio and hardware product homepages | 78 | Bold campaign-led hardware hero, crisp black system, clean first-screen hierarchy. |
| Analogue | https://www.analogue.co/ | Design-led consumer audio and hardware product homepages | 78 | Distinctive product-stage composition, strong dark merchandising shell, stable capture. |
| Sonos | https://www.sonos.com/ | Design-led consumer audio and hardware product homepages | 71 | Slightly below cutoff, but screenshot QA was clean and the whole-home hardware hero stayed visually strong. |

## Rejected and replacements

| Candidate | Status | Rejection note |
| --- | --- | --- |
| Aesop | Rejected theme attempt | Probe scored `78`, but screenshot/title showed a Cloudflare verification page; false-positive probe result, excluded. |
| Byredo | Rejected theme attempt | `blocked`; ecommerce shell plus unusable probe output for the theme attempt. |
| Le Labo | Rejected theme attempt | `busy_navigation`, `cluttered_first_viewport`; too commerce-heavy for a clean confirmation batch. |
| Diptyque Paris | Rejected theme attempt | Visually strong, but the fragrance theme as a whole did not yield 5 clean official-site candidates. |
| D.S. & Durga | Rejected theme attempt | Visually acceptable, but fragrance-theme coverage was too thin overall. |
| Nothing | Rejected after screenshot QA | Probe score passed, but the actual screenshot was dominated by a region-switch panel. |
| Rabbit | Rejected after screenshot QA | Distinctive, but a bottom cookie layer visibly contaminated the screenshot. |
| Light Phone | Rejected after screenshot QA | Too pale/near-blank in the captured viewport; insufficient first-screen evidence. |
| Transparent | Rejected | Score `63`; sparse catalog grid with weak first-screen impact. |
| Naim Audio | Rejected | Cookie modal remained centered in the hero. |
| Master & Dynamic | Rejected | Score `70`; cleaner than many, but still too commerce-heavy and busier than the final five. |
| Teenage Engineering | Rejected | `busy_navigation`, `cluttered_first_viewport`; not clean enough for the target batch. |
| Bang & Olufsen | Rejected | `overlay_dominated`; cookie layer still too large after dismissal attempts. |
| KEF | Rejected | `visually_ordinary`; first viewport read too generic. |
| Bowers & Wilkins | Rejected | `overlay_dominated`; cookie contamination. |
| Playdate | Rejected | `visually_ordinary`; playful but not visually strong enough for this batch. |
| HAY | Rejected theme attempt | `blocked`; no usable screenshot in furniture-theme attempt. |
| Muuto | Rejected theme attempt | Strong single-site result, but furniture-theme coverage was too weak overall. |
| Audo Copenhagen | Rejected theme attempt | `busy_navigation`, `cluttered_first_viewport`; furniture-theme coverage stayed too noisy. |

## Confirmation

User-selected keepers from this batch:

1. Analogue
2. Sonos

Dropped after review:

1. ROLI
2. Devialet
3. Marshall

This report is still preflight-only. If you want a 5-site ingestion batch later, 3 replacement candidates still need to be found under the same or a new theme.
