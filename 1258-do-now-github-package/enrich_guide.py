#!/usr/bin/env python3
"""Flow enriched do-now-assets READMEs into the standalone master guide HTML."""
import html, re, pathlib

ROOT = pathlib.Path(__file__).parent
ASSETS = ROOT / "do-now-assets"
GUIDE = ROOT / "1258-Workbook-Standalone.html"

def md_inline(s):
    s = html.escape(s.strip())
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s

def section(text, name):
    m = re.search(rf"## {re.escape(name)}\n(.*?)(?=\n## |\n\*\*Solution link|\Z)", text, re.S)
    return m.group(1).strip() if m else ""

# Columns in activity-section tables that leak answers; participants fill these in.
# Solutions live in the answer key at the end of the guide.
# anchor -> {exact header text: new header text}; cells in those columns are emptied.
BLANK_SPEC = {
    # all 13 "Board items" tables share the Expected / cue column
    **{a: {"Expected / cue": "Your answer"} for a in [
        "activity-0-3", "activity-1-a", "activity-1-c", "activity-2-b", "activity-3-c",
        "activity-5-b", "activity-5-c", "activity-5-d", "activity-6-c", "activity-7-d",
        "activity-8-a", "activity-b-x"]},
    "activity-1-b": {"CIO version cue": "Your CIO version", "Citizen version cue": "Your citizen version"},
    "activity-2-a": {"Expected habit": "Your verdict + evidence"},
    "activity-4-a": {"Example 1": "Your example 1", "Example 2": "Your example 2"},
    "activity-4-b": {"Role to assign": "Your role", "Output contract": "Your output contract"},
    "activity-4-c": {"Required shape": "Your required shape"},
    "activity-4-d": {"Ask answerable": "Your answerable question", "Ask unanswerable": "Your unanswerable question",
                      "Expected failure handling": "What happens without the rule?"},
    "activity-6-a": {"Issue to spot": "Your issue tags"},
    "activity-6-b": {"Field": "Field", "Type": "Type", "Why needed": "Why needed"},  # whole body is the answer key
    "activity-6-d": {"Prompt line": "Your prompt line"},
    "activity-7-b": {"Compute": "Your computation"},
    "activity-7-c": {"Minimum header": "Your minimum header"},
}

def blank_answer_cells(sec, anchor):
    spec = BLANK_SPEC.get(anchor)
    if not spec:
        return sec
    def fix_table(m):
        table = m.group(0)
        headers = re.findall(r"<th>(.*?)</th>", table)
        blank_idx = {i for i, h in enumerate(headers) if h in spec}
        if not blank_idx:
            return table
        for i in blank_idx:
            table = table.replace(f"<th>{headers[i]}</th>", f"<th>{spec[headers[i]]}</th>", 1)
        def fix_row(rm):
            parts = re.split(r"(<td>.*?</td>)", rm.group(0), flags=re.S)
            ci = -1
            for k, part in enumerate(parts):
                if part.startswith("<td>"):
                    ci += 1
                    if ci in blank_idx:
                        parts[k] = "<td></td>"
            return "".join(parts)
        return re.sub(r"<tr>(?!<th).*?</tr>", fix_row, table, flags=re.S)
    return re.sub(r"<table>.*?</table>", fix_table, sec, flags=re.S)

