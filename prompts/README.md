# Portable prompts

Plain-text versions of both skills, for tools that don't support Claude Skills — Claude.ai Projects, ChatGPT, Custom GPTs, Gemini, or any chat box.

| File | Equivalent to |
|---|---|
| [`coach-prompt.md`](coach-prompt.md) | [`skills/executive-presence`](../skills/executive-presence/) |
| [`practice-prompt.md`](practice-prompt.md) | [`skills/executive-presence-practice`](../skills/executive-presence-practice/) |

## How to use

Copy everything below the `---` line in the file and paste it into:

- **Claude.ai Project** → project custom instructions
- **Custom GPT** → the Instructions field
- **Any chat** → the first message, then describe your situation in the second

Then use it exactly as you'd use the skill. Describe a situation to the coach; say "drill me on BLUF" to the practice prompt.

## Use one at a time

Don't paste both into the same context. They pull in opposite directions — one writes the answer for you, the other refuses to — and combining them reliably produces the coach's behaviour, because writing the answer is the more attractive instruction. Use two separate Projects or two separate chats.

## What you lose versus the real skill

**The frameworks are condensed.** Each prompt inlines all 12, but in compressed form — the tests and the sharpest examples from the [full reference](../skills/executive-presence/references/frameworks.md) are trimmed to keep the paste manageable. Output is a step below the skill version.

**Recovering most of the gap:** if your tool accepts file attachments, attach the full `frameworks.md` alongside the prompt. The skill's own instruction is to read that file before responding, so this reproduces the real setup closely.

**No automatic triggering.** Skills activate on their own when your situation matches. A pasted prompt is always on — which is why it belongs in a dedicated Project or chat rather than your general-purpose one.

## Keeping these in sync

These are derived from the `SKILL.md` files. If you edit a skill, edit the matching prompt — nothing enforces this automatically. The prompt bodies deliberately track the skill text closely, so a diff of the two is usually readable enough to port changes by hand.
