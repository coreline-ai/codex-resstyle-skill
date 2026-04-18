---
name: response-style-sync
description: Create, refine, and sync project response style, agent execution rules, and LLM/proxy usage policy into AGENT.md and CLAUDE.md from reusable JSON profiles. Use when the user wants to standardize Korean-first answers, force dev-plan-first workflows, require clarification before risky decisions, block default cloud API usage, prefer proxies such as multi_model_tui, or keep AGENT.md / CLAUDE.md aligned with a shared project rule set across repositories.
---

# Response Style Sync

## Overview

Use this skill to manage project rules as reusable JSON profiles and sync them into `AGENT.md` / `CLAUDE.md`.
The skill supports three separate policy layers:
- response style
- agent execution policy
- LLM / proxy usage policy

## Quick workflow

1. Read any existing project rule sources.
- Check user instructions from the conversation.
- Read existing `AGENT.md`, `CLAUDE.md`, or other rule files if they exist.
- Extract stable defaults, not one-off task requests.

2. Create or update the three profiles.
- `response-style.profile.json`
- `agent-policy.profile.json`
- `llm-policy.profile.json`
- Recommended path: `<project>/.codex/rules/`

3. Sync the project files.
- Run `scripts/sync_project_rules.py --project <path> --style-profile ... --agent-policy ... --llm-policy ...`
- By default this updates both `AGENT.md` and `CLAUDE.md`.
- The script preserves content outside the managed block when files already exist.

4. Keep rules operational.
- Write short rules another agent can follow.
- Prefer explicit behavior over slogans.
- Keep style, workflow, and LLM-cost policy separate.

## Key naming convention

Use the new shorter keys by default:
- `profile_id`
- `language_mode`
- `detail_level`
- `planning_rules`
- `cloud_api_rules`

The script still accepts older aliases such as `profile_name`, `language_policy`, or `planning_policy` for backward compatibility.

## Profile split

### response-style profile
Use for:
- Korean-first or match-user language behavior
- answer structure
- detail level and tone
- verification reporting style
- formatting preferences

### agent-policy profile
Use for:
- ask-before-proceed rules
- dev-plan-first workflow
- parallel-agent preference
- scope expansion restrictions
- persona and review stance

### llm-policy profile
Use for:
- cloud API restriction policy
- proxy-first rules
- preferred repos such as `multi_model_tui`
- latest OSS proxy research checklist
- cost / compatibility / compliance notes

## Managed-file policy

The sync script uses a managed block:
- `<!-- BEGIN RESPONSE-STYLE-SYNC -->`
- `<!-- END RESPONSE-STYLE-SYNC -->`

Keep generated rules inside this block.
Keep project-specific exceptions outside it.

## Recommended extras to propose

If the user asks for a project rule system, also suggest these:

1. One profile bundle per repo
- Keep the three JSON files under `.codex/rules/`.

2. Presets
- Add `concise`, `standard`, `detailed`, `review-heavy`, or `release-mode` presets.

3. Escalation thresholds
- Define exactly when the agent must ask before proceeding:
  - destructive changes
  - cost-bearing cloud calls
  - architecture changes
  - unclear scope

4. Proxy selection checklist
- Evaluate compatibility, streaming, tool history, hosted tools, auth, logging, and human-input behavior before choosing a proxy.

5. Conflict policy
- State that higher-priority system/developer rules override project files.
- State that direct current-turn user requests override project defaults.

## Resources

### scripts/
- `sync_project_rules.py`
  - Initialize a starter 3-profile bundle.
  - Render and sync `AGENT.md` / `CLAUDE.md`.
  - Preserve non-managed file content when possible.
- `sync_response_style.py`
  - Backward-compatible wrapper for style-only usage.

### references/
- `style-profile-schema.md`
- `agent-policy-schema.md`
- `llm-policy-schema.md`
- `proxy-selection-checklist.md`

### assets/
- `response-style.profile.template.json`
- `agent-policy.profile.template.json`
- `llm-policy.profile.template.json`
- `AGENT.md.template`
- `CLAUDE.md.template`

## Minimal validation

After editing the profiles or templates:
- run `python3 scripts/sync_project_rules.py --init-bundle-dir <tmp/rules>` once
- run `python3 scripts/sync_project_rules.py --project <tmp/project> --style-profile ... --agent-policy ... --llm-policy ...`
- inspect generated `AGENT.md` and `CLAUDE.md`
- run the legacy wrapper once to confirm backward compatibility
- run `../../validate.sh` from the package root before Git push