# 🌐 Copilot-in-the-browser paragraph, keyed by activity anchor — only where it genuinely applies.
COPILOT = {
    "activity-0-2": "Write your baseline prompt P0 by actually running it once in your agency's Copilot (web or Edge sidebar) before class — the honest “before” sample is the whole point. Keep the prompt and output private.",
    "activity-0-3": "The approved tool in these scenarios maps to your agency-licensed Copilot with commercial data protection — but “approved tool” never means “any data.” Apply the same public / internal / personal test before pasting anything.",
    "activity-1-b": "Draft both versions in Copilot, then edit them yourself — Copilot is good at audience switching, but the skill you are practicing is judging whether each version is right for its reader.",
    "activity-2-a": "Ask Copilot for the source of each claim — its web-grounded answers include citations, but treat them as leads: open the cited page yourself and check the date and baseline before you post SUPPORTED.",
    "activity-2-c": "Copilot will happily suggest dataset names and URLs — that is exactly the trap this exercise trains: never repost a link you have not opened yourself in the same browser.",
    "activity-2-d": "Use Copilot to shortlist candidate datasets (“open data for &lt;your program area&gt;”), then bookmark only pages you opened and confirmed yourself.",
    "activity-3-a": "Paste the paragraph into Copilot with the reader named in the prompt (“for a deputy minister” / “for a resident with no policy background”) and compare its draft with yours — where did it over- or under-simplify?",
    "activity-3-b": "Ask Copilot to render the process as a Mermaid diagram or indented outline, then hunt for steps it invented — AI-generated diagrams always need a human diff against the source text.",
    "activity-3-c": "This is literally the Copilot question: your agency's browser Copilot runs under a government agreement, but that only settles which account is approved — the data-class test (public / internal / personal) still decides what you may paste.",
    "activity-3-d": "Your inventory contrast: agency-licensed Copilot in the browser is the sanctioned path; anything reached through personal accounts or unapproved tools goes in the shadow-AI column, even when it feels identical to use.",
    "activity-4-a": "Build your two examples once in Copilot and watch how the answer changes when examples are present — few-shot prompting works exactly the same way there.",
    "activity-4-b": "Copilot honors role + contract prompts: “You are a government records officer. Return … in 5 bullets” works verbatim in the browser chat — try your final version there after the exercise.",
    "activity-4-c": "Copilot can output tables and JSON on demand; the lesson transfers directly — state the columns you want, in the order you want them, or it will choose for you.",
    "activity-4-d": "You can paste this public excerpt into Copilot with your grounding rule (“answer only from this text; if not stated, say not stated”) — a safe, realistic way to see grounded answering work, since the excerpt contains no sensitive data.",
    "activity-5-d": "Copilot ships with injection defenses — after class, try A1-style phrasing on a harmless prompt and observe the refusal. Knowing what a blocked attack looks like helps you recognize unblocked ones elsewhere.",
    "activity-6-b": "Copilot is a decent schema-drafting partner: describe your 311-style rows and ask for field names, types, and justifications — then apply the same critique you used here.",
    "activity-6-d": "Your cleaning prompt can run in Copilot over small, non-sensitive samples; for real agency data the same prompt belongs in an approved pipeline, not a browser chat.",
    "activity-7-b": "Let Copilot do the arithmetic chain (users × requests × tokens × days), then change one assumption and recompute — sensitivity, not the point estimate, is the skill.",
    "activity-7-c": "The discipline transfers unchanged: keep one named, versioned prompt with its tests, and reuse that exact prompt in Copilot every time rather than retyping variations.",
    "activity-7-d": "Copilot's web-grounded mode is RAG in action: it retrieves pages, then reasons over them — watch for retrieval fails (wrong or stale page) vs reasoning fails (right page, wrong conclusion), exactly as you sorted here.",
    "activity-8-d": "Ask Copilot the question, then verify on the official agency or Federal Register page — Copilot is the fast first pass; the authoritative site is the verdict.",
    "activity-9-a": "Run your rewritten P10 in Copilot and compare it against the P0 output you saved in Do Now 0.2 — that before/after pair is your personal evidence that prompt craft changes results.",
    "activity-9-b": "A strong first use case for most teams is shaped exactly like Copilot's strengths: drafting, summarizing, and triaging text your staff already produce, with a human reviewing before anything leaves the building.",
    "activity-9-c": "Name which guardrails Copilot already gives you (tenant boundary, commercial data protection, no training on your data) and which you must still own yourself (review before sending, grounding, approved data only).",
}

