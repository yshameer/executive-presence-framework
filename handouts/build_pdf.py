from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_CENTER

TEAL       = colors.HexColor("#0F6E56")
TEAL_LIGHT = colors.HexColor("#E1F5EE")
BLUE_LIGHT = colors.HexColor("#E6F1FB")
BLUE_DARK  = colors.HexColor("#0C447C")
RED_LIGHT  = colors.HexColor("#FCEBEB")
RED_DARK   = colors.HexColor("#791F1F")
PURPLE_L   = colors.HexColor("#EEEDFE")
PURPLE_D   = colors.HexColor("#3C3489")
AMBER_L    = colors.HexColor("#FAEEDA")
AMBER_D    = colors.HexColor("#633806")
CORAL_L    = colors.HexColor("#FAECE7")
CORAL_D    = colors.HexColor("#4A1B0C")
GRAY_LT    = colors.HexColor("#F1EFE8")
GRAY_MD    = colors.HexColor("#888780")
GRAY_DK    = colors.HexColor("#444441")
WHITE      = colors.white
BLACK      = colors.HexColor("#1A1A1A")

W, H = letter
MARGIN = 0.75 * inch
CW = W - 2 * MARGIN

base = getSampleStyleSheet()
def style(name, parent="Normal", **kw):
    return ParagraphStyle(name, parent=base[parent], **kw)

S = {
    "cover_title": style("cover_title", fontSize=32, textColor=TEAL, fontName="Helvetica-Bold", spaceAfter=6, leading=38),
    "cover_sub":   style("cover_sub",   fontSize=13, textColor=GRAY_MD, fontName="Helvetica", spaceAfter=4, leading=18),
    "cover_tag":   style("cover_tag",   fontSize=11, textColor=GRAY_MD, fontName="Helvetica-Oblique", spaceAfter=0),
    "part":        style("part",        fontSize=13, textColor=WHITE, fontName="Helvetica-Bold", leading=17),
    "part_sub":    style("part_sub",    fontSize=9,  textColor=colors.HexColor("#9FE1CB"), fontName="Helvetica", leading=12),
    "day_label":   style("day_label",   fontSize=9,  textColor=TEAL, fontName="Helvetica-Bold", spaceAfter=2),
    "h2":          style("h2",          fontSize=16, textColor=BLACK, fontName="Helvetica-Bold", spaceBefore=4, spaceAfter=4, leading=20),
    "h3":          style("h3",          fontSize=11, textColor=BLACK, fontName="Helvetica-Bold", spaceBefore=8, spaceAfter=3),
    "body":        style("body",        fontSize=10, textColor=BLACK, fontName="Helvetica", spaceAfter=5, leading=15),
    "small":       style("small",       fontSize=9,  textColor=GRAY_MD, fontName="Helvetica", spaceAfter=3, leading=13),
    "tbl_hdr":     style("tbl_hdr",     fontSize=9,  textColor=WHITE, fontName="Helvetica-Bold", leading=13),
    "tbl_cell":    style("tbl_cell",    fontSize=9,  textColor=BLACK, fontName="Helvetica", leading=13),
}

thinB = {"style": 1, "size": 1, "color": colors.HexColor("#CCCCCC")}
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus.flowables import HRFlowable as HR
bd = colors.HexColor("#CCCCCC")
from reportlab.lib import colors as C
BORDER = (0.3, bd)

def cellpad(t, extra=None):
    base_style = [
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
        ("RIGHTPADDING",  (0,0), (-1,-1), 8),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
    ]
    if extra: base_style += extra
    t.setStyle(TableStyle(base_style))
    return t

def gap(h=6): return Spacer(1, h)

def callout(text, bg=BLUE_LIGHT, fg=BLUE_DARK):
    t = Table([[Paragraph(text, style("_cb", fontSize=10, textColor=fg, fontName="Helvetica", leading=14))]], colWidths=[CW])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING", (0,0), (-1,-1), 12), ("RIGHTPADDING", (0,0), (-1,-1), 12),
    ]))
    return t

