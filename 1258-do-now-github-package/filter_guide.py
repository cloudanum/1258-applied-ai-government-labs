#!/usr/bin/env python3
"""Build 1258-DoNow-Master-Guide-Standalone_custom_filter.html.

Like the _custom edition, but rebalanced so each of the 11 students matches
~40% of the 41 activities, plus a sticky student filter bar (pure HTML/CSS/JS,
no dependencies) and a static Student relevance map. Reads the enriched
standalone guide; does NOT modify the original or the _custom edition.
"""
import re, pathlib, collections
from customize_guide import TARGET

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "1258-DoNow-Master-Guide-Standalone.html"
OUT = ROOT / "1258-DoNow-Master-Guide-Standalone_custom_filter.html"

STUDENTS = ["Tyler Moule", "Joe C", "Tyler Bested", "John Cayton", "Vikas Vaid", "Rob H.",
            "Natalie Sherwood", "Lynn Ibrus", "Fabrice Simo", "Jerri", "Vijayalakshmi"]

# anchor -> students for whom this activity is relevant (~40% of activities per student)
RELEVANCE = {
 "activity-0-1": ["Vijayalakshmi", "Joe C", "Vikas Vaid"],
 "activity-0-2": ["Vijayalakshmi", "Natalie Sherwood", "Rob H."],
 "activity-0-3": ["Jerri", "Vikas Vaid", "Lynn Ibrus", "Joe C"],
 "activity-1-a": ["Tyler Moule", "Lynn Ibrus", "Tyler Bested", "Fabrice Simo", "Rob H.", "Vikas Vaid"],
 "activity-1-b": ["John Cayton", "Rob H.", "Natalie Sherwood", "Vikas Vaid", "Lynn Ibrus"],
 "activity-1-c": ["Tyler Moule", "Jerri", "Joe C"],
 "activity-1-d": ["Tyler Bested", "Vijayalakshmi", "Tyler Moule"],
 "activity-2-a": ["Rob H.", "John Cayton", "Natalie Sherwood", "Fabrice Simo", "Tyler Bested", "Vijayalakshmi"],
 "activity-2-b": ["Tyler Bested", "Lynn Ibrus", "Fabrice Simo", "Tyler Moule", "Natalie Sherwood"],
 "activity-2-c": ["John Cayton", "Joe C", "Vijayalakshmi", "Fabrice Simo", "Rob H."],
 "activity-2-d": ["John Cayton", "Lynn Ibrus", "Jerri", "Natalie Sherwood"],
 "activity-3-a": ["Natalie Sherwood", "Rob H.", "Vikas Vaid", "Vijayalakshmi", "John Cayton", "Fabrice Simo"],
 "activity-3-b": ["Joe C", "Fabrice Simo", "Tyler Bested", "Rob H.", "John Cayton"],
 "activity-3-c": ["Jerri", "Lynn Ibrus", "Vikas Vaid", "Natalie Sherwood", "Vijayalakshmi"],
 "activity-3-d": ["Vikas Vaid", "Vijayalakshmi", "Rob H.", "Tyler Moule"],
 "activity-4-a": ["Vikas Vaid", "Natalie Sherwood", "Vijayalakshmi", "Joe C", "Fabrice Simo"],
 "activity-4-b": ["Tyler Moule", "Joe C", "Fabrice Simo", "Rob H.", "Natalie Sherwood"],
 "activity-4-c": ["Lynn Ibrus", "Vijayalakshmi", "Natalie Sherwood", "Fabrice Simo", "Tyler Bested"],
 "activity-4-d": ["Jerri", "Vikas Vaid", "Rob H.", "Tyler Moule", "John Cayton", "Joe C"],
 "activity-5-a": ["Jerri", "Lynn Ibrus", "Vikas Vaid", "Rob H.", "Vijayalakshmi"],
 "activity-5-b": ["Vikas Vaid", "Vijayalakshmi", "Jerri", "Joe C"],
 "activity-5-c": ["John Cayton", "Tyler Moule", "Jerri", "Tyler Bested"],
 "activity-5-d": ["Jerri", "Vikas Vaid", "Vijayalakshmi"],
 "activity-5-x": ["Tyler Moule", "John Cayton", "Jerri", "Natalie Sherwood", "Fabrice Simo"],
 "activity-6-a": ["Lynn Ibrus", "John Cayton", "Tyler Bested", "Rob H.", "Natalie Sherwood"],
 "activity-6-b": ["Tyler Bested", "Jerri", "John Cayton", "Tyler Moule"],
 "activity-6-c": ["Lynn Ibrus", "Tyler Bested", "Fabrice Simo", "Rob H."],
 "activity-6-d": ["Lynn Ibrus", "Vijayalakshmi", "Vikas Vaid", "Joe C"],
 "activity-7-a": ["Tyler Bested", "Tyler Moule", "Vikas Vaid"],
 "activity-7-b": ["Lynn Ibrus", "Tyler Bested", "Joe C"],
 "activity-7-c": ["Tyler Bested", "Jerri", "Joe C"],
 "activity-7-d": ["Jerri", "Vikas Vaid", "Tyler Moule", "John Cayton"],
 "activity-8-a": ["Tyler Bested", "Lynn Ibrus", "Tyler Moule", "Joe C", "Fabrice Simo"],
 "activity-8-b": ["Joe C", "Jerri", "John Cayton", "Tyler Moule", "Vikas Vaid"],
 "activity-8-c": ["Lynn Ibrus", "Natalie Sherwood", "Rob H.", "Tyler Bested"],
 "activity-8-d": ["Rob H.", "Natalie Sherwood", "John Cayton", "Vijayalakshmi", "Lynn Ibrus", "Fabrice Simo"],
 "activity-9-a": ["Vijayalakshmi", "Natalie Sherwood", "Vikas Vaid", "Rob H.", "Fabrice Simo"],
 "activity-9-b": ["Joe C", "Jerri", "John Cayton", "Fabrice Simo", "Tyler Bested"],
 "activity-9-c": ["Jerri", "Lynn Ibrus", "Tyler Moule", "Joe C", "Rob H."],
 "activity-9-d": ["John Cayton", "Joe C", "Tyler Moule", "Fabrice Simo"],
 "activity-b-x": ["Jerri", "Vikas Vaid", "Natalie Sherwood"],
}

