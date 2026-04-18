#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from shutil import copyfile


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def asset_path(name: str) -> Path:
    return skill_root() / "assets" / name


def project_sync_script() -> Path:
    return skill_root() / "scripts" / "sync_project_rules.py"


def init_profile(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    copyfile(asset_path("response-style.profile.template.json"), path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Backward-compatible response-style sync wrapper")
    parser.add_argument("--project", help="Project directory to update")
    parser.add_argument("--profile", help="Path to response-style profile JSON")
    parser.add_argument("--targets", default="AGENT.md,CLAUDE.md", help="Comma-separated target files")
    parser.add_argument("--init-profile", help="Write a starter style profile template to this path and exit")
    args = parser.parse_args()

    if args.init_profile:
        output = Path(args.init_profile).expanduser().resolve()
        init_profile(output)
        print(f"Initialized profile template at {output}")
        return 0

    if not args.project or not args.profile:
        parser.error("--project and --profile are required unless --init-profile is used")

    cmd = [
        sys.executable,
        str(project_sync_script()),
        "--project",
        args.project,
        "--style-profile",
        args.profile,
        "--targets",
        args.targets,
    ]
    return subprocess.call(cmd)


if __name__ == "__main__":
    raise SystemExit(main())
