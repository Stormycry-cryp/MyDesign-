#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path
import os


LIB = Path(os.environ.get("DESIGNSTYLE_LIBRARY", str(Path.home() / ".codex" / "designstyle-library")))
CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
SEVERE_FLAGS = {"blocked", "404", "overlay_dominated", "blank", "generic_template", "visually_ordinary"}


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"https?://", "", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")[:72] or "candidate"


def dismiss_common_overlays(page) -> list[str]:
    clicked: list[str] = []
    labels = [
        "Accept all cookies",
        "Accept All Cookies",
        "Accept",
        "Agree",
        "I agree",
        "Reject all",
        "Necessary only",
        "Got it",
        "Continue",
        "Close",
    ]
    for label in labels:
        try:
            locator = page.get_by_role("button", name=label)
            for index in range(min(locator.count(), 4)):
                item = locator.nth(index)
                if item.is_visible():
                    item.click(timeout=1200)
                    clicked.append(label)
                    page.wait_for_timeout(400)
                    return clicked
        except Exception:
            pass
    return clicked


def score(data: dict) -> tuple[int, list[str], list[str]]:
    reasons: list[str] = []
    flags: list[str] = []
    value = 50

    if data.get("error"):
        return 0, ["capture failed"], ["blocked"]

    text = (data.get("bodyText") or "").lower()
    title = (data.get("title") or "").lower()
    h1_text = " ".join(data.get("h1") or []).lower()

    if len(text) < 80:
        value -= 30
        flags.append("blank")
    if "page not found" in text or "page not found" in h1_text or "404" in title:
        value -= 50
        flags.append("404")
    if any(token in text for token in ["verify you are human", "access denied", "you have been blocked", "captcha"]):
        value -= 50
        flags.append("blocked")
    if data.get("overlayTextLength", 0) > 260:
        value -= 25
        flags.append("overlay_dominated")

    if data.get("h1"):
        value += 8
        reasons.append("clear first-screen headline")
    if len(data.get("buttons") or []) >= 1:
        value += 5
        reasons.append("visible action controls")
    if len(data.get("images") or []) + len(data.get("videos") or []) >= 1:
        value += 8
        reasons.append("visual or product media evidence")
    if len(data.get("fontRoles") or []) >= 5:
        value += 7
        reasons.append("multiple typography roles")
    if len(set(data.get("backgrounds") or [])) >= 3:
        value += 6
        reasons.append("surface contrast variety")
    if len(data.get("dataProductTerms") or []) >= 2:
        value += 6
        reasons.append("data/product UI language visible")

    if data.get("navCount", 0) > 18:
        value -= 8
        flags.append("busy_navigation")
    if data.get("visibleTextBlocks", 0) > 100:
        value -= 8
        flags.append("cluttered_first_viewport")
    if len(data.get("images") or []) == 0 and len(data.get("videos") or []) == 0 and len(data.get("h1") or []) <= 1:
        value -= 12
        flags.append("visually_ordinary")
    if len(set(data.get("fontRoles") or [])) <= 2 and len(set(data.get("backgrounds") or [])) <= 2:
        value -= 10
        flags.append("generic_template")
    if data.get("overlayClicked"):
        flags.append("overlay_dismissed")

    return max(0, min(100, value)), reasons, flags


