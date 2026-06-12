#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SKILL_NAMES = ("designstyle", "add-designstyle", "use-designstyle")
AGENT_SKILL_DIRS = {
    "codex": Path.home() / ".codex" / "skills",
    "claude": Path.home() / ".claude" / "skills",
    "opencode": Path.home() / ".config" / "opencode" / "skills",
    "openclaw": Path.home() / ".openclaw" / "skills",
}
DEFAULT_LIBRARY = Path(
    os.environ.get("DESIGNSTYLE_LIBRARY", str(Path.home() / ".codex" / "designstyle-library"))
)


def copy_dir(source: Path, target: Path, *, dry_run: bool) -> None:
    if not source.exists():
        raise FileNotFoundError(f"Missing source: {source}")
    print(f"{'Would copy' if dry_run else 'Copying'} {source} -> {target}")
    if dry_run:
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target, dirs_exist_ok=True)


def selected_agents(value: str) -> list[str]:
    if value == "all":
        return list(AGENT_SKILL_DIRS)
    agents = [item.strip().lower() for item in value.split(",") if item.strip()]
    unknown = [agent for agent in agents if agent not in AGENT_SKILL_DIRS]
    if unknown:
        names = ", ".join(sorted(AGENT_SKILL_DIRS))
        raise argparse.ArgumentTypeError(f"Unknown agent(s): {', '.join(unknown)}. Use: {names}, all")
    return agents


def main() -> int:
    parser = argparse.ArgumentParser(description="Install MyDesign DesignStyle skills and material library.")
    parser.add_argument(
        "--agent",
        default="codex",
        help="Agent target: codex, claude, opencode, openclaw, comma-separated list, or all. Default: codex.",
    )
    parser.add_argument(
        "--library-path",
        default=str(DEFAULT_LIBRARY),
        help="Where to copy designstyle-library. Default: DESIGNSTYLE_LIBRARY or ~/.codex/designstyle-library.",
    )
    parser.add_argument("--skills-only", action="store_true", help="Install skills without copying the material library.")
    parser.add_argument("--library-only", action="store_true", help="Copy the material library without installing skills.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned copies without writing files.")
    args = parser.parse_args()

    agents = selected_agents(args.agent)
    library_path = Path(args.library_path).expanduser()

    if args.skills_only and args.library_only:
        parser.error("--skills-only and --library-only cannot be used together")

    if not args.library_only:
        for agent in agents:
            target_root = AGENT_SKILL_DIRS[agent]
            for skill_name in SKILL_NAMES:
                copy_dir(ROOT / "skills" / skill_name, target_root / skill_name, dry_run=args.dry_run)

    if not args.skills_only:
        copy_dir(ROOT / "designstyle-library", library_path, dry_run=args.dry_run)

    print("\nDone.")
    print(f"Library path: {library_path}")
    print("Set DESIGNSTYLE_LIBRARY to this path if your agent does not use the default Codex location.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
