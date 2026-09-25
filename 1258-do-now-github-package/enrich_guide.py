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

    doc = doc[:start] + sec + doc[end:]
    count += 1

GUIDE.write_text(doc)
print(f"enriched {count} sections")
for p in problems: print("PROBLEM:", p)
