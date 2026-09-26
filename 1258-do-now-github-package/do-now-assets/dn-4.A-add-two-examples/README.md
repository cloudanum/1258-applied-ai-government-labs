# Do Now 4.A: Add Two Examples 🎯

**Time:** 5 minutes
**Format:** No special tooling or environment required, this activity is done mentally and captured in Zoom chat (or as comments on the Mural board if you are in the room).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240795063/94dd3b87eefbad8c222457fe2965925f612f9d64

## Goal
Upgrade weak prompt W1, "Write an email about the outage.", with two concrete input/output examples: one for residents, one for a non-technical council member using the same facts. You walk away with a prompt that shows the model what good looks like instead of describing it.

**Assets:** Weak prompt W1 (see `board-items.tsv`).

**🌐 MS Co-pilot Specific Info:** Build your two examples once in Copilot and watch how the answer changes when examples are present, few-shot prompting works exactly the same way there.

**🧩 Pattern watch:** Design pattern, **Few-shot prompting**: two input/output examples beat a paragraph of instructions. Anti-pattern, **Vague instruction**: one line of intent and disappointment at the result.

> ℹ️ **Good to know:** Few-shot prompting for language models was popularized by the 2020 GPT-3 paper from OpenAI. The authors showed a model could perform a new task from just a few examples in the prompt, with no retraining, and called it in-context learning. Your two examples are that technique at whiteboard scale. (Source: [arXiv, Brown et al. (GPT-3)](https://arxiv.org/abs/2005.14165))

## Run steps 🪜
1. Find weak prompt W1 on the Mural board or the instructor's screen and note what is missing: the facts, the audience, the length, the tone.
2. Post Example 1 to Zoom chat as one structured line: `EX1 input: outage window + impacted service -> output: short resident email with status and next update time`.
3. Post Example 2 the same way, changing only the audience: `EX2 input: same facts -> output: version for a non-technical council member`.
4. Reply to one classmate's example pair, naming the single thing their example pins down better than yours.
5. If the instructor is capturing on Mural, copy your two examples onto a sticky next to W1.
6. Before the key is revealed, reply in chat with the one thing your examples would most change in the model's first draft: tone, length, or facts.

## Key takeaway 💡
Two concrete input/output examples teach the model your audience, tone, and length better than any stack of adjectives.

## Study further 📚
- [What is few-shot prompting?, IBM Think](https://www.ibm.com/think/topics/few-shot-prompting), why examples inside the prompt beat instructions alone, with patterns you can reuse.
- [Prompt engineering techniques, Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering), how few-shot examples and clear instructions shape model responses.
- [Prompting guide, Hugging Face](https://huggingface.co/docs/transformers/main/tasks/prompting), zero-shot vs. few-shot prompting illustrated with open models.

## Common mistake to name ⚠️
Adding more adjectives instead of examples; "write a professional, concise, empathetic email" still leaves the model guessing, while one input/output pair settles it.

## If finished early ⏩
Improve one of your examples by adding a constraint, audience, format, source limit, or refusal rule, and post in chat which constraint changed the output most.

**Solution link in master guide:** `#answer-4-a`
