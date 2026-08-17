#!/usr/bin/env bash
# Publish the participant-facing subset of this folder to the public repo.
#
#   facilitator/publish.sh            # sync, leak-check, commit, push
#   facilitator/publish.sh --dry-run  # sync and leak-check only, then stop
#
# FACILITATOR ONLY. This folder is the only working copy. The public repo is a
# strict subset of it, cloned fresh into a temp directory each time and thrown
# away afterwards — so there is no second checkout to drift, and no way to edit
# the public copy by mistake.
#
# The public repo is PUBLIC. Everything excluded below is excluded because it
# would either spoil an exercise or embarrass us.

set -euo pipefail

REMOTE="${PUBLISH_REMOTE:-https://github.com/iorlas/ai-adoption-hc-data.git}"
BRANCH="master"
SUBDIR="data-analytics"

DRY_RUN=0
[[ "${1:-}" == "--dry-run" ]] && DRY_RUN=1

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/"

for tool in git rsync; do
  command -v "$tool" >/dev/null || { echo "error: $tool not found" >&2; exit 2; }
done

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "Cloning the public repo …"
git clone -q --depth 1 --branch "$BRANCH" "$REMOTE" "$TMP/repo"

DST="$TMP/repo/$SUBDIR/"
mkdir -p "$DST"

rsync -a --delete \
  --exclude 'facilitator/' \
  --exclude 'facilitator.md' \
  --exclude 'answers.md' \
  --exclude 'session-4/fallback/' \
  --exclude '.git/' \
  --exclude '.DS_Store' \
  --exclude '__pycache__/' \
  --exclude '.venv/' \
  "$SRC" "$DST"

# --- the safety net -------------------------------------------------------
# If any of these ever appear in the public copy, something leaked.
LEAKS=$(grep -rIl \
  -e 'FACILITATOR ONLY' \
  -e 'Answer key' \
  -e 'answer-key' \
  -e 'Never on screen' \
  "$DST" 2>/dev/null || true)

if [[ -n "$LEAKS" ]]; then
  echo "REFUSING: facilitator material found in the public copy:" >&2
  echo "$LEAKS" >&2
  exit 1
fi

echo "Clean — no facilitator material in the published subset."
echo

cd "$TMP/repo"

if [[ -z "$(git status --porcelain)" ]]; then
  echo "Nothing to publish — the public repo already matches."
  exit 0
fi

git --no-pager diff --stat
echo

if [[ "$DRY_RUN" -eq 1 ]]; then
  echo "--dry-run: stopping before commit. Nothing was pushed."
  exit 0
fi

git add -A
git commit -q -m "${PUBLISH_MSG:-Publish participant material}"
git push -q origin "$BRANCH"

echo "Pushed to the public repo ($BRANCH)."