# 🛡️ MITRE ATLAS link + relevance paragraph for security/governance activities.
# anchor -> (url, link label, relevance text)
ATLAS = {
    "activity-5-a": ("https://atlas.mitre.org/", "MITRE ATLAS matrix",
        "The eight risks you just ranked (R1 to R8) are not hypothetical: each maps to techniques in MITRE ATLAS, the public knowledge base of real attacks against AI systems. Open the matrix, find the technique that matches your top-ranked risk, and read across the tactics row to see how such an attack typically unfolds from reconnaissance to impact. That is exactly the context a funding decision needs."),
    "activity-5-b": ("https://atlas.mitre.org/techniques/AML.T0024.000", "ATLAS AML.T0024.000: Infer Training Data Membership",
        "This documented technique shows an attacker asking an AI system ordinary-looking questions to learn whether a specific person's record was in the training data. It is a pure confidentiality failure with no server breach involved, which makes it a concrete example of why the C in CIA deserves its own column when the asset is a model rather than a database."),
    "activity-5-c": ("https://atlas.mitre.org/studies", "ATLAS case studies",
        "The ATLAS case studies catalog real AI incidents at operating organizations, not lab demos. Reading one study before you screen your own use case makes 'high-impact' concrete: these documented harms are what OMB's screening questions are designed to catch before deployment."),
    "activity-5-d": ("https://atlas.mitre.org/techniques/AML.T0051.000", "ATLAS AML.T0051.000: LLM Prompt Injection, Direct",
        "Every attack sticky in this exercise is an instance of ATLAS technique AML.T0051, the cataloged technique for crafted prompts that make a model act outside its intended rules. The page lists real-world procedures and mitigations, so your success/fail calls on the board map directly onto how practitioners classify and defend these attacks."),
    "activity-5-x": ("https://atlas.mitre.org/mitigations", "ATLAS mitigations",
        "ATLAS pairs every attack technique with mitigations, and each mitigation implies the lifecycle stage where it belongs, from data preparation to deployment monitoring. Comparing that list with your workflow map shows which stages in your process currently carry no named mitigation and no owner."),
    "activity-9-c": ("https://atlas.mitre.org/mitigations/AML.M0003", "ATLAS AML.M0003: Predictive AI Model Hardening",
        "This mitigation is an example of a guardrail with a name, an owner, and a scope, which is exactly the shape your guardrail needs. Browse how ATLAS writes it up: a guardrail that cannot be stated this precisely is usually a wish, not a control."),
}

# Activity time budget in minutes, by complexity (5 = quick sort/post, 7 = standard, 8 = multi-step, 10 = build/critique)
TIME = {
 "activity-0-1": 5, "activity-0-2": 5, "activity-0-3": 7,
 "activity-1-a": 7, "activity-1-b": 5, "activity-1-c": 7, "activity-1-d": 7,
 "activity-2-a": 7, "activity-2-b": 8, "activity-2-c": 7, "activity-2-d": 5,
 "activity-3-a": 5, "activity-3-b": 8, "activity-3-c": 7, "activity-3-d": 8,
 "activity-4-a": 7, "activity-4-b": 7, "activity-4-c": 7, "activity-4-d": 8,
 "activity-5-a": 8, "activity-5-b": 7, "activity-5-c": 7, "activity-5-d": 8, "activity-5-x": 10,
 "activity-6-a": 10, "activity-6-b": 10, "activity-6-c": 5, "activity-6-d": 8,
 "activity-7-a": 5, "activity-7-b": 7, "activity-7-c": 8, "activity-7-d": 8,
 "activity-8-a": 8, "activity-8-b": 7, "activity-8-c": 10, "activity-8-d": 5,
 "activity-9-a": 7, "activity-9-b": 5, "activity-9-c": 5, "activity-9-d": 7,
 "activity-b-x": 7,
}

# Images embedded into the page so the guide is fully self-sufficient.
# anchor -> (asset image path relative to package root, caption)
EMBED = {
 "activity-3-b": ("do-now-assets/dn-3.B-text-to-diagram/process-flow-start.png", "Starter flow for process text P1:"),
 "activity-5-a": ("do-now-assets/dn-5.A-rank-these-risks/risk-grid.png", "The 3x3 ranking grid (likelihood x impact):"),
 "activity-6-a": ("do-now-assets/dn-6.A-six-dimensions-on-ten-rows/ten-rows.png", "The ten rows to tag:"),
 "activity-8-c": ("do-now-assets/dn-8.C-critique-this-dashboard/dashboard-sample.png", "Sample dashboard to critique (deliberately flawed):"),
 "activity-1-a": ("do-now-assets/diagrams/dn-1a-ml-or-genai.png", "Routing decision: classic ML or GenAI?"),
 "activity-1-c": ("do-now-assets/diagrams/dn-1c-prompt-or-train.png", "Decision guide: prompt first, train only when the signals justify it."),
 "activity-4-b": ("do-now-assets/diagrams/dn-4b-prompt-anatomy.png", "Anatomy of a well-shaped prompt:"),
 "activity-4-d": ("do-now-assets/diagrams/dn-4d-grounding.png", "The grounding loop:"),
 "activity-5-d": ("do-now-assets/diagrams/dn-5d-defense-layers.png", "Defense in depth against prompt injection:"),
 "activity-6-d": ("do-now-assets/diagrams/dn-6d-cleaning-pipeline.png", "The cleaning pipeline your prompt should describe:"),
 "activity-7-c": ("do-now-assets/diagrams/dn-7c-prompt-lifecycle.png", "A prompt under change management:"),
 "activity-7-d": ("do-now-assets/diagrams/dn-7d-rag-layers.png", "Where a RAG answer can break:"),
}

