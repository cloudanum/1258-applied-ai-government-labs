#!/usr/bin/env python3
"""Flow enriched do-now-assets READMEs into the standalone master guide HTML."""
import html, re, pathlib

ROOT = pathlib.Path(__file__).parent
ASSETS = ROOT / "do-now-assets"
GUIDE = ROOT / "1258-DoNow-Master-Guide-Standalone.html"

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
    d["goal"] = section(t, "Goal")
    d["why"] = re.split(r"\n\s*\*\*Assets", section(t, "Why it matters"))[0].strip()
    steps = section(t, "Run steps 🪜")
    d["steps"] = re.findall(r"^\d+\.\s+(.*)$", steps, re.M)
    d["takeaway"] = section(t, "Key takeaway 💡")
    study = section(t, "Study further 📚")
    d["study"] = re.findall(r"^- \[(.+?)\]\((https?://[^)]+)\)[,—]?\s+(.*)$", study, re.M)
    d["mistake"] = section(t, "Common mistake to name ⚠️")
    d["early"] = section(t, "If finished early ⏩")
    d["bonus"] = section(t, "⭐ Bonus (optional)")
    m = re.search(r"#(answer-[a-z0-9-]+)", t)
    d["anchor"] = m.group(1).replace("answer-", "activity-")
    return d

doc = GUIDE.read_text()
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
    sec = blank_answer_cells(sec, r["anchor"])
    if r["anchor"] in COPILOT:
        cop = f"<p><span class='label'>🌐 With Copilot in the browser:</span> {COPILOT[r['anchor']]}</p>"
        sec = sec.replace("<p><span class='label'>💡 Key takeaway:</span>", cop + "<p><span class='label'>💡 Key takeaway:</span>", 1)
        rp = folder / "README.md"
        rt = rp.read_text()
        if "With Copilot in the browser" not in rt:
            plain = no_emdash(re.sub(r"<[^>]+>", "", COPILOT[r["anchor"]]))
            rt = rt.replace("\n## Run steps 🪜",
                            f"\n**🌐 With Copilot in the browser:** {plain}\n\n## Run steps 🪜", 1)
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

    doc = doc[:start] + sec + doc[end:]
    count += 1

doc = add_samples(doc)
doc = no_emdash(doc)
GUIDE.write_text(doc)
print(f"enriched {count} sections")
for p in problems: print("PROBLEM:", p)
