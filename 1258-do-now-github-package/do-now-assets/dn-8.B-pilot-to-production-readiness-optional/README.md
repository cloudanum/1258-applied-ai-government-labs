# Do Now 8.B: Pilot to Production Readiness (Optional) 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, this activity is done mentally and captured directly on the Mural board (or in Zoom chat if you are remote).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240813063/96493788b851180ec096c7fc5acca7b2be029bce

## Goal
Score a pilot-to-production readiness checklist, five items rated 0 (not addressed), 1 (partial), or 2 (production-ready), and convert the lowest-scoring item into a concrete next action with a named owner. Post it as `lowest item: ___ | next action: ___ | owner: ___`.

**Assets:** Pilot-to-production readiness checklist pinned on the board (see `board-items.tsv`).

**🧩 Pattern watch:** Design pattern, **Pilot gate**: readiness scored item by item before production is discussed. Anti-pattern, **Demo-to-production leap**: it worked in the meeting, so it ships.

**🏛️ Framework link:** [FISMA (Federal Information Security Modernization Act)](https://www.congress.gov/bill/117th-congress/house-bill/3076), FISMA's continuous-monitoring model is the law behind this checklist habit: authorization and readiness are not one-time events.

## Run steps 🪜
1. Find the five readiness checklist items on the board and read each as a question about evidence, not effort.
2. Score every item 0–2 on its sticky: 0 = not addressed, 1 = partial, 2 = you could show an auditor the artifact today.
3. Be strict on the 2s: a plan to build monitoring is a 1; only a running weekly drift report with a named owner is a 2.
4. Mark your lowest-scoring item; if two tie, pick the one that would hurt most in public on day one.
5. Add one sticky with the next action for that gap: what gets built or signed, and the named owner.
6. Remote? Post in Zoom chat: `lowest item: ___ | next action: ___ | owner: ___`, then compare with a neighbor, different lowest items are a finding, not a mistake.

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
