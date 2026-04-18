#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST_BASE="${CODEX_HOME:-$HOME/.codex}/skills"
DEST="$DEST_BASE/response-style-sync"
mkdir -p "$DEST_BASE"
rm -rf "$DEST"
cp -R "$ROOT/response-style-sync" "$DEST"
echo "Installed response-style-sync to $DEST"
