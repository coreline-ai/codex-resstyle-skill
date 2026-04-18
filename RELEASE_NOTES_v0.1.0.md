# codex-resstyle-skill v0.1.0

First public release of `codex-resstyle-skill`.

## What this release is for
This release packages a reusable Codex skill workflow for teams that want to keep response style, execution rules, and LLM/proxy policy aligned across repositories.

Instead of hand-editing project guidance in multiple places, you can keep one rule bundle and sync it into both `AGENT.md` and `CLAUDE.md`.

## Highlights
- **Three-profile rule bundle**
  - response style
  - agent execution policy
  - llm / proxy policy
- **Two-file sync target**
  - generate both `AGENT.md` and `CLAUDE.md` from the same bundle
- **Backward compatibility**
  - legacy style-only flow still works through `sync_response_style.py`
- **Repository-ready packaging**
  - install / uninstall scripts
  - local validation script
  - example profiles
  - release and roadmap docs

## Included in v0.1.0
- `response-style-sync/` Codex skill folder
- JSON templates for all three profile types
- `coreline-agent` example profiles
- `sync_project_rules.py` multi-profile sync script
- `sync_response_style.py` legacy wrapper
- `validate.sh` local release check
- `FILE_DESIGN.md` for package structure and ownership

## Validation
Release candidate validated with:
- Python syntax compile check
- starter bundle initialization
- generated `AGENT.md` / `CLAUDE.md` smoke test
- legacy style-only wrapper smoke test
- temporary `CODEX_HOME` install smoke test

## Good fit
This release is a good fit if you want to:
- standardize response style across multiple repos
- keep Codex/Claude guidance synchronized
- encode dev-plan-first and proxy-first rules into project files
- maintain backward compatibility while moving to a 3-profile structure

## Next up
See [`ROADMAP.md`](./ROADMAP.md) for the post-`v0.1.0` draft roadmap.

## Suggested GitHub release title
`v0.1.0 — Initial public release`
