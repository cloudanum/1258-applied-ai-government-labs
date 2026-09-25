# Do Now 4.C: Ask for the Shape You Need 🎯

**Time:** 5 minutes
**Format:** No special tooling or environment required — this activity is done mentally and captured in Zoom chat (or as comments on the Mural board if you are in the room).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240797055/48454776887941b3f2ac135dd8b50ec87eb3e071

## Goal
By the end of this five-minute warm-up you will have written one precise format instruction that turns the messy source text M1 — three complaints (missed pickup, broken sign, water leak) tangled together with three locations (Bank St, Elgin St, Bronson Ave) and three dates (Jan 3, Jan 4, Jan 5) — into a shape an operations team can actually use. The required shape is a table with the columns issue, location, date, priority, and next action, and your job is to ask for exactly that: a named container plus named columns, nothing vague. The artifact you produce is a single format instruction posted in chat; the instinct you build is that if you do not name the shape, the model picks it for you — and it will usually pick prose.

## Why it matters
Operations work runs on rows and fields, not paragraphs: a table or JSON object can be sorted, filtered, and imported into a ticket system, while a nicely written summary cannot. Forcing a useful output format is a core AI-at-work habit; doing it in chat makes the reasoning visible and easy to correct.

**Assets:** Messy source text M1 (see `board-items.tsv`).

## Run steps 🪜
1. Read the messy source M1 on the Mural board or the instructor's screen: three complaints, three locations, three dates, all crammed into one sentence.
2. Decide which container your consumer needs — table, bullets, or JSON. For an operations review, the target is a table.
3. Name the columns explicitly: issue, location, date, priority, next action. Unnamed columns become invented columns.
4. Write the format instruction only — no extra story — e.g. `Normalize this for operations review. Return a table with columns: issue, location, date, priority, next action.`
5. Post your instruction to Zoom chat exactly as you would send it to the model — the instruction itself is the deliverable, not the answer.
6. Scan the chat for a classmate's instruction that differs from yours and reply naming one container or field choice you would borrow.
7. If the instructor is capturing on Mural, paste your instruction onto a sticky under M1 so the room can vote on the cleanest one.

## Key takeaway 💡
If you do not name the shape, the model chooses it — so specify the container (table, bullets, JSON) and the exact columns or fields, and messy input becomes usable output on the first pass.

## Study further 📚
- [Structured outputs — Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/structured-outputs) — forcing model responses into JSON schemas you define.
- [Control generated output — Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/control-generated-output) — configuring response formats and schemas for predictable output.
- [Structured Outputs guide — OpenAI](https://platform.openai.com/docs/guides/structured-outputs) — the reference for JSON Schema-constrained responses.

## Common mistake to name ⚠️
Writing a long paragraph of instructions and never naming the output shape — the deliverable here is one crisp format instruction with named columns, not an essay about the data.

## If finished early ⏩
Rewrite your table request as a JSON request with the same five fields, and note in chat which version operations could actually import into a ticket system.

**Solution link in master guide:** `#answer-4-c`
