#!/usr/bin/env bash
#
# dawdrive-ai-skills installer
#
# Skills in this repo live as categorised markdown files:
#     skills/<domain>/[<subdomain>/]<name>.md
#
# Claude Code expects each skill in its own directory:
#     ~/.claude/skills/<name>/SKILL.md
#
# This script does that mapping. It asks before every write, never overwrites
# without confirmation, and makes no network calls. Read it — that is the whole
# point of this repo.

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC_DIR="$REPO_DIR/skills"
DEST_DIR="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"

bold() { printf '\033[1m%s\033[0m\n' "$1"; }
dim()  { printf '\033[2m%s\033[0m\n' "$1"; }

confirm() {
  local prompt="$1" reply
  read -r -p "$prompt [y/N] " reply || return 1
  [[ "$reply" =~ ^[Yy]$ ]]
}

# Value of a top-level front-matter key, or empty.
frontmatter() {
  awk -v key="$2" '
    NR == 1 && $0 != "---" { exit }
    NR > 1 && $0 == "---"  { exit }
    index($0, key ":") == 1 { sub("^" key ": *", ""); print; exit }
  ' "$1"
}

if [[ ! -d "$SRC_DIR" ]]; then
  echo "error: no skills/ directory found at $SRC_DIR" >&2
  exit 1
fi

# Portable to bash 3.2 (macOS system bash) — no mapfile.
PATHS=()
while IFS= read -r line; do
  PATHS+=("$line")
done < <(find "$SRC_DIR" -type f -name '*.md' | sort)

if [[ ${#PATHS[@]:-0} -eq 0 ]]; then
  echo "error: no skills found in $SRC_DIR" >&2
  exit 1
fi

bold "dawdrive-ai-skills"
echo
echo "Source:      $SRC_DIR"
echo "Destination: $DEST_DIR"
echo
bold "Available skills:"
for path in "${PATHS[@]}"; do
  name="$(basename "$path" .md)"
  category="$(dirname "${path#"$SRC_DIR"/}")"
  desc="$(frontmatter "$path" description)"
  printf '  • %-20s [%s]\n' "$name" "$category"
  printf '    %s…\n' "${desc:0:88}"
done
echo
dim "This script only copies files. It makes no network calls and touches nothing outside $DEST_DIR."
echo

if ! confirm "Continue?"; then
  echo "Aborted. Nothing was written."
  exit 0
fi

mkdir -p "$DEST_DIR"
installed=0

for path in "${PATHS[@]}"; do
  name="$(basename "$path" .md)"
  target="$DEST_DIR/$name"

  echo
  bold "── $name"

  if confirm "Print it before installing?"; then
    echo
    cat "$path"
    echo
  fi

  if [[ -e "$target" ]]; then
    echo "  ! $target already exists."
    if ! confirm "  Overwrite it?"; then
      echo "  Skipped $name."
      continue
    fi
    rm -rf "${target:?}"
  fi

  if confirm "Install $name?"; then
    mkdir -p "$target"
    cp "$path" "$target/SKILL.md"
    echo "  ✓ installed to $target/SKILL.md"
    installed=$((installed + 1))
  else
    echo "  Skipped $name."
  fi
done

# Seed the intake log if skill-intake was installed and no log exists yet.
LOG="$DEST_DIR/INTAKE_LOG.md"
if [[ -d "$DEST_DIR/skill-intake" && ! -f "$LOG" && -f "$REPO_DIR/templates/INTAKE_LOG.md" ]]; then
  echo
  if confirm "Create an empty intake log at $LOG?"; then
    cp "$REPO_DIR/templates/INTAKE_LOG.md" "$LOG"
    echo "  ✓ created $LOG"
  fi
fi

echo
bold "Done — $installed skill(s) installed."
echo "Restart your Claude Code session to pick them up."
