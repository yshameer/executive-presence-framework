#!/usr/bin/env bash
#
# Install the executive-presence skills for Claude Code, Codex, or both.
#
#   ./install.sh                  auto-detect which agents are set up, install for each
#   ./install.sh --claude         user scope, Claude Code only      (~/.claude/skills)
#   ./install.sh --codex          user scope, Codex only            (~/.agents/skills)
#   ./install.sh --project        this repo, both agents            (./.claude/skills, ./.agents/skills)
#   ./install.sh --dir PATH       install into an explicit directory
#   ./install.sh --coach-only     install the coaching skill, not the drill
#   ./install.sh --practice-only  install the drill skill, not the coach
#   ./install.sh --dry-run        print what would happen, change nothing
#
# Both skills are plain directories with a SKILL.md, which is the format Claude
# Code and Codex share. Installing is a copy; the only difference between the
# two agents is where the copy lands.

set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/skills"

CLAUDE_USER="$HOME/.claude/skills"
CODEX_USER="$HOME/.agents/skills"
CLAUDE_PROJECT=".claude/skills"
CODEX_PROJECT=".agents/skills"

SKILLS=(executive-presence executive-presence-practice)
TARGETS=()
DRY_RUN=0
MODE=""

die() { printf 'error: %s\n' "$1" >&2; exit 1; }

while [ $# -gt 0 ]; do
  case "$1" in
    --claude)        MODE="explicit"; TARGETS+=("$CLAUDE_USER") ;;
    --codex)         MODE="explicit"; TARGETS+=("$CODEX_USER") ;;
    --project)       MODE="explicit"; TARGETS+=("$CLAUDE_PROJECT" "$CODEX_PROJECT") ;;
    --dir)           shift; [ $# -gt 0 ] || die "--dir needs a path"; MODE="explicit"; TARGETS+=("$1") ;;
    --coach-only)    SKILLS=(executive-presence) ;;
    --practice-only) SKILLS=(executive-presence-practice) ;;
    --dry-run)       DRY_RUN=1 ;;
    -h|--help)       awk 'NR>1 && /^#/ {sub(/^# ?/,""); print; next} NR>1 {exit}' "$0"; exit 0 ;;
    *)               die "unknown option: $1 (try --help)" ;;
  esac
  shift
done

[ -d "$SRC" ] || die "can't find skills/ next to this script (looked in $SRC)"

# No explicit target: install wherever an agent is already set up.
if [ "$MODE" != "explicit" ]; then
  if [ -d "$HOME/.claude" ]; then
    TARGETS+=("$CLAUDE_USER")
  fi
  if [ -d "$HOME/.agents" ] || [ -d "$HOME/.codex" ]; then
    TARGETS+=("$CODEX_USER")
  fi

  if [ ${#TARGETS[@]} -eq 0 ]; then
    cat >&2 <<'EOF'
Found neither ~/.claude nor ~/.agents — no agent appears to be set up here.

Pick a target explicitly:
  ./install.sh --claude     Claude Code   (~/.claude/skills)
  ./install.sh --codex      Codex         (~/.agents/skills)
  ./install.sh --project    this repo     (./.claude/skills, ./.agents/skills)
EOF
    exit 1
  fi
fi

label_for() {
  case "$1" in
    "$CLAUDE_USER")    echo "Claude Code (user)" ;;
    "$CODEX_USER")     echo "Codex (user)" ;;
    "$CLAUDE_PROJECT") echo "Claude Code (this repo)" ;;
    "$CODEX_PROJECT")  echo "Codex (this repo)" ;;
    *)                 echo "custom path" ;;
  esac
}

for target in "${TARGETS[@]}"; do
  printf '\n%s\n  %s\n' "$(label_for "$target")" "$target"

  for skill in "${SKILLS[@]}"; do
    [ -d "$SRC/$skill" ] || die "missing source skill: $SRC/$skill"
    dest="$target/$skill"

    if [ -e "$dest" ]; then
      action="replace"
    else
      action="install"
    fi

    if [ "$DRY_RUN" -eq 1 ]; then
      printf '  would %s  %s\n' "$action" "$skill"
      continue
    fi

    mkdir -p "$target"
    # Replace the skill directory wholesale so a removed reference file doesn't linger.
    rm -rf "$dest"
    cp -R "$SRC/$skill" "$dest"
    printf '  %-9s %s\n' "$action" "$skill"
  done
done

if [ "$DRY_RUN" -eq 1 ]; then
  printf '\nDry run — nothing was written.\n'
  exit 0
fi

cat <<'EOF'

Done. Restart your agent so it picks the skills up.

  Claude Code   describe a situation and the right skill triggers itself
  Codex         /skills to confirm they loaded, or $executive-presence to
                invoke one explicitly

Try: "I have to tell leadership on Thursday that the migration is slipping."
EOF
