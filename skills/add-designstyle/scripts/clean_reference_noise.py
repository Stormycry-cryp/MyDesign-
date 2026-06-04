#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


LIB = Path.home() / ".codex" / "designstyle-library"
SCIENTIFIC_PX = re.compile(r"\b\d+(?:\.\d+)?e[+-]?\d+px\b", re.I)


def clean_scientific_px_lists(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        if SCIENTIFIC_PX.search(line):
            parts = [part.strip() for part in line.split(";")]
            kept = [part for part in parts if not SCIENTIFIC_PX.search(part)]
            line = "; ".join(kept) if kept else re.sub(SCIENTIFIC_PX, "filtered abnormal computed value", line)
        lines.append(line)
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def iter_active_text_files(lib: Path) -> list[Path]:
    roots = [
        lib / "references",
        lib / "dimensions",
        lib / "design-systems",
        lib / "indexes",
    ]
    files: list[Path] = []
    for root in roots:
        if root.exists():
            files.extend(path for path in root.rglob("*") if path.is_file() and path.suffix in {".md", ".json", ".svg"})
    return sorted(files)


def main() -> int:
    parser = argparse.ArgumentParser(description="Remove abnormal scientific-notation px values from active reference text artifacts.")
    parser.add_argument("--library", default=str(LIB))
    parser.add_argument("--check", action="store_true", help="Fail if active text artifacts still contain scientific-notation px values.")
    args = parser.parse_args()

    lib = Path(args.library).expanduser()
    changed: list[Path] = []
    remaining: list[Path] = []
    for path in iter_active_text_files(lib):
        text = path.read_text(encoding="utf-8", errors="ignore")
        if not SCIENTIFIC_PX.search(text):
            continue
        if args.check:
            remaining.append(path)
            continue
        cleaned = clean_scientific_px_lists(text)
        path.write_text(cleaned, encoding="utf-8")
        changed.append(path)

    if args.check:
        for path in remaining:
            print(path)
        return 1 if remaining else 0

    print(f"cleaned={len(changed)}")
    for path in changed:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
