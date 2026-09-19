# Example 1 — Delivering a slip to leadership

**Skill:** `executive-presence` · **Mode:** spoken · **Stakes:** high

Shows the full five-part response: diagnosis, frameworks, the words, a delivery note, a coaching note. This is the shape a high-stakes spoken scenario gets.

---

## The ask

> I have to tell our leadership team on Thursday that the platform migration is slipping by about a month. We said end of Q3, it's going to be end of October. The main reason is we found way more undocumented dependencies in the legacy billing service than anyone expected — about 40 vs the 12 we scoped for. Two of them touch payment processing so we can't rush them. How do I handle this meeting?

---

## The response

### Diagnosis

You have two problems and only one of them is the date. The first is the slip itself, which is a fact you can state in ten seconds. The second is what leadership will infer about your estimating — if 12 became 40, the question forming in their heads is "what else is wrong in your plan?"

The meeting is won or lost on the second problem. Most people over-explain the first, which makes the second one worse: the longer you spend justifying the miss, the more it sounds like you're still surprised by your own project.

### Frameworks

- **SCR** to open — this is a change to a commitment, so it needs framing, not a bare announcement. The Complication is the discovery, not the delay.
- **BLUF** inside the Resolution — the new date goes early and unqualified.
- **C·D·S** for the numbers — 40 vs 12 is your strongest asset. It converts "we were wrong" into "we found something," which is a different conversation.
- **Decisive Answering** for what follows. Expect "can you compress it?" and have the answer ready.

Sequence: SCR to open, then stop talking. Let them ask.

### The words — your opening, ~40 seconds

> "When we scoped the platform migration in [month], we committed to end of Q3, and the team has hit every milestone up to this one. **[S]**
>
> Two weeks ago we finished dependency mapping on the legacy billing service. We scoped 12 undocumented dependencies. There are 40. Two of them touch payment processing directly, which means they need full regression testing rather than a cutover. **[C]**
>
> The migration will complete end of October — four weeks past our Q3 commitment. I'm not going to compress that, and I want to tell you why in one line: the two payment dependencies are the ones where a rushed cutover costs us more than four weeks. Everything else is on the original track. **[R]**"

*Then stop.*

### The words — the pushback you should expect

**"Can we get any of it sooner?"**

> "Yes — [component] and [component] are independent of billing and can land [date], on the original timeline. What moves to October is the billing cutover specifically. If it's useful I'll split the release so you get [X]% of the migration on the original date."

**"Why didn't we know this in [month]?"**

Don't get defensive, and don't over-apologise:

> "Our scoping was based on the service documentation, which listed 12. The documentation was wrong — we found the other 28 by instrumenting the service in staging, which is work we did after scoping. What I'd change is running that instrumentation *before* committing to a date on any legacy service. I'm applying that to [next migration phase] now."

**"What's the risk we slip again?"**

> "Low, and here's the basis: the 40 are now enumerated rather than estimated — we've mapped all of them, and 38 are routine. The two payment ones are the schedule. I'll flag by [specific date] if either moves."

### Delivery note

Two cues:

Pause after **"There are 40."** That number is doing all your work — give them two full seconds to react to it before you continue. If you rush into "which means…" you'll flatten the one moment where they understand this was a discovery rather than a miss.

And pause after **"four weeks past our Q3 commitment."** The instinct will be to immediately soften it with justification. Don't. Say the date, stop, and let the silence sit. If someone jumps in with a question, you've landed it.

Watch your pace on the "why didn't we know" answer — that's the moment you'll want to speed up. Deliberately slow down instead.

### Coaching note

The trap here is leading with the cause instead of the date. It feels more logical — set up the problem, then reveal the consequence — and it reliably reads as burying the lede. By sentence three of dependency detail, leadership has stopped listening for information and started listening for how bad the number is. Give them the number first; they'll listen to the reasoning much better once they have it.
