#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import urljoin, urlparse


LIB = Path.home() / ".codex" / "designstyle-library"
CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

MOTION_PATTERNS = {
    "transition": re.compile(r"transition(?:-[a-z-]+)?\s*:[^;}{]+", re.I),
    "animation": re.compile(r"animation(?:-[a-z-]+)?\s*:[^;}{]+", re.I),
    "keyframes": re.compile(r"@keyframes\s+[-_\w]+", re.I),
    "easing": re.compile(r"cubic-bezier\([^)]+\)|\b(?:ease-in-out|ease-in|ease-out|linear|ease)\b", re.I),
    "transform": re.compile(r"transform\s*:[^;}{]+|(?:translate3d|translateX|translateY|scale3d|scale|rotate|matrix3d?)\([^)]+\)", re.I),
    "reduced_motion": re.compile(r"prefers-reduced-motion", re.I),
    "intersection": re.compile(r"IntersectionObserver", re.I),
    "request_animation_frame": re.compile(r"requestAnimationFrame", re.I),
    "gsap": re.compile(r"\bgsap\b|ScrollTrigger", re.I),
    "framer": re.compile(r"framer-motion|AnimatePresence|motionValue", re.I),
    "swiper": re.compile(r"\bswiper\b|swiper-wrapper|new\s+Swiper", re.I),
}

BLOCKED_PATTERNS = [
    re.compile(r"attention required!\s*\|\s*cloudflare", re.I),
    re.compile(r"cloudflare ray id", re.I),
    re.compile(r"performance\s*&\s*security by cloudflare", re.I),
    re.compile(r"just a moment", re.I),
    re.compile(r"checking your browser", re.I),
    re.compile(r"verify you are human", re.I),
    re.compile(r"security challenge", re.I),
    re.compile(r"cf-chl|challenge-platform", re.I),
]
SCIENTIFIC_PX_RE = re.compile(r"\d+(?:\.\d+)?e[+-]?\d+px", re.I)

COMPONENT_STYLE_KEYS = [
    "display",
    "position",
    "top",
    "left",
    "right",
    "bottom",
    "zIndex",
    "color",
    "backgroundColor",
    "border",
    "borderTop",
    "borderRight",
    "borderBottom",
    "borderLeft",
    "borderRadius",
    "boxShadow",
    "fontFamily",
    "fontSize",
    "fontWeight",
    "letterSpacing",
    "lineHeight",
    "padding",
    "paddingTop",
    "paddingRight",
    "paddingBottom",
    "paddingLeft",
    "margin",
    "gap",
    "columnGap",
    "rowGap",
    "alignItems",
    "justifyContent",
    "transition",
    "transitionDuration",
    "transitionTimingFunction",
    "transform",
    "opacity",
    "cursor",
    "backdropFilter",
]

COMPONENT_CAPTURE_JS = """
() => {
  const styleKeys = %s;
  const cleanText = (value) => (value || '').replace(/\\s+/g, ' ').trim();
  const visible = (el) => {
    const rect = el.getBoundingClientRect();
    const style = getComputedStyle(el);
    return rect.width > 0 && rect.height > 0 && style.display !== 'none' && style.visibility !== 'hidden';
  };
  const styleOf = (el) => {
    const cs = getComputedStyle(el);
    const out = {};
    for (const key of styleKeys) out[key] = cs[key] || '';
    return out;
  };
  const rectOf = (el) => {
    const r = el.getBoundingClientRect();
    return {
      x: Math.round(r.x * 10) / 10,
      y: Math.round(r.y * 10) / 10,
      width: Math.round(r.width * 10) / 10,
      height: Math.round(r.height * 10) / 10,
      viewportVisible: r.bottom >= 0 && r.right >= 0 && r.top <= innerHeight && r.left <= innerWidth
    };
  };
  const classHint = (el) => cleanText(String(el.className || '')).split(' ').filter(Boolean).slice(0, 5).join(' ');
  const sample = (category, selector, limit) => Array.from(document.querySelectorAll(selector))
    .filter(visible)
    .slice(0, limit)
    .map((el, index) => {
      const id = `ds-${category.toLowerCase().replace(/[^a-z0-9]+/g, '-')}-${index}`;
      el.setAttribute('data-designstyle-sample-id', id);
      return {
        sampleId: id,
        category,
        tag: el.tagName.toLowerCase(),
        role: el.getAttribute('role') || '',
        ariaLabel: el.getAttribute('aria-label') || '',
        type: el.getAttribute('type') || '',
        classHint: classHint(el),
        text: cleanText(el.innerText || el.textContent || '').slice(0, 160),
        href: el.tagName.toLowerCase() === 'a' ? (el.href || '') : '',
        rect: rectOf(el),
        styles: styleOf(el)
      };
    });
  const samples = [
    ...sample('Navigation', 'header, nav, [role="navigation"], header a, nav a', 24),
    ...sample('Button', 'button, a[role="button"], input[type="button"], input[type="submit"], a[class*="button" i], a[class*="btn" i], [class*="button" i], [class*="btn" i]', 32),
    ...sample('Card', 'article, [class*="card" i], [class*="tile" i], [class*="item" i], li:has(a), section:has(img)', 28),
    ...sample('Form', 'form, label, input, textarea, select', 28),
    ...sample('Icon', 'svg, [class*="icon" i], img[width][height]', 28),
    ...sample('Section', 'main > section, body > section, section', 20)
  ];
  const byCategory = {};
  for (const item of samples) byCategory[item.category] = (byCategory[item.category] || 0) + 1;
  return {
    capturedAt: new Date().toISOString(),
    viewport: {w: innerWidth, h: innerHeight, docW: document.documentElement.scrollWidth, docH: document.documentElement.scrollHeight},
    styleKeys,
    counts: byCategory,
    samples
  };
}
""" % json.dumps(COMPONENT_STYLE_KEYS)


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"https?://", "", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text[:80] or "style-reference"


