#!/usr/bin/env bash
set -euo pipefail
DEST="${CODEX_HOME:-$HOME/.codex}/skills/response-style-sync"
rm -rf "$DEST"
echo "Removed $DEST"
