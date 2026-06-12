#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LIBRARY = Path.home() / ".codex" / "designstyle-library"
DEFAULT_QUERIES = ROOT / "references" / "search-regression-queries.json"
SEARCH = ROOT / "scripts" / "search_references.py"


def load_search_module():
    spec = importlib.util.spec_from_file_location("search_references", SEARCH)
    if not spec or not spec.loader:
        raise RuntimeError(f"Could not load {SEARCH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def top_results(search, cards: list[dict[str, object]], query: str, need: str, limit: int) -> list[dict[str, object]]:
    needs = search.parse_need(need)
    query_tokens = search.tokens(query) + search.need_tokens(needs)
    rows: list[tuple[int, dict[str, object], dict[str, int]]] = []
    for card in cards:
        if not search.scene_need_matches(card, needs):
            continue
        score, factors = search.card_score(query_tokens, card)
        if score > 0:
            rows.append((score, card, factors))
    rows.sort(key=lambda item: (-item[0], str(item[1].get("title"))))
    return [
        {
            "rank": index + 1,
            "score": score,
            "slug": card.get("slug"),
            "title": card.get("title"),
            "category_tags": card.get("category_tags") or [],
            "page_scope": card.get("page_scope") or "",
            "scene_gate_percent": factors.get("scene_gate_percent", 0),
        }
        for index, (score, card, factors) in enumerate(rows[:limit])
    ]


def contains_forbidden(card: dict[str, object] | None, terms: list[str]) -> bool:
    if not card:
        return False
    blob = json.dumps(
        {
            "slug": card.get("slug"),
            "title": card.get("title"),
            "category_tags": card.get("category_tags"),
            "page_scope": card.get("page_scope"),
        },
        ensure_ascii=False,
    ).lower()
    return any(term.lower() in blob for term in terms)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run DesignStyle search regression queries.")
    parser.add_argument("--library", default=str(DEFAULT_LIBRARY))
    parser.add_argument("--queries", default=str(DEFAULT_QUERIES))
    parser.add_argument("--json-output", default="")
    parser.add_argument("--top3-threshold", type=float, default=0.9)
    args = parser.parse_args()

    search = load_search_module()
    lib = Path(args.library).expanduser()
    queries = json.loads(Path(args.queries).read_text(encoding="utf-8"))
    cards = search.load_cards(lib)
    results = []
    top3_hits = 0
    wrong_top1 = 0

    for case in queries:
        top = top_results(search, cards, str(case["query"]), str(case.get("need") or ""), 5)
        top3_slugs = {str(item.get("slug")) for item in top[:3]}
        expected = {str(item) for item in case.get("expected_top3", [])}
        hit = bool(top3_slugs & expected)
        if hit:
            top3_hits += 1
        forbidden = contains_forbidden(top[0] if top else None, [str(item) for item in case.get("forbidden_top1_terms", [])])
        if forbidden:
            wrong_top1 += 1
        results.append(
            {
                "id": case.get("id"),
                "query": case.get("query"),
                "need": case.get("need"),
                "expected_top3": case.get("expected_top3", []),
                "top5": top,
                "top3_hit": hit,
                "wrong_top1": forbidden,
            }
        )

    total = len(results)
    top3_rate = top3_hits / total if total else 0
    payload = {
        "library": str(lib),
        "queries": total,
        "top3_hits": top3_hits,
        "top3_rate": round(top3_rate, 4),
        "wrong_top1": wrong_top1,
        "threshold": args.top3_threshold,
        "passed": top3_rate >= args.top3_threshold and wrong_top1 == 0,
        "results": results,
    }
    text = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.json_output:
        output = Path(args.json_output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0 if payload["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
