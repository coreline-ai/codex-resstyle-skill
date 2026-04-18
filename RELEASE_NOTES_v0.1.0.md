# codex-resstyle-skill v0.1.0

First public release of `codex-resstyle-skill`.

## Highlights
- Manage project defaults in three separate JSON profiles:
  - response style
  - agent execution policy
  - llm / proxy policy
- Sync the bundle into both `AGENT.md` and `CLAUDE.md`.
- Keep backward compatibility for legacy style-only usage.
- Include install / uninstall / local validate scripts for fast repository adoption.

## Included in this release
- `response-style-sync/` Codex skill folder
- JSON templates for all three profile types
- `coreline-agent` example profiles
- `sync_project_rules.py` multi-profile sync script
- `sync_response_style.py` legacy wrapper
- `validate.sh` local release check

## Validation
Release candidate validated with:
- Python syntax compile check
- starter bundle initialization
- generated `AGENT.md` / `CLAUDE.md` smoke test
- legacy style-only wrapper smoke test
- temporary `CODEX_HOME` install smoke test

## Recommended GitHub release body
Use the contents of this file as the initial GitHub release description for tag `v0.1.0`.
