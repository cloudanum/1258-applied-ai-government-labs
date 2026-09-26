# Do Now 4.C: Ask for the Shape You Need 🎯

**Time:** 5 minutes
**Format:** No special tooling or environment required, this activity is done mentally and captured in Zoom chat (or as comments on the Mural board if you are in the room).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240797055/48454776887941b3f2ac135dd8b50ec87eb3e071

## Goal
Write one precise format instruction that turns messy source text M1 (three complaints, three locations, three dates crammed into one sentence) into a table with named columns an operations team can use. You walk away with a single format instruction posted in chat: a named container plus named columns.

**Assets:** Messy source text M1 (see `board-items.tsv`).

**🌐 MS Co-pilot Specific Info:** Copilot can output tables and JSON on demand; the lesson transfers directly, state the columns you want, in the order you want them, or it will choose for you.

**🧩 Pattern watch:** Design pattern, **Schema-first output**: state the columns or keys before the model writes a word. Anti-pattern, **Prose first, parse later**: a lovely paragraph that no system can consume.

## Run steps 🪜
1. Read the messy source M1: three complaints, three locations, three dates, all crammed into one sentence.
2. Decide which container your consumer needs; for an operations review, the target is a table.
3. Name the columns explicitly: issue, location, date, priority, next action. Unnamed columns become invented columns.
4. Write the format instruction only, e.g. `Normalize this for operations review. Return a table with columns: issue, location, date, priority, next action.`
5. Post your instruction to Zoom chat exactly as you would send it to the model; the instruction is the deliverable, not the answer.
6. Reply to one classmate's instruction naming a container or field choice you would borrow; if the instructor is capturing on Mural, paste yours on a sticky under M1.

## Key takeaway 💡
If you do not name the shape, the model chooses it, so specify the container (table, bullets, JSON) and the exact columns or fields, and messy input becomes usable output on the first pass.

## Study further 📚
- [Structured outputs, Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/structured-outputs), forcing model responses into JSON schemas you define.
- [Control generated output, Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/control-generated-output), configuring response formats and schemas for predictable output.
- [Structured Outputs guide, OpenAI](https://platform.openai.com/docs/guides/structured-outputs), the reference for JSON Schema-constrained responses.

## Common mistake to name ⚠️
Writing a long paragraph of instructions and never naming the output shape, the deliverable here is one crisp format instruction with named columns, not an essay about the data.

## If finished early ⏩
Rewrite your table request as a JSON request with the same five fields, and note in chat which version operations could actually import into a ticket system.

**Solution link in master guide:** `#answer-4-c`
