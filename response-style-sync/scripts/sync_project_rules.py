#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from shutil import copyfile
from typing import Any

BEGIN_MARKER = "<!-- BEGIN RESPONSE-STYLE-SYNC -->"
END_MARKER = "<!-- END RESPONSE-STYLE-SYNC -->"

PROFILE_TEMPLATE_MAP = {
    "response-style.profile.json": "response-style.profile.template.json",
    "agent-policy.profile.json": "agent-policy.profile.template.json",
    "llm-policy.profile.json": "llm-policy.profile.template.json",
}


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def asset_path(name: str) -> Path:
    return skill_root() / "assets" / name


def load_json(path: str | None) -> dict[str, Any] | None:
    if not path:
        return None
    file_path = Path(path).expanduser().resolve()
    if not file_path.exists():
        raise SystemExit(f"Profile file does not exist: {file_path}")
    data = json.loads(file_path.read_text())
    if not isinstance(data, dict):
        raise SystemExit(f"Profile must be a JSON object: {file_path}")
    return data


def value(profile: dict[str, Any], *keys: str, default: Any = None) -> Any:
    for key in keys:
        if key in profile:
            return profile[key]
    return default


def bullet_block(items: Any) -> str:
    if items is None:
        return "- not configured"
    if isinstance(items, dict):
        return "\n".join(f"- {key}: {value}" for key, value in items.items())
    if isinstance(items, list):
        return "\n".join(f"- {item}" for item in items)
    return f"- {items}"


def key_value_line(label: str, value: Any) -> str:
    return f"- {label}: {value}"


def section(title: str, lines: list[str]) -> str:
    return title + "\n" + "\n".join(lines)


def render_style_block(profile: dict[str, Any] | None) -> str:
    if not profile:
        return "- not configured"
    tone = value(profile, "tone_tags", "tone", default=[])
    blocks = [
        section("### Summary", [
            key_value_line("Profile", value(profile, "profile_id", "profile_name", default="(unknown)")),
            key_value_line("Language mode", value(profile, "language_mode", "language_policy", default="(unknown)")),
            key_value_line("Detail level", value(profile, "detail_level", "verbosity", default="(unknown)")),
            key_value_line("Tone", ", ".join(tone) if isinstance(tone, list) else tone),
        ]),
        section("### Answer Principles", [bullet_block(value(profile, "answer_principles", "core_rules"))]),
        section("### Simple Answer Principles", [bullet_block(value(profile, "simple_answer_principles", "simple_answer_rules"))]),
        section("### Default Section Order", [bullet_block(value(profile, "default_section_order", "project_answer_order"))]),
        section("### Project Update Principles", [bullet_block(value(profile, "project_update_principles", "project_answer_rules"))]),
        section("### Formatting Preferences", [bullet_block(value(profile, "formatting_preferences", "formatting_rules"))]),
        section("### Avoid Patterns", [bullet_block(value(profile, "avoid_patterns", "avoid_rules"))]),
        section("### Verification Defaults", [bullet_block(value(profile, "verification_defaults", "verification_policy"))]),
        section("### Override Rules", [bullet_block(value(profile, "override_rules", "override_policy"))]),
        section("### Recommended Status Update Sections", [bullet_block(value(profile, "status_update_sections", "status_update_template"))]),
    ]
    return "\n\n".join(blocks)


def render_agent_block(profile: dict[str, Any] | None) -> str:
    if not profile:
        return "- not configured"
    blocks = [
        section("### Summary", [key_value_line("Profile", value(profile, "profile_id", "profile_name", default="(unknown)"))]),
        section("### Request Defaults", [bullet_block(value(profile, "request_defaults", "request_rules"))]),
        section("### Clarification Rules", [bullet_block(value(profile, "clarification_rules", "clarification_policy"))]),
        section("### Planning Rules", [bullet_block(value(profile, "planning_rules", "planning_policy"))]),
        section("### Parallel Rules", [bullet_block(value(profile, "parallel_rules", "parallel_policy"))]),
        section("### Scope Rules", [bullet_block(value(profile, "scope_rules", "scope_control"))]),
        section("### Persona Defaults", [bullet_block(value(profile, "persona_defaults", "persona"))]),
        section("### Execution Principles", [bullet_block(value(profile, "execution_principles", "review_policy"))]),
        section("### Override Rules", [bullet_block(value(profile, "override_rules", "override_policy"))]),
    ]
    return "\n\n".join(blocks)


