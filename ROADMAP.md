# ROADMAP

> This roadmap is a draft, not a promise.
> Priorities may change based on real usage feedback.

## Post-v0.1.0 priorities

### Short-term
#### 1. Profile validation and linting
- add optional JSON schema validation
- detect missing required sections before sync
- report deprecated legacy keys with warnings instead of silent compatibility only

#### 2. Better profile presets
- ship reusable presets such as:
  - concise-korean
  - release-reporting
  - review-heavy
  - proxy-first-strict

#### 3. Improved generated output controls
- allow selective sync targets
- allow partial section disable/enable
- improve managed block customization

## Mid-term
### 4. Project-level overrides
- support a shared base profile plus per-repo override files
- keep overrides explicit and easy to diff

### 5. More output targets
- evaluate support for additional rule files beyond:
  - `AGENT.md`
  - `CLAUDE.md`
- keep the default path simple while making target expansion optional

### 6. Better release/validation automation
- add optional CI examples for validate checks
- document release flow for tags and GitHub releases

## Stretch
### 7. Marketplace-ready packaging
- package metadata refinement for broader skill distribution
- publishing checklist and example release workflow

### 8. Richer policy composition
- compose multiple policy bundles safely
- support organization-level baseline + project-level override

### 9. Guided bootstrap flow
- interactive starter generation for new repositories
- suggested presets based on project type

## Out of scope for now
- automatic cloud API integration
- proxy implementation bundling
- hard dependency on one specific hosting platform
