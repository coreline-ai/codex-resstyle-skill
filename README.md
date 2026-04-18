# codex-resstyle-skill

Reusable Codex skill package for managing three project rule profiles and syncing them into `AGENT.md` / `CLAUDE.md`.

## What this package manages

1. **Response style**
- language preference
- answer detail level
- default section order
- verification wording

2. **Agent execution policy**
- Korean-first interaction rules
- ask-before-proceed rules
- dev-plan-first workflow
- parallel-agent preference
- scope expansion restrictions
- persona / review posture

3. **LLM / proxy policy**
- cloud API restriction policy
- proxy-first planning
- preferred proxy repos such as `multi_model_tui`
- proxy selection checks
- compliance / cost guidance

## Included

- `response-style-sync/`
  - actual Codex skill folder
- `examples/`
  - `coreline-agent.response-style.json`
  - `coreline-agent.agent-policy.json`
  - `coreline-agent.llm-policy.json`
  - `coreline-agent.profile.json` (legacy style-only example)
- `FILE_DESIGN.md`
  - package file design and responsibility split
- `CHANGELOG.md`
  - package change history
- `LICENSE.md`
  - current distribution status for this package
- `validate.sh`
  - local smoke validation script
- `install.sh`
  - installs the skill into `${CODEX_HOME:-$HOME/.codex}/skills`
- `uninstall.sh`
  - removes the installed skill

## Key naming policy

This package now uses shorter, more consistent keys.

Examples:
- `profile_name` → `profile_id`
- `language_policy` → `language_mode`
- `verbosity` → `detail_level`
- `planning_policy` → `planning_rules`
- `cloud_api_policy` → `cloud_api_rules`

The sync script still accepts old keys for backward compatibility.

## Install

```bash
./install.sh
```

## Uninstall

```bash
./uninstall.sh
```

## Initialize a new 3-profile bundle

```bash
python3 response-style-sync/scripts/sync_project_rules.py   --init-bundle-dir ./.codex/rules
```

This creates:
- `response-style.profile.json`
- `agent-policy.profile.json`
- `llm-policy.profile.json`

## Sync into a project

```bash
python3 response-style-sync/scripts/sync_project_rules.py   --project /path/to/project   --style-profile /path/to/response-style.profile.json   --agent-policy /path/to/agent-policy.profile.json   --llm-policy /path/to/llm-policy.profile.json
```

## Backward-compatible style-only flow

```bash
python3 response-style-sync/scripts/sync_response_style.py   --init-profile ./.codex/response-style.profile.json

python3 response-style-sync/scripts/sync_response_style.py   --project /path/to/project   --profile /path/to/response-style.profile.json
```

## Example: apply bundled coreline profiles

```bash
python3 response-style-sync/scripts/sync_project_rules.py   --project /path/to/project   --style-profile ./examples/coreline-agent.response-style.json   --agent-policy ./examples/coreline-agent.agent-policy.json   --llm-policy ./examples/coreline-agent.llm-policy.json
```

## Validate before Git push

```bash
./validate.sh
```

What it checks:
- Python syntax
- starter bundle init
- AGENT.md / CLAUDE.md generation
- legacy style-only wrapper
- temp `CODEX_HOME` install smoke

## Recommended usage pattern

- Keep one rule bundle per project under `.codex/rules/`
- Generate both `AGENT.md` and `CLAUDE.md` from the same bundle
- Keep project-specific exceptions outside the managed sync block
- Add more presets later if needed, for example:
  - `concise-korean.response-style.json`
  - `review-heavy.agent-policy.json`
  - `proxy-first-strict.llm-policy.json`

## Git distribution note

`LICENSE.md` is currently a conservative placeholder (`All rights reserved until the owner picks a public license`).
Choose and replace it before publishing this package as open source.