# 🧩 Pattern watch: one design pattern and one anti-pattern for selected activities.
# anchor -> (pattern name, pattern line, anti-pattern name, anti-pattern line)
PATTERNS = {
 "activity-1-a": ("Right tool for the task", "route prediction and scoring to classic ML, language work to GenAI.",
                   "GenAI hammer", "when every problem looks like a prompt, forecasting ends up done by a chatbot."),
 "activity-2-a": ("Citation required", "a claim only ships with a source URL and a checked date.",
                   "Plausible citation", "accepting a confident-sounding source nobody opened."),
 "activity-2-c": ("Verified retrieval", "treat every AI-suggested dataset as a lead, not a link to repost.",
                   "Confident fabrication accepted", "reposting a dataset URL that was never opened."),
 "activity-3-a": ("Audience-first prompting", "name the reader in the prompt before asking for the summary.",
                   "One-size summary", "the same paragraph for the CIO and the resident."),
 "activity-3-b": ("Dual coding", "pair every process text with a diagram, then diff the two.",
                   "Diagram hallucination", "the AI adds steps nobody wrote, and nobody checks."),
 "activity-3-c": ("Classify before you paste", "data class decides the tool, never convenience.",
                   "Paste first, ask later", "the paste happens in a second; the incident review takes weeks."),
 "activity-4-a": ("Few-shot prompting", "two input/output examples beat a paragraph of instructions.",
                   "Vague instruction", "one line of intent and disappointment at the result."),
 "activity-4-b": ("Persona plus output contract", "a named role and a stated shape make outputs reviewable.",
                   "Prompt and pray", "no role, no shape, no way to say what 'wrong' means."),
 "activity-4-c": ("Schema-first output", "state the columns or keys before the model writes a word.",
                   "Prose first, parse later", "a lovely paragraph that no system can consume."),
 "activity-4-d": ("Grounding with an escape hatch", "answers only from the source, with an explicit 'not stated' path.",
                   "Answer everything", "remove the refusal path and the model invents politely."),
 "activity-5-d": ("Defense in depth", "input scan, instruction hierarchy, tool allowlist, in layers.",
                   "System prompt as perimeter", "'we told it not to' is a wish, not a control."),
 "activity-5-x": ("Checkpoints in the lifecycle", "responsible-AI practices attached to stages with named owners.",
                   "Ethics as afterthought", "a review scheduled for the week after launch."),
 "activity-6-a": ("Quality dimensions checklist", "validity, uniqueness, completeness, consistency, timeliness, accuracy, checked per column.",
                   "Clean it later", "later never comes; downstream models learn the dirt."),
 "activity-6-b": ("Schema as contract", "field names, types, and justifications agreed before data moves.",
                   "Implicit schema", "columns by vibe, discovered by the next team."),
 "activity-6-d": ("Deterministic rules, checkable output", "explicit rules plus a JSON contract you can test.",
                   "Vague cleanup request", "'please fix the data' returns data you cannot audit."),
 "activity-7-b": ("Sensitivity analysis", "change one assumption at a time and watch the cost curve.",
                   "Single point estimate", "one confident number with no range and no driver named."),
 "activity-7-c": ("Prompt as versioned artifact", "name, owner, tests, and rollback for every production prompt.",
                   "Prompt drift", "silent edits in production with nothing to catch the regression."),
 "activity-7-d": ("Layered failure diagnosis", "name the layer: retrieval, coverage, reasoning, governance.",
                   "Blame the model", "one bucket called 'AI is wrong' with four different fixes inside."),
 "activity-8-a": ("Failure-driven metrics", "pick the metric that catches the failure you actually fear.",
                   "Accuracy theater", "one aggregate number that hides the failure that matters."),
 "activity-8-b": ("Pilot gate", "readiness scored item by item before production is discussed.",
                   "Demo-to-production leap", "it worked in the meeting, so it ships."),
 "activity-8-c": ("Honest defaults", "zero baselines, defined denominators, units on every axis.",
                   "Truncated-axis drama", "an 82 to 98 climb drawn to look like a rocket."),
 "activity-9-a": ("Baseline-first refinement", "keep the before prompt so improvement is measurable.",
                   "Rewrite without a baseline", "a new prompt that feels better and proves nothing."),
 "activity-9-b": ("Named user, measurable result", "a use case is a sentence with a user and a number in it.",
                   "Solution looking for a problem", "a tool in search of a task."),
 "activity-9-c": ("Named guardrail with an owner", "risk, guardrail, and owner stated as one triple.",
                   "Vague reassurance", "'we will be careful' survives no audit."),
 "activity-b-x": ("Rubric-based moderation", "a 0 to 3 scale with an escalation rule for the top score.",
                   "Moderation by gut feel", "borderline calls that change with the reviewer."),
}