# Paragraphs rewritten where the expanded relevance list differs from the _custom paragraph's named examples.
PARA_OVERRIDE = {
 "activity-1-d": "Tyler Bested has the class's Python background, so a zero-setup browser demo of entity and sentiment analysis shows what an ML API returns before any code gets written. Vijayalakshmi listed extract as a core verb, and named-entity recognition is extraction in its purest form; Tyler Moule can read the JSON response with a practitioner's eye.",
 "activity-7-a": "Tyler Bested and Tyler Moule have the technical background to pull an interesting model down after class, and Vikas in IT can read licenses and limitation sections with an operator's eye. The tour shows all three where vetted models live and what a trustworthy model card must say.",
}

def activity_id(anchor):
    return anchor.replace("activity-", "").replace("-", ".").upper()

# sanity checks before building
counts = collections.Counter()
for a, names in RELEVANCE.items():
    assert 1 <= len(names) <= 6, (a, names)
    assert all(n in STUDENTS for n in names), a
    counts.update(names)
for s, c in counts.items():
    print(f"  {s:18s} {c:2d} activities ({c/41*100:.0f}%)")
    assert 14 <= c <= 19, (s, c)

doc = SRC.read_text()
doc = doc.replace("<b>Do Now Activity Master Guide, Standalone Board Edition</b>",
    "<b>Do Now Activity Master Guide, Standalone Board Edition (Custom: student filter edition)</b>")
doc = doc.replace("<div class=\"notice\">",
    "<div class=\"notice\"><b>Custom filter edition:</b> use the sticky filter bar at the top to show only the "
    "activities relevant to one student (about 40 percent of the 41 activities each, matched from the class intake "
    "sheet). The Student relevance map below prints the same matching for handouts. ", 1)

# CSS for filter UI
doc = doc.replace(".activity p { margin:4pt 0; }",
    ".activity p { margin:4pt 0; }\n"
    "#filterbar { position:sticky; top:0; z-index:20; background:#fff; border-bottom:1px solid #cbd2d9;"
    "  padding:6pt 8pt; display:flex; flex-wrap:wrap; gap:4pt; align-items:center; box-shadow:0 1pt 3pt #e4e7eb; }\n"
    "#filterbar .flabel { font-weight:bold; font-size:9pt; margin-right:2pt; }\n"
    ".fbtn { border:1px solid var(--line); background:var(--soft); border-radius:999px; padding:2pt 9pt;"
    "  cursor:pointer; font-size:8.6pt; color:var(--ink); }\n"
    ".fbtn:hover { border-color:var(--accent); }\n"
    ".fbtn.active { background:var(--accent); color:#fff; border-color:var(--accent); }\n"
    "#fcount { font-size:8.6pt; color:var(--accent); font-weight:bold; margin-left:4pt; }\n"
    "#fmatches { flex-basis:100%; font-size:8.2pt; color:var(--muted); }\n"
    "@media print { #filterbar { display:none; } }")

