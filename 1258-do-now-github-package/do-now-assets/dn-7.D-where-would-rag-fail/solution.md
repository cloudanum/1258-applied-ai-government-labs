# Sample / solution

## Why this approach works
Naming the layer, retrieval, reasoning, coverage, or governance, is what makes the diagnosis defensible: all four failures produce the same fluent, confident, wrong answer, but each has a different fix and a different owner. The one-bucket answer "the AI is wrong" can never say who acts next.

## A complete solution
The full placement: G1 to retrieval fail (a footnote definition on page 84 was split off by chunking; fix is citation-aware chunking); G2 to governance fail (an archived document disagrees with the current one; fix is versioning with effective dates); G3 to reasoning fail (multi-step arithmetic over three tables is beyond any retriever; fix is a calculation tool); G4 on the retrieval/governance boundary ("the latest directive" is unrankable with no date metadata indexed; fix is effective-date metadata plus recency ranking); G5 to coverage fail (the answer is simply not in the approved corpus; fix is an explicit "not stated" answer that escalates the source gap); G6 to governance fail (a sensitive paragraph reached the wrong role; fix is role-aware retrieval filtering).

G4 is the trickiest placement: the model can only reason over what retrieval hands it, and the retriever can only rank by the metadata the corpus carries, so retrieval fails first, and the missing dates trace to an onboarding rule that never required them, the governance half.

The remote chat post reads: "G1-retrieval, G2-governance, G3-reasoning, G4-retrieval/governance, G5-coverage, G6-governance. Fix for G6: role-aware retrieval filtering, so the sensitive paragraph never enters the context window for a user whose role does not authorize it. Redacting after generation is too late, because the model has already seen it." If a neighbor places G2 under retrieval, the defense is that the retriever worked exactly as configured; the process that left an archived document in the approved corpus is what broke, and only versioning with effective dates prevents the next disagreement.
