---
name: designstyle
description: Use when a user asks for designstyle, /designstyle, style-reference library work, or is ambiguous between adding a visual reference and using existing references for a design.
---

# Designstyle

Route designstyle work to the right local skill. This skill is a thin coordinator for:

- `add-designstyle`: capture a website, app screen, image, or URL into the local designstyle reference library.
- `use-designstyle`: apply existing local references to a new page, app screen, prototype, visual system, or frontend UI.

Do not duplicate the child skills. After routing, open the selected child `SKILL.md` and follow it.

## Evidence Layers

Report which progressive-disclosure layer the task used:

- L0 Router: this `designstyle` skill chooses `add-designstyle`, `use-designstyle`, or `add-designstyle -> use-designstyle`.
- L1 Cards: `indexes/cards/*.json` for fast candidate ranking.
- L2 Dimensions: `dimensions/<slug>/*.md` for selective scene/layout/type/color/assets/motion/component evidence.
- L3 Full Reference: `references/*.md` for complete evidence.
- L4 On-Demand Evidence: retained screenshots and component-style JSON, plus fresh source-URL recapture when L0-L3 evidence is insufficient. Raw DOM snapshots are not stored in the default library.

If L1/L2 files are missing, route through `add-designstyle` generation/validation or say that only L3/L4 evidence is available.

## Shared Contract

After routing, the selected child skill must report:

- Routing:
- Reason:
- Evidence layers read or generated:
- Scene/page fit:
- Required dimensions:
- Missing evidence:
- Reuse boundary:
- Next handoff:

For complete visual-system tasks, these Required dimensions are mandatory:

- Reference text grammar.
- Style tokens.
- Spacing rhythm.

If any mandatory dimension is missing, say it explicitly. Do not infer it from adjacent evidence or broad style words.

## Handoff Rules

`add-designstyle -> use-designstyle`:

- Report the new reference's best future use.
- Report dimensions with strong evidence.
- Report dimensions with weak or missing evidence.
- Report suggested Use roles.

`use-designstyle -> add-designstyle`:

- If coverage is partial or weak, produce an Add-Designstyle Backlog.
- The backlog must name missing scene, missing page scope, missing dimensions, needed evidence level, and suggested reference type.

## Route

Use `add-designstyle` when the user:

- Provides a URL, screenshot, product page, app screen, visual reference, gallery item, or example site.
- Says add, save, record, extract, analyze, 拆解, 入库, 收录, 学这个, or build a reusable style reference.
- Wants code/design/aesthetic evidence captured for later reuse.

Use `use-designstyle` when the user:

- Wants to design, redesign, build, prototype, or polish a webpage, landing page, app screen, frontend UI, or visual system.
- Asks to use, reference, draw from, apply, 套用, 借鉴, or select from the local designstyle library.
- Gives a product/theme and asks for visual directions, reference matrices, or implementation guidance.

Use both, in order, when the user:

- Provides new references and asks to design from them.
- Says to learn/add a style and then apply it.
- The local library lacks a needed scene-fit reference but the user supplies one.

For mixed tasks: run `add-designstyle` first, validate the reference entry, then run `use-designstyle` against the updated library.

## Required Dimension Check

Whichever route is selected, preserve or request these dimensions when the task involves a complete visual system:

- Reference text grammar: H1/H2/eyebrow/CTA/body/meta samples, sentence rhythm, claim density, naming style, and copy boundaries.
- Style tokens: background/surface layers, borders, radii, shadows, button/input/control density, icon/stroke style, hover/focus states.
- Spacing rhythm: header height, hero padding, section gaps, grid gutters, card padding, text measure, CTA spacing, media margins, and mobile compression.

If these dimensions are missing from the reference evidence, say so instead of pretending the library supports them.

## Output

Start with a short routing statement:

```markdown
Routing: add-designstyle | use-designstyle | add-designstyle -> use-designstyle
Reason: <one sentence>
Evidence layers read: L0 router; <L1/L2/L3/L4 as applicable>
Missing evidence, if any: <one sentence or "none">
```

Then continue with the selected child skill workflow.

## Do Not Do

- Do not force a use workflow when the user is asking to add or analyze a reference.
- Do not force an add workflow when the user is asking to design from existing references.
- Do not treat generic style words as enough evidence; check scene/page fit first.
- Do not claim reference text, style token, or spacing evidence exists unless it was captured or provided.