def textfix(s):
    """Make injected README text self-sufficient: no references to files or links outside the page."""
    s = re.sub(r"\s*\(see `board-items\.tsv`[^)]*\)", "", s)
    s = s.replace("the table in `board-items.tsv`", "the table below")
    s = s.replace("the cues in `board-items.tsv`", "the cues in the table below")
    s = s.replace("`board-items.tsv`", "the items table")
    s = s.replace("the starter-flow image `process-flow-start.png`", "the starter flow shown below")
    s = s.replace("`process-flow-start.png`", "the starter flow below")
    s = s.replace("the 3×3 likelihood/impact grid (`risk-grid.png`)", "the 3×3 likelihood/impact grid shown below")
    s = s.replace("(see `risk-grid.png` for the axes)", "(axes shown below)")
    s = s.replace("`risk-grid.png`", "the grid below")
    s = s.replace("Ten-row sample grid (`ten-rows.png`; row-by-row detail in the items table)", "Ten-row sample grid shown below")
    s = s.replace("pull up the ten-row grid, `ten-rows.png`", "pull up the ten-row grid below")
    s = s.replace("`ten-rows.png`", "the grid below")
    s = s.replace("the sample dashboard (`dashboard-sample.png`)", "the sample dashboard below")
    s = s.replace("`dashboard-sample.png`", "the dashboard below")
    s = s.replace("the Mural board linked above", "the Mural board your instructor shares in Zoom chat")
    s = s.replace("the board linked above", "the board your instructor shares in Zoom chat")
    s = s.replace("five-minute", "short").replace("Five-minute", "Short")
    return s

def no_emdash(s):
    s = s.replace("—", ", ")
    s = re.sub(r",\s*,", ",", s)
    s = re.sub(r", {2,}", ", ", s)
    s = re.sub(r",\s*\.", ".", s)
    s = re.sub(r"\s+,", ",", s)
    s = re.sub(r"\(, ", "(", s)
    s = re.sub(r", \)", ")", s)
    s = re.sub(r",\s*(</(?:p|li|td|th|h3)>)", r".\1", s)
    return s

# Sample-answer overrides where the key text is an instruction rather than a participant-format answer.
SAMPLE_OVERRIDE = {
    ("activity-2-a", 2): "SUPPORTED — &lt;source URL&gt; — &lt;date checked&gt;",
}

