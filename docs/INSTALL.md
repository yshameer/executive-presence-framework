# Install

The two skills are plain directories containing a `SKILL.md`. **Claude Code and Codex both read that format**, so the same files serve both agents — only the install location differs.

| Agent | Scope | Path |
|---|---|---|
| Claude Code | personal | `~/.claude/skills/` |
| Claude Code | project | `<repo>/.claude/skills/` |
| Codex | personal | `~/.agents/skills/` |
| Codex | repo | `<repo>/.agents/skills/` or `$CWD/.agents/skills/` |
| Codex | system | `/etc/codex/skills/` |

---

## Fastest path — the install script

Handles every case above, and by default installs for whichever agents you already have set up.

```bash
git clone https://github.com/yshameer/executive-presence-framework.git
cd executive-presence-framework
./install.sh
```

| Flag | Effect |
|---|---|
| *(none)* | Auto-detect: installs for Claude Code and/or Codex, whichever is present |
| `--claude` | Claude Code only, `~/.claude/skills` |
| `--codex` | Codex only, `~/.agents/skills` |
| `--project` | Into the current repo, both agents |
| `--dir PATH` | An explicit directory |
| `--coach-only` / `--practice-only` | Just one of the two skills |
| `--dry-run` | Print what would happen, change nothing |

Start with `./install.sh --dry-run` if you want to see the targets first. Re-running replaces an existing install rather than merging into it, so a reference file you deleted upstream doesn't linger.

---

## Claude Code

### As a plugin (updatable)

```bash
/plugin marketplace add yshameer/executive-presence-framework
```

```bash
/plugin install executive-presence@executive-presence-framework
```

Pull updates later with `/plugin marketplace update executive-presence-framework`.

This path is Claude-only — `.claude-plugin/` is Claude Code's packaging format and Codex ignores it.

### By copying

```bash
cp -R skills/executive-presence skills/executive-presence-practice ~/.claude/skills/
```

### For a whole team

Commit the skills into the repo everyone works in:

```bash
mkdir -p .claude/skills && cp -R skills/* .claude/skills/
```

Restart Claude Code. Confirm with `/plugins`, or just describe a situation — skills load automatically and aren't invoked by name.

---

## Codex

### Personal

```bash
mkdir -p ~/.agents/skills && cp -R skills/* ~/.agents/skills/
```

### For a repo

Codex checks `$CWD/.agents/skills` and `$REPO_ROOT/.agents/skills`, so committing the skills makes them available to everyone working in that repo:

```bash
mkdir -p .agents/skills && cp -R skills/* .agents/skills/
git add .agents/skills && git commit -m "Add executive presence skills"
```

Restart Codex, then run `/skills` — it lists everything found at startup, which is the quickest way to confirm the install landed in a directory Codex actually scans.

### Invoking

Codex supports both routes:

- **Implicitly** — describe a matching situation and Codex selects the skill, same as Claude Code
- **Explicitly** — `$executive-presence` or `$executive-presence-practice`, or pick from `/skills`

Implicit invocation is on by default. To force explicit-only for a skill, add an `agents/openai.yaml` inside that skill's directory with `policy: allow_implicit_invocation: false`. These skills ship without that file, which means both routes work.

---

## Both agents at once

Nothing conflicts — the skills are independent copies in separate directories.

```bash
./install.sh --claude --codex
```

Or by hand:

```bash
cp -R skills/* ~/.claude/skills/
cp -R skills/* ~/.agents/skills/
```

The practical difference you'll notice is invocation style, not behaviour: Claude Code triggers on description alone, while Codex gives you `$skill-name` as an explicit override when it doesn't pick up on its own.

---

## Neither agent — plain chat

For Claude.ai Projects, ChatGPT, Gemini, or any chat box without skill support, use the self-contained prompts in [`../prompts/`](../prompts/):

- [`coach-prompt.md`](../prompts/coach-prompt.md)
- [`practice-prompt.md`](../prompts/practice-prompt.md)

Each inlines a condensed version of all 12 frameworks, so it works as a single paste with no file loading. Drop one into a Project's custom instructions or a Custom GPT's system prompt.

Trade-off: the condensed frameworks are terser than [the full reference](../skills/executive-presence/references/frameworks.md), so output is a step below the skill version. If your tool accepts file attachments, attach the full `frameworks.md` alongside and you recover most of the gap.

> Codex also has a `~/.codex/prompts/` custom-prompt mechanism, but OpenAI has deprecated it in favour of skills. Install the skills instead — the prompts here are for tools with neither.

---

## Verify the install

Same checks on both agents.

**The coach** — ask for something that should trigger it:

> "My VP just asked why the Q3 numbers are down. I have 10 minutes before the call."

You should get a diagnosis, named frameworks, and usable words — not a general essay about communication. If you get the essay, the skill didn't load.

**The drill** — ask to practise:

> "Drill me on BLUF."

You should get a scenario **and nothing else**. No model answer, no suggested structure. If it hands you an example answer in the same message, the skill didn't load.

If either fails on Codex, run `/skills` first — the most common cause is the files landing somewhere Codex doesn't scan.

---

## Rebuilding the PDF handout

Only needed if you edit the frameworks and want a fresh printable version.

```bash
pip install reportlab
```

```bash
python handouts/build_pdf.py
```
