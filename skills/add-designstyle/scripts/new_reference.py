#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


LIB = Path.home() / ".codex" / "designstyle-library"


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"https?://", "", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text[:80] or "style-reference"


def yaml_list(values: list[str]) -> str:
    return "[" + ", ".join('"' + v.replace('"', '\\"') + '"' for v in values) + "]"


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a high-fidelity designstyle reference template.")
    parser.add_argument("name")
    parser.add_argument("--url", default="")
    parser.add_argument("--tags", default="")
    parser.add_argument("--category-tags", default="")
    parser.add_argument("--style-tags", default="")
    parser.add_argument("--structure-tags", default="")
    parser.add_argument("--motion-tags", default="")
    parser.add_argument("--code-tags", default="")
    parser.add_argument("--best-for", default="")
    parser.add_argument("--avoid-for", default="")
    parser.add_argument("--community-signal", default="")
    parser.add_argument("--page-scope", default="")
    parser.add_argument("--library", default=str(LIB))
    args = parser.parse_args()

    lib = Path(args.library).expanduser()
    for folder in ["references", "screenshots", "assets", "reviews", "indexes"]:
        (lib / folder).mkdir(parents=True, exist_ok=True)

    slug = slugify(args.name)
    today = date.today().isoformat()
    path = lib / "references" / f"{today}-{slug}.md"
    if path.exists():
        raise SystemExit(f"Already exists: {path}")

    tags = [tag.strip() for tag in args.tags.split(",") if tag.strip()]
    category_tags = [tag.strip() for tag in args.category_tags.split(",") if tag.strip()]
    style_tags = [tag.strip() for tag in args.style_tags.split(",") if tag.strip()] or tags
    structure_tags = [tag.strip() for tag in args.structure_tags.split(",") if tag.strip()]
    motion_tags = [tag.strip() for tag in args.motion_tags.split(",") if tag.strip()]
    code_tags = [tag.strip() for tag in args.code_tags.split(",") if tag.strip()]
    best = [item.strip() for item in args.best_for.split(",") if item.strip()]
    avoid = [item.strip() for item in args.avoid_for.split(",") if item.strip()]
    community_signal = args.community_signal.replace('"', '\\"')
    page_scope = args.page_scope.replace('"', '\\"')

    content = f'''---
title: "{args.name}"
source_url: "{args.url}"
captured_at: "{today}"
tags: {yaml_list(tags)}
category_tags: {yaml_list(category_tags)}
style_tags: {yaml_list(style_tags)}
structure_tags: {yaml_list(structure_tags)}
motion_tags: {yaml_list(motion_tags)}
code_tags: {yaml_list(code_tags)}
best_for: {yaml_list(best)}
avoid_for: {yaml_list(avoid)}
community_signal: "{community_signal}"
page_scope: "{page_scope}"
evidence_screenshot: "screenshots/{slug}-desktop.png"
evidence_quality: "TODO: visual screenshot plus DOM/style/resource extraction"
---

# Style Reference: {args.name}

## Essence
TODO: one to three sentences naming the transferable design idea, not vague praise.

## When To Use
- TODO

## When Not To Use
- TODO

## Evidence Snapshot
- Captured URL: TODO
- Page title: TODO
- Screenshot: screenshots/{slug}-desktop.png
- Viewport: TODO
- Community signal: TODO
- Page scope: TODO
- Secondary pages inspected: TODO
- H1 observed: TODO
- H2 samples: TODO
- Navigation samples: TODO
- Images observed: TODO
- Video observed: TODO
- Overlays or fixed elements: TODO

## Visual System
- Layout: TODO
- Typography: TODO
- Color: TODO
- Density: TODO
- Shape: TODO
- Shadow/depth: TODO

## Typography And Reading Rhythm
- Observed font stack counts: TODO
- Observed font sizes: TODO
- Observed weights: TODO
- Observed letter spacing: TODO
- Preserve role relationships: TODO

## Color, Material, And Contrast
- Observed text colors: TODO
- Observed backgrounds: TODO
- UI shell colors vs asset-driven colors: TODO

## Layout Geometry And Spacing
- First viewport structure: TODO
- Macro geometry: TODO
- Media/card aspect stability: TODO
- Observed border radii: TODO

## Dimension And Ratio System
- Viewport and document: TODO
- Observed media ratios: TODO
- Observed spacing samples: TODO
- Preserve ratios as implementation constraints: TODO
- Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.

## Assets
- Image style: TODO
- Illustration/icon style: TODO
- Texture/pattern: TODO
- Likely sources or production method: TODO

## Code Surface
- Framework/runtime hints: TODO
- Public stylesheet/script URLs: TODO
- CSS variables/tokens observed: TODO
- Layout primitives observed: TODO
- Component or class naming clues: TODO
- Asset CDN and media loading patterns: TODO

## Motion
- Page transitions: TODO
- Micro-interactions: TODO
- Scroll/entrance behavior: TODO
- Timing/easing: TODO

## Motion Code And Runtime Evidence
- Motion source: TODO
- CSS animation/transition evidence: TODO
- Public CSS/JS probe keywords: TODO
- Public CSS/JS motion snippets: TODO
- Exact motion parameters: TODO
- JavaScript/runtime motion evidence: TODO
- Stylesheet evidence: TODO
- Interpreted motion tags: TODO
- Use this as implementation guidance only where evidence is direct. If CSS/JS is minified or only CDN names are visible, mark library/framework attribution as weak.

## Interaction And Components
- Navigation: TODO
- Buttons/links: TODO
- Cards/sections: TODO
- Forms/inputs: TODO
- Feedback states: TODO

## Implementation Notes
- CSS/layout primitives: TODO
- Token ideas: TODO
- Libraries or techniques: TODO
- Performance/accessibility concerns: TODO

## Borrow
- TODO

## Avoid Copying
- TODO

## Evidence Limits
- TODO: contamination, inaccessible areas, source limits, proprietary boundaries.

## Self Review
- Evidence quality: TODO
- Reuse value: TODO
- Missing pieces: TODO
- Revision made: TODO
'''
    path.write_text(content, encoding="utf-8")
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
