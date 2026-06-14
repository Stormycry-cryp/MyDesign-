#!/usr/bin/env python3
from __future__ import annotations

import argparse
import binascii
import colorsys
import math
import json
import re
import struct
import zlib
from pathlib import Path
import os


LIB = Path(os.environ.get("DESIGNSTYLE_LIBRARY", str(Path.home() / ".codex" / "designstyle-library")))

DIMENSIONS = {
    "scene": {
        "file": "scene.md",
        "title": "Scene",
        "observed": [
            ("Product scene", "category_tags"),
            ("Audience", "best_for"),
            ("Page scope", "page_scope"),
            ("Community signal", "community_signal"),
            ("Essence", "Essence"),
            ("When to use", "When To Use"),
            ("When not to use", "When Not To Use"),
        ],
        "inference": ["Borrow"],
    },
    "layout_spacing": {
        "file": "layout-spacing.md",
        "title": "Layout And Spacing",
        "observed": [
            ("Visual layout", "Visual System"),
            ("Layout geometry", "Layout Geometry And Spacing"),
            ("Dimension ratios", "Dimension And Ratio System"),
            ("Implementation notes", "Implementation Notes"),
        ],
        "inference": ["Borrow"],
    },
    "type_copy": {
        "file": "type-copy.md",
        "title": "Type And Copy",
        "observed": [
            ("Typography rhythm", "Typography And Reading Rhythm"),
            ("Reference text", "Reference Text And Copy Grammar"),
            ("H1/H2/navigation samples", "Evidence Snapshot"),
            ("Visual typography", "Visual System"),
        ],
        "inference": ["Borrow"],
    },
    "color_surface": {
        "file": "color-surface.md",
        "title": "Color And Surface",
        "observed": [
            ("Color/material", "Color, Material, And Contrast"),
            ("Surface grammar", "Style Tokens And Surface Grammar"),
            ("Visual color", "Visual System"),
        ],
        "inference": ["Borrow"],
    },
    "assets": {
        "file": "assets.md",
        "title": "Assets",
        "observed": [
            ("Assets", "Assets"),
            ("Images/video observed", "Evidence Snapshot"),
            ("Asset loading", "Code Surface"),
        ],
        "inference": ["Borrow"],
    },
    "motion_code": {
        "file": "motion-code.md",
        "title": "Motion And Code",
        "observed": [
            ("Motion", "Motion"),
            ("Motion code", "Motion Code And Runtime Evidence"),
            ("Code surface", "Code Surface"),
            ("Implementation notes", "Implementation Notes"),
        ],
        "inference": ["Borrow"],
    },
    "components_states": {
        "file": "components-states.md",
        "title": "Components And States",
        "observed": [
            ("Components", "Interaction And Components"),
            ("Component grammar", "Component Grammar"),
            ("Code surface", "Code Surface"),
        ],
        "inference": ["Borrow"],
    },
}

CARD_STRENGTH_DIMS = {
    "layout_spacing": "layout_spacing",
    "type_copy": "type_copy",
    "motion_code": "motion_code",
}

LIST_FIELDS = {
    "tags",
    "category_tags",
    "style_tags",
    "structure_tags",
    "motion_tags",
    "code_tags",
    "best_for",
    "avoid_for",
}

CSS_DURATION_RE = re.compile(r"(?<![\w.-])(\d*\.?\d+)(ms|s)(?![\w-])", re.I)
CSS_EASING_RE = re.compile(r"cubic-bezier\([^)]+\)|steps\([^)]+\)|\b(?:ease-in-out|ease-in|ease-out|linear|ease)\b", re.I)
MOTION_STATE_KEYS = ["transform", "opacity", "backgroundColor", "color", "borderColor", "boxShadow", "border", "borderBottom", "borderTop"]


def slug_from_reference(path: Path) -> str:
    slug = path.stem
    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", slug)
    return slug or path.stem


def parse_list(value: str) -> list[str]:
    value = value.strip()
    if not value or value == "[]":
        return []
    if value.startswith("[") and value.endswith("]"):
        try:
            data = json.loads(value)
            if isinstance(data, list):
                return [str(item).strip() for item in data if str(item).strip()]
        except json.JSONDecodeError:
            inner = value[1:-1]
            return [item.strip().strip("'\"") for item in inner.split(",") if item.strip().strip("'\"")]
    return [value.strip("'\"")]


def read_json_dict(path: Path) -> dict[str, object]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def parse_frontmatter(text: str) -> dict[str, object]:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    data: dict[str, object] = {}
    for line in parts[1].splitlines():
        if ":" not in line:
            continue
        key, raw = line.split(":", 1)
        key = key.strip()
        raw = raw.strip()
        if key in LIST_FIELDS:
            data[key] = parse_list(raw)
        else:
            data[key] = raw.strip("'\"")
    return data


def section(text: str, name: str) -> str:
    match = re.search(rf"^## {re.escape(name)}\s*$([\s\S]*?)(?=^## |\Z)", text, re.M)
    return match.group(1).strip() if match else ""


def source_value(text: str, meta: dict[str, object], source: str) -> str:
    if source in meta:
        value = meta[source]
        if isinstance(value, list):
            return ", ".join(value)
        return str(value)
    return section(text, source)


def clean_value(value: str) -> str:
    value = re.sub(r"\n{3,}", "\n\n", value.strip())
    return value


def has_observed_value(value: str) -> bool:
    value = clean_value(value).lower()
    if not value:
        return False
    weak = {"todo", "n/a", "none recorded yet", "missing", "unknown"}
    compact = re.sub(r"[^a-z0-9]+", " ", value).strip()
    if compact in weak:
        return False
    lines = [line.strip() for line in value.splitlines() if line.strip()]
    useful = 0
    for line in lines:
        stripped = line.lstrip("- ").strip()
        if not stripped:
            continue
        if stripped.endswith(":") or stripped.lower() in weak:
            continue
        if re.search(r"\btodo\b", stripped, re.I):
            continue
        useful += 1
    return useful > 0


def bullet_block(label: str, value: str) -> str:
    value = clean_value(value)
    if not has_observed_value(value):
        return ""
    if "\n" not in value:
        return f"- {label}: {value}"
    indented = "\n".join(f"  {line}" if line else "" for line in value.splitlines())
    return f"- {label}:\n{indented}"


def markdown_list(values: list[str]) -> str:
    if not values:
        return "- None recorded."
    return "\n".join(f"- {item}" for item in values)


def dimension_markdown(name: str, text: str, meta: dict[str, object]) -> str:
    spec = DIMENSIONS[name]
    observed_blocks = []
    missing = []
    for label, source in spec["observed"]:
        value = source_value(text, meta, source)
        block = bullet_block(label, value)
        if block:
            observed_blocks.append(block)
        else:
            missing.append(f"{label} from {source}")

    inference_blocks = []
    for source in spec["inference"]:
        value = source_value(text, meta, source)
        block = bullet_block(source, value)
        if block:
            inference_blocks.append(block)

    limits = section(text, "Avoid Copying") or "Brand identity, proprietary assets, product names, claims, and exact copy."
    observed = "\n".join(observed_blocks) if observed_blocks else "- No observed values recorded in the full reference."
    inference = "\n".join(inference_blocks) if inference_blocks else "- No generator inference. Read the full reference before adapting."
    missing_text = markdown_list(missing) if missing else "- None recorded."
    return f"""# {spec["title"]}

## Observed
{observed}

## Inference
{inference}

## Missing Evidence
{missing_text}

## Do Not Copy
{clean_value(limits)}
"""


def observed_count(dimension_text: str) -> int:
    match = re.search(r"^## Observed\s*$([\s\S]*?)(?=^## |\Z)", dimension_text, re.M)
    if not match:
        return 0
    observed = match.group(1)
    if "No observed values recorded" in observed:
        return 0
    return sum(1 for line in observed.splitlines() if has_observed_value(line))


