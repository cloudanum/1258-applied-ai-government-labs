# Do Now 3.B: Text to Diagram 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required — this activity is done mentally (sketching the flow in your head or on paper) and captured directly on the Mural board (or as a text flow in Zoom chat if you are remote).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240792054/63f54322d2c0f75ce405203e025fe4fb52ed5c96

## Goal
By the end of this five-minute exercise you will have converted process text P1 — an intake-to-response flow for a citizen inquiry — into a simple diagram of three to five boxes and arrows, and marked the one decision the text leaves undefined: what counts as "sensitive" enough to trigger human review. The artifact is your flow on the Mural board plus one comment naming the missing decision rule. The deeper skill is that drawing a process is an audit, not an art project: the moment prose becomes boxes and arrows, hidden assumptions and missing rules have nowhere to hide. That instinct — use AI to draft the diagram, then hunt for what it silently invented or skipped — is what makes text-to-diagram prompting safe to use on real government processes.

## Why it matters
Converting text steps into a flow becomes defensible when learners must place, mark, or choose and then explain one decision — and the decision that matters here is the one the source text never wrote down. Process owners who draw their workflows catch undefined rules before an AI system automates around them.

**Assets:** Process text P1 and the starter-flow image `process-flow-start.png` (see `board-items.tsv` for the capture template).

## Run steps 🪜
1. Open the Mural board linked above and read process text P1; compare it with the starter flow in `process-flow-start.png`: Intake → Classify → Sensitive? → Human review / Respond.
2. Rebuild the flow yourself with three to five shapes: one box per step, arrows for order, and a clearly labeled branch for the "Sensitive?" decision.
3. Label *both* branches out of the decision — "yes → human review" and "no → respond" — because a decision with an unlabeled arrow is a red flag on any government process.
4. Mark the one missing decision with a Mural comment or contrasting sticky: what rule decides "sensitive"? The text never says — that gap is the finding.
5. Working remotely? Post your flow in Zoom chat as text instead, using the fallback template: `Intake -> Classify -> Sensitive? -> (yes) Human review / (no) Respond -> missing rule: what counts as sensitive`.
6. Compare your flow with a neighbor's: did they place the decision in the same spot? A different placement usually means a different assumption about the process — surface it before the instructor reveals the sample answer.

## Key takeaway 💡
Drawing the flow is the audit — the moment prose becomes boxes and arrows, the missing decision rule (here: what counts as sensitive) has nowhere to hide.

## Study further 📚
- [About Mermaid — Mermaid documentation](https://mermaid.js.org/intro/) — the standard text-to-diagram language AI assistants emit when asked to draw flows.
- [Business Process Model and Notation (BPMN) — OMG](https://www.omg.org/spec/BPMN/) — the official specification for process-diagram notation used across government and industry.
- [Creating diagrams — GitHub Docs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) — how Mermaid text turns into rendered flowcharts in real documents.

## Common mistake to name ⚠️
Transcribing the text into boxes without questioning it — a pretty diagram of an undefined process. Require one marked gap (the missing "sensitive" rule) to be named out loud before diagrams are compared.

## If finished early ⏩
Write the missing decision rule yourself — e.g. "sensitive = contains personal identifiers or case details" — add it as a comment on the board, then mark which box in your flow a human must always own.

## ⭐ Bonus (optional)
Ask your approved AI assistant to turn P1 into a Mermaid flowchart and render it. Compare it to your hand-drawn flow: note one thing the AI drew better and one decision it silently invented — that silent invention is exactly the risk to remember when diagramming real processes.

**Solution link in master guide:** `#answer-3-b`
