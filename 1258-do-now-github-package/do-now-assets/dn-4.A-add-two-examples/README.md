# Do Now 4.A: Add Two Examples 🎯

**Time:** 5 minutes
**Format:** No special tooling or environment required — this activity is done mentally and captured in Zoom chat (or as comments on the Mural board if you are in the room).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240795063/94dd3b87eefbad8c222457fe2965925f612f9d64

## Goal
By the end of this five-minute warm-up you will have taken the one-line weak prompt W1 — "Write an email about the outage." — and upgraded it with two concrete input/output examples, posted in chat where everyone can see them. The first example pairs realistic facts (outage window plus impacted service) with the short resident email you actually want, complete with status and next update time. The second reuses the same facts but shows the version written for a non-technical council member, so the model sees how audience alone changes the output. The artifact you produce is a prompt that demonstrates good instead of describing it, and the instinct you build is that two examples pin down tone, length, and structure better than a paragraph of instructions ever will.

## Why it matters
Adding two examples is the cheapest accuracy upgrade in prompt engineering: it converts a vague request into a pattern the model can imitate, and it makes your intent inspectable by colleagues. Improving a prompt with two examples is a core AI-at-work habit; doing it in chat makes the reasoning visible and easy to correct.

**Assets:** Weak prompt W1 (see `board-items.tsv`).

**🌐 With Copilot in the browser:** Build your two examples once in Copilot and watch how the answer changes when examples are present — few-shot prompting works exactly the same way there.

## Run steps 🪜
1. Find weak prompt W1 — "Write an email about the outage." — on the Mural board or the instructor's screen, and read it slowly.
2. List mentally what is missing: the facts, the audience, the length, the tone. Those gaps are exactly what your two examples must fill.
3. Post Example 1 to Zoom chat as one structured line: `EX1 input: outage window + impacted service -> output: short resident email with status and next update time`.
4. Post Example 2 the same way, but change the audience: `EX2 input: same facts -> output: version for a non-technical council member`.
5. Read two classmates' example pairs in chat and reply to one, naming the single thing their example pins down better than yours.
6. If the instructor is capturing on Mural instead, copy your two examples onto a sticky next to W1 so the board holds the room's best pairs.
7. Before the key is revealed, reply in chat with the one thing your examples would most change in the model's first draft: tone, length, or facts.

## Key takeaway 💡
Two concrete input/output examples teach the model your audience, tone, and length better than any stack of adjectives — show the model what good looks like, don't just describe it.

## Study further 📚
- [What is few-shot prompting? — IBM Think](https://www.ibm.com/think/topics/few-shot-prompting) — why examples inside the prompt beat instructions alone, with patterns you can reuse.
- [Prompt engineering techniques — Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering) — how few-shot examples and clear instructions shape model responses.
- [Prompting guide — Hugging Face](https://huggingface.co/docs/transformers/main/tasks/prompting) — zero-shot vs. few-shot prompting illustrated with open models.

## Common mistake to name ⚠️
Adding more adjectives instead of examples — "write a professional, concise, empathetic email" still leaves the model guessing, while one input/output pair settles it.

## If finished early ⏩
Improve one of your examples by adding a constraint — audience, format, source limit, or refusal rule — and post in chat which constraint changed the output most.

**Solution link in master guide:** `#answer-4-a`
