# Do Now 4.D: Answer Only From This Document 🎯

**Time:** 5 minutes
**Format:** No special tooling or environment required, this activity is done mentally and captured directly on the Mural board (or in Zoom chat if you are remote).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240798047/bb4f7fc797862f071a0bbf242278714c38d59ba8

## Goal
Write three things against the records-retention policy excerpt and pin them on the board: one question the excerpt can answer, one it cannot, and the grounding rule that ties them together. You walk away knowing grounding is only proven by the unanswerable question.

**Assets:** The `records_retention_policy.md` excerpt (quoted in `board-items.tsv`).

**🌐 MS Co-pilot Specific Info:** You can paste this public excerpt into Copilot with your grounding rule (“answer only from this text; if not stated, say not stated”), a safe, realistic way to see grounded answering work, since the excerpt contains no sensitive data.

**🧩 Pattern watch:** Design pattern, **Grounding with an escape hatch**: answers only from the source, with an explicit 'not stated' path. Anti-pattern, **Answer everything**: remove the refusal path and the model invents politely.

## Run steps 🪜
1. Read the policy excerpt sticky carefully: seven years, litigation-hold exception, drafts destroyed after approval if no hold applies.
2. Write one question the excerpt clearly answers and place it on the board under “Ask answerable”.
3. Write one question the excerpt does not answer, on a topic a real resident might ask about that the excerpt never mentions, and place it under “Ask unanswerable”.
4. Draft the grounding rule as a sticky next to both questions: answers only from the excerpt, with an explicit fallback for when the text is silent.
5. Comment on your unanswerable question predicting what the model would invent without the rule.
6. Comment on one classmate's unanswerable question: is it truly unanswerable from the excerpt? Remote? Post `Answerable: ___ | Unanswerable: ___ | Rule: ___` in Zoom chat.

## Key takeaway 💡
The unanswerable question is the real test of grounding, a model that can say "not stated" and quote the sentence it relied on is grounded, while one that smoothly answers everything is inventing.

## Study further 📚
- [Grounding overview, Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview), how grounding connects model responses to your source documents.
- [Retrieval augmented generation (RAG), Microsoft Learn](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview), the standard pattern for answering only from enterprise content.
- [What is retrieval-augmented generation?, IBM Think](https://www.ibm.com/think/topics/retrieval-augmented-generation), why grounding to sources reduces hallucination.

## Common mistake to name ⚠️
Asking only answerable questions, every model looks grounded when you only ask what the text covers, so the unanswerable question is what actually proves it.

## If finished early ⏩
Add a second grounding rule, require a quote plus a page or section reference for every claim, and note in a comment which of the board's questions just became harder to bluff.

## ⭐ Bonus (optional)
Write one deliberately tricky question that is almost answered by the excerpt, for example, “Does the seven-year rule apply to email?”, and explain in a Mural comment why the only defensible grounded answer is “not stated.”

**Solution link in master guide:** `#answer-4-d`