def yaml_list(values: list[str]) -> str:
    return "[" + ", ".join('"' + v.replace('"', '\\"') + '"' for v in values) + "]"


def q(value: str) -> str:
    return value.replace('"', '\\"').replace("\n", " ")


def blocked_evidence_reasons(payload: object) -> list[str]:
    text = json.dumps(payload, ensure_ascii=False).lower() if not isinstance(payload, str) else payload.lower()
    reasons = []
    for pattern in BLOCKED_PATTERNS:
        if pattern.search(text):
            reasons.append(pattern.pattern)
    return reasons


def sanitize_computed_value(value: object) -> object:
    if isinstance(value, str):
        if SCIENTIFIC_PX_RE.search(value):
            return "filtered abnormal computed value"
        return value
    if isinstance(value, list):
        return [sanitize_computed_value(item) for item in value]
    if isinstance(value, dict):
        return {key: sanitize_computed_value(item) for key, item in value.items()}
    return value


def dismiss_common_overlays(page) -> list[str]:
    clicked: list[str] = []
    labels = [
        "Accept all cookies",
        "Accept All Cookies",
        "Accept",
        "I agree",
        "Agree",
        "Allow all",
        "Got it",
        "Continue",
        "Reject all",
        "Necessary only",
    ]
    def click_first_visible(locator, label: str) -> bool:
        try:
            count = min(locator.count(), 6)
            for index in range(count):
                candidate = locator.nth(index)
                if candidate.is_visible():
                    candidate.click(timeout=1500)
                    clicked.append(label)
                    page.wait_for_timeout(500)
                    return True
        except Exception:
            return False
        return False

    for label in labels:
        if click_first_visible(page.get_by_role("button", name=label), label):
            break
    if not clicked:
        patterns = [
            ("cookie accept pattern", re.compile(r"accept( all)?( cookies)?|agree|allow all|got it", re.I)),
            ("cookie reject pattern", re.compile(r"reject all|necessary only|decline", re.I)),
            ("close overlay", re.compile(r"^(close|dismiss|×)$", re.I)),
        ]
        targets = page.locator("button, [role='button'], a, [aria-label]")
        for label, pattern in patterns:
            if click_first_visible(targets.filter(has_text=pattern), label):
                break
    return clicked


def choose_secondary_links(base_url: str, links: list[dict], limit: int = 3) -> list[dict]:
    base_host = urlparse(base_url).netloc.replace("www.", "")
    keywords = [
        "pricing",
        "product",
        "products",
        "solutions",
        "customers",
        "case",
        "work",
        "projects",
        "about",
        "docs",
        "blog",
        "resources",
        "shop",
        "collections",
        "features",
    ]
    scored: list[tuple[int, str, str]] = []
    seen: set[str] = set()
    for item in links:
        href = (item.get("href") or "").strip()
        text = re.sub(r"\s+", " ", item.get("text") or "").strip()
        if not href or href.startswith(("mailto:", "tel:", "javascript:", "#")):
            continue
        full = urljoin(base_url, href)
        parsed = urlparse(full)
        if parsed.scheme not in {"http", "https"}:
            continue
        if parsed.netloc.replace("www.", "") != base_host:
            continue
        normalized = parsed._replace(fragment="", query="").geturl().rstrip("/")
        if normalized.rstrip("/") == base_url.rstrip("/") or normalized in seen:
            continue
        haystack = f"{parsed.path} {text}".lower()
        score = 0
        for index, keyword in enumerate(keywords):
            if keyword in haystack:
                score += 100 - index
        if score <= 0:
            continue
        seen.add(normalized)
        scored.append((score, normalized, text or parsed.path))
    scored.sort(key=lambda row: (-row[0], len(row[1])))
    return [{"url": url, "text": text} for _, url, text in scored[:limit]]


