# Sample / solution

## Why this approach works
The rewrite converts a wish into an instruction set: role, audience, source limits, output format, and a refusal rule remove the model's guessing, and the citation requirement turns fluent invention into checkable quotation. Naming the single biggest change with its technique category is what makes the improvement repeatable.

## A complete solution
A realistic P0, the kind people actually write: "Summarize this email and tell me what to do."

A complete P10 rewrite: "You are a senior correspondence officer in a municipal permits office. Your reader is an intake clerk who is not a subject-matter expert and needs a quick brief before responding. Using only the email pasted below, summarize the resident's request in three bullet points, list any deadlines or fees it mentions, and end with one recommended next action. Quote the exact sentence from the email that supports each bullet, and if the email does not state something, write 'not stated' instead of guessing. Do not invent policy, cite regulations, or draft the reply itself."

The private one-line note, in the capture format: `biggest change: added explicit constraints + citation requirement (technique category: constraints).` The defense a learner should be able to give aloud: "The citation requirement changed the output most, because forcing the model to quote the email instead of paraphrasing freely made the two places where it had been inventing a deadline immediately visible." This P10 deliberately stays at Bloom's L1/L2, retrieve and summarize, because the summary must be checkable against the source email; climbing one level above the home level set in Do Now 0.2 is a separate prompt decision.
