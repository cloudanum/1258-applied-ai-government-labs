#!/usr/bin/env python3
"""Generate instructional diagrams embedded into the master guide (base64).

Each PNG lands in do-now-assets/diagrams/ and is referenced by EMBED in enrich_guide.py.
Style: flat boxes and arrows, course palette (accent #0b5fff, warn amber, muted grays).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import pathlib

OUT = pathlib.Path(__file__).parent / "do-now-assets" / "diagrams"
OUT.mkdir(exist_ok=True)

ACCENT, SOFT, WARN, BAD, MUT = "#0b5fff", "#e8eef7", "#fff4d6", "#ffd9d9", "#52606d"

def box(ax, x, y, w, h, text, fc=SOFT, ec=ACCENT, fs=8.6, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.012,rounding_size=0.014",
                                fc=fc, ec=ec, lw=1.3))
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=fs,
            fontweight="bold" if bold else "normal", wrap=True)

def arrow(ax, x1, y1, x2, y2, label="", fs=7.8, color=MUT, dy=0.035):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=13,
                                 color=color, lw=1.4))
    if label:
        ax.text((x1+x2)/2, (y1+y2)/2 + dy, label, ha="center", fontsize=fs, color=color, style="italic")

def canvas(w=9.2, h=2.6):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    return fig, ax

def save(fig, name):
    fig.savefig(OUT / name, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print("wrote", name)

# 1.A: classic ML vs GenAI routing
fig, ax = canvas(h=2.9)
box(ax, 0.02, 0.38, 0.24, 0.26, "New use case:\nwhat is the core job?", fc=WARN, ec="#d97706", bold=True)
box(ax, 0.40, 0.62, 0.27, 0.26, "Predict a number or label\nfrom historical data", bold=True)
box(ax, 0.40, 0.10, 0.27, 0.26, "Produce or transform\nlanguage / content", bold=True)
box(ax, 0.76, 0.62, 0.22, 0.26, "CLASSIC ML\n(forecast, classify,\ncluster, optimize)", fc="#e4f5e9", ec="#1a7f37")
box(ax, 0.76, 0.10, 0.22, 0.26, "GenAI\n(draft, summarize,\nreword, extract)", fc="#e4ecfb", ec=ACCENT)
arrow(ax, 0.26, 0.55, 0.40, 0.72, "prediction / scoring")
arrow(ax, 0.26, 0.45, 0.40, 0.26, "language in, language out")
arrow(ax, 0.67, 0.75, 0.76, 0.75)
arrow(ax, 0.67, 0.23, 0.76, 0.23)
ax.text(0.5, 0.01, "Uncertain which? The use case needs a sharper definition before any tool is chosen.",
        ha="center", fontsize=7.8, color=MUT, style="italic")
save(fig, "dn-1a-ml-or-genai.png")

# 1.C: prompt it or train it
fig, ax = canvas(h=2.9)
box(ax, 0.02, 0.38, 0.23, 0.26, "Recurring task\nfor the model", fc=WARN, ec="#d97706", bold=True)
box(ax, 0.35, 0.66, 0.28, 0.24, "Few runs, varied input,\nno labeled dataset?", bold=True)
box(ax, 0.35, 0.08, 0.28, 0.24, "High volume + stable format\n+ labels + repeatability", bold=True)
box(ax, 0.72, 0.66, 0.26, 0.24, "PROMPT\n(examples + contract)", fc="#e4ecfb", ec=ACCENT)
box(ax, 0.72, 0.08, 0.26, 0.24, "TRAIN / FINE-TUNE\n(or hybrid)", fc="#e4f5e9", ec="#1a7f37")
arrow(ax, 0.25, 0.56, 0.35, 0.75)
arrow(ax, 0.25, 0.44, 0.35, 0.22)
arrow(ax, 0.63, 0.78, 0.72, 0.78)
arrow(ax, 0.63, 0.20, 0.72, 0.20)
ax.text(0.5, 0.01, "Rule of thumb: prompt first; train only when volume, labels, and repeatability justify it.",
        ha="center", fontsize=7.8, color=MUT, style="italic")
save(fig, "dn-1c-prompt-or-train.png")

# 4.B: prompt anatomy (role + contract)
fig, ax = canvas(h=2.4)
box(ax, 0.02, 0.30, 0.20, 0.40, "1. ROLE\n\n'You are a records\nofficer.'", fc="#e4ecfb", ec=ACCENT, bold=True)
box(ax, 0.28, 0.30, 0.20, 0.40, "2. TASK\n\n'Summarize this\nrequest.'", fc="#e4ecfb", ec=ACCENT, bold=True)
box(ax, 0.54, 0.30, 0.22, 0.40, "3. OUTPUT CONTRACT\n\n'5 bullets: issues,\nexemptions, draft.'", fc="#e4ecfb", ec=ACCENT, bold=True)
box(ax, 0.82, 0.30, 0.16, 0.40, "Consistent,\nreviewable\noutput", fc="#e4f5e9", ec="#1a7f37", bold=True)
arrow(ax, 0.22, 0.50, 0.28, 0.50)
arrow(ax, 0.48, 0.50, 0.54, 0.50)
arrow(ax, 0.76, 0.50, 0.82, 0.50)
ax.text(0.5, 0.06, "Anti-pattern 'prompt and pray': one vague line, then disappointment at the answer.",
        ha="center", fontsize=7.8, color="#b42318", style="italic")
save(fig, "dn-4b-prompt-anatomy.png")

# 4.D: grounding loop
fig, ax = canvas(h=2.6)
box(ax, 0.02, 0.56, 0.24, 0.30, "Approved excerpt\n(the only source)", fc=WARN, ec="#d97706", bold=True)
box(ax, 0.02, 0.12, 0.24, 0.30, "Reader question", bold=True)
box(ax, 0.38, 0.34, 0.24, 0.34, "Answer ONLY\nfrom the text", fc="#e4ecfb", ec=ACCENT, bold=True)
box(ax, 0.74, 0.56, 0.24, 0.30, "Stated? -> answer\n+ quote the line", fc="#e4f5e9", ec="#1a7f37")
box(ax, 0.74, 0.12, 0.24, 0.30, "Not stated? ->\nsay 'not stated'", fc="#fbe4e4", ec="#b42318")
arrow(ax, 0.26, 0.71, 0.38, 0.56)
arrow(ax, 0.26, 0.27, 0.38, 0.44)
arrow(ax, 0.62, 0.56, 0.74, 0.68)
arrow(ax, 0.62, 0.44, 0.74, 0.30)
ax.text(0.5, 0.02, "The unanswerable question is the test: a grounded model must be able to refuse.",
        ha="center", fontsize=7.8, color=MUT, style="italic")
save(fig, "dn-4d-grounding.png")

# 5.D: injection defense layers
fig, ax = canvas(h=3.0)
box(ax, 0.01, 0.68, 0.20, 0.22, "User turn\n(can be hostile)", fc=BAD, ec="#b42318")
box(ax, 0.01, 0.40, 0.20, 0.22, "Documents / web\n(can hide payloads)", fc=BAD, ec="#b42318")
box(ax, 0.01, 0.12, 0.20, 0.22, "Tool results", fc=BAD, ec="#b42318")
box(ax, 0.30, 0.40, 0.17, 0.24, "L1  Input scan\n+ data/command\nseparation", fc=WARN, ec="#d97706", bold=True)
box(ax, 0.52, 0.40, 0.17, 0.24, "L2  Instruction\nhierarchy:\nsystem > user", fc=WARN, ec="#d97706", bold=True)
box(ax, 0.74, 0.40, 0.11, 0.24, "L3  Tool\nallowlist", fc=WARN, ec="#d97706", bold=True)
box(ax, 0.89, 0.40, 0.10, 0.24, "Safe\naction", fc="#e4f5e9", ec="#1a7f37", bold=True)
for y in (0.79, 0.51, 0.23):
    arrow(ax, 0.21, y, 0.30, 0.52)
arrow(ax, 0.47, 0.52, 0.52, 0.52)
arrow(ax, 0.69, 0.52, 0.74, 0.52)
arrow(ax, 0.85, 0.52, 0.89, 0.52)
ax.text(0.5, 0.02, "Anti-pattern: 'the system prompt told it not to.' Politeness is not a perimeter; layers are.",
        ha="center", fontsize=7.8, color="#b42318", style="italic")
save(fig, "dn-5d-defense-layers.png")

# 6.D: cleaning pipeline
fig, ax = canvas(h=2.4)
box(ax, 0.02, 0.30, 0.20, 0.42, "Messy rows\n(dupes, bad dates,\nstray wards)", fc=BAD, ec="#b42318", bold=True)
box(ax, 0.30, 0.30, 0.30, 0.42, "Explicit cleaning rules\n1. normalize dates (ISO)\n2. dedupe by request_id\n3. flag, never silently drop", fc=WARN, ec="#d97706", bold=True)
box(ax, 0.68, 0.30, 0.30, 0.42, "Machine-checkable output\nJSON: rows, flags,\nremoved_duplicate_ids", fc="#e4f5e9", ec="#1a7f37", bold=True)
arrow(ax, 0.22, 0.51, 0.30, 0.51)
arrow(ax, 0.60, 0.51, 0.68, 0.51)
ax.text(0.5, 0.06, "Design pattern: deterministic rules + an output contract you can test, not 'please clean this.'",
        ha="center", fontsize=7.8, color=MUT, style="italic")
save(fig, "dn-6d-cleaning-pipeline.png")

# 7.C: prompt-as-code lifecycle
fig, ax = canvas(w=9.6, h=2.4)
steps = [("Draft", SOFT, ACCENT), ("Version\n(name, owner)", WARN, "#d97706"), ("Test cases", WARN, "#d97706"),
         ("Deploy", "#e4f5e9", "#1a7f37"), ("Monitor\n+ rollback note", "#e4f5e9", "#1a7f37")]
x = 0.02
for label, fc, ec in steps:
    box(ax, x, 0.34, 0.16, 0.34, label, fc=fc, ec=ec, bold=True)
    if x > 0.02:
        arrow(ax, x - 0.035, 0.51, x, 0.51)
    x += 0.195
arrow(ax, x - 0.095, 0.34, 0.10, 0.16, "regression? edit and re-version", dy=-0.045)
ax.text(0.5, 0.05, "Anti-pattern 'prompt drift': silent edits in production with no version and no test to catch them.",
        ha="center", fontsize=7.8, color="#b42318", style="italic")
save(fig, "dn-7c-prompt-lifecycle.png")

# 7.D: RAG pipeline with failure layers
fig, ax = canvas(w=9.6, h=2.9)
box(ax, 0.02, 0.40, 0.15, 0.24, "Citizen\nquestion", bold=True)
box(ax, 0.24, 0.40, 0.17, 0.24, "RETRIEVE\nchunks from\napproved corpus", fc="#e4ecfb", ec=ACCENT, bold=True)
box(ax, 0.48, 0.40, 0.17, 0.24, "AUGMENT\nprompt with\nchunks", fc="#e4ecfb", ec=ACCENT, bold=True)
box(ax, 0.72, 0.40, 0.12, 0.24, "GENERATE\nanswer", fc="#e4ecfb", ec=ACCENT, bold=True)
box(ax, 0.89, 0.40, 0.09, 0.24, "Answer", fc="#e4f5e9", ec="#1a7f37", bold=True)
arrow(ax, 0.17, 0.52, 0.24, 0.52); arrow(ax, 0.41, 0.52, 0.48, 0.52)
arrow(ax, 0.65, 0.52, 0.72, 0.52); arrow(ax, 0.84, 0.52, 0.89, 0.52)
ax.text(0.325, 0.24, "RETRIEVAL FAIL\nwrong / stale / footnote chunk", ha="center", fontsize=7.4, color="#b42318")
ax.text(0.565, 0.24, "COVERAGE FAIL\nanswer not in corpus", ha="center", fontsize=7.4, color="#b42318")
ax.text(0.78, 0.24, "REASONING FAIL\nright text, wrong logic", ha="center", fontsize=7.4, color="#b42318")
ax.text(0.5, 0.80, "GOVERNANCE FAIL: permissions leak across the whole chain (any box can leak to the wrong reader)",
        ha="center", fontsize=7.4, color="#b42318", style="italic")
save(fig, "dn-7d-rag-layers.png")

print("all diagrams generated in", OUT)

# 0.2: Bloom's taxonomy ladder with signature prompting verbs (per neurals.ca mapping)
fig, ax = plt.subplots(figsize=(9.4, 3.0))
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
levels = [
    ("L1 Remember", "list, define,\nextract, quote", "#e4ecfb", "confident fabrication"),
    ("L2 Understand", "summarize, explain,\nparaphrase", "#dbe7fa", "smoothing: lost caveats"),
    ("L3 Apply", "classify, calculate,\nexecute", "#cfe0f7", "executional error"),
    ("L4 Analyze", "compare, diagnose,\ntrace, infer", "#ffe9c2", "spurious connection"),
    ("L5 Evaluate", "judge, score,\nrecommend, critique", "#ffd9a8", "hidden assumptions"),
    ("L6 Create", "design, generate,\nsynthesize, invent", "#ffb3b3", "unverifiable plausibility"),
]
w = 0.148
for i, (lvl, verbs, fc, risk) in enumerate(levels):
    x = 0.02 + i * 0.162
    y = 0.16 + i * 0.105
    ax.add_patch(FancyBboxPatch((x, y), w, 0.34, boxstyle="round,pad=0.008,rounding_size=0.012",
                                fc=fc, ec=ACCENT if i < 3 else "#d97706", lw=1.2))
    ax.text(x + w/2, y + 0.265, lvl, ha="center", fontsize=8.2, fontweight="bold")
    ax.text(x + w/2, y + 0.115, verbs, ha="center", fontsize=7.2)
    ax.text(x + w/2, max(0.015, y - 0.085), "risk: " + risk, ha="center", fontsize=6.6,
            color="#b42318", style="italic")
ax.annotate("", xy=(0.99, 0.97), xytext=(0.02, 0.60),
            arrowprops=dict(arrowstyle="-|>", color=MUT, lw=1.4))
ax.text(0.52, 0.955, "higher level = wider output space = more creativity AND more risk",
        ha="center", fontsize=8.2, color=MUT, style="italic")
ax.text(0.52, 0.02, "Map your own top 4 verbs to a level: that is your home level on the ladder.",
        ha="center", fontsize=8.0, fontweight="bold")
fig.savefig(OUT / "dn-02-bloom-ladder.png", dpi=140, bbox_inches="tight")
plt.close(fig)
print("wrote dn-02-bloom-ladder.png")