def capture_interaction_states(page, samples: list[dict], limit: int = 12) -> list[dict]:
    states: list[dict] = []
    interactive = [
        sample
        for sample in samples
        if sample.get("category") in {"Button", "Navigation", "Form"} and sample.get("sampleId")
    ][:limit]
    for sample in interactive:
        sample_id = str(sample["sampleId"])
        selector = f'[data-designstyle-sample-id="{sample_id}"]'
        try:
            target = page.locator(selector).first
            if not target.is_visible(timeout=700):
                continue
            before = page.evaluate(
                """([selector, keys]) => {
                  const el = document.querySelector(selector);
                  if (!el) return {};
                  const cs = getComputedStyle(el);
                  const out = {};
                  for (const key of keys) out[key] = cs[key] || '';
                  return out;
                }""",
                [selector, COMPONENT_STYLE_KEYS],
            )
            target.hover(timeout=1200)
            page.wait_for_timeout(120)
            hover = page.evaluate(
                """([selector, keys]) => {
                  const el = document.querySelector(selector);
                  if (!el) return {};
                  const cs = getComputedStyle(el);
                  const out = {};
                  for (const key of keys) out[key] = cs[key] || '';
                  return out;
                }""",
                [selector, COMPONENT_STYLE_KEYS],
            )
            try:
                target.focus(timeout=700)
            except Exception:
                pass
            focus = page.evaluate(
                """([selector, keys]) => {
                  const el = document.querySelector(selector);
                  if (!el) return {};
                  const cs = getComputedStyle(el);
                  const out = {};
                  for (const key of keys) out[key] = cs[key] || '';
                  return out;
                }""",
                [selector, COMPONENT_STYLE_KEYS],
            )
            changed_hover = {k: hover.get(k) for k in COMPONENT_STYLE_KEYS if hover.get(k) != before.get(k)}
            changed_focus = {k: focus.get(k) for k in COMPONENT_STYLE_KEYS if focus.get(k) != before.get(k)}
            states.append(
                {
                    "sampleId": sample_id,
                    "category": sample.get("category", ""),
                    "text": sample.get("text", ""),
                    "hover_changed": changed_hover,
                    "focus_changed": changed_focus,
                }
            )
        except Exception as exc:
            states.append(
                {
                    "sampleId": sample_id,
                    "category": sample.get("category", ""),
                    "text": sample.get("text", ""),
                    "error": f"{type(exc).__name__}: {exc}",
                }
            )
    return states