def add_samples(doc):
    """Fill the first body row's blanked cells from the answer key so participants see the form."""
    for anchor, spec in BLANK_SPEC.items():
        ans_id = anchor.replace("activity-", "answer-")
        ai = doc.find(f"id='{ans_id}'")
        si = doc.find(f"id='{anchor}'")
        if ai == -1 or si == -1:
            continue
        ans_end = doc.find("id='answer-", ai + 5)
        ans_seg = doc[ai: ans_end if ans_end != -1 else len(doc)]
        ans_tables = re.findall(r"<table>.*?</table>", ans_seg, re.S)
        sec_start = doc.rfind("<section class='activity'>", 0, si)
        sec_end = doc.find("</section>", si) + len("</section>")
        sec = doc[sec_start:sec_end]

        tbl_n = [-1]  # which blanked table we're on (pairs with answer-key tables in order)

        def sample_row(tm):
            table = tm.group(0)
            headers = re.findall(r"<th>(.*?)</th>", table)
            blank_idx = [i for i, h in enumerate(headers) if h in spec or h in spec.values()]
            if not blank_idx or not ans_tables:
                return table
            tbl_n[0] += 1
            ans_table = ans_tables[tbl_n[0]] if tbl_n[0] < len(ans_tables) else ans_tables[0]
            ans_row = re.findall(r"<tr>(?!<th)(.*?)</tr>", ans_table, re.S)
            if not ans_row:
                return table
            acells = [re.sub(r"<[^>]+>", "", c).strip()
                      for c in re.findall(r"<td>(.*?)</td>", ans_row[0], re.S)]
            rows = re.findall(r"(<tr>(?!<th).*?</tr>)", table, re.S)
            if not rows:
                return table
            first = rows[0]
            parts = re.split(r"(<td>.*?</td>)", first, flags=re.S)
            ci = -1
            filled = False
            for k, part in enumerate(parts):
                if not part.startswith("<td>"):
                    continue
                ci += 1
                if ci in blank_idx:
                    override = SAMPLE_OVERRIDE.get((anchor, ci))
                    if override:
                        val = override
                    elif len(acells) == len(headers):
                        val = html.escape(acells[ci])
                    elif len(blank_idx) == 1 and len(acells) >= 2:
                        val = html.escape(acells[-1])
                    else:
                        continue
                    parts[k] = "<td class='sample'><i>" + ("Sample: " if not filled else "") + val + "</i></td>"
                    filled = True
            new_table = table.replace(first, "".join(parts), 1)
            return new_table + ("<p class='small'><i>First row is a completed sample — "
                                "follow its form and format for the remaining rows.</i></p>")
        new_sec = re.sub(r"<table>.*?</table>", sample_row, sec, flags=re.S)
        doc = doc[:sec_start] + new_sec + doc[sec_end:]
    return doc

def parse_readme(p):
    t = p.read_text()
    d = {}
    d["goal"] = textfix(section(t, "Goal"))
    d["why"] = textfix(re.split(r"\n\s*\*\*Assets", section(t, "Why it matters"))[0].strip())
    steps = textfix(section(t, "Run steps 🪜"))
    d["steps"] = re.findall(r"^\d+\.\s+(.*)$", steps, re.M)
    d["takeaway"] = textfix(section(t, "Key takeaway 💡"))
    study = section(t, "Study further 📚")
    d["study"] = re.findall(r"^- \[(.+?)\]\((https?://[^)]+)\)[,—]?\s+(.*)$", study, re.M)
    d["mistake"] = textfix(section(t, "Common mistake to name ⚠️"))
    d["early"] = textfix(section(t, "If finished early ⏩"))
    d["bonus"] = textfix(section(t, "⭐ Bonus (optional)"))
    m = re.search(r"#(answer-[a-z0-9-]+)", t)
    d["anchor"] = m.group(1).replace("answer-", "activity-")
    return d

doc = GUIDE.read_text()
doc = doc.replace("<b>Do Now Activity Master Guide — Standalone Board Edition</b>", "<b>Workbook, Standalone Board Edition</b>", 1)
doc = doc.replace("cannot see the slide deck or workbook", "cannot see the slide deck")
doc = doc.replace("<h1>1258 Applied AI for Government IT Professionals</h1>",
    "<h1>1258 Applied AI for Government IT Professionals</h1><p style='font-size:12pt; margin:0 0 4pt;'>By <b>Imran Ahmad</b></p>", 1)
# minimal code styling for inline capture templates
doc = doc.replace("td { font-size:8.5pt; }",
    "td { font-size:8.5pt; }\n"
    "code { background:#f5f7fa; border:1px solid #e4e7eb; border-radius:3pt; padding:0 2.5pt; font-size:8.6pt; }\n"
    "ol { margin:4pt 0 6pt 20pt; padding:0; }\n"
    "td.sample { background:#fdf6e3; }\n"
    "h2.answers { page-break-before: always; }\n"
    ".activity p { margin:4pt 0; }")
doc = doc.replace("<h2>Expected solutions / answer key</h2>",
    "<h2 class='answers'>Expected solutions / answer key</h2>")
doc = doc.replace("td.sample { background:#fdf6e3; }",
    "td.sample { background:#fdf6e3; }\nimg.board { max-width:100%; border:1px solid #b8c0cc; border-radius:4pt; margin:3pt 0; }")