def probe(name: str, url: str, out_dir: Path, width: int, height: int, timeout_ms: int) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    screenshot = out_dir / f"{slugify(name)}-aesthetic.png"
    if not CHROME.exists():
        return {"name": name, "url": url, "score": 0, "allowed_to_write": False, "flags": ["blocked"], "reasons": [f"Chrome not found: {CHROME}"], "screenshot": str(screenshot)}

    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:
        return {"name": name, "url": url, "score": 0, "allowed_to_write": False, "flags": ["blocked"], "reasons": [f"Playwright import failed: {exc}"], "screenshot": str(screenshot)}

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, executable_path=str(CHROME))
            page = browser.new_page(
                viewport={"width": width, "height": height},
                user_agent="Mozilla/5.0 add-designstyle-aesthetic-probe/1.0",
            )
            page.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)
            page.wait_for_timeout(1600)
            clicked = dismiss_common_overlays(page)
            page.wait_for_timeout(600)
            data = page.evaluate(
                """(clicked) => {
                  const visible = (el) => {
                    const cs = getComputedStyle(el);
                    const rect = el.getBoundingClientRect();
                    if (cs.display === 'none' || cs.visibility === 'hidden' || rect.width < 2 || rect.height < 2) return '';
                    return (el.innerText || el.textContent || '').replace(/\\s+/g, ' ').trim();
                  };
                  const inViewport = (el) => {
                    const r = el.getBoundingClientRect();
                    return r.bottom > 0 && r.top < innerHeight && r.right > 0 && r.left < innerWidth;
                  };
                  const all = Array.from(document.querySelectorAll('body *')).filter(inViewport);
                  const texts = all.map(visible).filter(Boolean);
                  const styles = all.filter(el => visible(el)).slice(0, 140).map(el => {
                    const cs = getComputedStyle(el);
                    return {
                      font: `${cs.fontSize}/${cs.fontWeight}/${cs.fontFamily}`,
                      bg: cs.backgroundColor
                    };
                  });
                  const overlaySelectors = '[role="dialog"], [aria-modal="true"], .modal, .cookie, [class*="cookie"], [class*="consent"]';
                  const overlayText = Array.from(document.querySelectorAll(overlaySelectors)).filter(inViewport).map(visible).filter(Boolean).join(' ');
                  const productTerms = texts.join(' ').match(/dashboard|analytics|metric|report|insight|data|workflow|status|revenue|customer|chart|map|explore|visual|monitor|workspace/gi) || [];
                  return {
                    finalUrl: location.href,
                    title: document.title,
                    h1: Array.from(document.querySelectorAll('h1')).filter(inViewport).map(visible).filter(Boolean).slice(0, 3),
                    buttons: Array.from(document.querySelectorAll('button,a[role="button"],a')).filter(inViewport).map(visible).filter(Boolean).slice(0, 24),
                    navCount: Array.from(document.querySelectorAll('nav a, header a')).filter(inViewport).length,
                    images: Array.from(document.images).filter(inViewport).map(img => ({alt: img.alt || '', w: img.naturalWidth, h: img.naturalHeight})).slice(0, 20),
                    videos: Array.from(document.querySelectorAll('video, video source')).filter(inViewport).map(v => v.currentSrc || v.src || '').filter(Boolean).slice(0, 10),
                    fontRoles: Array.from(new Set(styles.map(s => s.font))).slice(0, 20),
                    backgrounds: Array.from(new Set(styles.map(s => s.bg).filter(x => x && x !== 'rgba(0, 0, 0, 0)'))).slice(0, 20),
                    visibleTextBlocks: texts.length,
                    bodyText: texts.join(' ').slice(0, 1800),
                    dataProductTerms: Array.from(new Set(productTerms.map(x => x.toLowerCase()))).slice(0, 20),
                    overlayClicked: clicked,
                    overlayTextLength: overlayText.length,
                    viewport: {w: innerWidth, h: innerHeight, docH: document.documentElement.scrollHeight}
                  };
                }""",
                clicked,
            )
            page.screenshot(path=str(screenshot), full_page=False)
            browser.close()
    except Exception as exc:
        data = {"error": f"{type(exc).__name__}: {exc}"}

    value, reasons, flags = score(data)
    severe = sorted(set(flags) & SEVERE_FLAGS)
    data.update(
        {
            "name": name,
            "url": url,
            "screenshot": str(screenshot),
            "score": value,
            "minimum_score": None,
            "reasons": reasons,
            "flags": flags,
            "severe_flags": severe,
        }
    )
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description="Probe first-viewport UI aesthetic fit before add-designstyle writes a reference.")
    parser.add_argument("--name", required=True)
    parser.add_argument("--url", required=True)
    parser.add_argument("--minimum-score", type=int, default=75)
    parser.add_argument("--out-dir", default=str(LIB / "reviews" / f"{date.today().isoformat()}-aesthetic-probes"))
    parser.add_argument("--width", type=int, default=1440)
    parser.add_argument("--height", type=int, default=1000)
    parser.add_argument("--timeout-ms", type=int, default=18000)
    args = parser.parse_args()

    result = probe(args.name, args.url, Path(args.out_dir).expanduser(), args.width, args.height, args.timeout_ms)
    result["minimum_score"] = args.minimum_score
    result["allowed_to_write"] = result["score"] >= args.minimum_score and not result.get("severe_flags")
    result["decision"] = "proceed" if result["allowed_to_write"] else "warn_user_before_writing"
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["allowed_to_write"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