# targeted block + data-students on every activity section
for anchor, names in RELEVANCE.items():
    tag = f"<a id='{anchor}'></a>"
    i = doc.find(tag)
    assert i != -1, anchor
    start = doc.rfind("<section class='activity'>", 0, i)
    end = doc.find("</section>", i) + len("</section>")
    sec = doc[start:end]
    para = PARA_OVERRIDE.get(anchor, TARGET[anchor][1])
    block = (f"<p><span class='label'>👥 Relevant for:</span> <b>{', '.join(names)}</b></p>"
             f"<p class='small'>{para}</p>")
    marker = "<p><span class='label'>💡 Key takeaway:</span>"
    assert marker in sec, anchor
    sec = sec.replace(marker, block + marker, 1)
    sec = sec.replace("<section class='activity'>",
                      f"<section class='activity' data-students='{'|'.join(names)}'>", 1)
    doc = doc[:start] + sec + doc[end:]

# wrap answer blocks so they filter too
def wrap_answers(doc):
    out, pos = [], 0
    ans_start = doc.find("<h2 class='answers'>")
    out.append(doc[:ans_start])
    seg = doc[ans_start:]
    parts = re.split(r"(?=<a id='answer-)", seg)
    out.append(parts[0])
    for part in parts[1:]:
        m = re.match(r"<a id='(answer-[a-z0-9-]+)'></a>", part)
        anchor = m.group(1).replace("answer-", "activity-")
        names = RELEVANCE.get(anchor, [])
        if part.endswith("</body></html>"):
            part = part[:-len("</body></html>")] + "</div></body></html>"
            out.append(f"<div class='ansblock' data-students='{'|'.join(names)}'>" + part)
        else:
            out.append(f"<div class='ansblock' data-students='{'|'.join(names)}'>" + part + "</div>")
    return "".join(out)
doc = wrap_answers(doc)

# student relevance map (static, printable) after the activity index
rows = []
for s in STUDENTS:
    ids = [activity_id(a) for a, names in RELEVANCE.items() if s in names]
    rows.append(f"<tr><td><b>{s}</b></td><td>{len(ids)} of 41</td><td>{', '.join(ids)}</td></tr>")
map_html = ("<h2>Student relevance map</h2><p>Based on the class intake sheet (Main tab): vertical, self-rated "
    "ML/GenAI/Python skills, the four verbs each student listed, and stated use cases. Each student matches about "
    "40 percent of the activities.</p><table><thead><tr><th>Student</th><th>Relevant activities</th>"
    "<th>Activity IDs</th></tr></thead><tbody>" + "".join(rows) + "</tbody></table>")
doc = doc.replace("</ol>", "</ol>" + map_html, 1)  # first </ol> closes the activity index

# filter bar right after <body>, plus JS before </body>
buttons = ["<button class='fbtn active' data-name=''>All students</button>"] + [
    f"<button class='fbtn' data-name='{s}'>{s.split()[0]}{' ' + s.split()[1][0] + '.' if s.startswith('Tyler') else ''}</button>"
    for s in STUDENTS]
filterbar = ("<div id='filterbar'><span class='flabel'>🎓 Filter by student:</span>" + "".join(buttons) +
    "<span id='fcount'></span><span id='fmatches'></span></div>")
doc = doc.replace("<body>", "<body>" + filterbar, 1)

js = """<script>
(function(){
  var btns = document.querySelectorAll('.fbtn');
  btns.forEach(function(b){
    b.addEventListener('click', function(){
      btns.forEach(function(x){ x.classList.remove('active'); });
      b.classList.add('active');
      var name = b.getAttribute('data-name');
      var blocks = document.querySelectorAll('[data-students]');
      var n = 0, ids = [];
      blocks.forEach(function(s){
        var ok = !name || s.getAttribute('data-students').split('|').indexOf(name) !== -1;
        s.style.display = ok ? '' : 'none';
        if (ok && name && s.classList.contains('activity')) {
          n++;
          var h = s.querySelector('h3');
          if (h) ids.push(h.textContent.replace(/^\\d+\\.\\s*/, '').replace(' 🎯',''));
        }
      });
      document.getElementById('fcount').textContent = name ? (n + ' of 41 activities') : '';
      document.getElementById('fmatches').textContent = name ? ids.join('  ·  ') : '';
      window.scrollTo(0, 0);
    });
  });
})();
</script>"""
doc = doc.replace("</body>", js + "</body>", 1)

OUT.write_text(doc)
print("written:", OUT.name)
print("data-students blocks:", doc.count("data-students="), "| buttons:", doc.count("class='fbtn"))
