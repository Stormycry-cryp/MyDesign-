#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path
import os


LIB = Path(os.environ.get("DESIGNSTYLE_LIBRARY", str(Path.home() / ".codex" / "designstyle-library")))
HERE = Path(__file__).resolve().parent
BUILD = HERE / "build_progressive_reference.py"
CLEAN = HERE / "clean_reference_noise.py"
VALIDATE = HERE / "validate_progressive_library.py"
SCORE = HERE / "score_reference_quality.py"
BACKFILL_L3 = HERE / "backfill_reference_l3.py"


def references(lib: Path, limit: int | None) -> list[Path]:
    refs = sorted((lib / "references").glob("*.md"))
    return refs[:limit] if limit is not None else refs


def run_step(cmd: list[str], dry_run: bool) -> dict[str, object]:
    if dry_run:
        return {"status": "planned", "command": cmd, "returncode": 0, "stdout": "", "stderr": ""}
    result = subprocess.run(cmd, text=True, capture_output=True)
    return {
        "status": "ok" if result.returncode == 0 else "partial",
        "command": cmd,
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }


def write_report(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Backfill progressive DesignStyle layers for existing references.")
    parser.add_argument("--library", default=str(LIB))
    parser.add_argument("--limit", type=int)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--report", default=f"reviews/{date.today().isoformat()}-progressive-backfill.json")
    args = parser.parse_args()

    lib = Path(args.library).expanduser()
    refs = references(lib, args.limit)
    mode = "dry-run" if args.dry_run else "write"
    steps: list[dict[str, object]] = []

    if args.dry_run:
        for ref in refs:
            steps.append(
                {
                    "status": "planned",
                    "reference": str(ref),
                    "command": [sys.executable, str(BUILD), "--reference", str(ref), "--library", str(lib)],
                }
            )
    else:
        clean = run_step([sys.executable, str(CLEAN), "--library", str(lib)], dry_run=False)
        steps.append({"name": "clean_reference_noise", **clean})
        l3 = run_step([sys.executable, str(BACKFILL_L3), "--library", str(lib)], dry_run=False)
        steps.append({"name": "backfill_reference_l3", **l3})
        for ref in refs:
            result = run_step([sys.executable, str(BUILD), "--reference", str(ref), "--library", str(lib)], dry_run=False)
            steps.append({"name": "build_progressive_reference", "reference": str(ref), **result})
        validate = run_step([sys.executable, str(VALIDATE), "--library", str(lib), "--json"], dry_run=False)
        steps.append({"name": "validate_progressive_library", **validate})
        score = run_step([sys.executable, str(SCORE), "--library", str(lib)], dry_run=False)
        steps.append({"name": "score_reference_quality", **score})

    partial = [step for step in steps if step.get("status") == "partial" or step.get("returncode") not in {None, 0}]
    payload = {
        "mode": mode,
        "library": str(lib),
        "planned": len(refs),
        "status": "partial" if partial else "ok",
        "partial_count": len(partial),
        "steps": steps,
    }
    if not args.dry_run:
        write_report(lib / args.report, payload)

    print(f"mode={mode} planned={len(refs)} status={payload['status']} partial={len(partial)}")
    if not args.dry_run:
        print(lib / args.report)
    for step in partial[:12]:
        name = step.get("name") or Path(str(step.get("reference", ""))).name or "step"
        stderr = str(step.get("stderr") or "").strip().splitlines()
        stdout = str(step.get("stdout") or "").strip().splitlines()
        note = (stderr or stdout or ["partial"])[-1]
        print(f"partial: {name}: {note[:240]}")
    return 0 if not partial else 1


if __name__ == "__main__":
    raise SystemExit(main())
