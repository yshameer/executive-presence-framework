# Example 4 — A practice drill, end to end

**Skill:** `executive-presence-practice`

Shows the thing that makes the drill work: **the first message contains a scenario and nothing else.** No model answer, no suggested structure, no hint.

---

## Turn 1 — you

> Drill me on BLUF. 5 minutes.

## Turn 2 — the skill

> **Scenario — BLUF under pressure**
>
> You run platform engineering. Your CFO has pulled you into a 15-minute slot because cloud spend is up.
>
> What you know:
>
> - Cloud spend went from **$142K/month in January to $198K/month in June** — up 39%
> - Traffic over the same period grew **11%**
> - Your audit two weeks ago found **$31K/month** in waste: 14 untagged dev environments running 24/7, auto-scaling misconfigured on the prod API tier, and no reserved instances on your two largest workloads
> - Reserved instances on those two workloads would save an estimated **$18K/month**, but require a **12-month commitment**
> - You need **3 engineer-weeks** to do the remediation, and your team is currently committed to the Q3 migration
>
> She opens with:
>
> > "Cloud costs are up 40% and I need to understand whether this is growth or sloppiness. I'm looking at a 20% cut across infrastructure. Talk me through it."
>
> **Write your spoken answer. You have about 60 seconds — aim for 5–7 sentences.**
>
> Take a few minutes, then paste what you'd say.

*[The message ends here. No example. No structure to fill in.]*

## Turn 3 — you

> So there are a few things going on here. We did see traffic growth over the period which accounts for some of it, and we've also had some inefficiencies in how dev environments are managed that we've been aware of for a while. I did an audit recently and found some issues around tagging and auto-scaling configuration. I think there's definitely room to reduce spend, and I'd like to propose we look at reserved instances as well, which could help. I'd want to avoid a flat 20% cut though because that might affect production capacity. Happy to put together a plan.

## Turn 4 — the skill

> **What worked**
>
> "I'd want to avoid a flat 20% cut because that might affect production capacity" — that's the one place you took a position. Good instinct, wrong position in the answer: it's the fifth sentence, and it's hedged with "might."
>
> **What to fix**
>
> You opened with **"So there are a few things going on here."** That's a sentence that transfers zero information and signals you're assembling the answer live. Under a BLUF standard it's disqualifying on its own — your CFO asked a binary question (growth or sloppiness?) and sentence one doesn't answer it.
>
> The bigger problem: **you had the answer and didn't use it.** Spend up 39%, traffic up 11%. That gap *is* the answer to her question, and it's the number that reframes the conversation from "cut 20%" to "recover $31K." You mentioned traffic growth and the audit as separate facts and never connected them. She has to do that arithmetic herself — and she won't, she'll just proceed with the 20% cut.
>
> Your weakest sentence:
>
> > "I did an audit recently and found some issues around tagging and auto-scaling configuration."
>
> Rewritten:
>
> > "The audit found $31K a month in waste — 14 dev environments running 24/7, and auto-scaling misconfigured on prod."
>
> Same fact. One is a topic; the other is a number she can act on.
>
> **Framework check**
>
> BLUF fails. The test is: if she stopped listening after sentence one, would she know your answer? After "there are a few things going on here," she knows nothing. She'd have to reach sentence four to learn there's waste, and she never learns how much.
>
> You also hedged three times — "some of it," "I think there's definitely," "might affect." Count those; under pressure that rate goes up, not down.
>
> **One possible strong version**
>
> > "It's mostly sloppiness, and I can name the number. Spend is up 39% while traffic is up 11% — so growth explains maybe a quarter of it. My audit two weeks ago found $31K a month in waste: 14 untagged dev environments running around the clock, and misconfigured auto-scaling on the prod tier. I can recover that in three engineer-weeks, plus another $18K a month if you'll approve a 12-month reserved instance commitment. That's $49K against your $40K target — so I'd rather hit the number this way than take a flat 20% cut, which would come out of production capacity."
>
> Note what that does: it concedes her point in the first four words. "It's mostly sloppiness" is disarming precisely because it's what she suspected — and it buys you the right to define the remedy. Yours spent five sentences avoiding that concession.
>
> Also: 20% of $198K is ~$40K, and your fixes total $49K. **You had a number that beat her target and didn't say it.** That's the combination the scenario was built around.
>
> **Carry forward**
>
> When you have two numbers that imply a conclusion, state the conclusion. "39% vs 11%" isn't the insight — "growth explains a quarter of it" is.
>
> ---
>
> Next: same framework with a harder version — the CFO interrupts you at sentence two? Or switch to A·D·A and practise holding a position under pushback?

---

## What to notice

**The scenario carries five hard numbers**, one of which ($40K target vs $49K recoverable) only pays off if you combine it with another. That's deliberate — the drill is designed around a conclusion you have to spot.

**The critique quotes exact phrases.** "You opened with 'So there are a few things going on here'" is actionable. "Be more direct" is not.

**The model answer comes last**, marked as *one possible strong version*. Reverse that order and there's no drill left.

**One takeaway, not five.** There were at least six things wrong with that answer. Three got named.