# Environment intro (cover): tools, access, and which channel to use when
ENV = """<h2>Your learning environment</h2>
<p>Everything in this guide runs on tools already available in class. Nothing needs to be installed.</p>
<ul>
<li><b>Zoom chat</b>, for short text answers and verdicts. The instructor pastes all links for the day here.</li>
<li><b>Mural</b>, every student has access. The instructor shares the board link in Zoom chat when an activity starts. Spatial work (dragging stickies, ranking on grids, mapping workflows) is captured here.</li>
<li><b>CloudShare lab VM with JupyterHub</b>, used for the hands-on labs later in the day, not in these warm-ups. Do Now 0.1 confirms you can reach it.</li>
</ul>
<p><b>Which channel when</b> (the <i>Capture</i> line in each activity header names the default):</p>
<ul>
<li><i>Mural</i> for anything spatial: sorting, ranking, clustering, mapping.</li>
<li><i>Zoom chat</i> for short text: one- or two-sentence answers, verdicts, structured lines such as <code>VERIFIED: &lt;url&gt;</code>.</li>
<li><i>Private notes</i> for baseline or reflection items that must not be shared.</li>
<li>The instructor may combine them: decide on Mural, then defend one choice in Zoom chat.</li>
</ul>"""
doc = doc.replace("<h2>Activity index</h2>", ENV + "<h2>Activity index</h2>", 1)
doc = doc.replace("41 five-minute Do Now activities", "41 short Do Now activities")
doc = doc.replace("Use this after the 5-minute capture.", "Use this after the timed capture.")
doc = doc.replace("use Mural for spatial tasks, Zoom chat for short text, and private notes for baseline/reflection items.",
    "use Mural for spatial tasks, Zoom chat for short text, and private notes for baseline/reflection items. <b>No sandbox or special tooling is needed</b> — every activity is done mentally and captured on the Mural board or in Zoom chat.")