def capture_with_playwright(
    url: str,
    screenshot: Path,
    dom_path: Path,
    width: int,
    height: int,
    timeout: int,
    inspect_secondary: bool = True,
) -> tuple[bool, str, dict]:
    if not CHROME.exists():
        return False, f"Chrome not found: {CHROME}", {}
    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:
        return False, f"Playwright import failed: {exc}", {}

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, executable_path=str(CHROME))
            page = browser.new_page(viewport={"width": width, "height": height}, user_agent="Mozilla/5.0 designstyle-capture/2.0")
            page.goto(url, wait_until="domcontentloaded", timeout=timeout * 1000)
            page.wait_for_timeout(1800)
            clicked = dismiss_common_overlays(page)
            page.evaluate(
                """async () => {
                  for (const y of [0, Math.round(innerHeight * 0.45), 0]) {
                    scrollTo(0, y);
                    await new Promise(r => setTimeout(r, 220));
                  }
                }"""
            )
            data = page.evaluate(
                """(clicked) => {
                  const visibleText = (el) => {
                    const text = (el.innerText || el.textContent || '').replace(/\\s+/g, ' ').trim();
                    const style = getComputedStyle(el);
                    const rect = el.getBoundingClientRect();
                    if (!text || style.display === 'none' || style.visibility === 'hidden' || rect.width === 0 || rect.height === 0) return '';
                    return text;
                  };
                  const sample = (selector, limit) => Array.from(document.querySelectorAll(selector)).map(visibleText).filter(Boolean).slice(0, limit);
                  const styleSample = (selector, limit) => Array.from(document.querySelectorAll(selector)).filter(el => visibleText(el)).map(el => {
                    const cs = getComputedStyle(el);
                    return `${el.tagName}:${cs.fontFamily}:${cs.fontSize}:${cs.fontWeight}:${cs.letterSpacing}:${cs.lineHeight}`;
                  }).slice(0, limit);
                  const colorSample = (selector, limit) => Array.from(document.querySelectorAll(selector)).filter(el => {
                    const rect = el.getBoundingClientRect();
                    return rect.width > 0 && rect.height > 0;
                  }).map(el => {
                    const cs = getComputedStyle(el);
                    return `${el.tagName}:${cs.color}:${cs.backgroundColor}`;
                  }).slice(0, limit);
                  return {
                    url: location.href,
                    title: document.title,
                    h1: sample('h1', 4),
                    h2: sample('h2', 8),
                    nav: sample('nav a, header a, [role="navigation"] a', 24),
                    buttons: sample('button, a[role="button"], .button, [class*="button"]', 20),
                    images: Array.from(document.images).map(img => ({alt: img.alt || '', src: img.currentSrc || img.src, w: img.naturalWidth, h: img.naturalHeight})).filter(x => x.src).slice(0, 40),
                    videos: Array.from(document.querySelectorAll('video, video source')).map(v => v.currentSrc || v.src || '').filter(Boolean).slice(0, 20),
                    links: Array.from(document.querySelectorAll('a[href]')).map(a => ({href: a.href || a.getAttribute('href') || '', text: visibleText(a)})).filter(x => x.href).slice(0, 240),
                    stylesheets: Array.from(document.querySelectorAll('link[rel="stylesheet"]')).map(x => x.href).filter(Boolean).slice(0, 24),
                    scripts: Array.from(document.scripts).map(x => x.src).filter(Boolean).slice(0, 36),
                    fontFamilies: styleSample('body,h1,h2,h3,p,a,button', 80),
                    fontSizes: styleSample('h1,h2,h3,p,a,button', 80),
                    colors: colorSample('body,h1,h2,h3,p,a,button,section,header', 100),
                    radii: Array.from(document.querySelectorAll('button,a,img,article,section,div')).filter(el => {
                      const rect = el.getBoundingClientRect();
                      return rect.width > 0 && rect.height > 0;
                    }).map(x => getComputedStyle(x).borderRadius).filter(x => x && x !== '0px').slice(0, 50),
                    viewport: {w: innerWidth, h: innerHeight, docW: document.documentElement.scrollWidth, docH: document.documentElement.scrollHeight},
                    textSample: Array.from(document.querySelectorAll('main, body')).map(visibleText).filter(Boolean)[0]?.slice(0, 1600) || '',
                    overlaysClicked: clicked
                  };
                }""",
                clicked,
            )
            component_evidence = page.evaluate(COMPONENT_CAPTURE_JS)
            component_evidence["stateSamples"] = capture_interaction_states(
                page, component_evidence.get("samples", [])
            )
            data["componentEvidence"] = component_evidence
            blocked_reasons = blocked_evidence_reasons(data)
            if blocked_reasons:
                browser.close()
                return False, f"blocked/security challenge captured: {', '.join(blocked_reasons[:3])}", data
            home_content = page.content()
            page.screenshot(path=str(screenshot), full_page=False)
            secondary = []
            if inspect_secondary:
                for link in choose_secondary_links(data.get("url") or url, data.get("links") or [], limit=3):
                    try:
                        page.goto(link["url"], wait_until="domcontentloaded", timeout=min(timeout, 10) * 1000)
                        page.wait_for_timeout(900)
                        summary = page.evaluate(
                            """(link) => {
                              const visibleText = (el) => {
                                const text = (el.innerText || el.textContent || '').replace(/\\s+/g, ' ').trim();
                                const style = getComputedStyle(el);
                                const rect = el.getBoundingClientRect();
                                if (!text || style.display === 'none' || style.visibility === 'hidden' || rect.width === 0 || rect.height === 0) return '';
                                return text;
                              };
                              const sample = (selector, limit) => Array.from(document.querySelectorAll(selector)).map(visibleText).filter(Boolean).slice(0, limit);
                              return {
                                url: location.href,
                                sourceText: link.text || '',
                                title: document.title,
                                h1: sample('h1', 2),
                                h2: sample('h2', 4),
                                viewport: {w: innerWidth, h: innerHeight, docW: document.documentElement.scrollWidth, docH: document.documentElement.scrollHeight}
                              };
                            }""",
                            link,
                        )
                        secondary.append(summary)
                    except Exception as exc:
                        secondary.append({"url": link["url"], "sourceText": link.get("text", ""), "error": f"{type(exc).__name__}: {exc}"})
            else:
                secondary.append({"note": "secondary page inspection skipped; prioritized homepage computed component evidence"})
            data["secondaryPages"] = secondary
            dom_path.write_text(home_content, encoding="utf-8", errors="ignore")
            browser.close()
        return screenshot.exists(), "playwright capture ok", data
    except Exception as exc:
        return False, f"Playwright capture failed: {type(exc).__name__}: {exc}", {}


