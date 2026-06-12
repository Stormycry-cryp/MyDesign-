Routing: add-designstyle
Reason: daily DesignStyle candidate discovery for a coherent theme; stop after preflight and ask for confirmation before any ingestion.
Evidence layers read: L0 router; prior daily candidate reports; live aesthetic probe screenshots
Missing evidence, if any: none for preflight; no active references were written

# Daily UI Candidates - 2026-06-08

## Theme

Contemporary architecture and interior design studios

This stays different from the recent hospitality and watch/jewelry batches while keeping one coherent official-site theme.

## Preflight status

- Used the local `probe_aesthetic_fit.py` preflight on official studio/practice sites only.
- Rejected blocked, timeout-heavy, Cloudflare, overlay-dominated, or generic-looking first viewports.
- Kept two borderline candidates only because their screenshots were stable and clean even though the numeric score stayed slightly below `75`.
- Did not run full `add-designstyle`.
- Did not write any active references, cards, dimensions, or design-system artifacts.

## Contact sheet

- Contact sheet: [2026-06-08-daily-ui-candidates-contact-sheet.png](/Users/chenyunzhe/Documents/Codex/2026-06-04/files-mentioned-by-the-user-designstyle/work/DesignStyle/reports/2026-06-08-daily-ui-candidates-contact-sheet.png)

## Candidate table

| Name | URL | Theme | Score | Notes |
| --- | --- | --- | ---: | --- |
| AvroKO | https://www.avroko.com/ | Contemporary architecture and interior design studios | 84 | Clean interior-design hero, strong type contrast, stable capture. |
| Roman and Williams | https://www.romanandwilliams.com/ | Contemporary architecture and interior design studios | 82 | Distinctive editorial-commerce studio mix, rich material imagery, clean first viewport after cookie dismissal. |
| Seymourpowell | https://www.seymourpowell.com/ | Contemporary architecture and interior design studios | 78 | Strong strategic-design agency framing, clear headline, stable screenshot. |
| Adjaye Associates | https://www.adjaye.com/ | Contemporary architecture and interior design studios | 70 | Borderline score, but screenshot QA was clean and project-led rather than overlay-led. |
| OMA | https://oma.com/ | Contemporary architecture and interior design studios | 70 | Borderline score, but the homepage capture is visually distinctive and stable enough for confirmation review. |

## Rejected and replacements

| Candidate | Status | Rejection note |
| --- | --- | --- |
| BIG | Rejected | `TimeoutError`; homepage never reached a usable `domcontentloaded` state in probe. |
| David Chipperfield Architects | Rejected | `TimeoutError`; not reliable enough for a captureable batch. |
| Heatherwick Studio | Rejected | `TimeoutError`; no dependable screenshot. |
| Olson Kundig | Rejected | `TimeoutError`; failed the captureability requirement. |
| Norm Architects | Rejected | `TimeoutError`; unstable for probe capture. |
| Studio Gang | Rejected | `TimeoutError`; no usable first-viewport evidence. |
| Yabu Pushelberg | Rejected | `capture failed`; blocked/timeout-like behavior. |
| Studioilse | Rejected | `capture failed`; no usable screenshot. |
| Kelly Wearstler | Rejected | `capture failed`; unstable official-site probe result. |
| Vincent Van Duysen | Rejected | `capture failed`; not dependable enough for the 2026-06-08 batch. |
| Rockwell Group | Rejected | `generic_template`; first viewport looked too ordinary after overlay dismissal. |
| Rottet Studio | Rejected | `overlay_dominated`; large consent/promo layer contaminated the viewport. |
| Neri&Hu | Rejected | `generic_template`; sparse first screen with weak visible UI evidence. |
| Kengo Kuma & Associates | Rejected | Score 63; image-rich but the first viewport read too repetitive and text-heavy. |
| Snøhetta | Rejected | `cluttered_first_viewport`; too much copy and module density for a clean contact-sheet candidate. |
| Design Hotels | Rejected | Score 69; good brand, but reads more like hospitality search/discovery than studio/practice UI. |
| Aman Essentials | Rejected | `visually_ordinary`; first viewport lacked enough structure for the target bar. |
| Sagrada | Rejected | Cloudflare challenge page (`Attention Required!`), excluded. |
| A Practice for Everyday Life | Rejected | `ERR_CONNECTION_CLOSED`; unusable for probe capture. |
| Meyer Davis | Rejected | `TimeoutError`; no stable screenshot. |

## Confirmation

If this set looks right, confirm these 5 exact candidates before any add-designstyle ingestion:

1. AvroKO
2. Roman and Williams
3. Seymourpowell
4. Adjaye Associates
5. OMA
