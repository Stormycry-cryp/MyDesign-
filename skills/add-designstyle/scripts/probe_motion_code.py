from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent
REVIEWS = ROOT / "reviews"
OUT = REVIEWS / "motion-code-probe.json"

MOTION_PATTERNS = {
    "keyframes": re.compile(r"@keyframes\s+[-_\w]+", re.I),
    "transition": re.compile(r"transition(?:-[a-z-]+)?\s*:[^;}{]+", re.I),
    "animation": re.compile(r"animation(?:-[a-z-]+)?\s*:[^;}{]+", re.I),
    "duration": re.compile(r"(?:transition|animation)-duration\s*:[^;}{]+|\b\d+(?:\.\d+)?m?s\b", re.I),
    "easing": re.compile(r"(?:transition|animation)-timing-function\s*:[^;}{]+|cubic-bezier\([^)]+\)|\b(?:ease-in-out|ease-in|ease-out|linear|ease)\b", re.I),
    "transform": re.compile(r"transform\s*:[^;}{]+|\.style\.transform\s*=", re.I),
    "transform_function": re.compile(r"(?:translate3d|translateX|translateY|scale3d|scale|rotate|rotate3d|skew|matrix3d?)\([^)]+\)", re.I),
    "scroll_snap": re.compile(r"scroll-snap-[a-z-]+\s*:[^;}{]+", re.I),
    "reduced_motion": re.compile(r"prefers-reduced-motion", re.I),
    "swiper": re.compile(r"\bswiper\b|swiper-wrapper|new\s+Swiper", re.I),
    "gsap": re.compile(r"\bgsap\b|ScrollTrigger", re.I),
    "framer": re.compile(r"framer-motion|motionValue|AnimatePresence", re.I),
    "intersection": re.compile(r"IntersectionObserver", re.I),
    "request_animation_frame": re.compile(r"requestAnimationFrame", re.I),
    "video": re.compile(r"\bHTMLVideoElement\b|\.play\(\)|\.pause\(\)|<video", re.I),
}

NOISY_HOST_HINTS = [
    "googletagmanager",
    "google-analytics",
    "facebook",
    "pinterest",
    "reddit",
    "bing",
    "doubleclick",
    "yotpo",
    "okendo",
    "gorgias",
    "hotjar",
    "klaviyo",
    "attentive",
]


def load_evidence() -> list[dict]:
    rows: list[dict] = []
    for name in ["beauty-cold-start-evidence.json", "beauty-replacement-evidence.json"]:
        rows.extend(json.loads((REVIEWS / name).read_text(encoding="utf-8")))
    return rows


def is_noisy(url: str) -> bool:
    low = url.lower()
    return any(hint in low for hint in NOISY_HOST_HINTS)


def choose_urls(item: dict) -> list[str]:
    css = [url for url in item.get("cssHrefs") or [] if url and not is_noisy(url)]
    scripts = [url for url in item.get("scripts") or [] if url and not is_noisy(url)]
    videos = [url for url in item.get("videoSources") or [] if url]
    return css[:8] + scripts[:8] + videos[:4]


def fetch(url: str) -> tuple[str, str | None]:
    request = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 designstyle-motion-probe/1.0",
            "Accept": "text/css,application/javascript,text/javascript,text/plain,*/*;q=0.1",
        },
    )
    try:
        with urlopen(request, timeout=12) as response:
            content_type = response.headers.get("content-type", "")
            data = response.read(350_000)
    except (OSError, URLError) as exc:
        return "", f"{type(exc).__name__}: {exc}"
    if "video/" in content_type:
        return f"[binary video asset: {content_type}]", None
    return data.decode("utf-8", errors="ignore"), None


def snippets(text: str) -> dict[str, list[str]]:
    found: dict[str, list[str]] = {}
    compact = re.sub(r"\s+", " ", text)
    for name, pattern in MOTION_PATTERNS.items():
        matches = []
        for match in pattern.finditer(compact):
            start = max(0, match.start() - 90)
            end = min(len(compact), match.end() + 140)
            matches.append(compact[start:end].strip())
            if len(matches) >= 5:
                break
        if matches:
            found[name] = matches
    return found


def main() -> int:
    rows = load_evidence()
    selected = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    results: dict[str, dict] = {}
    for item in rows:
        name = item.get("name")
        if selected and name not in selected:
            continue
        urls = choose_urls(item)
        resources = []
        aggregate: dict[str, list[str]] = {}
        for url in urls:
            text, error = fetch(url)
            resource = {
                "url": url,
                "error": error,
                "bytes_sampled": len(text),
                "matches": snippets(text) if text and not error else {},
            }
            for key, values in resource["matches"].items():
                aggregate.setdefault(key, [])
                for value in values:
                    if len(aggregate[key]) < 8:
                        aggregate[key].append(value)
            resources.append(resource)
        results[name] = {
            "source_url": item.get("finalUrl") or item.get("url"),
            "resources_checked": len(resources),
            "urls_checked": urls,
            "motion_evidence": aggregate,
            "resources": resources,
        }
        print(f"{name}: checked {len(resources)} resources; evidence keys: {', '.join(aggregate) or 'none'}")
    OUT.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
