# Install

Pick the path that matches how you use Claude.

| Your setup | Use |
|---|---|
| Claude Code, want updates | [Plugin marketplace](#option-1--claude-code-plugin) |
| Claude Code, want it local and editable | [Copy the folders](#option-2--copy-the-skill-folders) |
| One project only, shared with a team | [Project skills](#option-3--project-scoped-skills) |
| Claude.ai, ChatGPT, or any other chat UI | [Portable prompts](#option-4--no-skill-support) |

---

## Option 1 — Claude Code plugin

Gets both skills at once and lets you pull updates later.

```bash
/plugin marketplace add yshameer/executive-presence-framework
```

```bash
/plugin install executive-presence@executive-presence-framework
```

Restart Claude Code, then confirm both skills are listed:

```bash
/plugins
```

To update later:

```bash
/plugin marketplace update executive-presence-framework
```

---

## Option 2 — Copy the skill folders

Skills are self-contained directories. Copying is all that's required.

```bash
cp -R skills/executive-presence skills/executive-presence-practice ~/.claude/skills/
```

Expected result:

```
~/.claude/skills/
├── executive-presence/
│   ├── SKILL.md
│   └── references/frameworks.md
└── executive-presence-practice/
    ├── SKILL.md
    └── references/frameworks.md
```

Restart Claude Code. The skills load automatically — there's nothing to register.

Take **one** of the two if you only want one. Each folder works alone, which is why `references/frameworks.md` is duplicated rather than shared.

---

## Option 3 — Project-scoped skills

To make the skills available to everyone working in a specific repo, commit them into that repo:

```bash
mkdir -p .claude/skills
cp -R /path/to/executive-presence-framework/skills/* .claude/skills/
git add .claude/skills && git commit -m "Add executive presence skills"
```

Anyone who clones the repo gets them. Useful for a team that wants a shared standard for how updates and escalations get written.

---

## Option 4 — No skill support

For Claude.ai Projects, ChatGPT, or any chat interface without skills, use the self-contained prompts in [`../prompts/`](../prompts/):

- [`coach-prompt.md`](../prompts/coach-prompt.md) — the coaching skill
- [`practice-prompt.md`](../prompts/practice-prompt.md) — the drill skill

Each one inlines a condensed version of all 12 frameworks, so it works as a single paste with no file loading. Drop it into a Project's custom instructions or a Custom GPT's system prompt and it behaves like the skill.

Trade-off: the condensed frameworks are terser than [the full reference](../skills/executive-presence/references/frameworks.md). Output quality is a step below the real skill. If your tool supports file attachments, attach the full `frameworks.md` alongside the prompt and you get most of the gap back.

---

## Verify the install

Ask for something that should trigger the coach:

> "My VP just asked why the Q3 numbers are down. I have 10 minutes before the call."

You should get a diagnosis, named frameworks, and usable words — not a general essay about communication. If you get the essay, the skill didn't load.

Then check the drill:

> "Drill me on BLUF."

You should get a scenario **and nothing else** — no model answer, no suggested structure. If it hands you an example answer in the same message, the skill didn't load.

---

## Rebuilding the PDF handout

Only needed if you edit the frameworks and want a fresh printable version.

```bash
pip install reportlab
```

```bash
python handouts/build_pdf.py
```
