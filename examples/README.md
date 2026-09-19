# Examples

Worked demonstrations of both skills. Read these to calibrate what good output looks like before you judge your own results.

| # | Example | Skill | Demonstrates |
|---|---|---|---|
| 1 | [Bad news to leadership](01-bad-news-to-leadership.md) | coach | The full five-part response on a high-stakes spoken moment |
| 2 | [Saying no on Slack](02-slack-reply-at-capacity.md) | coach | Calibration — same skill, ~80 words, no delivery note |
| 3 | [Peer conflict](03-peer-conflict-listen-first.md) | coach | Declining the requested deliverable and saying why |
| 4 | [A drill, end to end](04-practice-drill.md) | practice | Scenario → your attempt → critique → model answer |

Read 1 and 2 together — they're the clearest illustration that the coach sizes its response to the moment rather than applying a fixed template.

## Where these come from

Examples 1–3 are the three scenarios in [`skills/executive-presence/evals/evals.json`](../skills/executive-presence/evals/evals.json), the same cases used to produce the [benchmark numbers](../benchmarks/README.md). The prompts are verbatim from the eval file.

Example 4 is an authored demonstration of a drill in the format the practice skill specifies.

**The responses shown are illustrative, not captured transcripts.** They're written to the standard the skills specify — the right shape, the right level of specificity, the right calibration. A live run will differ in wording, and should. If your output matches these in *structure* — diagnosis before frameworks, real words with placeholders, delivery notes only when spoken — the skill is working.

## Using these as a standard

Three things to check in your own results:

1. **Did it diagnose, or restate?** A diagnosis names a challenge you hadn't articulated. "You need to communicate this clearly" is a restatement.
2. **Are the words usable?** You should be able to paste the worked example, fill the `[brackets]`, and send it. If you'd still have to write it yourself, it hasn't delivered.
3. **Did it size correctly?** A Slack reply that came back with five sections is over-engineered. Say "shorter."

For the practice skill there's only one check that matters: **did the first message contain a model answer?** If it did, the skill isn't loaded, because that's the one rule it exists to enforce.