def extract_json(dom: str) -> dict:
    match = re.search(r'data-designstyle-json="([^"]+)"', dom)
    if not match:
        return {}
    raw = match.group(1)
    raw = raw.replace("&quot;", '"').replace("&amp;", "&").replace("&#39;", "'")
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {}


def fallback_extract(dom: str, url: str) -> dict:
    title = re.search(r"<title[^>]*>(.*?)</title>", dom, re.I | re.S)
    h1 = re.findall(r"<h1[^>]*>(.*?)</h1>", dom, re.I | re.S)
    h2 = re.findall(r"<h2[^>]*>(.*?)</h2>", dom, re.I | re.S)
    links = re.findall(r"<a[^>]*>(.*?)</a>", dom, re.I | re.S)
    stylesheets = re.findall(r'<link[^>]+rel=["\']stylesheet["\'][^>]+href=["\']([^"\']+)["\']', dom, re.I)
    scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', dom, re.I)
    imgs = re.findall(r'<img[^>]+(?:src|data-src)=["\']([^"\']+)["\']', dom, re.I)
    clean = lambda s: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()
    return {
        "url": url,
        "title": clean(title.group(1)) if title else "",
        "h1": [clean(x) for x in h1[:4] if clean(x)],
        "h2": [clean(x) for x in h2[:8] if clean(x)],
        "nav": [clean(x) for x in links[:24] if clean(x)],
        "images": [{"src": x, "alt": "", "w": 0, "h": 0} for x in imgs[:40]],
        "videos": re.findall(r'<(?:video|source)[^>]+src=["\']([^"\']+)["\']', dom, re.I)[:20],
        "stylesheets": stylesheets[:24],
        "scripts": scripts[:36],
        "fontFamilies": [],
        "fontSizes": [],
        "colors": [],
        "radii": [],
        "viewport": {},
        "textSample": clean(re.sub(r"<[^>]+>", " ", dom))[:1600],
    }


def absolute_url(base: str, value: str) -> str:
    if value.startswith("//"):
        return "https:" + value
    if value.startswith("http://") or value.startswith("https://"):
        return value
    parsed = urlparse(base)
    if value.startswith("/"):
        return f"{parsed.scheme}://{parsed.netloc}{value}"
    root = base.rsplit("/", 1)[0]
    return f"{root}/{value}"


def fetch_text(url: str, timeout: int = 8) -> str:
    import urllib.request

    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 designstyle-capture/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        content_type = resp.headers.get("content-type", "")
        if "video/" in content_type or "image/" in content_type or "font/" in content_type:
            return ""
        return resp.read(220_000).decode("utf-8", errors="ignore")


def collect_motion(urls: list[str], base: str) -> tuple[list[str], dict[str, list[str]]]:
    checked = []
    evidence: dict[str, list[str]] = {}
    for url in urls[:12]:
        full = absolute_url(base, url)
        try:
            text = fetch_text(full)
        except Exception:
            continue
        if not text:
            continue
        checked.append(full)
        compact = re.sub(r"\s+", " ", text)
        for name, pattern in MOTION_PATTERNS.items():
            matches = evidence.setdefault(name, [])
            for match in pattern.finditer(compact):
                start = max(0, match.start() - 70)
                end = min(len(compact), match.end() + 130)
                snippet = compact[start:end].strip()
                if snippet not in matches and len(matches) < 5:
                    matches.append(snippet)
                if len(matches) >= 5:
                    break
    evidence = {k: v for k, v in evidence.items() if v}
    return checked, evidence


def list_values(raw: str) -> list[str]:
    return [x.strip() for x in raw.split(",") if x.strip()]


def summarize_list(values: list, limit: int = 5) -> str:
    cleaned = []
    for value in values:
        text = str(value)
        if SCIENTIFIC_PX_RE.search(text):
            continue
        cleaned.append(text[:180])
        if len(cleaned) >= limit:
            break
    return "; ".join(cleaned) or "none observed"


