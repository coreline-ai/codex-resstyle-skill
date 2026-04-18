# codex-resstyle-skill file design

## 목적
`codex-resstyle-skill`은 프로젝트 규칙을 3개 프로필로 나누어 관리하고, 이를 `AGENT.md` / `CLAUDE.md`에 동기화하는 패키지다.

## 최상위 구조

```text
codex-resstyle-skill/
├── README.md
├── FILE_DESIGN.md
├── CHANGELOG.md
├── LICENSE.md
├── RELEASE_NOTES_v0.1.0.md
├── ROADMAP.md
├── .gitignore
├── validate.sh
├── install.sh
├── uninstall.sh
├── examples/
│   ├── coreline-agent.response-style.json
│   ├── coreline-agent.agent-policy.json
│   ├── coreline-agent.llm-policy.json
│   └── coreline-agent.profile.json
└── response-style-sync/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/
    │   ├── response-style.profile.template.json
    │   ├── agent-policy.profile.template.json
    │   ├── llm-policy.profile.template.json
    │   ├── AGENT.md.template
    │   └── CLAUDE.md.template
    ├── references/
    │   ├── style-profile-schema.md
    │   ├── agent-policy-schema.md
    │   ├── llm-policy-schema.md
    │   └── proxy-selection-checklist.md
    └── scripts/
        ├── sync_project_rules.py
        └── sync_response_style.py
```

## 프로필 분리 원칙

### 1) response-style profile
답변 형식과 표현 방식만 관리한다.

주요 키:
- `profile_id`
- `language_mode`
- `detail_level`
- `tone_tags`
- `answer_principles`
- `simple_answer_principles`
- `default_section_order`
- `project_update_principles`
- `formatting_preferences`
- `avoid_patterns`
- `verification_defaults`
- `override_rules`
- `status_update_sections`

### 2) agent-policy profile
작업 방식과 개발 실행 규칙을 관리한다.

주요 키:
- `profile_id`
- `request_defaults`
- `clarification_rules`
- `planning_rules`
- `parallel_rules`
- `scope_rules`
- `persona_defaults`
- `execution_principles`
- `override_rules`

### 3) llm-policy profile
모델/비용/프록시/조사 규칙을 관리한다.

주요 키:
- `profile_id`
- `cloud_api_rules`
- `proxy_rules`
- `preferred_proxies`
- `proxy_selection_checks`
- `research_rules`
- `compliance_rules`
- `override_rules`

## 구 키 호환 정책
- 새 키 이름을 기본 스키마로 사용한다.
- 기존 키(`profile_name`, `language_policy`, `planning_policy` 등)는 읽기 호환만 유지한다.
- README / examples / templates / schema 문서는 새 키 이름 기준으로 설명한다.
- style-only wrapper는 계속 지원한다.

## 스크립트 설계

### `sync_project_rules.py`
주 동기화 스크립트다.

역할:
- 3개 프로필 읽기
- 구/신 키 alias 해석
- `AGENT.md` / `CLAUDE.md` 템플릿 렌더링
- managed block만 교체
- 기존 수동 문구 보존
- starter bundle 초기화

핵심 옵션:
- `--project`
- `--style-profile`
- `--agent-policy`
- `--llm-policy`
- `--targets`
- `--init-bundle-dir`

### `sync_response_style.py`
기존 단일 스타일 프로필 사용자용 호환 wrapper다.

역할:
- `--init-profile`
- `--project --profile`
를 받아 내부적으로 `sync_project_rules.py`의 style-only 경로를 호출한다.

## Git 배포용 마감 파일
- `.gitignore`: Python cache / macOS metadata / temp files 제외
- `CHANGELOG.md`: 패키지 변경 이력
- `LICENSE.md`: MIT 라이선스
- `RELEASE_NOTES_v0.1.0.md`: GitHub Release 본문 초안
- `ROADMAP.md`: `v0.1.0` 이후 우선순위 초안
- `validate.sh`: init / sync / install smoke 검증

## 추천 확장 포인트
- preset 디렉터리 추가
- 프로젝트별 override 파일 지원
- JSON schema 검증 추가
- `.claude/commands/`용 보조 명령 생성
