# Do Now 7.D: Where Would RAG Fail? 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, this activity is done mentally and captured directly on the Mural board (or in Zoom chat if you are remote).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240811068/742737513120bf3105f3ff20334aed989eac0367

## Goal
Sort six RAG failure scenarios (G1–G6) into the layer that actually broke, **Retrieval fail**, **Reasoning fail**, or **Governance fail**, with coverage failure as an honest fourth case, and add one Mural comment naming a concrete fix for the scenario you know best.

**Assets:** RAG scenario stickies G1–G6 (see `board-items.tsv`).

**🌐 MS Co-pilot Specific Info:** Copilot's web-grounded mode is RAG in action: it retrieves pages, then reasons over them, watch for retrieval fails (wrong or stale page) vs reasoning fails (right page, wrong conclusion), exactly as you sorted here.

**🧩 Pattern watch:** Design pattern, **Layered failure diagnosis**: name the layer: retrieval, coverage, reasoning, governance. Anti-pattern, **Blame the model**: one bucket called 'AI is wrong' with four different fixes inside.

> ℹ️ **Good to know:** Retrieval-augmented generation was formalized in a 2020 NeurIPS paper by Lewis and colleagues at Facebook AI Research. Rather than memorizing everything, the model looks documents up at answer time. Nearly every grounded government assistant you will evaluate descends from that paper, failure modes included. (Source: [arXiv, Lewis et al. (2020)](https://arxiv.org/abs/2005.11401))

## Run steps 🪜
1. Read all six scenario stickies G1–G6; for each, ask where the breakdown lives: the document, the model, the corpus, or the permissions.
2. Drag each sticky into **Retrieval fail**, **Reasoning fail**, or **Governance fail**; park true coverage problems (the answer is simply not in the approved corpus, that is G5) at the boundary and say so.
3. Watch the tricky ones: G1 hinges on a footnote definition on page 84 (chunking), G2 is an archived document disagreeing with the current one (stale corpus), and G4 asks for "the latest directive" with no date metadata.
4. Check G3 honestly: multi-step arithmetic over three tables is a reasoning fail needing a calculation tool, not better chunks.
5. Pick the scenario you know best and add a Mural comment naming its fix: citation-aware chunking, versioning with effective dates, recency ranking, an explicit "not stated" answer, or role-aware retrieval filtering (G6).
6. Remote? Post your six placements in Zoom chat as `G1-retrieval, G2-governance...` plus your one fix, then defend one placement a neighbor made differently before the key is revealed.

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