count, problems = 0, []
for folder in sorted(ASSETS.glob("dn-*")):
    r = parse_readme(folder / "README.md")
    tag = f"<a id='{r['anchor']}'></a>"
    i = doc.find(tag)
    if i == -1:
        problems.append(f"{folder.name}: anchor {r['anchor']} not found"); continue
    start = doc.rfind("<section class='activity'>", 0, i)
    end = doc.find("</section>", i) + len("</section>")
    sec = doc[start:end]

    # header cleanup: per-activity time, no Mural URL, no asset-pack links (self-sufficient page)
    sec = sec.replace("Time:</span> 5 minutes", f"Time:</span> {TIME[r['anchor']]} minutes", 1)
    sec = re.sub(r" \| <span class='label'>Mural:</span> <a href='https://app\.mural\.co[^']*'>[^<]*</a>", "", sec, count=1)
    sec = re.sub(r" \| <span class='label'>Asset pack:</span> <a href='do-now-assets[^']*'>README</a> · <a href='[^']*'>items</a> · <a href='[^']*'>solution</a>", "", sec, count=1)
    sec = sec.replace("<span class='label'>Assets:</span> Private notes/Prompt Card.",
                      "<span class='label'>Assets:</span> Private notes.")

    sec = re.sub(r"(<span class='label'>Goal:</span> ).*?(?=</p>)",
                 lambda m: m.group(1) + md_inline(r["goal"]), sec, count=1, flags=re.S)
    sec = re.sub(r"(<span class='label'>Why it matters:</span> ).*?(?=</p>)",
                 lambda m: m.group(1) + md_inline(r["why"]), sec, count=1, flags=re.S)
    steps_html = "<p class='label'>Run steps 🪜:</p><ol>" + "".join(
        f"<li>{md_inline(s)}</li>" for s in r["steps"]) + "</ol>"
    sec = re.sub(r"<p class='label'>Run steps:</p><ul>.*?</ul>",
                 lambda m: steps_html, sec, count=1, flags=re.S)
    sec = re.sub(r"(<span class='label'>Common mistake to name:</span> ).*?(?=</p>)",
                 lambda m: m.group(1) + md_inline(r["mistake"]), sec, count=1, flags=re.S)
    sec = re.sub(r"(<span class='label'>If finished early:</span> ).*?(?=</p>)",
                 lambda m: m.group(1) + md_inline(r["early"]), sec, count=1, flags=re.S)

    extras = (f"<p><span class='label'>💡 Key takeaway:</span> {md_inline(r['takeaway'])}</p>"
              f"<p class='label'>📚 Study further:</p><ul>" + "".join(
                  f"<li><a href='{u}'>{md_inline(t)}</a> — {md_inline(desc)}</li>"
                  for t, u, desc in r["study"]) + "</ul>")
    sec = sec.replace("<p><span class='label'>Capture and done:</span>", extras + "<p><span class='label'>Capture and done:</span>", 1)

    if r["bonus"]:
        sec = sec.replace("<p class='small'><span class='label'>Accuracy check:</span>",
                          f"<p><span class='label'>⭐ Bonus (optional):</span> {md_inline(r['bonus'])}</p>"
                          "<p class='small'><span class='label'>Accuracy check:</span>", 1)
    sec = sec.replace("</h3>", " 🎯</h3>", 1)
    fmt = ("<p class='small'><span class='label'>Format:</span> No sandbox or tooling required — "
           "done mentally; captured on the Mural board or in Zoom chat (see run steps).</p>")
    sec = re.sub(r"(<p class='meta'>.*?</p>)", lambda m: m.group(1) + fmt, sec, count=1, flags=re.S)
    if r["anchor"] in EMBED:
        import base64
        img_path = ROOT / EMBED[r["anchor"]][0]
        b64 = base64.b64encode(img_path.read_bytes()).decode()
        img_html = (f"<p class='label'>{EMBED[r['anchor']][1]}</p>"
                    f"<p><img class='board' src='data:image/png;base64,{b64}'></p>")
        sec = re.sub(r"(<p><span class='label'>Assets:</span>.*?</p>)",
                     lambda m: m.group(1) + img_html, sec, count=1, flags=re.S)
    sec = blank_answer_cells(sec, r["anchor"])
    if r["anchor"] in COPILOT:
        cop = f"<p><span class='label'>🌐 MS Co-pilot Specific Info:</span> {COPILOT[r['anchor']]}</p>"
        sec = sec.replace("<p><span class='label'>💡 Key takeaway:</span>", cop + "<p><span class='label'>💡 Key takeaway:</span>", 1)
        rp = folder / "README.md"
        rt = rp.read_text()
        if "MS Co-pilot Specific Info" not in rt:
            plain = no_emdash(re.sub(r"<[^>]+>", "", COPILOT[r["anchor"]]))
            rt = rt.replace("\n## Run steps 🪜",
                            f"\n**🌐 MS Co-pilot Specific Info:** {plain}\n\n## Run steps 🪜", 1)
            rp.write_text(rt)
    if r["anchor"] in ATLAS:
        url, label, text = ATLAS[r["anchor"]]
        atl = (f"<p><span class='label'>🛡️ Real incident, MITRE ATLAS:</span> "
               f"<a href='{url}'>{label}</a>. {text}</p>")
        sec = sec.replace("<p><span class='label'>💡 Key takeaway:</span>", atl + "<p><span class='label'>💡 Key takeaway:</span>", 1)
        rp = folder / "README.md"
        rt = rp.read_text()
        if "MITRE ATLAS" not in rt:
            rt = rt.replace("\n## Run steps 🪜",
                            no_emdash(f"\n**🛡️ Real incident, MITRE ATLAS:** [{label}]({url}). {text}\n\n## Run steps 🪜"), 1)
            rp.write_text(rt)
    if r["anchor"] in PATTERNS:
        pn, pl, an, al = PATTERNS[r["anchor"]]
        pat = (f"<p><span class='label'>🧩 Pattern watch:</span><br>"
               f"<b><u>Design pattern, {pn}:</u></b> {pl}<br>"
               f"<b><u>Anti-pattern, {an}:</u></b> {al}</p>")
        sec = sec.replace("<p><span class='label'>💡 Key takeaway:</span>", pat + "<p><span class='label'>💡 Key takeaway:</span>", 1)
        rp = folder / "README.md"
        rt = rp.read_text()
        if "Pattern watch" not in rt:
            rt = rt.replace("\n## Run steps 🪜",
                            no_emdash(f"\n**🧩 Pattern watch:** Design pattern, **{pn}**: {pl} Anti-pattern, **{an}**: {al}\n\n## Run steps 🪜"), 1)
            rp.write_text(rt)

    doc = doc[:start] + sec + doc[end:]
    count += 1

doc = add_samples(doc)
doc = no_emdash(doc)
GUIDE.write_text(doc)
print(f"enriched {count} sections")
for p in problems: print("PROBLEM:", p)
