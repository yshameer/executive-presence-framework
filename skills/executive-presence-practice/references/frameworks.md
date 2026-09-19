# The 12 Frameworks

Grouped by what they govern. Contents:

| Group | Frameworks |
|---|---|
| [Structure](#structure) | 1 BLUF · 2 Minto Pyramid · 3 C·D·S |
| [Thinking](#thinking) | 4 PMI · 5 SCR · 6 Story Structure |
| [Interaction](#interaction) | 7 Decisive Answering · 8 Meeting Lead · 9 A·D·A · 10 Read Before You Respond |
| [Embodiment](#embodiment) | 11 Pause Principle · 12 Consistency Compound |

---

## Structure

### 1. BLUF — Bottom Line Up Front

Answer or recommendation first, reasoning second.

**Test:** If they stopped reading after your first sentence, would they know what you want?

❌ "We looked at the data, ran the analysis, considered the options, and after everything we think maybe we should go with Option B..."
✅ "We should go with Option B. It cuts cost by 20% with acceptable risk. Here's why."

❌ "There were some challenges with the timeline and after talking to the team we realised there might be a delay..."
✅ "The launch will slip by 2 weeks. Root cause is 3 unresolved blockers in QA. Here's the recovery plan."

**Use for:** any update, written or spoken. This is the default.

---

### 2. Minto Pyramid

Governing thought → 3 key arguments → supporting data.

- **Vertical logic:** each level answers "Why?" from the level above
- **Horizontal MECE:** arguments at the same level are mutually exclusive and collectively exhaustive — no overlaps, no gaps

**Example:**
> **Top:** Cloud costs jumped 40% due to 3 controllable issues — not organic growth — and we have a fix plan recovering ~25% within 30 days.
>
> **Arguments:** 3 untagged dev environments running 24/7 · Misconfigured auto-scaling on prod API · No reserved instances on top 2 workloads
>
> **Data:** ~$8K/mo waste, shutting down this week · Triggered 8× unnecessarily, fixed in config · Switching saves est. 35%

**Use for:** emails, briefs, structured arguments, anything where the full case matters.

**Note:** write bottom-up if you need to think it through. Send top-down always.

---

### 3. C·D·S — Claim · Data · So what

- **Claim** — the assertion
- **Data** — the specific number that proves it
- **So what** — the implication or decision it drives

| Vague | Precise |
|---|---|
| "A lot of customers complained" | "38 support tickets in 72 hrs — 3× our weekly average" |
| "The team is pretty stretched" | "We're at 112% capacity — 3 engineers on 2 projects each" |
| "The team has been slow" | "Velocity fell 38% over six weeks (34 → 21 points/sprint)" |
| "We're going to be a bit late" | "v2.0 ships Oct 3 — 21 days past the Sept 12 target" |

**No exact number?** Use a range ("between 15–25%") or anchor to a reference ("roughly 2× what we saw in Q1"). Both beat "quite a bit."

**Use for:** status updates, proposals, making any case. Every adjective is a candidate for replacement with a number.

---

## Thinking

### 4. PMI — Plus / Minus / Interesting (de Bono)

A thinking tool, not a presenting tool. Run it privately, then present the conclusion with Minto or BLUF.

| Column | Content |
|---|---|
| **Plus** | Genuine upsides — value created, problems solved. Specific, with data. |
| **Minus** | Real downsides — cost, risk, what breaks. Name the probability or cost. |
| **Interesting** | Questions raised, dependencies, second-order effects. Neither good nor bad yet. |

**Example — hiring decision:**

*Plus:* Restores velocity toward v2.0 (21 → 34+ pts/sprint). Reduces burnout on 8-person team at 112% load.
*Minus:* ~$90K/mo additional burn. Runway shrinks 14 → 11 months. 60–90 day ramp delays gains.
*Interesting:* Does hiring signal confidence to investors or concern? Can we hire contract first as a hedge? Does the delay cost more than $90K/mo in slipped revenue?
*Recommendation:* Hire 2 now, not 3 — targeting the roles that unblock v2.0. $60K/mo buys 12+ weeks of velocity without fully stressing runway.

**The Interesting column is the differentiator.** It's where the real risks hide, and naming what you don't know yet signals seniority. Never leave it blank.

**Use for:** trade-off decisions, contested recommendations, anywhere you need to demonstrate you've stress-tested your own position.

---

### 5. SCR — Situation · Complication · Resolution

| Part | Purpose |
|---|---|
| **Situation** | Stable context everyone agrees on. No tension yet. |
| **Complication** | What changed or is at risk. The "why does this matter now?" moment. |
| **Resolution** | Your recommendation, with urgency behind it. |

❌ "We need to hire 2 engineers. Here are 3 reasons: velocity is down, the bug backlog is growing, v2.0 is delayed."

✅ "We built a team capable of shipping every quarter. **[S]** Over the last six weeks, three engineers left simultaneously and velocity dropped 38%. **[C]** To get back on track without stressing runway, we should hire 2 senior engineers now and revisit the third post-funding. **[R]**"

**The Complication is the sentence that matters most.** It must create genuine tension. "Sales are up" is a situation. "Sales are up but NPS dropped 12 points — we're growing ourselves into a churn problem" is a complication.

**Use for:** meeting openings, exec summaries, framing any change or ask. Nests with Minto — use SCR to open, Minto to structure the Resolution.

---

### 6. Story Structure — Hook · Context · Insight · CTA

| Part | Purpose | Test |
|---|---|---|
| **Hook** | Grab attention in sentence one | Would they lean forward or check their phone? |
| **Context** | Set the stakes | Is something genuinely at risk? |
| **Insight** | The reframe they couldn't see | Is this new, or restating data? |
| **CTA** | One specific ask | A decision, or vague "let's discuss"? |

**4 hook types:**
- **Surprising stat** — "Last quarter, 40% of our support tickets came from 3% of our features."
- **Specific moment** — "On Tuesday at 2am, our on-call engineer got their 11th page of the week."
- **Provocative question** — "What if our biggest growth risk isn't competition — it's our own product?"
- **Sharp contrast** — "Twelve months ago we had 3 enterprise customers. Today we have 31 — and we're about to lose the first one."

Never open with "Today I want to talk about..." — it loses the room in three words.

**Full example — enterprise pivot all-hands:**
> *Hook:* "Eighteen customers are generating more revenue than twelve hundred."
> *Context:* "Self-serve: 1,240 customers, 34% annual churn, three competitors just cut prices 30%. Enterprise: 18 deals in six months, 6% churn, $87K average ARR. Top 10 accounts are 58% of revenue."
> *Insight:* "Enterprise costs 4× more to serve — but LTV is 22× higher. We've been optimising for volume when we should have been optimising for value."
> *CTA:* "Leave today with one commitment to something you'll do differently next quarter."

**The audience is the hero, not you.** Frame around what they need to see or do, not what you discovered.

**Use for:** all-hands, investor updates, high-stakes persuasion, anything that needs to be remembered a week later.

---

## Interaction

### 7. Decisive Answering

Three valid answers to a direct question:

| Answer | How |
|---|---|
| **Yes** | State it. Then what it means or what happens next. |
| **No** | State it. Then the reason, and what you'd recommend instead. |
| **I'll find out by [specific time]** | Own the gap. "Soon" and "ASAP" don't count. |

**Avoid:** "It depends" · "That's a good question" · "I'm not totally sure but..." · "We'll have to see" · "Potentially, yes"

These read as unpreparedness, not caution. They also shift the cognitive work back to the person who asked.

**Examples:**
> *"Will the feature be ready for Friday's demo?"*
> "Yes — core functionality is ready. Two minor UI gaps won't affect the demo flow. I'll brief the demo team by Thursday noon."

> *"Should we discount 20% to close this quarter?"*
> "No. At 20% we're below floor margin on this deal tier. I'd offer 10% with extended payment terms — closes the quarter, protects margin."

**Credibility = saying + doing.** "I'll find out by Thursday" creates an obligation that Thursday must satisfy.

---

### 8. Meeting Lead — the 3-sentence opening

1. "We're here to **decide** [specific decision]." — *decide*, not *discuss*
2. "My recommendation is [stance] — [one-line reason with data]."
3. "I want to hear your [concerns/input on X], and we need to leave with [specific outcome]."

❌ "Thanks everyone for joining. So, um, we wanted to get together to talk about the pricing question and kind of hear everyone's thoughts. Who wants to start?"

✅ "We're here to decide whether to raise prices 8% in Q1. My recommendation is yes — I'll share why in 2 minutes, then I want to hear your pushback. We need a decision by end of this call."

**In someone else's meeting:** when given the floor, still lead with your stance. "My view is X. Here's why." Don't wait for permission to have a position.

**Use for:** opening any meeting you're running, and structuring your contribution to meetings you're not.

---

### 9. A·D·A — Acknowledge · Data · Affirm or Adjust

For handling pushback.

- **Acknowledge** — show you heard it. Don't dismiss, don't immediately counter.
- **Data** — respond with evidence, not a louder restatement of your opinion.
- **Affirm or Adjust** — restate your position with support, or update openly.

**The critical distinction:**

| Caving | Updating |
|---|---|
| Changing because someone pushed harder or outranks you | Changing because they introduced new data or a valid argument |
| Destroys credibility | Builds credibility |

You have to know which one you're doing. From the inside, under pressure, they feel similar.

**Avoid:** "You're probably right..." · "Yeah, I can see that..." · "Maybe we should reconsider..." — said under pressure, these signal you don't believe your own recommendation.

**Use:**
- "I hear the concern. The data still points to X because..."
- "That's a real risk. I've factored it in — here's how."
- "If [condition] changes, I'd revisit. As of now I'm holding my recommendation."
- "That's new information I hadn't considered — let me update my view." *(only when true)*

**Example — holding (pressure, no new data):**
> CFO: "You can't just measure events in leads. There's brand value, retention."
> "Brand value is real — I'm not dismissing it. But we don't currently have a way to measure it, which means we can't compare it to pipeline contribution. What I can measure is that $80K generated 3 qualified leads — $26K per lead against a $3–4K paid benchmark. I'm holding my recommendation, but if you can point me to data on event-driven retention lift, I'll factor it in."

**Example — updating (genuine new data):**
> VP Product: "Our top customer says if we don't ship SSO by month end, they're pausing a $280K renewal."
> "That changes my recommendation. A $280K renewal risk wasn't in my analysis. SSO moves to the front of the sprint. Can you get me the deadline in writing so I can sequence around it?"

---

### 10. Read Before You Respond

Executive presence is not only what you say — it's what you understood before you spoke.

**Move 1 — Ask one question before you advocate.** In a contested room, surface what you don't know about their position first. This is reconnaissance, not softness.
> "Before I give you my view — what's driving the concern on your side? I want to make sure I'm solving the right problem."

The answer often changes your framing. Sometimes it changes your recommendation.

**Move 2 — Reframe for the audience.** Same recommendation, different lead.

| Audience | They optimise for | Lead with |
|---|---|---|
| CFO | Cost, risk, predictability | The number and the downside protection |
| CEO | Strategy, speed, market position | The strategic bet and what it unlocks |
| Engineering | Feasibility, technical debt, clarity | The constraint and what you're protecting |
| Sales | Pipeline, timing, competitive position | Customer impact and timeline |
| Your team | Workload, priority, meaning | What changes for them and what you're removing |

*Same recommendation — "pause feature work for one sprint":*
- **CFO:** "Two weeks of debt work now avoids an estimated 8–10 weeks of reactive cost next quarter."
- **CEO:** "We're one incident away from an enterprise churn event. This protects the segment we're betting on."
- **Team:** "I'm clearing the roadmap for two weeks so you can fix what's been bothering you. Nothing new gets added."

**Move 3 — Name what you heard before you counter.**
> "So the concern is that pausing features signals to customers that we're slowing down. Is that the core worry, or is there more?"

Two effects: you're demonstrably listening, and you frequently discover you'd misread the objection.

**The most senior person in the room is often the one asking the sharpest question, not giving the longest answer.**

---

## Embodiment

### 11. Pause Principle

Delivery is a claim about how much you trust your own content. A perfectly structured argument delivered fast, with rising intonation and no pauses, still reads as junior.

| Habit | Why it works |
|---|---|
| **Pause before answering** | Two seconds of silence signals consideration. "So, um, that's a great question..." signals buying time. |
| **Pause after your recommendation** | Say it, then stop. Rushing to justify is the most common tell of low confidence. |
| **Land your sentences** | Upward inflection turns a statement into a question. "We should ship Friday?" ≠ "We should ship Friday." |
| **Slow down as stakes rise** | The default under pressure is to speed up. Drop ~20%. It reads as control. |

**Self-audit:**

| Tell | Fix |
|---|---|
| "So, um..." before answering | Pause instead. Silence beats filler. |
| Justifying immediately after your recommendation | Stop talking. Let it land. |
| Statements ending in upward pitch | Land the sentence. Drop the tone. |
| Speaking faster when challenged | Deliberately slow to ~80% of normal pace. |
| Trailing off at the end of a point | Finish the sentence fully, then stop. |

**Use for:** any spoken scenario. Give one or two cues tied to the specific moment, not general advice.

---

### 12. Consistency Compound

Research separates short-term impressions (appearance, confidence, communication style — read in seconds) from long-term evaluations (interpersonal integrity, values in action, outcome delivery — built over months).

Frameworks 1–11 optimise for the moment. This one optimises for accumulation, and over time it outweighs the rest.

| Behaviour | In practice |
|---|---|
| **Outcome delivery** | Every "I'll get back to you by Thursday" is a credibility contract. Kept, it compounds. Broken, it discounts everything you say afterwards. Only commit to timelines you'd bet money on. |
| **Values in action** | People judge your values by your behaviour when holding them costs you something. Do you credit the team when you presented the win? Do you give the honest recommendation when it's unpopular? |
| **Consistency across audiences** | Same position to your team, your manager, your peers. Presence collapses fast when people compare notes and find three versions of your view. |

**Quarterly check:**
1. What did I commit to, and did I deliver it?
2. Where did my stated values and actual behaviour diverge?
3. Would my team, manager, and peers describe my position on [key issue] the same way?
4. What did I get wrong, and did I say so out loud?

**Use for:** scenarios involving trust repair, reputation, a commitment the user may not be able to keep, or where they're tempted to tell different people different things. Also relevant when someone's advice-seeking reveals a pattern rather than a one-off.

---

## How they combine

A typical high-stakes sequence:

1. **PMI** to think it through privately
2. **Minto** to structure the argument
3. **SCR** to open the conversation
4. **C·D·S** to anchor every claim
5. **Read Before You Respond** to understand the room before advocating
6. **Decisive Answering** for the questions that follow
7. **A·D·A** when challenged
8. **Pause Principle** throughout the delivery
9. **Consistency Compound** doing the work no single conversation can

Most scenarios need three or four of these, not all nine.
