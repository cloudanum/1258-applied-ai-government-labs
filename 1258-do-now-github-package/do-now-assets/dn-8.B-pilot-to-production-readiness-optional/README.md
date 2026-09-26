# Do Now 8.B: Pilot to Production Readiness (Optional) 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, this activity is done mentally and captured directly on the Mural board (or in Zoom chat if you are remote).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240813063/96493788b851180ec096c7fc5acca7b2be029bce

## Goal
By the end of this five-minute warm-up you will have scored a pilot-to-production readiness checklist, five items pinned on the board, each rated 0 (not addressed), 1 (partial), or 2 (production-ready), and converted the lowest-scoring item into a concrete next action with a named owner. The artifact you produce is one visible score set plus a gap sticky in the form `lowest item: ___ | next action: ___ | owner: ___`, for example "monitoring, add a weekly drift report, owned by the ML lead." The instinct being built is checklist discipline: production readiness is not a vibe or a successful demo, it is a short list of boring capabilities, monitoring, evaluation, escalation paths, cost controls, where every gap must carry a score, an action, and a name.

## Why it matters
Most AI pilots never reach production, and the ones that fail publicly usually skipped an unglamorous checklist item that everyone assumed someone else owned. Scoring pilot gaps becomes defensible when learners must place, mark, or choose and then explain one decision.

**Assets:** Pilot-to-production readiness checklist pinned on the board (see `board-items.tsv`).

**🧩 Pattern watch:** Design pattern, **Pilot gate**: readiness scored item by item before production is discussed. Anti-pattern, **Demo-to-production leap**: it worked in the meeting, so it ships.

## Run steps 🪜
1. Open the Mural board and find the five readiness checklist items pinned there, read each one as a question about evidence, not effort.
2. Score every item 0–2 directly on its sticky: 0 = not addressed, 1 = partial, 2 = you could show an auditor the artifact today.
3. Be strict with yourself on the 2s, a plan to build monitoring is a 1; only a running weekly drift report with a named owner is a 2.
4. Mark your lowest-scoring item with a tag or comment; if two items tie, pick the one that would hurt most in public if it failed on day one.
5. Add one new sticky with the next action for that gap: what specifically gets built or signed, and the name of the owner who will do it.
6. Remote or chat fallback? Post in Zoom chat: `lowest item: ___ | next action: ___ | owner: ___`, then compare your gap with a neighbor's before the debrief, different lowest items are a finding, not a mistake.

## Key takeaway 💡
A pilot is ready for production only when every checklist gap carries a score, a next action, and a named owner, anything less is a demo with momentum.

## Study further 📚
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), the U.S. government's reference for the governance capabilities a production AI system needs.
- [MLOps for AI with Azure OpenAI, Microsoft Learn](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/ai-machine-learning-mlops), official best practices for moving models from experiment to operations.
- [MLOps: continuous delivery and automation pipelines in machine learning, Google Cloud](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning), what production-grade ML operations actually involve.

## Common mistake to name ⚠️
Scoring every item a comfortable 1 or 2 with no evidence behind the number; require the lowest item to be defended with one concrete example from the pilot before scores are accepted.

## If finished early ⏩
Write the go/no-go rule: which score on which checklist item would block production entirely, and who signs off on the exception?

**Solution link in master guide:** `#answer-8-b`