def before_after(before, after):
    lw = (CW - 4) / 2
    rows = [[
        Paragraph("<b><font color='#791F1F'>&#10007;  Before</font></b><br/><br/>" +
                  f"<i><font color='#791F1F'>{before}</font></i>",
                  style("_ba", fontSize=9, fontName="Helvetica", leading=14)),
        Paragraph("<b><font color='#085041'>&#10003;  After</font></b><br/><br/>" +
                  f"<font color='#085041'>{after}</font>",
                  style("_ba2", fontSize=9, fontName="Helvetica", leading=14)),
    ]]
    t = Table(rows, colWidths=[lw, lw], spaceBefore=4, spaceAfter=6)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), RED_LIGHT),
        ("BACKGROUND", (1,0), (1,-1), TEAL_LIGHT),
        ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("VALIGN", (0,0), (-1,-1), "TOP"), ("GRID", (0,0), (-1,-1), 0.3, WHITE),
    ]))
    return t

def std_table(headers, rows, col_widths=None, hdr_bg=TEAL):
    if col_widths is None: col_widths = [CW/len(headers)]*len(headers)
    data = [[Paragraph(h, S["tbl_hdr"]) for h in headers]]
    for row in rows:
        data.append([Paragraph(str(c), S["tbl_cell"]) for c in row])
    t = Table(data, colWidths=col_widths, spaceBefore=4, spaceAfter=6)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), hdr_bg),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, GRAY_LT]),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#CCCCCC")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    return t

def part_banner(number, title, subtitle):
    t = Table([[
        Paragraph(f"PART {number}", style("_pn", fontSize=9, textColor=colors.HexColor("#9FE1CB"), fontName="Helvetica-Bold", leading=12)),
    ],[
        Paragraph(title, S["part"]),
    ],[
        Paragraph(subtitle, S["part_sub"]),
    ]], colWidths=[CW])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), TEAL),
        ("TOPPADDING", (0,0), (-1,-1), 3), ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("LEFTPADDING", (0,0), (-1,-1), 14), ("RIGHTPADDING", (0,0), (-1,-1), 14),
    ]))
    return KeepTogether([gap(8), t, gap(6)])

def section_header(label, title, is_new=False):
    lbl = label.upper()
    if is_new:
        lbl += "   •   NEW IN V2"
    return KeepTogether([
        gap(10),
        Paragraph(lbl, S["day_label"]),
        Paragraph(title, S["h2"]),
        HRFlowable(width="100%", thickness=0.5, color=TEAL, spaceAfter=6, spaceBefore=2),
    ])

def insight_box(text):
    return callout(f"<b>Key insight:</b> {text}", bg=BLUE_LIGHT, fg=BLUE_DARK)

def pmi_table(plus, minus, interesting):
    w = CW/3
    rows = [[
        Paragraph(f"<b><font color='#085041'>Plus</font></b><br/><br/><font color='#0F6E56'>{plus}</font>", style("_p", fontSize=9, fontName="Helvetica", leading=14)),
        Paragraph(f"<b><font color='#791F1F'>Minus</font></b><br/><br/><font color='#993C1D'>{minus}</font>", style("_m", fontSize=9, fontName="Helvetica", leading=14)),
        Paragraph(f"<b><font color='#3C3489'>Interesting</font></b><br/><br/><font color='#534AB7'>{interesting}</font>", style("_i", fontSize=9, fontName="Helvetica", leading=14)),
    ]]
    t = Table(rows, colWidths=[w,w,w], spaceBefore=4, spaceAfter=6)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), TEAL_LIGHT),
        ("BACKGROUND", (1,0), (1,-1), RED_LIGHT),
        ("BACKGROUND", (2,0), (2,-1), PURPLE_L),
        ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("VALIGN", (0,0), (-1,-1), "TOP"), ("GRID", (0,0), (-1,-1), 0.3, WHITE),
    ]))
    return t

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(TEAL); canvas.setLineWidth(0.5)
    canvas.line(MARGIN, H-0.5*inch, W-MARGIN, H-0.5*inch)
    canvas.setFont("Helvetica", 8); canvas.setFillColor(GRAY_MD)
    canvas.drawString(MARGIN, H-0.42*inch, "Executive Presence — Communication Frameworks")
    canvas.drawRightString(W-MARGIN, H-0.42*inch, "Version 2  ·  12 Frameworks")
    canvas.setStrokeColor(colors.HexColor("#DDDDDD"))
    canvas.line(MARGIN, 0.55*inch, W-MARGIN, 0.55*inch)
    canvas.drawCentredString(W/2, 0.38*inch, f"Page {doc.page}")
    canvas.restoreState()

