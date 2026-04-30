<div align="center">

<img width="2752" height="1536" alt="AI 규칙 관리자 활용 가이드" src="https://github.com/user-attachments/assets/b01ca766-1c7d-4420-a9cc-69cba081043b" />

<img width="0" height="0" alt="똑똑한 프로젝트 규칙 관리 가이드" src="https://github.com/user-attachments/assets/a18ed235-f42b-4a7e-97c5-c0853cf5a579" />

# codex-resstyle-skill

[![Release](https://img.shields.io/github/v/release/coreline-ai/codex-resstyle-skill?display_name=tag)](https://github.com/coreline-ai/codex-resstyle-skill/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE.md)
[![Validate](https://img.shields.io/badge/validate-local%20script-blue)](#validate-before-release)

Reusable Codex skill package for managing three project rule profiles and syncing them into `AGENT.md` / `CLAUDE.md`.

**Current release:** `v0.1.0`

</div>

Quick links:
- [Release notes](./RELEASE_NOTES_v0.1.0.md)
- [Roadmap](./ROADMAP.md)
- [File design](./FILE_DESIGN.md)
- [License](./LICENSE.md)

---

## 한국어

### 소개
`codex-resstyle-skill`은 프로젝트별 규칙을 3개의 JSON 프로필로 관리하고, 이를 `AGENT.md` / `CLAUDE.md`에 동기화하는 Codex 스킬 패키지입니다.

관리 대상:
1. **답변 스타일**
- 언어 우선순위
- 답변 길이/밀도
- 기본 섹션 순서
- 검증 결과를 설명하는 방식

2. **에이전트 실행 규칙**
- 한국어 우선 응답
- 진행 전 확인이 필요한 상황 정의
- dev-plan 우선 워크플로우
- 병렬 에이전트 우선 전략
- 범위 확장 제한

3. **LLM / 프록시 정책**
- 클라우드 API 사용 제한 정책
- 프록시 우선 계획
- `multi_model_tui` 같은 우선 검토 프록시
- 프록시 선택 기준과 운영/비용 정책

### 포함 내용
- `response-style-sync/`
  - 실제 Codex skill 폴더
- `examples/`
  - `coreline-agent.response-style.json`
  - `coreline-agent.agent-policy.json`
  - `coreline-agent.llm-policy.json`
  - `coreline-agent.profile.json` (legacy style-only example)
- `FILE_DESIGN.md`
  - 파일 구조와 책임 분리 문서
- `CHANGELOG.md`
  - 변경 이력
- `RELEASE_NOTES_v0.1.0.md`
  - GitHub Release 본문 초안
- `ROADMAP.md`
  - v0.1.0 이후 roadmap 초안
- `validate.sh`
  - 로컬 smoke 검증 스크립트

### 키 네이밍 정책
이 패키지는 더 짧고 일관된 키 이름을 기본으로 사용합니다.

예:
- `profile_name` → `profile_id`
- `language_policy` → `language_mode`
- `verbosity` → `detail_level`
- `planning_policy` → `planning_rules`
- `cloud_api_policy` → `cloud_api_rules`

기존 키도 호환을 위해 계속 읽습니다.

### 설치
```bash
./install.sh
```

### 제거
```bash
./uninstall.sh
```

### 3-프로필 번들 초기화
```bash
python3 response-style-sync/scripts/sync_project_rules.py \
  --init-bundle-dir ./.codex/rules
```

생성 파일:
- `response-style.profile.json`
- `agent-policy.profile.json`
- `llm-policy.profile.json`

### 프로젝트에 동기화
```bash
python3 response-style-sync/scripts/sync_project_rules.py \
  --project /path/to/project \
  --style-profile /path/to/response-style.profile.json \
  --agent-policy /path/to/agent-policy.profile.json \
  --llm-policy /path/to/llm-policy.profile.json
```

### 기존 style-only 방식 호환
```bash
python3 response-style-sync/scripts/sync_response_style.py \
  --init-profile ./.codex/response-style.profile.json

python3 response-style-sync/scripts/sync_response_style.py \
  --project /path/to/project \
  --profile /path/to/response-style.profile.json
```

### 릴리즈 전 검증
```bash
./validate.sh
```

검증 내용:
- Python syntax 확인
- starter bundle init
- `AGENT.md` / `CLAUDE.md` 생성 smoke
- legacy style-only wrapper smoke
- temp `CODEX_HOME` 설치 smoke

### 권장 사용 방식
- 프로젝트별 규칙 번들은 `.codex/rules/` 아래에 둡니다.
- 같은 번들로 `AGENT.md`와 `CLAUDE.md`를 함께 생성합니다.
- 프로젝트별 예외 규칙은 managed block 바깥에 둡니다.
- 이후 필요하면 preset을 추가합니다.

---

## English

### Overview
`codex-resstyle-skill` is a reusable Codex skill package for managing project rules as three JSON profiles and syncing them into `AGENT.md` / `CLAUDE.md`.

What it manages:
1. **Response style**
- language preference
- answer detail level
- default section order
- verification wording

2. **Agent execution policy**
- Korean-first interaction defaults
- ask-before-proceed rules
- dev-plan-first workflow
- parallel-agent preference
- scope expansion restrictions

3. **LLM / proxy policy**
- cloud API restriction policy
- proxy-first planning
- preferred proxy repos such as `multi_model_tui`
- proxy selection checks and cost/compliance guidance

### Included
- `response-style-sync/`
  - actual Codex skill folder
- `examples/`
  - `coreline-agent.response-style.json`
  - `coreline-agent.agent-policy.json`
  - `coreline-agent.llm-policy.json`
  - `coreline-agent.profile.json` (legacy style-only example)
- `FILE_DESIGN.md`
  - file layout and ownership notes
- `CHANGELOG.md`
  - release history
- `RELEASE_NOTES_v0.1.0.md`
  - draft GitHub release body
- `ROADMAP.md`
  - post-v0.1.0 roadmap draft
- `validate.sh`
  - local smoke validation script

### Key naming policy
This package now uses shorter, more consistent keys.

Examples:
- `profile_name` → `profile_id`
- `language_policy` → `language_mode`
- `verbosity` → `detail_level`
- `planning_policy` → `planning_rules`
- `cloud_api_policy` → `cloud_api_rules`

Older keys are still accepted for backward compatibility.

### Install
```bash
./install.sh
```

### Uninstall
```bash
./uninstall.sh
```

### Initialize a new 3-profile bundle
```bash
python3 response-style-sync/scripts/sync_project_rules.py \
  --init-bundle-dir ./.codex/rules
```

This creates:
- `response-style.profile.json`
- `agent-policy.profile.json`
- `llm-policy.profile.json`

### Sync into a project
```bash
python3 response-style-sync/scripts/sync_project_rules.py \
  --project /path/to/project \
  --style-profile /path/to/response-style.profile.json \
  --agent-policy /path/to/agent-policy.profile.json \
  --llm-policy /path/to/llm-policy.profile.json
```

### Backward-compatible style-only flow
```bash
python3 response-style-sync/scripts/sync_response_style.py \
  --init-profile ./.codex/response-style.profile.json

python3 response-style-sync/scripts/sync_response_style.py \
  --project /path/to/project \
  --profile /path/to/response-style.profile.json
```

### Validate before release
```bash
./validate.sh
```

Validation covers:
- Python syntax
- starter bundle initialization
- `AGENT.md` / `CLAUDE.md` generation smoke
- legacy style-only wrapper smoke
- temporary `CODEX_HOME` install smoke

### Recommended usage pattern
- Keep one rule bundle per project under `.codex/rules/`
- Generate both `AGENT.md` and `CLAUDE.md` from the same bundle
- Keep project-specific exceptions outside the managed sync block
- Add presets later if needed
