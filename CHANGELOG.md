# Changelog

## [v0.1.0] - 2026-04-18

### Added
- 3-profile rule bundle structure for response style, agent execution policy, and llm/proxy policy.
- `sync_project_rules.py` for multi-profile sync into `AGENT.md` / `CLAUDE.md`.
- `FILE_DESIGN.md` documenting package structure and profile ownership.
- `validate.sh` for local smoke validation before push or release.
- Git distribution helper files: `.gitignore`, `CHANGELOG.md`, `LICENSE.md`.
- Example profiles for `coreline-agent`.

### Changed
- Refined profile keys to a shorter and more consistent naming scheme.
- Kept backward compatibility for older key names in sync scripts.
- Expanded README with installation, validation, release, and Git distribution guidance.