def summarize_secondary_pages(values: list[dict]) -> str:
    if not values:
        return "none found in automated first pass"
    rows: list[str] = []
    for item in values[:3]:
        if item.get("error"):
            rows.append(f"{item.get('sourceText') or 'link'} -> {item.get('url')} failed {item.get('error')}")
            continue
        h1 = summarize_list(item.get("h1") or [], 2)
        h2 = summarize_list(item.get("h2") or [], 2)
        rows.append(f"{item.get('sourceText') or 'link'} -> {item.get('url')} | title: {item.get('title','')} | h1: {h1} | h2: {h2}")
    return " || ".join(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture a website into a designstyle reference.")
    parser.add_argument("--name", required=True)
    parser.add_argument("--url", required=True)
    parser.add_argument("--category-tags", default="")
    parser.add_argument("--style-tags", default="")
    parser.add_argument("--structure-tags", default="")
    parser.add_argument("--motion-tags", default="")
    parser.add_argument("--code-tags", default="")
    parser.add_argument("--best-for", default="")
    parser.add_argument("--avoid-for", default="")
    parser.add_argument("--community-signal", required=True)
    parser.add_argument("--page-scope", required=True)
    parser.add_argument("--library", default=str(LIB))
    parser.add_argument("--width", type=int, default=1440)
    parser.add_argument("--height", type=int, default=1000)
    parser.add_argument("--timeout", type=int, default=12)
    parser.add_argument("--replace", action="store_true", help="Overwrite today's existing reference for this slug.")
    parser.add_argument("--output-reference", help="Overwrite this existing reference file instead of creating a dated file.")
    parser.add_argument("--skip-secondary", action="store_true", help="Skip secondary pages and prioritize first-page component evidence.")
    args = parser.parse_args()

    lib = Path(args.library).expanduser()
    for folder in ["references", "screenshots", "assets", "reviews", "indexes"]:
        (lib / folder).mkdir(parents=True, exist_ok=True)

    slug = slugify(args.name)
    today = date.today().isoformat()
    screenshot_rel = f"screenshots/{slug}-desktop.png"
    screenshot = lib / screenshot_rel
    dom_path = lib / "assets" / f"{today}-{slug}-dom.html"
    component_path = lib / "assets" / f"{today}-{slug}-component-styles.json"
    ok, browser_log, captured_data = capture_with_playwright(
        args.url,
        screenshot,
        dom_path,
        args.width,
        args.height,
        args.timeout,
        inspect_secondary=not args.skip_secondary,
    )
    if not dom_path.exists():
        dom_path.write_text(
            f"<!doctype html><title>{q(args.name)}</title><body>capture failed: {q(browser_log)}</body>",
            encoding="utf-8",
        )
    dom = dom_path.read_text(encoding="utf-8", errors="ignore")
    data = captured_data or extract_json(dom) or fallback_extract(dom, args.url)
    component_evidence = data.get("componentEvidence") if isinstance(data.get("componentEvidence"), dict) else {}
    blocked_reasons = blocked_evidence_reasons(data)
    component_evidence = sanitize_computed_value(component_evidence)
    component_payload = {
        "slug": slug,
        "name": args.name,
        "source_url": args.url,
        "final_url": data.get("url") or args.url,
        "captured_at": today,
        "screenshot": screenshot_rel,
        "evidence_quality": "blocked/security challenge captured" if blocked_reasons else "computed component styles from live DOM" if component_evidence else "component style capture unavailable",
        "blocked_reasons": blocked_reasons,
        "component_evidence": component_evidence,
    }
    component_path.write_text(json.dumps(component_payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    final_url = data.get("url") or args.url
    resource_urls = (data.get("stylesheets") or []) + (data.get("scripts") or [])
    checked_urls, motion = collect_motion(resource_urls, final_url)
    motion_keys = sorted(motion)
    exact_params = []
    for key in ["transition", "animation", "easing", "transform", "keyframes"]:
        exact_params.extend(motion.get(key, [])[:3])
    if not exact_params:
        exact_params = ["no direct code evidence; preserve only visible motion intent"]

    category_tags = list_values(args.category_tags)
    style_tags = list_values(args.style_tags)
    structure_tags = list_values(args.structure_tags)
    motion_tags = list_values(args.motion_tags) or motion_keys
    code_tags = list_values(args.code_tags) or motion_keys
    tags = list(dict.fromkeys(category_tags + style_tags + structure_tags + motion_tags + code_tags))
    best_for = list_values(args.best_for) or [args.page_scope]
    avoid_for = list_values(args.avoid_for)

    viewport = data.get("viewport") or {}
    images = data.get("images") or []
    videos = data.get("videos") or []
    fonts = data.get("fontFamilies") or []
    font_sizes = data.get("fontSizes") or []
    colors = data.get("colors") or []
    radii = data.get("radii") or []
    title = data.get("title") or args.name
    h1 = data.get("h1") or []
    h2 = data.get("h2") or []
    nav = data.get("nav") or []
    buttons = data.get("buttons") or []
    text_sample = data.get("textSample") or ""
    overlays_clicked = data.get("overlaysClicked") or []
    secondary_pages = data.get("secondaryPages") or []

    evidence_quality = "visual screenshot plus DOM/style/resource extraction" if ok else f"partial DOM extraction; screenshot failed: {browser_log[:160]}"
    path = Path(args.output_reference).expanduser() if args.output_reference else lib / "references" / f"{today}-{slug}.md"
    if not path.is_absolute():
        path = lib / path
    if path.exists() and not args.replace and not args.output_reference:
        digest = hashlib.sha1(args.url.encode()).hexdigest()[:6]
        path = lib / "references" / f"{today}-{slug}-{digest}.md"

    content = f'''---
title: "{q(args.name)}"
source_url: "{q(args.url)}"
captured_at: "{today}"
tags: {yaml_list(tags)}
category_tags: {yaml_list(category_tags)}
style_tags: {yaml_list(style_tags)}
structure_tags: {yaml_list(structure_tags)}
motion_tags: {yaml_list(motion_tags)}
code_tags: {yaml_list(code_tags)}
best_for: {yaml_list(best_for)}
avoid_for: {yaml_list(avoid_for)}
community_signal: "{q(args.community_signal)}"
page_scope: "{q(args.page_scope)}"
evidence_screenshot: "{screenshot_rel}"
evidence_quality: "{q(evidence_quality)}"
---

# Style Reference: {args.name}

## Essence
{args.name} is captured as a {", ".join(category_tags) or "website"} reference for {args.page_scope}. Reuse the observable structure, asset handling, component density, and motion evidence below; do not treat the brand identity as the reusable part.

## When To Use
- Use for {args.page_scope} work where the category fit is {", ".join(category_tags) or "unspecified"}.
- Use when the desired mechanics match these observed tags: {", ".join(style_tags + structure_tags + motion_tags) or "see evidence sections"}.

## When Not To Use
- Do not use when the task needs a different page scope than `{args.page_scope}` and no secondary page evidence is available.
- Do not use as proof of UX quality beyond the captured public page.
- Do not use to copy brand identity, claims, proprietary images, or exact campaign language.

## Evidence Snapshot
- Captured URL: {final_url}
- Page title: {title}
- Screenshot: {screenshot_rel}
- Viewport: {viewport or f"{args.width}x{args.height}"}
- Community signal: {args.community_signal}
- Page scope: {args.page_scope}
- Secondary pages inspected: {summarize_secondary_pages(secondary_pages)}
- H1 observed: {summarize_list(h1, 4)}
- H2 samples: {summarize_list(h2, 6)}
- Navigation samples: {summarize_list(nav, 12)}
- Images observed: {summarize_list([f"{img.get('alt','') or 'image'} {img.get('w',0)}x{img.get('h',0)} {img.get('src','')}" for img in images], 8)}
- Video observed: {summarize_list(videos, 5)}
- Overlays or fixed elements: clicked common overlay buttons {summarize_list(overlays_clicked, 3)}; inspect screenshot before final use.

## Visual System
- Layout: infer from screenshot and viewport; primary page text sample starts `{q(text_sample[:260])}`.
- Typography: observed font stacks and role rhythm are recorded below.
- Color: observed computed foreground/background pairs are recorded below.
- Density: navigation count {len(nav)}, image count {len(images)}, document height {viewport.get('docH', 'unknown')}.
- Shape: border radii samples recorded below.
- Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.

## Typography And Reading Rhythm
- Observed font stack counts: {summarize_list(fonts, 12)}
- Observed font sizes: {summarize_list(font_sizes, 16)}
- Observed weights: included in font size samples as `tag:size:weight:letterSpacing`.
- Observed letter spacing: included in font size samples.
- Preserve role relationships: keep display/UI/body scale relationships from screenshot rather than copying exact typefaces.

## Color, Material, And Contrast
- Observed text colors: {summarize_list(colors, 16)}
- Observed backgrounds: included in computed color pairs.
- UI shell colors vs asset-driven colors: decide from screenshot; do not infer beyond captured page.

## Layout Geometry And Spacing
- First viewport structure: captured in screenshot at {args.width}x{args.height}; record exact split/sidebar/hero geometry during manual refinement.
- Macro geometry: document size {viewport}.
- Media/card aspect stability: image natural sizes include {summarize_list([f"{img.get('w',0)}x{img.get('h',0)}" for img in images], 10)}.
- Observed border radii: {summarize_list(radii, 12)}

## Dimension And Ratio System
- Viewport and document: {viewport or f"{args.width}x{args.height}"}
- Observed media ratios: {summarize_list([f"{img.get('w',0)}:{img.get('h',0)}" for img in images if img.get('w') and img.get('h')], 10)}
- Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
- Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
- Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.

## Assets
- Image style: {summarize_list([img.get('alt') or img.get('src') for img in images], 8)}
- Illustration/icon style: inspect screenshot; automated pass records image sources only.
- Texture/pattern: inspect screenshot before use.
- Likely sources or production method: asset URLs/domains in image samples.

## Code Surface
- Framework/runtime hints: {", ".join([k for k in motion_keys if k in {"framer", "gsap", "swiper", "intersection", "request_animation_frame"}]) or "no direct runtime hint found"}
- Public stylesheet/script URLs: {summarize_list(checked_urls, 10)}
- CSS variables/tokens observed: automated pass did not isolate variables; inspect fetched resources for token naming if needed.
- Layout primitives observed: infer from screenshot and DOM; automated pass records page shape but not semantic layout primitives.
- Component or class naming clues: DOM saved at `assets/{today}-{slug}-dom.html` for manual inspection.
- Component computed-style evidence: `assets/{today}-{slug}-component-styles.json`
- Asset CDN and media loading patterns: {summarize_list([img.get('src') for img in images], 8)}

## Motion
- Page transitions: {", ".join(motion.get("transition", [])[:3]) or "no direct transition evidence found"}
- Micro-interactions: infer only when backed by transition/animation evidence or visible screenshot states.
- Scroll/entrance behavior: {", ".join(motion.get("intersection", [])[:2] + motion.get("request_animation_frame", [])[:2]) or "not proven in automated pass"}
- Timing/easing: {", ".join(motion.get("easing", [])[:5]) or "no direct timing evidence found"}

## Motion Code And Runtime Evidence
- Motion source: public styles/scripts sampled from captured DOM.
- CSS animation/transition evidence: {summarize_list(motion.get("transition", []) + motion.get("animation", []) + motion.get("keyframes", []), 8)}
- Public CSS/JS probe keywords: {", ".join(motion_keys) or "none"}
- Public CSS/JS motion snippets: {summarize_list([item for values in motion.values() for item in values], 10)}
- Exact motion parameters: {summarize_list(exact_params, 10)}
- JavaScript/runtime motion evidence: {summarize_list(motion.get("intersection", []) + motion.get("request_animation_frame", []) + motion.get("gsap", []) + motion.get("framer", []) + motion.get("swiper", []), 8)}
- Stylesheet evidence: {summarize_list(checked_urls, 8)}
- Interpreted motion tags: {", ".join(motion_tags) or "none"}
- Use this as implementation guidance only where evidence is direct. If CSS/JS is minified or only CDN names are visible, mark library/framework attribution as weak.

## Interaction And Components
- Navigation: {summarize_list(nav, 16)}
- Buttons/links: {summarize_list(buttons, 12)}
- Computed component styles: `assets/{today}-{slug}-component-styles.json`
- Cards/sections: inspect screenshot and DOM; automated pass records visible text and media.
- Forms/inputs: automated pass did not classify forms.
- Feedback states: not captured; do not infer.

## Implementation Notes
- CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
- Token ideas: extract from computed colors, font roles, and CSS resources.
- Libraries or techniques: {", ".join(motion_keys) or "none proven"}
- Performance/accessibility concerns: heavy media count {len(images)} and scripts {len(data.get('scripts') or [])}; check reduced-motion and image loading before copying motion patterns.

## Borrow
- Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
- Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Avoid Copying
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.

## Evidence Limits
- Automated capture covers one desktop viewport and public DOM/resources only.
- Secondary page evidence is summary-only unless listed above; screenshots remain the primary captured page.
- Some CSS/JS may be bundled, minified, blocked, or dynamically injected after capture.

## Self Review
- Evidence quality: {evidence_quality}
- Reuse value: useful for {args.page_scope} if category and screenshot match the future task.
- Missing pieces: mobile screenshot, secondary page screenshots, manual overlay classification, exact spacing measurements.
- Revision made: generated from live screenshot, DOM extraction, public resource sampling, and motion/code keyword probing.
'''
    path.write_text(content, encoding="utf-8")
    print(path)
    print(screenshot)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
