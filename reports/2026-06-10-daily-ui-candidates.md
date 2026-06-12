Routing: add-designstyle
Reason: daily DesignStyle candidate discovery for a coherent theme; stop after preflight and ask for confirmation before any ingestion.
Evidence layers read: L0 router; prior daily candidate reports; web/source URL verification
Missing evidence, if any: browser screenshot preflight and contact sheet are blocked in this environment; no active references were written

# Daily UI Candidates - 2026-06-10

## Theme

Independent film distribution and cinema-culture brand sites

This stays different from the recent watch/jewelry, architecture/interior, and consumer hardware batches while keeping one coherent official-brand/editorial theme.

## What happened

- I selected a new coherent theme and narrowed it to official film-distribution / cinema-culture brands with distinctive editorial-first homepages.
- I attempted the local `add-designstyle` aesthetic preflight workflow first.
- The official `probe_aesthetic_fit.py` workflow was available, but browser launch failed before page capture on every candidate in this environment.
- Because that browser failure happens before page render, I could not honestly produce screenshot-based preflight scores or a real screenshot contact sheet.
- I did not run full `add-designstyle`.
- I did not write any active references, cards, dimensions, or design-system artifacts.

## Preflight blocker

- Blocking tool step: `python3 /Users/chenyunzhe/.codex/skills/add-designstyle/scripts/probe_aesthetic_fit.py ...`
- Failure mode: Playwright browser launch aborts immediately with macOS sandbox errors such as `bootstrap_check_in ... Permission denied (1100)` and `TargetClosedError`.
- Impact: captureability is unverified for this run, and no screenshot contact sheet could be created without inventing evidence.

## Provisional candidate table

These are strong same-theme candidates, but they are still **provisional** until screenshot preflight can run cleanly.

| Name | URL | Theme | Score | Notes |
| --- | --- | --- | ---: | --- |
| A24 | https://a24films.com/ | Independent film distribution and cinema-culture brand sites | n/a | Official film studio/distributor with a strong editorial-commerce hybrid shell; preflight blocked before capture. |
| MUBI | https://mubi.com/ | Independent film distribution and cinema-culture brand sites | n/a | Official streaming/cinema brand with recognizable editorial-first visual language; preflight blocked before capture. |
| The Criterion Collection | https://www.criterion.com/ | Independent film distribution and cinema-culture brand sites | n/a | Official cinema catalog/publishing brand; usually strong graphic-system candidate, but this run could not verify screenshot cleanliness. |
| NEON | https://neonrated.com/ | Independent film distribution and cinema-culture brand sites | n/a | Official film distributor site with campaign-led visual direction; preflight blocked before capture. |
| Janus Films | https://www.janusfilms.com/ | Independent film distribution and cinema-culture brand sites | n/a | Official classic-film distributor with restrained editorial shell; preflight blocked before capture. |

## Rejected and replacements

| Candidate | Status | Rejection note |
| --- | --- | --- |
| NOWNESS | Rejected from final five | Strong visual quality, but it reads more like broad culture editorial than film-distribution / cinema-brand UI. |
| Bleecker Street | Replacement not kept | Theme-fit is acceptable, but weaker visual distinctiveness than the final five. |
| Annapurna Pictures | Replacement not kept | Theme-fit is acceptable, but brand/site consistency is less dependable for the 2026-06-10 batch. |

## Confirmation

If you want to keep this theme direction, confirm these 5 provisional candidates first:

1. A24
2. MUBI
3. The Criterion Collection
4. NEON
5. Janus Films

Before any add-designstyle ingestion, the browser preflight blocker still needs to be resolved so I can generate a real screenshot contact sheet and actual preflight evidence.