def render_llm_block(profile: dict[str, Any] | None) -> str:
    if not profile:
        return "- not configured"
    blocks = [
        section("### Summary", [key_value_line("Profile", value(profile, "profile_id", "profile_name", default="(unknown)"))]),
        section("### Cloud API Rules", [bullet_block(value(profile, "cloud_api_rules", "cloud_api_policy"))]),
        section("### Proxy Rules", [bullet_block(value(profile, "proxy_rules", "proxy_policy"))]),
        section("### Preferred Proxies", [bullet_block(value(profile, "preferred_proxies", "preferred_proxy_repos"))]),
        section("### Proxy Selection Checks", [bullet_block(value(profile, "proxy_selection_checks", "proxy_selection_criteria"))]),
        section("### Research Rules", [bullet_block(value(profile, "research_rules", "research_policy"))]),
        section("### Compliance Rules", [bullet_block(value(profile, "compliance_rules", "compliance_policy"))]),
        section("### Override Rules", [bullet_block(value(profile, "override_rules", "override_policy"))]),
    ]
    return "\n\n".join(blocks)


def render_template(template_text: str, style: dict[str, Any] | None, agent: dict[str, Any] | None, llm: dict[str, Any] | None) -> str:
    return (
        template_text.replace("{{response_style_block}}", render_style_block(style))
        .replace("{{agent_policy_block}}", render_agent_block(agent))
        .replace("{{llm_policy_block}}", render_llm_block(llm))
    )


def extract_managed_block(rendered: str) -> str:
    start = rendered.index(BEGIN_MARKER)
    end = rendered.index(END_MARKER) + len(END_MARKER)
    return rendered[start:end]


def merge_into_existing(existing: str, managed_block: str) -> str:
    if BEGIN_MARKER in existing and END_MARKER in existing:
        start = existing.index(BEGIN_MARKER)
        end = existing.index(END_MARKER) + len(END_MARKER)
        return existing[:start] + managed_block + existing[end:]
    existing = existing.rstrip()
    if existing:
        return existing + "\n\n" + managed_block + "\n"
    return managed_block + "\n"


def sync_file(project_dir: Path, filename: str, style: dict[str, Any] | None, agent: dict[str, Any] | None, llm: dict[str, Any] | None) -> Path:
    template_text = asset_path(f"{filename}.template").read_text()
    rendered = render_template(template_text, style, agent, llm)
    managed_block = extract_managed_block(rendered)
    target = project_dir / filename
    if target.exists():
        target.write_text(merge_into_existing(target.read_text(), managed_block))
    else:
        target.write_text(rendered + "\n")
    return target


def init_bundle_dir(path: Path) -> list[Path]:
    path.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for output_name, template_name in PROFILE_TEMPLATE_MAP.items():
        target = path / output_name
        copyfile(asset_path(template_name), target)
        written.append(target)
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync project rules into AGENT.md / CLAUDE.md")
    parser.add_argument("--project", help="Project directory to update")
    parser.add_argument("--style-profile", help="Path to response-style profile JSON")
    parser.add_argument("--agent-policy", help="Path to agent-policy profile JSON")
    parser.add_argument("--llm-policy", help="Path to llm-policy profile JSON")
    parser.add_argument("--targets", default="AGENT.md,CLAUDE.md", help="Comma-separated target files")
    parser.add_argument("--init-bundle-dir", help="Write starter profile bundle to this directory and exit")
    args = parser.parse_args()

    if args.init_bundle_dir:
        written = init_bundle_dir(Path(args.init_bundle_dir).expanduser().resolve())
        print("Initialized rule bundle:")
        for path in written:
            print(f"- {path}")
        return 0

    if not args.project:
        parser.error("--project is required unless --init-bundle-dir is used")

    style = load_json(args.style_profile)
    agent = load_json(args.agent_policy)
    llm = load_json(args.llm_policy)
    if not any([style, agent, llm]):
        parser.error("At least one of --style-profile, --agent-policy, --llm-policy is required")

    project_dir = Path(args.project).expanduser().resolve()
    if not project_dir.exists():
        raise SystemExit(f"Project directory does not exist: {project_dir}")

    targets = [target.strip() for target in args.targets.split(",") if target.strip()]
    written = [sync_file(project_dir, target, style, agent, llm) for target in targets]
    print("Synced project rules to:")
    for path in written:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
