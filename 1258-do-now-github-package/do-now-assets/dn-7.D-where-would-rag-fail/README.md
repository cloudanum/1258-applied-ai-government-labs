# Do Now 7.D: Where Would RAG Fail? 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, this activity is done mentally and captured directly on the Mural board (or in Zoom chat if you are remote).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240811068/742737513120bf3105f3ff20334aed989eac0367

## Goal
By the end of this five-minute warm-up you will have sorted six RAG failure scenarios (G1–G6) into the layer that actually broke, **Retrieval fail**, **Reasoning fail**, or **Governance fail**, with coverage failure as an honest fourth case, and proposed one concrete fix for the scenario you know best. You will leave the board with all six stickies placed and one Mural comment naming a specific fix, such as citation-aware chunking, versioning with effective dates, a calculation tool, or role-aware retrieval filtering. The instinct being built is diagnostic discipline: "the RAG system failed" is not a diagnosis, because a chunking bug, a stale corpus, a missing document, and a permissions leak all look identical to the citizen who got a wrong answer, but they have completely different fixes and owners.

## Why it matters
RAG is the pattern most agencies will deploy first, and its failures are silent: the answer reads fluently whether the retrieval missed a footnote, the model could not do the math, or the corpus was months out of date. Predicting failure modes becomes defensible when learners must place, mark, or choose and then explain one decision.

**Assets:** RAG scenario stickies G1–G6 (see `board-items.tsv`).

**🌐 MS Co-pilot Specific Info:** Copilot's web-grounded mode is RAG in action: it retrieves pages, then reasons over them, watch for retrieval fails (wrong or stale page) vs reasoning fails (right page, wrong conclusion), exactly as you sorted here.

## Run steps 🪜
1. Open the Mural board and read all six scenario stickies G1–G6 slowly, for each one, ask where the breakdown lives: the document, the model, the corpus, or the permissions.
2. Drag each sticky into **Retrieval fail**, **Reasoning fail**, or **Governance fail**; if a scenario is really a coverage problem (the answer is simply not in the approved corpus, that is G5), park it at the boundary and say so.
3. Watch the tricky ones: G1 hinges on a definition buried in a footnote on page 84 (chunking), G2 is an archived document disagreeing with the current one (stale corpus), and G4 asks for "the latest directive" when the corpus has no date metadata.
4. Check G3 honestly: multi-step arithmetic over three tables is not something retrieval can fix no matter how good the chunks are, that is a reasoning fail needing a calculation tool.
5. Pick the one scenario you know best and add a Mural comment naming its fix: citation-aware chunking, versioning with effective dates, recency ranking, an explicit "not stated" answer that escalates the source gap, or role-aware retrieval filtering (G6).
6. Remote? Post your six placements in Zoom chat as `G1-retrieval, G2-governance...` plus your one fix, then find a neighbor (or a chat reply) who placed one sticky differently and defend your layer before the key is revealed.

## Key takeaway 💡
When a RAG system fails, name the layer, retrieval, reasoning, coverage, or governance, because each failure has a different fix, a different owner, and a different oversight question.

## Study further 📚
- [RAG overview, Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview), official description of the retrieval-augmented generation pipeline and where it can break.
- [Retrieval-augmented generation in Azure AI Search, Microsoft Learn](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview), how indexing, chunking, and retrieval shape answer quality.
- [What is retrieval-augmented generation?, IBM Think](https://www.ibm.com/think/topics/retrieval-augmented-generation), clear explainer of RAG mechanics and its known weaknesses.

## Common mistake to name ⚠️
Accepting "RAG failed" as one bucket; require every failure to be named as retrieval, reasoning, coverage, or governance before any fix is discussed.

## If finished early ⏩
Turn one failure into a test case: the question, the expected source, and the expected refusal or citation the system should produce.

**Solution link in master guide:** `#answer-7-d`
