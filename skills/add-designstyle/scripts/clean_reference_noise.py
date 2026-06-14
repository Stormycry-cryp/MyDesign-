#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path
import os


LIB = Path(os.environ.get("DESIGNSTYLE_LIBRARY", str(Path.home() / ".codex" / "designstyle-library")))
SCIENTIFIC_PX = re.compile(r"\b\d+(?:\.\d+)?e[+-]?\d+px\b", re.I)
AUTOFILL_CONSENT_NOISE = re.compile(
    r"autofill|consent|cookie|onetrust|ot-sdk|hs-banner|hs-modal|recaptcha|captcha",
    re.I,
)
POSTHOG_KEY_PREFIX = "ph" + "c_"
REPLAY_KEY_PARAM = "replay" + "ApiKey"
ANALYTICS_KEY_NOISE = re.compile(r"\b" + POSTHOG_KEY_PREFIX + r"[A-Za-z0-9]+|\b" + REPLAY_KEY_PARAM + r"=[^&\"'\s]+", re.I)
TRUNCATED_CSS_DECLARATION = re.compile(
    r"(?:transition|animation|transform|@keyframes)\s*(?::\s*)?(?:$|\n|[^;{}\n]{0,160}$)",
    re.I,
)
CSS_EVIDENCE_LABEL = re.compile(
    r"Public CSS/JS motion snippets|CSS animation/transition evidence|JavaScript/runtime motion evidence|Page transitions|Scroll/entrance behavior|Timing/easing",
    re.I,
)
LONG_CODE_FRAGMENT = re.compile(r"[{}]|;[^\n]{0,80}(?:transition|animation|transform|requestAnimationFrame|IntersectionObserver)", re.I)


def clean_scientific_px_lists(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        if SCIENTIFIC_PX.search(line):
            parts = [part.strip() for part in line.split(";")]
            kept = [part for part in parts if not SCIENTIFIC_PX.search(part)]
            line = "; ".join(kept) if kept else re.sub(SCIENTIFIC_PX, "filtered abnormal computed value", line)
        lines.append(line)
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def clean_motion_noise_lines(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        if AUTOFILL_CONSENT_NOISE.search(line):
            continue
        stripped = line.strip()
        if CSS_EVIDENCE_LABEL.search(stripped) and len(stripped) > 360 and LONG_CODE_FRAGMENT.search(stripped):
            label = stripped.split(":", 1)[0]
            lines.append(f"{label}: missing evidence; removed truncated CSS/JS fragment. Use structured motion evidence instead.")
            continue
        looks_like_css_evidence = "{" in stripped or "}" in stripped or CSS_EVIDENCE_LABEL.search(stripped)
        if looks_like_css_evidence:
            tail = stripped[-180:]
            if TRUNCATED_CSS_DECLARATION.search(tail) and not re.search(r"[;}]\s*$", tail):
                continue
        lines.append(line)
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def noise_reasons(text: str) -> list[str]:
    reasons: list[str] = []
    if SCIENTIFIC_PX.search(text):
        reasons.append("scientific-notation px")
    if AUTOFILL_CONSENT_NOISE.search(text):
        reasons.append("autofill/consent noise")
    if ANALYTICS_KEY_NOISE.search(text):
        reasons.append("third-party analytics/replay key")
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("|") or stripped.startswith("#"):
            continue
        looks_like_css_evidence = "{" in stripped or "}" in stripped or CSS_EVIDENCE_LABEL.search(stripped)
        if not looks_like_css_evidence:
            continue
        if CSS_EVIDENCE_LABEL.search(stripped) and len(stripped) > 360 and LONG_CODE_FRAGMENT.search(stripped):
            reasons.append("truncated css declaration")
            break
        tail = stripped[-180:]
        if TRUNCATED_CSS_DECLARATION.search(tail) and not re.search(r"[;}]\s*$", tail):
            reasons.append("truncated css declaration")
            break
    return reasons


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
    remaining: list[tuple[Path, list[str]]] = []
    for path in iter_active_text_files(lib):
        text = path.read_text(encoding="utf-8", errors="ignore")
        reasons = noise_reasons(text)
        if not reasons:
            continue
        if args.check:
            remaining.append((path, reasons))
            continue
        cleaned = clean_motion_noise_lines(clean_scientific_px_lists(text))
        path.write_text(cleaned, encoding="utf-8")
        changed.append(path)

    if args.check:
        for path, reasons in remaining:
            print(f"{path}: {', '.join(reasons)}")
        return 1 if remaining else 0

    print(f"cleaned={len(changed)}")
    for path in changed:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
