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

def parse_readme(p):
    t = p.read_text()
    d = {}
    d["goal"] = section(t, "Goal")
    d["why"] = re.split(r"\n\s*\*\*Assets", section(t, "Why it matters"))[0].strip()
    steps = section(t, "Run steps 🪜")
    d["steps"] = re.findall(r"^\d+\.\s+(.*)$", steps, re.M)
    d["takeaway"] = section(t, "Key takeaway 💡")
    study = section(t, "Study further 📚")
    d["study"] = re.findall(r"^- \[(.+?)\]\((https?://[^)]+)\) — (.*)$", study, re.M)
    d["mistake"] = section(t, "Common mistake to name ⚠️")
    d["early"] = section(t, "If finished early ⏩")
    d["bonus"] = section(t, "⭐ Bonus (optional)")
    m = re.search(r"#(answer-[a-z0-9-]+)", t)
    d["anchor"] = m.group(1).replace("answer-", "activity-")
    return d

doc = GUIDE.read_text()
# minimal code styling for inline capture templates
doc = doc.replace("td { font-size:8.5pt; }",
    "td { font-size:8.5pt; }\ncode { background:#f5f7fa; border:1px solid #e4e7eb; border-radius:3pt; padding:0 2.5pt; font-size:8.6pt; }")
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

    doc = doc[:start] + sec + doc[end:]
    count += 1

GUIDE.write_text(doc)
print(f"enriched {count} sections")
for p in problems: print("PROBLEM:", p)
