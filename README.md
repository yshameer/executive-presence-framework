# Executive Presence Framework

**[yshameer.github.io/executive-presence-framework](https://yshameer.github.io/executive-presence-framework/)**

Two [Claude Skills](https://docs.claude.com/en/docs/claude-code/skills) for high-stakes workplace communication, built on 12 frameworks.

| Skill | What it does | Use when |
|---|---|---|
| **`executive-presence`** | Diagnoses the moment, picks the frameworks, and writes the actual words you'd say or send | You have a real situation to handle in the next hour |
| **`executive-presence-practice`** | Gives you a scenario, waits for *your* answer, then critiques it | You want to get better, not get a script |

The split matters. The coach writes for you; the drill partner refuses to. A drill where the model hands you a model answer up front is just coaching with extra steps.

Both skills share the same [12-framework reference](skills/executive-presence/references/frameworks.md) — BLUF, Minto Pyramid, C·D·S, PMI, SCR, Story Structure, Decisive Answering, Meeting Lead, A·D·A, Read Before You Respond, Pause Principle, Consistency Compound.

## Install

Three ways, depending on how you use Claude. Full detail in [docs/INSTALL.md](docs/INSTALL.md).

**As a Claude Code plugin** (recommended — gets both skills and keeps them updatable):

```bash
/plugin marketplace add <your-github-user>/executive-presence-framework
```

Then `/plugin install executive-presence@executive-presence-framework`.

**By copying the skill folders** into your personal skills directory:

```bash
cp -R skills/executive-presence skills/executive-presence-practice ~/.claude/skills/
```

**Without Claude Code at all** — paste a self-contained prompt from [`prompts/`](prompts/) into any chat interface. See [prompts/README.md](prompts/README.md).

## Use

You don't invoke these by name. Describe your situation and the right skill triggers itself:

> "I have to tell leadership on Thursday that the migration is slipping by a month."

→ **coach**: diagnosis, frameworks, the words, a delivery note.

> "Drill me on BLUF."

→ **practice**: a scenario with hard numbers, then silence until you answer.

The dividing line is whether you want to *attempt* something or *receive* something. More in [docs/USAGE.md](docs/USAGE.md), with worked transcripts in [`examples/`](examples/).

## What's in here

```
skills/            The two skills, verbatim — this is the installable artifact
  executive-presence/
    SKILL.md
    references/frameworks.md     the 12 frameworks
    evals/evals.json             test cases used to benchmark the skill
  executive-presence-practice/
    SKILL.md
    references/frameworks.md     identical copy — skills must be self-contained
prompts/           Portable versions for chat interfaces with no skill support
examples/          Worked transcripts showing what good output looks like
benchmarks/        Measured with-skill vs without-skill results
handouts/          Printable PDF of the frameworks, plus its build script
docs/              Install and usage guides
index.html         The GitHub Pages landing page
robots.txt         }
sitemap.xml        } crawler files for the Pages site
.nojekyll          }
```

### On `index.html`

The landing page restates the 12 frameworks in HTML so the content is indexable — search engines don't read `.md` files on github.com as well as they read a served page. Nothing generates it, so **if you change the frameworks, change the page too.** The Markdown in `skills/` stays canonical; it's what the skills actually read.

### On the duplicated `frameworks.md`

Both copies are byte-identical and must stay that way — a skill has to be self-contained so it still works when someone copies one folder out. Verify with:

```bash
diff skills/executive-presence/references/frameworks.md skills/executive-presence-practice/references/frameworks.md
```

## Does it actually work?

Measured against held-out scenarios, with and without the skill loaded. Full numbers and caveats in [benchmarks/](benchmarks/README.md).

| Skill | Pass rate with skill | Without | Delta |
|---|---|---|---|
| `executive-presence` | 100% ± 0% | 47% ± 46% | **+53pp** |
| `executive-presence-practice` | 100% ± 0% | 87% ± 23% | **+13pp** |

The coach shows the larger gain, and the ±46% spread on the baseline is the interesting part: unaided, the model handled these scenarios inconsistently rather than uniformly badly. The practice skill starts from a higher baseline because "give me a scenario" is an easier instruction to follow unaided — its value is in the one rule a model breaks constantly without it: *don't show the answer first*.

Three evals per skill, three runs each. That's enough to show direction, not enough for a confident effect size.

## License

MIT — see [LICENSE](LICENSE).

The frameworks themselves are drawn from published work in communication and decision-making: Barbara Minto's Pyramid Principle, Edward de Bono's PMI, BLUF from military briefing practice, and SCR from consulting practice. The synthesis, examples, and skill instructions here are original.
