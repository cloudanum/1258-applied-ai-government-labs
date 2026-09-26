# Do Now 3.B: Text to Diagram 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, this activity is done mentally (sketching the flow in your head or on paper) and captured directly on the Mural board (or as a text flow in Zoom chat if you are remote).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240792054/63f54322d2c0f75ce405203e025fe4fb52ed5c96

## Goal
Convert process text P1, an intake-to-response flow for a citizen inquiry, into a simple diagram of three to five boxes and arrows, and mark the one decision the text leaves undefined: what counts as "sensitive" enough to trigger human review. You walk away with your flow on the Mural board plus one comment naming the missing decision rule.

**Assets:** Process text P1 and the starter-flow image `process-flow-start.png` (see `board-items.tsv` for the capture template).

**🌐 MS Co-pilot Specific Info:** Ask Copilot to render the process as a Mermaid diagram or indented outline, then hunt for steps it invented, AI-generated diagrams always need a human diff against the source text.

**🧩 Pattern watch:** Design pattern, **Dual coding**: pair every process text with a diagram, then diff the two. Anti-pattern, **Diagram hallucination**: the AI adds steps nobody wrote, and nobody checks.

## Run steps 🪜
1. Open the Mural board linked above, read process text P1, and compare it with the starter flow in `process-flow-start.png`: Intake → Classify → Sensitive? → Human review / Respond.
2. Rebuild the flow yourself with three to five shapes: one box per step, arrows for order, and a clearly labeled branch for the "Sensitive?" decision.
3. Label *both* branches out of the decision, "yes → human review" and "no → respond": an unlabeled arrow on a decision is a red flag.
4. Mark the one missing decision with a Mural comment or contrasting sticky: what rule decides "sensitive"? The text never says, and that gap is the finding.
5. Remote? Post your flow in Zoom chat as text: `Intake -> Classify -> Sensitive? -> (yes) Human review / (no) Respond -> missing rule: what counts as sensitive`.
6. Compare flows with a neighbor: a decision placed differently usually means a different assumption about the process, so surface it before the instructor reveals the sample answer.

## Key takeaway 💡
Drawing the flow is the audit, the moment prose becomes boxes and arrows, the missing decision rule (here: what counts as sensitive) has nowhere to hide.

## Study further 📚
- [About Mermaid, Mermaid documentation](https://mermaid.js.org/intro/), the standard text-to-diagram language AI assistants emit when asked to draw flows.
- [Business Process Model and Notation (BPMN), OMG](https://www.omg.org/spec/BPMN/), the official specification for process-diagram notation used across government and industry.
- [Creating diagrams, GitHub Docs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams), how Mermaid text turns into rendered flowcharts in real documents.

## Common mistake to name ⚠️
Transcribing the text into boxes without questioning it: a pretty diagram of an undefined process.

## If finished early ⏩
Write the missing decision rule yourself, e.g. "sensitive = contains personal identifiers or case details", add it as a comment on the board, then mark which box in your flow a human must always own.

## ⭐ Bonus (optional)
Ask your approved AI assistant to turn P1 into a Mermaid flowchart and render it. Compare it to your hand-drawn flow: note one thing the AI drew better and one decision it silently invented, that silent invention is exactly the risk to remember when diagramming real processes.

**Solution link in master guide:** `#answer-3-b`
