# Benchmarks

Measured results comparing the model **with** each skill loaded against the **same model with no skill**, on held-out scenarios.

| Skill | With skill | Without | Delta | Detail |
|---|---|---|---|---|
| `executive-presence` | 100% ± 0% | 47% ± 46% | **+53pp** | [md](executive-presence.md) · [json](executive-presence.json) |
| `executive-presence-practice` | 100% ± 0% | 87% ± 23% | **+13pp** | [md](executive-presence-practice.md) · [json](executive-presence-practice.json) |

Run 2026-08-02. Three evals per skill, three runs per configuration, pass rate averaged across runs. The `.json` files carry per-run detail: which individual expectations passed, plus time and token counts.

## How to read this

**The coach's gain is large, and the spread is the interesting part.** A 47% baseline with a **±46%** standard deviation means the unaided model was inconsistent rather than uniformly bad — sometimes it produced a genuinely good coaching response, sometimes an essay about communication principles with no usable words in it. The skill's main effect is removing that variance. ±0% across nine runs is the number worth caring about here, more than the mean.

**The practice skill starts from a high baseline** because "give me a scenario" is an easy instruction to follow unaided — the model will produce a scenario. Its value is concentrated in the rule the model breaks constantly without it: **don't include the model answer in the same message.** That's a small delta in aggregate and the difference between a working drill and a useless one.

## What it costs

| Skill | Added tokens | Added time |
|---|---|---|
| `executive-presence` | ~+11.7K | ~+29s |
| `executive-presence-practice` | ~+6.8K | ~-3s (no change) |

Most of the token cost is loading `references/frameworks.md`. That's the trade: the skill reads all 12 frameworks before responding, which is also the reason its recommendations are specific rather than generic.

## Caveats

Read these before quoting the numbers anywhere.

- **Three evals per skill.** Enough to show direction, not enough for a confident effect size. Treat +53pp as "clearly helps," not as a measurement.
- **The evals were written alongside the skill**, so they test what it was built to do. They don't test scenarios nobody anticipated.
- **Pass/fail is graded against written expectations** (e.g. *"includes a delivery/pause instruction"*, *"uses bracketed placeholders instead of inventing facts"*), not against human preference. A response can satisfy every expectation and still be one a person wouldn't want to send.
- **Model names and paths are redacted** in the committed files (`<model-name>`, `<path/to/skill>`), so these aren't reproducible as-is against a specific model version.
- **Only `executive-presence` retained its eval definitions** — see [`skills/executive-presence/evals/evals.json`](../skills/executive-presence/evals/evals.json). The practice skill's eval file wasn't kept from the original run; its benchmark records that evals 0–2 ran, but the case definitions are gone.

## Re-running these

Skill evals are run with the `skill-creator` skill. Broadly: point it at a skill directory containing an `evals/evals.json`, and it runs each eval with and without the skill loaded, grading responses against each eval's `expected_output`.

To benchmark the practice skill you'd need to write a new `evals/evals.json` for it first. Three cases worth covering, based on what the skill actually promises:

1. **The one rule** — does the first message withhold the model answer entirely?
2. **Scenario quality** — does it include three or more hard numbers, a named counterpart role, and a stated format and length?
3. **Critique specificity** — does the feedback quote the user's actual words rather than give generic advice?
