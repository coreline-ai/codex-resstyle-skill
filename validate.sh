#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

python3 -m py_compile   response-style-sync/scripts/sync_project_rules.py   response-style-sync/scripts/sync_response_style.py

tmp_bundle="$(mktemp -d)"
python3 response-style-sync/scripts/sync_project_rules.py --init-bundle-dir "$tmp_bundle" >/dev/null

tmp_project="$(mktemp -d)"
python3 response-style-sync/scripts/sync_project_rules.py   --project "$tmp_project"   --style-profile examples/coreline-agent.response-style.json   --agent-policy examples/coreline-agent.agent-policy.json   --llm-policy examples/coreline-agent.llm-policy.json >/dev/null

test -f "$tmp_project/AGENT.md"
test -f "$tmp_project/CLAUDE.md"

tmp_project2="$(mktemp -d)"
python3 response-style-sync/scripts/sync_response_style.py   --project "$tmp_project2"   --profile examples/coreline-agent.profile.json >/dev/null

test -f "$tmp_project2/AGENT.md"
test -f "$tmp_project2/CLAUDE.md"

tmp_home="$(mktemp -d)"
CODEX_HOME="$tmp_home" ./install.sh >/dev/null
python3 "$tmp_home/skills/response-style-sync/scripts/sync_project_rules.py"   --project "$(mktemp -d)"   --style-profile examples/coreline-agent.response-style.json   --agent-policy examples/coreline-agent.agent-policy.json   --llm-policy examples/coreline-agent.llm-policy.json >/dev/null

echo "validate.sh: OK"