def on_first(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#DDDDDD"))
    canvas.line(MARGIN, 0.55*inch, W-MARGIN, 0.55*inch)
    canvas.setFont("Helvetica", 8); canvas.setFillColor(GRAY_MD)
    canvas.drawCentredString(W/2, 0.38*inch, f"Page {doc.page}")
    canvas.restoreState()

story = []

# ── COVER ─────────────────────────────────────────────────────────────────────
story += [
    gap(36),
    Paragraph("Executive Presence", S["cover_title"]),
    Paragraph("Communication Frameworks Reference Guide", S["cover_sub"]),
    Paragraph("Version 2  ·  12 Frameworks", S["cover_tag"]),
    gap(8),
    HRFlowable(width="100%", thickness=2, color=TEAL, spaceAfter=14),
    std_table(
        ["Group", "Frameworks", "What it governs"],
        [
            ["Structure",   "BLUF · Minto Pyramid · C·D·S", "How you organise what you say"],
            ["Thinking",    "PMI · SCR · Story Structure", "How you reason and frame"],
            ["Interaction", "Decisive Answering · Meeting Lead · A·D·A · Read Before You Respond", "How you handle live exchange"],
            ["Embodiment",  "Pause Principle · Consistency Compound", "How you deliver, and what compounds"],
        ],
        col_widths=[CW*0.16, CW*0.48, CW*0.36]
    ),
    gap(10),
    callout(
        "A Center for Talent Innovation survey found 89% of executives believe executive presence directly "
        "contributes to career advancement — but 81% of people told to &#8220;improve their executive presence&#8221; "
        "had no idea what to do with that feedback. These frameworks exist to make it concrete and practisable.",
        bg=GRAY_LT, fg=GRAY_DK
    ),
    gap(20),
    PageBreak(),
]

# ── PART ONE ──────────────────────────────────────────────────────────────────
story += [part_banner("ONE", "Structure", "How you organise what you say")]

story += [
    section_header("Framework 1", "Bottom Line Up Front (BLUF)"),
    Paragraph("State your answer or recommendation first. Explain why second. Executives read top-down — never make them wait for your point.", S["body"]),
    before_after(
        "We looked at the data, ran the analysis, considered all the options, and after everything we think maybe we should go with Option B...",
        "We should go with Option B. It cuts cost by 20% with acceptable risk. Here&#39;s why."
    ),
    before_after(
        "There were some challenges with the launch timeline and after talking to the team we realised there might be a delay...",
        "The launch will slip by 2 weeks. Root cause is 3 unresolved blockers in QA. Here&#39;s the recovery plan."
    ),
    insight_box("If someone stopped reading after your first sentence, would they still know what you want? If no — rewrite."),
]

story += [
    section_header("Framework 2", "Minto Pyramid Principle"),
    Paragraph("Structure any message so an exec can stop reading at any level and still have what they need.", S["body"]),
    Paragraph("<b>Vertical logic</b> — each point answers &#8220;Why?&#8221; from the level above. &nbsp; <b>Horizontal MECE</b> — points at the same level are mutually exclusive and collectively exhaustive.", S["body"]),
    std_table(
        ["Level", "Content", "Example"],
        [
            ["Governing thought", "Your single recommendation or answer", "Cloud costs jumped 40% due to 3 controllable issues — fix plan recovers 25% in 30 days."],
            ["Key arguments (×3)", "MECE reasons that answer &#8220;why?&#8221;", "Untagged dev envs · Misconfigured auto-scaling · No reserved instances"],
            ["Supporting data", "Evidence that proves each argument", "~$8K/mo waste · Triggered 8× unnecessarily · 35% savings on switch"],
        ],
        col_widths=[CW*0.2, CW*0.3, CW*0.5]
    ),
    insight_box("Write bottom-up if you need to think it through. Send top-down always."),
]

story += [
    section_header("Framework 3", "Talk With Data (C·D·S)"),
    Paragraph("Numbers make claims credible. Vague language makes them dismissible.", S["body"]),
    std_table(
        ["", "Element", "What it means"],
        [
            ["C", "Claim",   "Your point — the assertion you're making"],
            ["D", "Data",    "The specific number that proves it. No vague qualifiers."],
            ["S", "So what", "The implication or decision it drives"],
        ],
        col_widths=[CW*0.08, CW*0.2, CW*0.72]
    ),
    std_table(
        ["Vague", "Precise"],
        [
            ["&#8220;The team has been a bit slow&#8221;", "Velocity fell 38% over six weeks (34 → 21 story points/sprint), driven by 3 engineers out."],
            ["&#8220;We're going to be a bit late&#8221;",  "v2.0 ships Oct 3 — 21 days past the Sept 12 target."],
            ["&#8220;A lot of customers complained&#8221;", "38 support tickets in 72 hrs — 3× our weekly average."],
        ],
        col_widths=[CW*0.32, CW*0.68]
    ),
    Paragraph("<b>No exact number?</b> Use a range — &#8220;between 15–25%&#8221; beats &#8220;quite a bit.&#8221; Or anchor: &#8220;roughly 2× what we saw in Q1.&#8221;", S["body"]),
    insight_box("Stop reaching for adjectives (slow, late, bad). Reach for numbers."),
    PageBreak(),
]

# ── PART TWO ──────────────────────────────────────────────────────────────────
story += [part_banner("TWO", "Thinking", "How you reason and frame")]

story += [
    section_header("Framework 4", "PMI (de Bono)"),
    Paragraph("Use PMI to <i>think</i>. Use the Minto Pyramid to <i>present</i>. Showing you've stress-tested both sides earns trust.", S["body"]),
    pmi_table(
        "Genuine upsides — value created, problems solved. Be specific with data.",
        "Real downsides — cost, risk, what breaks. Name the probability or cost.",
        "Questions raised, dependencies, second-order effects. Neither good nor bad yet."
    ),
    Paragraph("<b>Example — hiring decision:</b>", S["h3"]),
    pmi_table(
        "Restores velocity toward v2.0 (21→34+ pts/sprint). Reduces burnout on 8-person team at 112% load.",
        "~$90K/mo additional burn. Runway shrinks 14→11 months. 60–90 day ramp delays gains.",
        "Does hiring signal confidence or concern to investors? Can we hire contract first as a hedge?"
    ),
    callout("<b>Recommendation:</b> <i>Hire 2 now (not 3) — targeting roles that unblock v2.0. $60K/mo buys back 12+ weeks of velocity without fully stressing runway.</i>", bg=TEAL_LIGHT, fg=TEAL),
    insight_box("A strong Interesting column is the mark of a senior thinker. Don't leave it blank."),
]

story += [
    section_header("Framework 5", "SCR Narrative Arc"),
    Paragraph("Logic convinces. Story moves people to act.", S["body"]),
    std_table(
        ["Part", "Purpose"],
        [
            ["S — Situation",    "The stable context everyone agrees on. No tension yet."],
            ["C — Complication", "The disruption. What changed, what's at risk. The &#8220;Why does this matter?&#8221; moment."],
            ["R — Resolution",   "What we do about it. Your BLUF recommendation, with context and urgency behind it."],
        ],
        col_widths=[CW*0.28, CW*0.72]
    ),
    before_after(
        "We need to hire 2 engineers. Here are 3 reasons: velocity is down, the bug backlog is growing, and v2.0 is delayed.",
        "[S] We built a team capable of shipping every quarter. [C] Over the last six weeks, three engineers left simultaneously and velocity dropped 38%. [R] To get back on track without stressing runway, we should hire 2 senior engineers now."
    ),
    callout("<b>The complication is the most important sentence you'll write.</b> &#8220;Sales are up&#8221; is a situation. &#8220;Sales are up but NPS dropped 12 points — we're growing into a churn problem&#8221; is a complication.", bg=AMBER_L, fg=AMBER_D),
    insight_box("SCR and Minto nest — use SCR to open, Minto to structure the recommendation inside the Resolution."),
]

story += [
    section_header("Framework 6", "Story Structure"),
    Paragraph("People remember stories. They forget slides.", S["body"]),
    std_table(
        ["Part", "Purpose", "Test"],
        [
            ["Hook",          "Grab attention in the first sentence", "Would someone lean forward or check their phone?"],
            ["Context",       "Set the stakes",                        "Is there real tension — something at risk?"],
            ["Insight",       "The thing they couldn't see before",    "Is this a reframe, or just restating data?"],
            ["Call to action","One specific ask",                      "Is it a decision, or vague &#8220;let's discuss&#8221;?"],
        ],
        col_widths=[CW*0.2, CW*0.4, CW*0.4]
    ),
    Paragraph("<b>4 types of hook:</b> Surprising stat · Specific moment · Provocative question · Sharp contrast", S["body"]),
    callout(
        "<b>Example — enterprise pivot all-hands:</b><br/><br/>"
        "<b>Hook:</b> <i>&#8220;Eighteen customers are generating more revenue than twelve hundred.&#8221;</i><br/><br/>"
        "<b>Context:</b> <i>&#8220;Self-serve: 1,240 customers, 34% annual churn, competitors cutting prices 30%. "
        "Enterprise: 18 deals in six months, 6% churn, $87K average ARR. Top 10 accounts = 58% of revenue.&#8221;</i><br/><br/>"
        "<b>Insight:</b> <i>&#8220;Enterprise costs 4&#215; more to serve — but LTV is 22&#215; higher. We've been optimising for volume, not value.&#8221;</i><br/><br/>"
        "<b>CTA:</b> <i>&#8220;Leave today with one commitment to something you'll do differently next quarter.&#8221;</i>",
        bg=PURPLE_L, fg=PURPLE_D
    ),
    insight_box("The audience is the hero — not you."),
    PageBreak(),
]

# ── PART THREE ────────────────────────────────────────────────────────────────
story += [part_banner("THREE", "Interaction", "How you handle live exchange")]

story += [
    section_header("Framework 7", "Decisive Answering"),
    Paragraph("Three valid answers exist. Everything else is hedging.", S["body"]),
    std_table(
        ["Answer", "How to use it"],
        [
            ["Yes", "State it. Say what it means or what happens next."],
            ["No",  "State it. Give the reason and what you'd recommend instead."],
            ["I'll find out by [time]", "Own the gap. Commit to a specific time — not &#8220;soon&#8221; or &#8220;ASAP&#8221;."],
        ],
        col_widths=[CW*0.28, CW*0.72]
    ),
    Paragraph("<b>Avoid:</b> &#8220;It depends&#8221; · &#8220;That's a good question&#8221; · &#8220;I'm not totally sure but...&#8221; · &#8220;We'll have to see&#8221;", S["body"]),
    callout("<b>Example:</b> &#8220;Should we discount 20% to close this quarter?&#8221;<br/><i>&#8220;No. At 20% we're below our floor margin on this deal tier. I'd offer 10% with extended payment terms — that closes the quarter and protects margin.&#8221;</i>", bg=TEAL_LIGHT, fg=TEAL),
    insight_box("Credibility = saying + doing. If you commit to &#8220;I'll find out by Thursday,&#8221; Thursday must deliver."),
]

story += [
    section_header("Framework 8", "Leading Meetings"),
    Paragraph("How you open a meeting signals whether you're running it or just attending it.", S["body"]),
    std_table(
        ["Sentence", "Template"],
        [
            ["1", "&#8220;We're here to <b>decide</b> [specific decision].&#8221; <i>(not &#8220;discuss&#8221;)</i>"],
            ["2", "&#8220;My recommendation is [clear stance] — [1-line reason with data].&#8221;"],
            ["3", "&#8220;I want to hear your [concerns] and we need to leave with [specific outcome].&#8221;"],
        ],
        col_widths=[CW*0.1, CW*0.9]
    ),
    before_after(
        "&#8220;Thanks everyone for joining. So, um, we wanted to get together to talk about the pricing question and kind of hear everyone&#39;s thoughts. Who wants to start?&#8221;",
        "&#8220;We're here to decide whether to raise prices 8% in Q1. My recommendation is yes — I'll share why in 2 minutes, then I want to hear your pushback. We need a decision by end of this call.&#8221;"
    ),
    insight_box("&#8220;We're here to decide X&#8221; (not &#8220;discuss X&#8221;) — discussion is the means; the decision is the point."),
]

story += [
    section_header("Framework 9", "Handling Pushback (A·D·A)"),
    Paragraph("Hold your ground without being defensive. Update without caving.", S["body"]),
    std_table(
        ["Step", "What to do"],
        [
            ["A — Acknowledge",      "Show you heard the concern. Don't dismiss, don't immediately counter."],
            ["D — Data",             "Respond with evidence, not a restated opinion louder."],
            ["A — Affirm or Adjust", "Restate if you still believe it. Update openly if they raised genuinely new information."],
        ],
        col_widths=[CW*0.28, CW*0.72]
    ),
    std_table(
        ["Caving", "Updating"],
        [
            ["Changing position because someone pushed harder or is more senior", "Changing position because they introduced new data or a valid argument"],
            ["Destroys credibility", "Builds credibility"],
        ],
        col_widths=[CW*0.5, CW*0.5], hdr_bg=RED_DARK
    ),
    callout(
        "<b>Hold:</b> <i>&#8220;Brand value is real — I'm not dismissing it. But we can't currently measure it. "
        "What I can measure is $80K generated 3 qualified leads — $26K per lead vs. our $3–4K paid benchmark. "
        "I'm holding my recommendation.&#8221;</i><br/><br/>"
        "<b>Update:</b> <i>&#8220;That changes my recommendation. A $280K renewal risk wasn't in my analysis. "
        "SSO moves to the front of the sprint.&#8221;</i>",
        bg=TEAL_LIGHT, fg=TEAL
    ),
    insight_box("You must know, in the moment, whether you're caving or updating. They feel similar from the inside."),
]

story += [
    section_header("Framework 10", "Read Before You Respond", is_new=True),
    Paragraph("Executive presence is not only what you say — it's what you understood before you spoke. "
              "Research consistently identifies two listening-side traits: a &#8220;listen to learn&#8221; orientation "
              "and the ability to read an audience. Most communication training ignores both.", S["body"]),

    Paragraph("<b>Move 1 — Ask one question before you advocate</b>", S["h3"]),
    Paragraph("Before making your case in a contested room, surface what you don't know about their position. This is not softness — it's reconnaissance.", S["body"]),
    callout("<i>&#8220;Before I give you my view — what's driving the concern on your side? I want to make sure I'm solving the right problem.&#8221;</i>", bg=GRAY_LT, fg=GRAY_DK),

    Paragraph("<b>Move 2 — Reframe for the audience</b>", S["h3"]),
    Paragraph("Same recommendation, different lead. Lead with what they optimise for.", S["body"]),
    std_table(
        ["Audience", "They optimise for", "Lead with"],
        [
            ["CFO",          "Cost, risk, predictability",         "The number and the downside protection"],
            ["CEO",          "Strategy, speed, market position",   "The strategic bet and what it unlocks"],
            ["Engineering",  "Feasibility, technical debt",        "The constraint and what you're protecting"],
            ["Sales",        "Pipeline, timing, competition",      "The customer impact and the timeline"],
            ["Your team",    "Workload, priority, meaning",        "What changes for them and what you're removing"],
        ],
        col_widths=[CW*0.18, CW*0.35, CW*0.47]
    ),
    callout(
        "<b>Same recommendation — &#8220;pause feature work for one sprint&#8221;:</b><br/><br/>"
        "<b>To the CFO:</b> <i>&#8220;Two weeks of debt work now avoids an estimated 8–10 weeks of reactive cost next quarter.&#8221;</i><br/>"
        "<b>To the CEO:</b> <i>&#8220;We're one incident away from an enterprise churn event. This protects the segment we're betting on.&#8221;</i><br/>"
        "<b>To the team:</b> <i>&#8220;I'm clearing the roadmap for two weeks so you can fix what's been bothering you. Nothing new gets added.&#8221;</i>",
        bg=CORAL_L, fg=CORAL_D
    ),

    Paragraph("<b>Move 3 — Name what you heard before you counter</b>", S["h3"]),
    Paragraph("Before disagreeing, prove you understood. Two effects: you're demonstrably listening, and you often discover you misread the objection.", S["body"]),
    callout("<i>&#8220;So the concern is that pausing features signals to customers that we're slowing down. Is that the core worry, or is there more?&#8221;</i>", bg=GRAY_LT, fg=GRAY_DK),

    insight_box("The most senior person in the room is often the one asking the sharpest question, not giving the longest answer."),
    PageBreak(),
]

# ── PART FOUR ─────────────────────────────────────────────────────────────────
story += [part_banner("FOUR", "Embodiment", "How you deliver, and what compounds over time")]

story += [
    section_header("Framework 11", "The Pause Principle", is_new=True),
    Paragraph("The best-structured argument, delivered at speed with rising intonation and no pauses, still reads as junior. "
              "Delivery is not decoration — it is a signal about how much you trust your own content.", S["body"]),

    std_table(
        ["Habit", "What it does"],
        [
            ["<b>Pause before answering</b>",     "Two seconds of silence signals consideration. &#8220;So, um, that's a great question...&#8221; signals you're buying time."],
            ["<b>Pause after your recommendation</b>", "Say it. Then stop. Rushing to justify is the most common tell of low confidence."],
            ["<b>Land your sentences</b>",        "Upward inflection turns a statement into a question. &#8220;We should ship Friday?&#8221; ≠ &#8220;We should ship Friday.&#8221;"],
            ["<b>Slow down as stakes rise</b>",   "The default under pressure is to speed up. Drop your pace ~20%. It reads as control."],
        ],
        col_widths=[CW*0.3, CW*0.7]
    ),

    Paragraph("<b>Quick self-audit</b>", S["h3"]),
    std_table(
        ["Tell", "Fix"],
        [
            ["&#8220;So, um...&#8221; before answering",             "Pause instead. Silence beats filler."],
            ["Justifying immediately after your recommendation", "Stop talking. Let it land."],
            ["Statements ending in upward pitch",                "Land the sentence. Drop the tone."],
            ["Speaking faster when challenged",                  "Deliberately slow to ~80% of normal pace."],
            ["Trailing off at the end of a point",               "Finish the sentence fully, then stop."],
        ],
        col_widths=[CW*0.45, CW*0.55], hdr_bg=AMBER_D
    ),
    insight_box("How you deliver is a claim about how much you believe what you're saying. Rushed delivery undermines even a perfect argument."),
]

story += [
    section_header("Framework 12", "The Consistency Compound", is_new=True),
    Paragraph("Research separates two categories of perception: <b>short-term impressions</b> (appearance, confidence, "
              "communication style — assessed in seconds) and <b>long-term evaluations</b> (interpersonal integrity, "
              "values in action, outcome delivery ability — built over months).", S["body"]),
    Paragraph("Frameworks 1–11 optimise for the moment. This one optimises for the accumulation. It is the only framework "
              "you cannot practise in a single session — and it outweighs all the others combined.", S["body"]),

    std_table(
        ["Behaviour", "What it means in practice"],
        [
            ["<b>Outcome delivery</b>",      "Every &#8220;I'll get back to you by Thursday&#8221; is a credibility contract. Kept, it compounds. Broken, it discounts everything you say afterwards. Only commit to timelines you'd bet money on."],
            ["<b>Values in action</b>",      "People judge your values by your behaviour when holding them costs you something. Do you credit the team when you presented the win? Do you give the honest recommendation when it's unpopular?"],
            ["<b>Consistency across audiences</b>", "Whether you say the same thing to your team, your manager, and your peers. Presence collapses fast when people compare notes and find three versions of your position."],
        ],
        col_widths=[CW*0.26, CW*0.74]
    ),

    Paragraph("<b>The quarterly check</b>", S["h3"]),
    callout(
        "1. What did I commit to this quarter, and did I deliver it?<br/>"
        "2. Where did my stated values and my actual behaviour diverge?<br/>"
        "3. Would my team, manager, and peers describe my position on [key issue] the same way?<br/>"
        "4. What did I get wrong, and did I say so out loud?",
        bg=PURPLE_L, fg=PURPLE_D
    ),
    insight_box("Executive presence built on delivery compounds. Executive presence built only on communication style depreciates the moment someone checks your track record."),
    PageBreak(),
]

# ── QUICK REFERENCE ───────────────────────────────────────────────────────────
story += [
    Paragraph("Quick Reference", S["h2"]),
    HRFlowable(width="100%", thickness=0.5, color=TEAL, spaceAfter=8, spaceBefore=2),
    std_table(
        ["#", "Framework", "When to use", "Core rule"],
        [
            ["1",  "BLUF",                   "Any written or verbal update",         "Answer first, explain second"],
            ["2",  "Minto Pyramid",          "Emails, briefs, structured arguments", "Governing answer → MECE arguments → data"],
            ["3",  "C·D·S",                  "Status updates, proposals",            "Claim + Data + So what"],
            ["4",  "PMI",                    "Decisions, trade-off analysis",        "Plus / Minus / Interesting → recommend"],
            ["5",  "SCR",                    "Meeting openings, exec summaries",     "Situation → Complication → Resolution"],
            ["6",  "Story Structure",        "All-hands, investor updates",          "Hook → Context → Insight → CTA"],
            ["7",  "Decisive Answering",     "Any direct question",                  "Yes / No / I'll find out by [time]"],
            ["8",  "Meeting Lead",           "Opening any meeting",                  "Decide, not discuss — stance in 3 sentences"],
            ["9",  "A·D·A",                  "Any pushback or challenge",            "Acknowledge → Data → Affirm or Adjust"],
            ["10", "Read Before You Respond","Contested rooms, cross-functional",    "Ask first · Reframe for audience · Name what you heard"],
            ["11", "Pause Principle",        "Every spoken interaction",             "Pause before · Pause after · Land it · Slow down"],
            ["12", "Consistency Compound",   "Ongoing, across quarters",             "Deliver what you committed. Same position to every audience."],
        ],
        col_widths=[CW*0.05, CW*0.22, CW*0.3, CW*0.43]
    ),
    gap(12),
    callout(
        "<b>The through-line:</b> Use <b>PMI</b> to think → <b>Minto</b> to structure → <b>SCR</b> to open → "
        "<b>C·D·S</b> to anchor every claim → <b>Read Before You Respond</b> to understand the room → "
        "<b>Decisive Answering</b> for questions → <b>A·D·A</b> for challenges → <b>Meeting Lead</b> to run the room → "
        "<b>Story Structure</b> to make it stick → <b>Pause Principle</b> to deliver it → and let the "
        "<b>Consistency Compound</b> do the work no single conversation can.<br/><br/>"
        "<i>Executive presence is not a personality trait. It is a set of practised habits — and the ones that "
        "compound matter more than the ones that impress.</i>",
        bg=GRAY_LT, fg=GRAY_DK
    ),
    gap(12),
    Paragraph("Sources informing v2", S["h3"]),
    Paragraph("Barbara Minto, <i>The Pyramid Principle</i> · Edward de Bono, PMI thinking tool · "
              "Sylvia Ann Hewlett, &#8220;The New Rules of Executive Presence,&#8221; <i>Harvard Business Review</i> (2024) · "
              "Dagley &amp; Gaskin, &#8220;Understanding Executive Presence,&#8221; <i>Consulting Psychology Journal</i> 66(3) (2014) · "
              "Chilcutt &amp; DuPont, <i>The Presence Principle</i> (2026) · MIT Sloan Executive Education (2026) · IMD (2026)",
              S["small"]),
]

doc = SimpleDocTemplate(
    "executive-presence-frameworks.pdf",
    pagesize=letter,
    leftMargin=MARGIN, rightMargin=MARGIN,
    topMargin=0.75*inch, bottomMargin=0.75*inch,
    title="Executive Presence — Communication Frameworks (v2)",
    author="",
)
doc.build(story, onFirstPage=on_first, onLaterPages=on_page)
print("Done")