def evidence_strength(dimension_text: str, dimension_name: str) -> str:
    count = observed_count(dimension_text)
    missing_only = "No observed values recorded" in dimension_text
    if count == 0 or missing_only:
        return "missing"
    if dimension_name == "motion_code" and "no direct code evidence" in dimension_text.lower():
        return "weak"
    if count >= 5:
        return "strong"
    if count >= 2:
        return "medium"
    return "weak"


def screenshot_strength(meta: dict[str, object], lib: Path) -> str:
    screenshot = str(meta.get("evidence_screenshot", "")).strip()
    if not screenshot:
        return "missing"
    if (lib / screenshot).exists():
        return "strong"
    return "weak"


def parse_png_rgb(path: Path, max_samples: int = 50000) -> tuple[list[tuple[int, int, int]], str]:
    try:
        data = path.read_bytes()
        if not data.startswith(b"\x89PNG\r\n\x1a\n"):
            return [], "screenshot is not PNG"
        pos = 8
        width = height = color_type = bit_depth = None
        idat = bytearray()
        while pos + 8 <= len(data):
            length = struct.unpack(">I", data[pos : pos + 4])[0]
            kind = data[pos + 4 : pos + 8]
            chunk = data[pos + 8 : pos + 8 + length]
            pos += 12 + length
            if kind == b"IHDR":
                width, height, bit_depth, color_type = struct.unpack(">IIBB", chunk[:10])[:4]
            elif kind == b"IDAT":
                idat.extend(chunk)
            elif kind == b"IEND":
                break
        if not width or not height or bit_depth != 8 or color_type not in {2, 6}:
            return [], f"unsupported PNG mode bit_depth={bit_depth} color_type={color_type}"
        channels = 3 if color_type == 2 else 4
        raw = zlib.decompress(bytes(idat))
        stride = width * channels
        rows = []
        prev = [0] * stride
        offset = 0
        for _ in range(height):
            filter_type = raw[offset]
            offset += 1
            row = list(raw[offset : offset + stride])
            offset += stride
            recon = [0] * stride
            for i, value in enumerate(row):
                left = recon[i - channels] if i >= channels else 0
                up = prev[i]
                up_left = prev[i - channels] if i >= channels else 0
                if filter_type == 0:
                    recon[i] = value
                elif filter_type == 1:
                    recon[i] = (value + left) & 255
                elif filter_type == 2:
                    recon[i] = (value + up) & 255
                elif filter_type == 3:
                    recon[i] = (value + ((left + up) // 2)) & 255
                elif filter_type == 4:
                    p = left + up - up_left
                    pa, pb, pc = abs(p - left), abs(p - up), abs(p - up_left)
                    predictor = left if pa <= pb and pa <= pc else up if pb <= pc else up_left
                    recon[i] = (value + predictor) & 255
                else:
                    return [], f"unsupported PNG filter {filter_type}"
            rows.append(recon)
            prev = recon
        step = max(1, int(math.sqrt((width * height) / max_samples)))
        pixels = []
        for y in range(0, height, step):
            row = rows[y]
            for x in range(0, width, step):
                idx = x * channels
                if channels == 4 and row[idx + 3] < 16:
                    continue
                pixels.append((row[idx], row[idx + 1], row[idx + 2]))
        return pixels, f"sampled {len(pixels)} pixels from {width}x{height} PNG"
    except (OSError, zlib.error, struct.error, binascii.Error) as exc:
        return [], f"failed to parse screenshot: {exc}"


def hex_to_rgb(value: str) -> tuple[int, int, int] | None:
    value = value.strip().lstrip("#")
    if len(value) == 3:
        value = "".join(ch * 2 for ch in value)
    if len(value) != 6 or not re.fullmatch(r"[0-9a-fA-F]{6}", value):
        return None
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def rel_luminance(rgb: tuple[int, int, int]) -> float:
    values = []
    for channel in rgb:
        c = channel / 255
        values.append(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * values[0] + 0.7152 * values[1] + 0.0722 * values[2]


def color_role(rgb: tuple[int, int, int]) -> str:
    lum = rel_luminance(rgb)
    h, s, v = colorsys.rgb_to_hsv(*(channel / 255 for channel in rgb))
    if lum > 0.9 and s < 0.12:
        return "background"
    if lum < 0.12 and s < 0.25:
        return "foreground"
    if s < 0.12:
        return "neutral surface"
    if v > 0.72 and s > 0.35:
        return "accent"
    if v < 0.45:
        return "deep accent"
    return "supporting color"


def nearest_palette(pixels: list[tuple[int, int, int]], max_colors: int = 10) -> list[dict[str, object]]:
    buckets: dict[tuple[int, int, int], int] = {}
    for rgb in pixels:
        key = tuple(round(channel / 16) * 16 for channel in rgb)
        key = tuple(min(255, channel) for channel in key)
        buckets[key] = buckets.get(key, 0) + 1
    colors = sorted(buckets.items(), key=lambda item: item[1], reverse=True)
    chosen: list[tuple[tuple[int, int, int], int]] = []
    for rgb, count in colors:
        if all(sum((rgb[i] - existing[i]) ** 2 for i in range(3)) ** 0.5 >= 34 for existing, _ in chosen):
            chosen.append((rgb, count))
        if len(chosen) >= max_colors:
            break
    total = sum(buckets.values()) or 1
    return [
        {
            "hex": rgb_to_hex(rgb),
            "rgb": list(rgb),
            "role": color_role(rgb),
            "source": "screenshot pixel sample",
            "share": round(count / total, 4),
            "luminance": round(rel_luminance(rgb), 4),
        }
        for rgb, count in chosen
    ]


def explicit_colors(text: str) -> list[dict[str, object]]:
    found: list[tuple[int, int, int]] = []
    for match in re.findall(r"#[0-9a-fA-F]{3,8}\b", text):
        rgb = hex_to_rgb(match[:7] if len(match) >= 7 else match)
        if rgb:
            found.append(rgb)
    for match in re.findall(r"rgba?\(([^)]+)\)", text, re.I):
        parts = [part.strip() for part in match.split(",")[:3]]
        if len(parts) == 3 and all(re.fullmatch(r"\d+(?:\.\d+)?", part) for part in parts):
            rgb = tuple(max(0, min(255, int(float(part)))) for part in parts)
            found.append(rgb)
    unique = []
    seen = set()
    for rgb in found:
        if rgb not in seen:
            seen.add(rgb)
            unique.append(rgb)
    return [
        {
            "hex": rgb_to_hex(rgb),
            "rgb": list(rgb),
            "role": color_role(rgb),
            "source": "explicit reference or DOM color",
            "luminance": round(rel_luminance(rgb), 4),
        }
        for rgb in unique[:32]
    ]


def line_values(text: str, label: str) -> list[str]:
    values = []
    pattern = rf"^- {re.escape(label)}:\s*(.*?)\s*$"
    for match in re.finditer(pattern, text, re.M):
        value = match.group(1).strip()
        lowered = value.lower()
        if not value or lowered in {"none", "none observed", "todo"}:
            continue
        if any(token in lowered for token in [
            "not captured",
            "do not infer",
            "automated pass did not",
            "inspect screenshot",
            "cookie",
            "hs-banner",
            "hs-modal",
            "eu-cookie",
        ]):
            continue
        if len(value) > 360 and ("{" in value or "}" in value or ";" in value):
            continue
        value = cleaned_component_value(value)
        if not value:
            continue
        if len(value) > 520:
            value = value[:520].rstrip() + "..."
        values.append(value)
    return values


def cleaned_component_value(value: str) -> str:
    parts = [part.strip() for part in value.split(";")]
    if len(parts) == 1:
        return "" if is_unusable_component_sample(parts[0]) else value
    kept = [part for part in parts if part and not is_unusable_component_sample(part)]
    return "; ".join(kept)


def reference_component_evidence_path(text: str, lib: Path) -> Path | None:
    match = re.search(r"`([^`]+component-styles\.json)`", text)
    if not match:
        return None
    path = Path(match.group(1))
    return path if path.is_absolute() else lib / path


def reference_motion_evidence_path(text: str, lib: Path) -> Path | None:
    match = re.search(r"`([^`]+motion\.json)`", text)
    if not match:
        return None
    path = Path(match.group(1))
    return path if path.is_absolute() else lib / path


def fallback_motion_item(text: str, slug: str) -> dict[str, object] | None:
    evidence = section(text, "Motion Code And Runtime Evidence") or section(text, "Motion")
    if not evidence:
        return None
    duration_match = re.search(r"(\d+(?:\.\d+)?)(ms|s)", evidence)
    easing_match = re.search(r"cubic-bezier\([^)]+\)|\b(?:ease-in-out|ease-in|ease-out|linear|ease)\b", evidence, re.I)
    transform_match = re.search(r"(translate[XY]?\([^)]+\)|scale[XY]?\([^)]+\)|rotate\([^)]+\))", evidence)
    duration_ms: int | str = "missing"
    if duration_match:
        value = float(duration_match.group(1))
        duration_ms = int(round(value * 1000)) if duration_match.group(2).lower() == "s" else int(round(value))
    selector_role = "component"
    trigger = "state-change"
    lowered = evidence.lower()
    if "hover" in lowered:
        trigger = "hover"
    if "card" in lowered:
        selector_role = "card"
    return {
        "id": f"motion-{slug}-fallback",
        "selector": "missing",
        "selector_role": selector_role,
        "trigger": trigger,
        "property": "transform" if transform_match else "missing",
        "from": "missing",
        "to": transform_match.group(1) if transform_match else "missing",
        "duration_ms": duration_ms,
        "delay_ms": 0,
        "easing": easing_match.group(0) if easing_match else "missing",
        "keyframes": [],
        "reduced_motion": "missing",
        "source": "L3 Motion Code And Runtime Evidence",
        "description": "Motion evidence was summarized from the L3 reference because structured motion JSON was missing.",
        "snippet": "",
    }


def normalized_noise_filter(value: object) -> list[str]:
    if not isinstance(value, list):
        return []
    result: list[str] = []
    for item in value:
        lowered = str(item).lower()
        if re.search(r"autofill", lowered):
            label = "browser-fill-rules"
        elif re.search(r"consent|cookie|onetrust|ot-sdk|hs-banner|hs-modal|recaptcha|captcha", lowered):
            label = "blocked-overlay-rules"
        else:
            label = re.sub(r"[^a-z0-9_-]+", "-", lowered).strip("-") or "filtered-rule"
        if label not in result:
            result.append(label)
    return result


MOTION_REQUIRED_FIELDS = ["selector", "selector_role", "trigger", "property", "duration_ms", "delay_ms", "easing", "description", "source"]


def missing_motion_fields(item: dict[str, object]) -> list[str]:
    missing: list[str] = []
    for field in MOTION_REQUIRED_FIELDS:
        if item.get(field) in {"", None, "missing"}:
            missing.append(field)
    return missing


def first_duration_ms(value: str) -> int | str:
    match = CSS_DURATION_RE.search(value)
    if not match:
        return "missing"
    amount = float(match.group(1))
    return int(round(amount * 1000)) if match.group(2).lower() == "s" else int(round(amount))


def first_easing(value: str) -> str:
    match = CSS_EASING_RE.search(value)
    return match.group(0) if match else "missing"


def css_property_name(value: str) -> str:
    parts = value.split("-")
    return parts[0] + "".join(part[:1].upper() + part[1:] for part in parts[1:])


def transition_declaration_parts(transition: str, styles: dict[str, object]) -> tuple[str, int, str] | None:
    transition_property = str(styles.get("transitionProperty") or "").strip()
    for part in [item.strip() for item in transition.split(",") if item.strip()]:
        if is_unusable_component_sample(part):
            continue
        duration = first_duration_ms(part)
        easing = first_easing(part)
        if not isinstance(duration, int) or duration <= 0 or easing == "missing":
            continue
        prop_match = re.match(r"([a-z-]+)\b", part, re.I)
        prop = prop_match.group(1).lower() if prop_match else transition_property.lower()
        if not prop or prop in {"all", "none", "z-index", "visibility"}:
            continue
        if prop.endswith("-webkit-transform"):
            prop = "transform"
        return css_property_name(prop), duration, easing
    return None


def role_from_component_category(category: str) -> str:
    lowered = category.lower()
    if "button" in lowered:
        return "button"
    if "navigation" in lowered:
        return "navigation"
    if "card" in lowered:
        return "card"
    if "form" in lowered:
        return "form"
    return "component"


def motion_item_id(item: dict[str, object]) -> str:
    raw = "-".join(str(item.get(key, "")) for key in ["selector_role", "trigger", "property", "duration_ms", "easing"])
    raw = re.sub(r"[^a-zA-Z0-9]+", "-", raw).strip("-").lower()
    return f"motion-{raw or 'item'}"


def motion_description(item: dict[str, object], label: str) -> str:
    role_names = {
        "card": "卡片",
        "button": "按钮",
        "navigation": "导航",
        "form": "表单",
        "component": "组件",
    }
    role = role_names.get(str(item.get("selector_role")), "组件")
    prop = str(item.get("property") or "motion")
    duration = item.get("duration_ms")
    easing = item.get("easing") or "missing"
    trigger = item.get("trigger") or "state-change"
    start = item.get("from") or "missing"
    end = item.get("to") or "missing"
    return f"{role}{trigger}：{prop} {start} -> {end}，{duration}ms {easing}，{trigger} 触发；样本 {label}"


def component_transition_motion_items(text: str, lib: Path, slug: str) -> list[dict[str, object]]:
    path = reference_component_evidence_path(text, lib)
    if not path or not path.exists():
        return []
    payload = read_json_dict(path)
    evidence = payload.get("component_evidence")
    if not isinstance(evidence, dict):
        return []
    samples = evidence.get("samples")
    states = evidence.get("stateSamples")
    if not isinstance(samples, list) or not isinstance(states, list):
        return []
    samples_by_id = {
        sample.get("sampleId"): sample
        for sample in samples
        if isinstance(sample, dict) and sample.get("sampleId")
    }
    items: list[dict[str, object]] = []
    seen: set[tuple[object, ...]] = set()
    samples_with_state_motion: set[object] = set()
    for state in states:
        if not isinstance(state, dict) or is_unusable_component_dict(state):
            continue
        sample = samples_by_id.get(state.get("sampleId"))
        if not isinstance(sample, dict) or is_unusable_component_dict(sample):
            continue
        styles = sample.get("styles") if isinstance(sample.get("styles"), dict) else {}
        if not styles:
            continue
        before = state.get("before") if isinstance(state.get("before"), dict) else {}
        category = str(state.get("category") or sample.get("category") or "Component")
        role = role_from_component_category(category)
        label = re.sub(r"\s+", " ", str(state.get("text") or sample.get("text") or state.get("sampleId") or category)).strip()[:80]
        for trigger, key in [("hover", "hover_changed"), ("focus", "focus_changed")]:
            changed = state.get(key)
            if not isinstance(changed, dict) or not changed:
                continue
            prop = next((name for name in MOTION_STATE_KEYS if changed.get(name)), "")
            if not prop:
                continue
            timing_source = str(
                changed.get("transition")
                or before.get("transition")
                or styles.get("transition")
                or changed.get("transitionDuration")
                or before.get("transitionDuration")
                or styles.get("transitionDuration")
                or ""
            )
            duration = first_duration_ms(timing_source)
            easing_source = str(
                changed.get("transitionTimingFunction")
                or before.get("transitionTimingFunction")
                or styles.get("transitionTimingFunction")
                or timing_source
            )
            easing = first_easing(easing_source)
            if not isinstance(duration, int) or duration <= 0 or easing == "missing":
                continue
            item: dict[str, object] = {
                "selector": f"[data-designstyle-sample-id=\"{state.get('sampleId', 'missing')}\"]",
                "selector_role": role,
                "trigger": trigger,
                "property": prop,
                "from": str(styles.get(prop) or "missing"),
                "to": str(changed.get(prop) or "missing"),
                "duration_ms": duration,
                "delay_ms": 0,
                "easing": easing,
                "keyframes": [],
                "reduced_motion": "missing",
                "source": "component-styles interaction evidence",
                "snippet": json.dumps({prop: changed.get(prop), "transition": timing_source}, ensure_ascii=False, sort_keys=True),
            }
            item["description"] = motion_description(item, label)
            item["id"] = motion_item_id(item)
            dedupe = (item["selector"], item["trigger"], item["property"], item["duration_ms"], item["easing"], item["to"])
            if dedupe in seen:
                continue
            seen.add(dedupe)
            samples_with_state_motion.add(state.get("sampleId"))
            items.append(item)
    for sample in samples:
        if not isinstance(sample, dict) or is_unusable_component_dict(sample):
            continue
        sample_id = sample.get("sampleId")
        if sample_id in samples_with_state_motion:
            continue
        styles = sample.get("styles") if isinstance(sample.get("styles"), dict) else {}
        transition = str(styles.get("transition") or "").strip()
        if not transition or transition.lower() in {"all", "none"}:
            continue
        parsed = transition_declaration_parts(transition, styles)
        if not parsed:
            continue
        prop, duration, easing = parsed
        category = str(sample.get("category") or "Component")
        role = role_from_component_category(category)
        label = re.sub(r"\s+", " ", str(sample.get("text") or sample.get("ariaLabel") or sample_id or category)).strip()[:80]
        item = {
            "selector": f"[data-designstyle-sample-id=\"{sample_id or 'missing'}\"]",
            "selector_role": role,
            "trigger": "state-change",
            "property": prop,
            "from": str(styles.get(prop) or "missing"),
            "to": "missing",
            "duration_ms": duration,
            "delay_ms": 0,
            "easing": easing,
            "keyframes": [],
            "reduced_motion": "missing",
            "source": "component-styles transition declaration",
            "snippet": json.dumps({"transition": transition}, ensure_ascii=False, sort_keys=True),
        }
        item["description"] = motion_description(item, label)
        item["id"] = motion_item_id(item)
        dedupe = (item["selector"], item["trigger"], item["property"], item["duration_ms"], item["easing"], item["to"])
        if dedupe in seen:
            continue
        seen.add(dedupe)
        items.append(item)
    return items


def build_motion_system(reference: Path, lib: Path, text: str, meta: dict[str, object]) -> dict[str, object]:
    slug = slug_from_reference(reference)
    path = reference_motion_evidence_path(text, lib)
    payload: dict[str, object] = {}
    if path and path.exists():
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            payload = {}
    items = payload.get("items") if isinstance(payload, dict) else None
    if not isinstance(items, list):
        items = []
    if not items:
        component_items = component_transition_motion_items(text, lib, slug)
        if component_items:
            items = component_items
        else:
            fallback = fallback_motion_item(text, slug)
            items = [fallback] if fallback else []
    normalized_items: list[dict[str, object]] = []
    omitted_incomplete: list[dict[str, object]] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        normalized = {
            "id": str(item.get("id") or f"motion-{len(normalized_items) + len(omitted_incomplete) + 1}"),
            "selector": str(item.get("selector") or "missing"),
            "selector_role": str(item.get("selector_role") or "missing"),
            "trigger": str(item.get("trigger") or "missing"),
            "property": str(item.get("property") or "missing"),
            "from": str(item.get("from") or "missing"),
            "to": str(item.get("to") or "missing"),
            "duration_ms": item.get("duration_ms", "missing"),
            "delay_ms": item.get("delay_ms", "missing"),
            "easing": str(item.get("easing") or "missing"),
            "keyframes": item.get("keyframes") if isinstance(item.get("keyframes"), list) else [],
            "reduced_motion": str(item.get("reduced_motion") or "missing"),
            "source": str(item.get("source") or "missing"),
            "description": str(item.get("description") or "missing"),
            "snippet": str(item.get("snippet") or ""),
        }
        missing_fields = missing_motion_fields(normalized)
        if missing_fields:
            omitted = dict(normalized)
            omitted["missing_fields"] = missing_fields
            omitted_incomplete.append(omitted)
            continue
        normalized_items.append(normalized)
    source_urls = payload.get("source_urls") if isinstance(payload.get("source_urls"), list) else []
    missing_notes = [f"{item.get('id', 'motion item')} lacks {field}" for item in omitted_incomplete for field in item.get("missing_fields", [])]
    return {
        "slug": slug,
        "title": str(meta.get("title") or slug),
        "reference_path": f"references/{reference.name}",
        "source_motion_path": str(path.relative_to(lib)) if path and path.exists() else "missing",
        "source_urls": source_urls,
        "items": normalized_items,
        "omitted_incomplete": omitted_incomplete,
        "missing": missing_notes or ([] if normalized_items else ["No complete structured motion evidence could be extracted."]),
        "noise_filtered": normalized_noise_filter(payload.get("noise_filtered")) if isinstance(payload, dict) else [],
    }


def motion_code_markdown(system: dict[str, object], limits: str) -> str:
    items = system.get("items") if isinstance(system.get("items"), list) else []
    if items:
        rows = []
        snippets = []
        missing = []
        for item in items:
            if not isinstance(item, dict):
                continue
            duration = item.get("duration_ms", "missing")
            delay = item.get("delay_ms", "missing")
            duration_text = f"{duration}ms" if isinstance(duration, int) else str(duration)
            delay_text = f"{delay}ms" if isinstance(delay, int) else str(delay)
            rows.append(
                "| {role} | {trigger} | {prop} | {duration} | {delay} | {easing} | {desc} |".format(
                    role=item.get("selector_role", "missing"),
                    trigger=item.get("trigger", "missing"),
                    prop=item.get("property", "missing"),
                    duration=duration_text,
                    delay=delay_text,
                    easing=item.get("easing", "missing"),
                    desc=str(item.get("description", "missing")).replace("|", "/"),
                )
            )
            if item.get("snippet"):
                snippets.append(f"### {item.get('id', 'motion')}\n\n```css\n{item.get('snippet')}\n```")
            for field in ["selector", "property", "duration_ms", "delay_ms", "easing", "trigger"]:
                if item.get(field) in {"", None, "missing"}:
                    missing.append(f"{item.get('id', 'motion item')} lacks {field}")
        missing_text = markdown_list(sorted(set(missing)) or list(system.get("missing") or []))
        snippet_text = "\n\n".join(snippets) if snippets else "No direct snippet appendix available."
        rows_text = "\n".join(rows)
    else:
        rows_text = "| Missing | Missing | Missing | missing | missing | missing | No structured motion evidence. |"
        snippet_text = "No direct snippet appendix available."
        missing_text = markdown_list(list(system.get("missing") or ["No structured motion evidence could be extracted."]))
    return f"""# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
{rows_text}

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: {system.get("source_motion_path", "missing")}

## Missing Evidence
{missing_text}

## Snippet Appendix
{snippet_text}

## Do Not Copy
{clean_value(limits)}
"""


def compact_style(styles: dict[str, object]) -> str:
    keys = [
        "display",
        "position",
        "color",
        "backgroundColor",
        "border",
        "borderRadius",
        "boxShadow",
        "fontFamily",
        "fontSize",
        "fontWeight",
        "letterSpacing",
        "lineHeight",
        "padding",
        "gap",
        "transition",
        "transitionDuration",
        "transitionTimingFunction",
        "transform",
        "opacity",
        "cursor",
        "backdropFilter",
    ]
    parts = []
    for key in keys:
        value = str(styles.get(key) or "").strip()
        if not value or value in {"0px", "none", "normal", "auto", "rgba(0, 0, 0, 0)", "matrix(1, 0, 0, 1, 0, 0)"}:
            continue
        if is_unusable_component_sample(value):
            continue
        parts.append(f"{key}={value}")
    return "; ".join(parts[:14])


def compact_sample(sample: dict[str, object]) -> str:
    rect = sample.get("rect") if isinstance(sample.get("rect"), dict) else {}
    styles = sample.get("styles") if isinstance(sample.get("styles"), dict) else {}
    text = str(sample.get("text") or sample.get("ariaLabel") or sample.get("classHint") or "").strip()
    if is_unusable_component_sample(text):
        return ""
    text = re.sub(r"\s+", " ", text)[:90] or "unlabeled"
    geometry = ""
    if rect:
        geometry = f"rect={rect.get('width')}x{rect.get('height')}@{rect.get('x')},{rect.get('y')}"
    style = compact_style(styles)
    bits = [f"{sample.get('tag', 'node')} {text}", geometry, style]
    return " | ".join(bit for bit in bits if bit)


def is_unusable_component_dict(sample: dict[str, object]) -> bool:
    checks = [
        sample.get("text"),
        sample.get("ariaLabel"),
        sample.get("classHint"),
        sample.get("sampleId"),
    ]
    return any(is_unusable_component_sample(str(value)) for value in checks if value)


def component_evidence_summary(text: str, lib: Path) -> dict[str, dict[str, list[str]]]:
    path = reference_component_evidence_path(text, lib)
    if not path or not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    evidence = payload.get("component_evidence", {})
    if not isinstance(evidence, dict):
        return {}
    samples = evidence.get("samples", [])
    states = evidence.get("stateSamples", [])
    if not isinstance(samples, list):
        samples = []
    if not isinstance(states, list):
        states = []

    result: dict[str, dict[str, list[str]]] = {}
    for name in ["Navigation", "Button", "Card", "Form", "Icon"]:
        matching = [
            sample
            for sample in samples
            if isinstance(sample, dict) and sample.get("category") == name and not is_unusable_component_dict(sample)
        ]
        style_evidence = []
        content_samples = []
        for sample in matching[:8]:
            line = compact_sample(sample)
            if line:
                style_evidence.append(line)
            text_sample = str(sample.get("text") or sample.get("ariaLabel") or "").strip()
            if text_sample and text_sample not in content_samples:
                content_samples.append(text_sample[:120])
        missing = [] if style_evidence else [f"{name} computed style evidence was not captured."]
        result[name] = {
            "style_evidence": style_evidence,
            "content_samples": content_samples[:4],
            "missing_evidence": missing,
        }

    state_lines = []
    for state in states[:8]:
        if not isinstance(state, dict):
            continue
        if is_unusable_component_dict(state):
            continue
        hover = state.get("hover_changed") if isinstance(state.get("hover_changed"), dict) else {}
        focus = state.get("focus_changed") if isinstance(state.get("focus_changed"), dict) else {}
        if not hover and not focus:
            continue
        label = str(state.get("text") or state.get("sampleId") or "interactive sample").strip()[:80]
        state_lines.append(f"{state.get('category', 'Component')} {label} | hover={hover} | focus={focus}")
    result["Feedback state"] = {
        "style_evidence": state_lines,
        "content_samples": [],
        "missing_evidence": [] if state_lines else ["Hover/focus computed-state deltas were not observed or did not change."],
    }
    return result


def is_unusable_component_sample(value: str) -> bool:
    lowered = value.lower()
    if re.search(r"\d+(?:\.\d+)?e[+-]\d+", lowered):
        return True
    if re.search(r"autofill|consent|cookie|onetrust|ot-sdk|hs-banner|hs-modal|recaptcha|captcha", lowered):
        return True
    return False


def component_entry(
    text: str,
    style_labels: list[str],
    content_labels: list[str] | None = None,
    missing_note: str = "Missing explicit component style evidence.",
) -> dict[str, list[str]]:
    style: list[str] = []
    content: list[str] = []
    for label in style_labels:
        style.extend(line_values(text, label))
    for label in content_labels or []:
        content.extend(line_values(text, label))
    missing = [] if style else [missing_note]
    return {
        "style_evidence": style,
        "content_samples": content[:4],
        "missing_evidence": missing,
    }


def merge_component_entries(primary: dict[str, dict[str, list[str]]], fallback: dict[str, dict[str, list[str]]]) -> dict[str, dict[str, list[str]]]:
    merged = fallback
    for name, values in primary.items():
        current = merged.setdefault(name, {"style_evidence": [], "content_samples": [], "missing_evidence": []})
        current["style_evidence"] = list(dict.fromkeys(values.get("style_evidence", []) + current.get("style_evidence", [])))[:10]
        current["content_samples"] = list(dict.fromkeys(values.get("content_samples", []) + current.get("content_samples", [])))[:6]
        current["missing_evidence"] = values.get("missing_evidence", []) if values.get("missing_evidence") else []
    return merged


def component_style_summary(text: str, lib: Path | None = None) -> dict[str, dict[str, list[str]]]:
    fallback = {
        "Navigation": component_entry(
            text,
            ["Density", "Header/hero/section spacing", "First viewport structure"],
            ["Navigation", "Navigation samples"],
            "Navigation spacing/density is not explicitly measured; use screenshot before implementation.",
        ),
        "Button": component_entry(
            text,
            ["Button/input/control density"],
            ["Buttons/links"],
            "Button size, padding, border, and state styling are not explicitly measured.",
        ),
        "Card": component_entry(
            text,
            ["Surface/background system", "Borders/dividers/radii", "Shadow/depth/material", "Observed border radii", "Shape", "Shadow/depth"],
            ["Cards/sections"],
            "Card surface, border, radius, and elevation evidence is incomplete.",
        ),
        "Form": component_entry(
            text,
            ["Button/input/control density", "Forms/inputs"],
            [],
            "Form/input style evidence is missing or not classified.",
        ),
        "Feedback state": component_entry(
            text,
            ["Feedback states", "Micro-interactions"],
            [],
            "Hover/focus/loading/empty/error state styling is not fully captured.",
        ),
        "Icon": component_entry(
            text,
            ["Icon/illustration stroke style", "Illustration/icon style"],
            [],
            "Icon stroke/fill style evidence is missing.",
        ),
    }
    if not lib:
        return fallback
    return merge_component_entries(component_evidence_summary(text, lib), fallback)


def design_system_strength(system: dict[str, object]) -> str:
    palette = system.get("palette", {})
    colors = palette.get("colors", []) if isinstance(palette, dict) else []
    components = system.get("component_styles", {})
    useful_components = 0
    if isinstance(components, dict):
        useful_components = sum(
            1
            for values in components.values()
            if isinstance(values, dict) and values.get("style_evidence")
        )
    if len(colors) >= 2 and useful_components >= 3:
        return "strong"
    if len(colors) >= 2 and useful_components >= 2:
        return "medium"
    if colors or useful_components:
        return "weak"
    return "missing"


def build_design_system(reference: Path, lib: Path, text: str, meta: dict[str, object]) -> dict[str, object]:
    slug = slug_from_reference(reference)
    screenshot_rel = str(meta.get("evidence_screenshot", "")).strip()
    screenshot = lib / screenshot_rel if screenshot_rel else None
    pixels: list[tuple[int, int, int]] = []
    screenshot_note = "missing screenshot path"
    if screenshot and screenshot.exists():
        pixels, screenshot_note = parse_png_rgb(screenshot)
    explicit = explicit_colors(text)
    colors = nearest_palette(pixels)
    existing_hex = {item["hex"] for item in colors}
    for item in explicit:
        if item["hex"] not in existing_hex:
            colors.append(item)
            existing_hex.add(item["hex"])
    colors = colors[:16]
    system = {
        "slug": slug,
        "title": str(meta.get("title") or slug),
        "reference_path": f"references/{reference.name}",
        "evidence": {
            "screenshot": screenshot_rel,
            "screenshot_sampling": screenshot_note,
            "color_sources": ["screenshot pixel sample", "explicit reference or DOM color"],
            "component_sources": [
                "computed component style JSON",
                "Interaction And Components",
                "Style Tokens And Surface Grammar",
                "Visual System",
            ],
            "limits": section_lines(text, "Evidence Limits") or ["No explicit evidence limits recorded."],
        },
        "palette": {
            "colors": colors,
            "mood_keywords": list(meta.get("style_tags") or [])[:8],
        },
        "component_styles": component_style_summary(text, lib),
    }
    system["evidence_strength"] = design_system_strength(system)
    return system


def token_name(value: str, fallback: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return cleaned or fallback


def unique_token_name(base: str, seen: set[str]) -> str:
    name = base
    index = 2
    while name in seen:
        name = f"{base}-{index}"
        index += 1
    seen.add(name)
    return name


def first_style_value(component_styles: dict[str, object], pattern: str) -> str:
    regex = re.compile(pattern)
    for values in component_styles.values():
        if not isinstance(values, dict):
            continue
        for line in values.get("style_evidence", []):
            match = regex.search(str(line))
            if match:
                return match.group(1).strip()
    return "missing"


def apply_tokens(system: dict[str, object], motion_system: dict[str, object]) -> dict[str, object]:
    colors = system.get("palette", {}).get("colors", [])
    component_styles = system.get("component_styles", {})
    if not isinstance(component_styles, dict):
        component_styles = {}

    color_tokens: dict[str, object] = {}
    seen_colors: set[str] = set()
    if isinstance(colors, list):
        for index, item in enumerate(colors[:12], start=1):
            if not isinstance(item, dict):
                continue
            hex_value = str(item.get("hex") or "").strip()
            if not re.fullmatch(r"#[0-9a-fA-F]{6}", hex_value):
                continue
            role = token_name(str(item.get("role") or f"color-{index}"), f"color-{index}")
            name = unique_token_name(role, seen_colors)
            color_tokens[name] = {
                "$type": "color",
                "$value": hex_value,
                "$description": f"Source: {item.get('source', 'missing')}",
            }
    if not color_tokens:
        color_tokens["missing"] = {"$type": "color", "$value": "missing", "$description": "No color token could be extracted."}

    radius = first_style_value(component_styles, r"borderRadius=([^;|]+)")
    spacing = first_style_value(component_styles, r"(?:padding|gap)=([^;|]+)")
    shadow = first_style_value(component_styles, r"boxShadow=([^;|]+)")
    font_size = first_style_value(component_styles, r"fontSize=([^;|]+)")
    font_weight = first_style_value(component_styles, r"fontWeight=([^;|]+)")

    motion_tokens: dict[str, object] = {}
    for item in motion_system.get("items", []) if isinstance(motion_system.get("items"), list) else []:
        if not isinstance(item, dict):
            continue
        motion_id = token_name(str(item.get("id") or "motion"), "motion")
        duration = item.get("duration_ms", "missing")
        delay = item.get("delay_ms", "missing")
        motion_tokens[motion_id] = {
            "duration": {
                "$type": "duration",
                "$value": f"{duration}ms" if isinstance(duration, int) else "missing",
            },
            "delay": {
                "$type": "duration",
                "$value": f"{delay}ms" if isinstance(delay, int) else "missing",
            },
            "easing": {"$type": "cubicBezier", "$value": str(item.get("easing") or "missing")},
            "property": {"$type": "string", "$value": str(item.get("property") or "missing")},
            "trigger": {"$type": "string", "$value": str(item.get("trigger") or "missing")},
            "transform": {"$type": "string", "$value": str(item.get("to") or "missing")},
            "$description": str(item.get("description") or "missing"),
        }
    if not motion_tokens:
        motion_tokens["missing"] = {"duration": {"$type": "duration", "$value": "missing"}, "$description": "No motion token could be extracted."}

    return {
        "color": color_tokens,
        "type": {
            "body": {
                "fontSize": {"$type": "dimension", "$value": font_size},
                "fontWeight": {"$type": "fontWeight", "$value": font_weight},
            }
        },
        "spacing": {"component": {"$type": "dimension", "$value": spacing}},
        "radius": {"component": {"$type": "dimension", "$value": radius}},
        "shadow": {"component": {"$type": "shadow", "$value": shadow}},
        "motion": motion_tokens,
    }


def design_system_with_apply(system: dict[str, object], motion_system: dict[str, object]) -> dict[str, object]:
    upgraded = dict(system)
    upgraded["evidence"] = {
        **(system.get("evidence", {}) if isinstance(system.get("evidence"), dict) else {}),
        "palette": system.get("palette", {}),
        "component_styles": system.get("component_styles", {}),
        "motion": motion_system,
    }
    upgraded["apply"] = apply_tokens(system, motion_system)
    return upgraded


def css_var_name(name: str) -> str:
    return re.sub(r"[^a-z0-9-]+", "-", name.lower()).strip("-") or "token"


def variables_css(system: dict[str, object]) -> str:
    apply = system.get("apply") if isinstance(system.get("apply"), dict) else {}
    lines = [":root {"]
    for name, token in (apply.get("color", {}) if isinstance(apply.get("color"), dict) else {}).items():
        if isinstance(token, dict):
            value = token.get("$value", "missing")
            lines.append(f"  --ds-color-{css_var_name(str(name))}: {value};")
    for group_name, prefix in [("spacing", "spacing"), ("radius", "radius"), ("shadow", "shadow")]:
        group = apply.get(group_name)
        if isinstance(group, dict):
            for name, token in group.items():
                if isinstance(token, dict):
                    lines.append(f"  --ds-{prefix}-{css_var_name(str(name))}: {token.get('$value', 'missing')};")
    motion = apply.get("motion")
    if isinstance(motion, dict):
        for name, token in motion.items():
            if not isinstance(token, dict):
                continue
            duration = token.get("duration", {}).get("$value", "missing") if isinstance(token.get("duration"), dict) else "missing"
            delay = token.get("delay", {}).get("$value", "missing") if isinstance(token.get("delay"), dict) else "missing"
            easing = token.get("easing", {}).get("$value", "missing") if isinstance(token.get("easing"), dict) else "missing"
            lines.append(f"  --ds-motion-{css_var_name(str(name))}-duration: {duration};")
            lines.append(f"  --ds-motion-{css_var_name(str(name))}-delay: {delay};")
            lines.append(f"  --ds-motion-{css_var_name(str(name))}-easing: {easing};")
    lines.append("}")
    return "\n".join(lines) + "\n"


def tailwind_theme(system: dict[str, object]) -> dict[str, object]:
    apply = system.get("apply") if isinstance(system.get("apply"), dict) else {}
    colors: dict[str, str] = {}
    for name, token in (apply.get("color", {}) if isinstance(apply.get("color"), dict) else {}).items():
        if isinstance(token, dict) and token.get("$value") != "missing":
            colors[css_var_name(str(name))] = str(token.get("$value"))
    spacing = apply.get("spacing", {}).get("component", {}).get("$value", "missing") if isinstance(apply.get("spacing"), dict) else "missing"
    radius = apply.get("radius", {}).get("component", {}).get("$value", "missing") if isinstance(apply.get("radius"), dict) else "missing"
    shadow = apply.get("shadow", {}).get("component", {}).get("$value", "missing") if isinstance(apply.get("shadow"), dict) else "missing"
    extend: dict[str, object] = {"colors": colors}
    if spacing != "missing":
        extend["spacing"] = {"ds-component": spacing}
    if radius != "missing":
        extend["borderRadius"] = {"ds-component": radius}
    if shadow != "missing":
        extend["boxShadow"] = {"ds-component": shadow}
    return {"theme": {"extend": extend}}


def motion_presets_css(system: dict[str, object]) -> str:
    apply = system.get("apply") if isinstance(system.get("apply"), dict) else {}
    motion = apply.get("motion") if isinstance(apply.get("motion"), dict) else {}
    blocks: list[str] = []
    for name, token in motion.items():
        if not isinstance(token, dict) or name == "missing":
            continue
        class_name = css_var_name(str(name))
        prop = token.get("property", {}).get("$value", "all") if isinstance(token.get("property"), dict) else "all"
        transform = token.get("transform", {}).get("$value", "missing") if isinstance(token.get("transform"), dict) else "missing"
        lines = [
            f".ds-motion-{class_name} {{",
            f"  transition-property: {prop if prop != 'missing' else 'all'};",
            f"  transition-duration: var(--ds-motion-{class_name}-duration);",
            f"  transition-delay: var(--ds-motion-{class_name}-delay);",
            f"  transition-timing-function: var(--ds-motion-{class_name}-easing);",
        ]
        if transform != "missing":
            lines.append(f"  transform: {transform};")
        lines.extend(["}", ""])
        blocks.append("\n".join(lines))
    if not blocks:
        blocks.append("/* missing: no motion presets could be generated from evidence */\n")
    blocks.append("@media (prefers-reduced-motion: reduce) {\n  [class*=\"ds-motion-\"] {\n    transition-duration: 0ms !important;\n    animation-duration: 0ms !important;\n  }\n}\n")
    return "\n".join(blocks)


def palette_markdown(system: dict[str, object]) -> str:
    colors = system.get("palette", {}).get("colors", [])
    rows = "\n".join(
        f"| `{item['hex']}` | {item.get('role', '')} | {item.get('source', '')} | {item.get('share', '')} |"
        for item in colors
    ) or "| Missing | Missing Evidence | No color evidence extracted | |"
    return f"""# Color System: {system['title']}

## Observed Palette
| Color | Role | Source | Screenshot Share |
|---|---|---|---|
{rows}

## Mood Keywords
{markdown_list(system.get('palette', {}).get('mood_keywords', []))}

## Evidence
- Screenshot: {system['evidence']['screenshot']}
- Sampling: {system['evidence']['screenshot_sampling']}
- Sources: {', '.join(system['evidence']['color_sources'])}

## Missing Evidence
{markdown_list(system['evidence']['limits'])}

## Do Not Copy
- Do not copy proprietary brand palettes blindly; adapt roles, contrast, and proportions.
"""


def component_markdown(system: dict[str, object]) -> str:
    blocks = []
    for name, values in system.get("component_styles", {}).items():
        if not isinstance(values, dict):
            blocks.append(f"## {name}\n{markdown_list([str(values)])}")
            continue
        blocks.append(
            f"""## {name}

### Style Evidence
{markdown_list(values.get("style_evidence", []))}

### Content Samples
{markdown_list(values.get("content_samples", []))}

### Missing Evidence
{markdown_list(values.get("missing_evidence", []))}
"""
        )
    return f"""# Component Style System: {system['title']}

{chr(10).join(blocks)}

## Evidence
- Sources: {', '.join(system['evidence']['component_sources'])}

## Do Not Copy
- Preserve component roles and density; do not copy proprietary component names, icons, or claims.
"""


def moodboard_svg(system: dict[str, object]) -> str:
    colors = system.get("palette", {}).get("colors", [])[:12]
    swatches = []
    for index, item in enumerate(colors):
        x = 24 + (index % 6) * 112
        y = 92 + (index // 6) * 104
        swatches.append(
            f'<rect x="{x}" y="{y}" width="88" height="56" rx="6" fill="{item["hex"]}"/>'
            f'<text x="{x}" y="{y + 76}" font-size="11" fill="#111">{item["hex"]}</text>'
        )
    if not swatches:
        swatches.append('<text x="24" y="110" font-size="16" fill="#555">Missing color evidence</text>')
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="720" height="300" viewBox="0 0 720 300">
  <rect width="720" height="300" fill="#f7f7f5"/>
  <text x="24" y="38" font-family="Arial, sans-serif" font-size="20" font-weight="700" fill="#111">{system['title']}</text>
  <text x="24" y="62" font-family="Arial, sans-serif" font-size="12" fill="#555">Color moodboard from screenshot pixels and explicit color evidence</text>
  {''.join(swatches)}
</svg>
"""


def section_lines(text: str, name: str) -> list[str]:
    content = section(text, name)
    lines = []
    for line in content.splitlines():
        cleaned = line.strip().lstrip("- ").strip()
        if cleaned and not re.search(r"\btodo\b", cleaned, re.I):
            lines.append(cleaned)
    return lines


def excerpt(value: str, limit: int = 180) -> str:
    value = " ".join(clean_value(value).split())
    return value[:limit]


def component_json_path(text: str, slug: str) -> str:
    match = re.search(r"`?(assets/[^`\s]+component-styles\.json)`?", text)
    if match:
        return match.group(1)
    return f"assets/*-{slug}-component-styles.json"


def card_missing_evidence(strength: dict[str, str], design_system: dict[str, object]) -> list[str]:
    missing: list[str] = []
    labels = {
        "screenshot": "screenshot",
        "layout_spacing": "layout/spacing",
        "type_copy": "type/copy",
        "motion_code": "motion/code",
        "design_system": "design-system",
    }
    for key, label in labels.items():
        if strength.get(key) == "missing":
            missing.append(f"{label} evidence is missing")
        elif strength.get(key) == "weak":
            missing.append(f"{label} evidence is weak")
    components = design_system.get("component_styles", {})
    if not isinstance(components, dict) or not components:
        missing.append("component/state evidence is missing")
    for limit in design_system.get("evidence", {}).get("limits", []):
        if isinstance(limit, str) and limit and "no explicit evidence limits" not in limit.lower():
            missing.append(limit)
    return sorted(set(missing))


def measurable_style_dna(text: str, meta: dict[str, object], motion_system: dict[str, object], limit: int = 12) -> list[dict[str, str]]:
    candidates: list[tuple[str, str]] = []
    section_sources = [
        "Layout Geometry And Spacing",
        "Dimension And Ratio System",
        "Typography And Reading Rhythm",
        "Style Tokens And Surface Grammar",
        "Color, Material, And Contrast",
        "Motion Code And Runtime Evidence",
    ]
    for source in section_sources:
        for line in section_lines(text, source):
            if re.search(r"\d", line) and len(line) <= 220:
                candidates.append((line, source))
    for item in motion_system.get("items", []) if isinstance(motion_system.get("items"), list) else []:
        if not isinstance(item, dict):
            continue
        duration = item.get("duration_ms", "missing")
        easing = item.get("easing", "missing")
        trigger = item.get("trigger", "missing")
        role = item.get("selector_role", "component")
        if duration != "missing":
            candidates.append((f"{role} {trigger} motion uses {duration}ms {easing}", "motion.json"))
    page_scope = str(meta.get("page_scope") or "")
    if page_scope and re.search(r"\d", page_scope):
        candidates.append((f"Page scope contains measured qualifier: {page_scope}", "frontmatter.page_scope"))

    dna: list[dict[str, str]] = []
    seen: set[str] = set()
    for decision, source in candidates:
        decision = " ".join(decision.split()).strip("- ")
        if not decision or decision.lower() in seen:
            continue
        if not re.search(r"\d", decision):
            continue
        seen.add(decision.lower())
        dna.append({"decision": decision, "evidence_source": source})
        if len(dna) >= limit:
            break
    return dna


def build_card(reference: Path, lib: Path, dimensions: dict[str, str], design_system: dict[str, object], motion_system: dict[str, object]) -> dict[str, object]:
    text = reference.read_text(encoding="utf-8", errors="ignore")
    meta = parse_frontmatter(text)
    slug = slug_from_reference(reference)
    evidence_limits = section_lines(text, "Evidence Limits")
    if not evidence_limits:
        evidence_limits = ["No explicit evidence limits recorded."]
    title = str(meta.get("title") or slug)
    relative_reference = f"references/{reference.name}"
    selection = str(meta.get("community_signal") or excerpt(section(text, "Essence")) or "Selected from existing reference library.")
    strength = {
        "screenshot": screenshot_strength(meta, lib),
        "layout_spacing": evidence_strength(dimensions["layout_spacing"], "layout_spacing"),
        "type_copy": evidence_strength(dimensions["type_copy"], "type_copy"),
        "motion_code": evidence_strength(dimensions["motion_code"], "motion_code"),
        "design_system": str(design_system.get("evidence_strength") or "missing"),
    }
    return {
        "slug": slug,
        "title": title,
        "reference_path": relative_reference,
        "category_tags": list(meta.get("category_tags") or []),
        "style_tags": list(meta.get("style_tags") or []),
        "structure_tags": list(meta.get("structure_tags") or []),
        "motion_tags": list(meta.get("motion_tags") or []),
        "code_tags": list(meta.get("code_tags") or []),
        "page_scope": str(meta.get("page_scope") or ""),
        "best_for": list(meta.get("best_for") or []),
        "avoid_for": list(meta.get("avoid_for") or []),
        "evidence_strength": strength,
        "missing_evidence": card_missing_evidence(strength, design_system),
        "dna": measurable_style_dna(text, meta, motion_system),
        "component_json_path": component_json_path(text, slug),
        "dimension_paths": {
            "scene": f"dimensions/{slug}/scene.md",
            "layout_spacing": f"dimensions/{slug}/layout-spacing.md",
            "type_copy": f"dimensions/{slug}/type-copy.md",
            "color_surface": f"dimensions/{slug}/color-surface.md",
            "assets": f"dimensions/{slug}/assets.md",
            "motion_code": f"dimensions/{slug}/motion-code.md",
            "components_states": f"dimensions/{slug}/components-states.md",
        },
        "design_system_paths": {
            "tokens": f"design-systems/{slug}/tokens.json",
            "palette": f"design-systems/{slug}/palette.md",
            "motion": f"design-systems/{slug}/motion.json",
            "variables_css": f"design-systems/{slug}/variables.css",
            "tailwind_theme": f"design-systems/{slug}/tailwind.theme.json",
            "motion_presets": f"design-systems/{slug}/motion-presets.css",
            "moodboard": f"design-systems/{slug}/moodboard.svg",
            "component_styles": f"design-systems/{slug}/component-styles.md",
        },
        "selection_note": selection,
        "evidence_limits": evidence_limits,
    }


def references_for_args(args: argparse.Namespace, lib: Path) -> list[Path]:
    if args.reference:
        return [Path(args.reference).expanduser()]
    if args.all:
        return sorted((lib / "references").glob("*.md"))
    raise SystemExit("Use --reference PATH or --all")


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def build_outputs(reference: Path, lib: Path) -> tuple[dict[str, object], dict[str, str], dict[str, object], dict[str, object]]:
    text = reference.read_text(encoding="utf-8", errors="ignore")
    meta = parse_frontmatter(text)
    dimensions = {name: dimension_markdown(name, text, meta) for name in DIMENSIONS}
    design_system = build_design_system(reference, lib, text, meta)
    motion_system = build_motion_system(reference, lib, text, meta)
    design_system = design_system_with_apply(design_system, motion_system)
    limits = section(text, "Avoid Copying") or "Brand identity, proprietary assets, product names, claims, and exact copy."
    dimensions["motion_code"] = motion_code_markdown(motion_system, limits)
    card = build_card(reference, lib, dimensions, design_system, motion_system)
    return card, dimensions, design_system, motion_system


def update_indexes(lib: Path) -> None:
    cards_dir = lib / "indexes" / "cards"
    cards = []
    facets: dict[str, dict[str, int]] = {
        "category_tags": {},
        "style_tags": {},
        "structure_tags": {},
        "motion_tags": {},
        "code_tags": {},
        "page_scope": {},
    }
    for path in sorted(cards_dir.glob("*.json")):
        card = json.loads(path.read_text(encoding="utf-8"))
        cards.append({
            "slug": card["slug"],
            "title": card["title"],
            "reference_path": card["reference_path"],
            "card_path": f"indexes/cards/{path.name}",
            "design_system_paths": card.get("design_system_paths", {}),
        })
        for key in ["category_tags", "style_tags", "structure_tags", "motion_tags", "code_tags"]:
            for value in card.get(key, []):
                facets[key][value] = facets[key].get(value, 0) + 1
        scope = card.get("page_scope", "")
        if scope:
            facets["page_scope"][scope] = facets["page_scope"].get(scope, 0) + 1
    write_json(lib / "indexes" / "manifest.json", {"cards": cards, "total_cards": len(cards)})
    write_json(lib / "indexes" / "facets.json", facets)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build progressive designstyle cards and dimension summaries.")
    parser.add_argument("--library", default=str(LIB))
    parser.add_argument("--reference")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    lib = Path(args.library).expanduser()
    refs = references_for_args(args, lib)
    planned_dimensions = 0
    cards = []
    for ref in refs:
        if not ref.exists():
            raise SystemExit(f"Reference not found: {ref}")
        card, dimensions, design_system, motion_system = build_outputs(ref, lib)
        cards.append(card)
        planned_dimensions += len(dimensions)
        if args.dry_run:
            continue
        slug = str(card["slug"])
        write_json(lib / "indexes" / "cards" / f"{slug}.json", card)
        dim_dir = lib / "dimensions" / slug
        dim_dir.mkdir(parents=True, exist_ok=True)
        for key, content in dimensions.items():
            filename = DIMENSIONS[key]["file"]
            (dim_dir / filename).write_text(content, encoding="utf-8")
        system_dir = lib / "design-systems" / slug
        system_dir.mkdir(parents=True, exist_ok=True)
        write_json(system_dir / "tokens.json", design_system)
        write_json(system_dir / "motion.json", motion_system)
        (system_dir / "variables.css").write_text(variables_css(design_system), encoding="utf-8")
        write_json(system_dir / "tailwind.theme.json", tailwind_theme(design_system))
        (system_dir / "motion-presets.css").write_text(motion_presets_css(design_system), encoding="utf-8")
        (system_dir / "palette.md").write_text(palette_markdown(design_system), encoding="utf-8")
        (system_dir / "component-styles.md").write_text(component_markdown(design_system), encoding="utf-8")
        (system_dir / "moodboard.svg").write_text(moodboard_svg(design_system), encoding="utf-8")

    if not args.dry_run:
        update_indexes(lib)

    action = "dry_run" if args.dry_run else "wrote"
    print(f"{action} planned_cards={len(cards)} planned_dimensions={planned_dimensions}")
    for card in cards:
        print(f"- {card['slug']}: {card['reference_path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
