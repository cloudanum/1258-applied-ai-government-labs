# Do Now 4.D: Answer Only From This Document 🎯

**Time:** 5 minutes
**Format:** No special tooling or environment required — this activity is done mentally and captured directly on the Mural board (or in Zoom chat if you are remote).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240798047/bb4f7fc797862f071a0bbf242278714c38d59ba8

## Goal
By the end of this five-minute warm-up you will have written three things against the records-retention policy excerpt — “Records are retained for seven years unless a litigation hold is active. Drafts may be destroyed after approval if no hold applies.” — and pinned them on the board: one question the excerpt can answer (“How long are records retained?”), one it cannot (“What is the retention rule for police body-worn video?”), and the grounding rule that ties it together (“Answer only from the text; if not stated, say ‘not stated’ and quote the sentence used”). The artifact you produce is a mini grounded-prompt test kit; the instinct you build is that grounding is only proven by the unanswerable question, because a model that answers everything smoothly is inventing — without the rule, it will happily fabricate body-worn video detail.

## Why it matters
Most government AI failures are not wrong facts so much as invented facts delivered with confidence; constraining answers to a source document is the foundation of retrieval-augmented generation and of every defensible citizen-facing assistant. Constraining answers to a source document becomes defensible when learners must place, mark, or choose and then explain one decision.

**Assets:** The `records_retention_policy.md` excerpt (quoted in `board-items.tsv`).

## Run steps 🪜
1. Open the Mural board and read the policy excerpt sticky carefully: seven years, litigation-hold exception, drafts destroyed after approval if no hold applies.
2. Write one question the excerpt clearly answers — “How long are records retained?” — and place it on the board under “Ask answerable”.
3. Write one question the excerpt does not answer — “What is the retention rule for police body-worn video?” — and place it under “Ask unanswerable”.
4. Draft the grounding rule as a sticky — `Answer only from the text; if not stated, say "not stated" and quote the sentence used` — and place it next to both questions.
5. Add a comment on your unanswerable question predicting what the model would invent without the rule — fabricated body-worn video retention detail is the classic failure.
6. Walk the board and comment on one classmate's unanswerable question: is it truly unanswerable from the excerpt, or does the text sneak in a partial answer?
7. Remote? Post all three items in one structured Zoom chat message: `Answerable: ___ | Unanswerable: ___ | Rule: ___`.

## Key takeaway 💡
The unanswerable question is the real test of grounding — a model that can say "not stated" and quote the sentence it relied on is grounded, while one that smoothly answers everything is inventing.

## Study further 📚
- [Grounding overview — Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview) — how grounding connects model responses to your source documents.
- [Retrieval augmented generation (RAG) — Microsoft Learn](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview) — the standard pattern for answering only from enterprise content.
- [What is retrieval-augmented generation? — IBM Think](https://www.ibm.com/think/topics/retrieval-augmented-generation) — why grounding to sources reduces hallucination.

## Common mistake to name ⚠️
Asking only answerable questions — every model looks grounded when you only ask what the text covers, so the unanswerable question is what actually proves it.

## If finished early ⏩
Add a second grounding rule — require a quote plus a page or section reference for every claim — and note in a comment which of the board's questions just became harder to bluff.

## ⭐ Bonus (optional)
Write one deliberately tricky question that is almost answered by the excerpt — for example, “Does the seven-year rule apply to email?” — and explain in a Mural comment why the only defensible grounded answer is “not stated.”

**Solution link in master guide:** `#answer-4-d`
