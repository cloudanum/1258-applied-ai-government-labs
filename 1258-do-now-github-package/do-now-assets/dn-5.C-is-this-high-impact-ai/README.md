# Do Now 5.C: Is This High-Impact AI? 🎯

**Time:** 5 minutes
**Format:** No special tooling or environment required, this activity is done mentally and captured directly on the Mural board (or in Zoom chat if you are remote).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240801056/0284e52906674ba3f43b9d17d36c604dd632ce2f

## Goal
By the end of this five-minute warm-up you will have screened six government use-case stickies (H1–H6) against one question, does the output touch people's rights, benefits, or safety?, and dragged each into High-impact: Yes, No, or Maybe. You will place the housing-benefits eligibility recommender (H1) and the child-welfare hotline triage (H3) under Yes, the internal meeting-notes summarizer (H2) and code-comment autocomplete (H6) under No, and argue about the public FAQ drafter (H4) and the fire-safety inspection flagging (H5) in the Maybe column. The artifact you produce is a sorted board plus one sticky annotated with its trigger; the instinct you build is that "high-impact" describes consequences for people, not the sophistication of the technology, and the label is what triggers extra review, testing, and oversight.

## Why it matters
Under federal AI policy (OMB M-25-21), the high-impact determination is the gate: it decides whether a use case needs an impact assessment, real-world testing, and meaningful human oversight before it ships. Screening use cases for high-impact triggers becomes defensible when learners must place, mark, or choose and then explain one decision.

**Assets:** Use-case stickies H1–H6 (see `board-items.tsv`).

**🛡️ Real incident, MITRE ATLAS:** [ATLAS case studies](https://atlas.mitre.org/studies). The ATLAS case studies catalog real AI incidents at operating organizations, not lab demos. Reading one study before you screen your own use case makes 'high-impact' concrete: these documented harms are what OMB's screening questions are designed to catch before deployment.

## Run steps 🪜
1. Open the Mural board and read all six use-case stickies H1–H6 slowly, for each one, ask who is affected if the model is wrong.
2. Drag the clear Yes placements first: H1 (housing-benefits eligibility, affects rights and benefits) and H3 (child-welfare hotline triage, safety and rights impact; a human must decide).
3. Drag the clear No placements: H2 (internal meeting notes, low impact if no decisions are automated) and H6 (code-comment autocomplete, low rights impact, though you still protect the code).
4. Argue the Maybes: H4 (drafting public FAQs from approved content, a content risk, not high-impact by itself) and H5 (fire-safety inspection flagging, resource allocation with a safety effect).
5. Pick one Yes sticky and add a comment naming its trigger in one sentence, e.g. `H1: Yes, affects rights/benefits; needs strong review`.
6. Find a classmate's Maybe you disagree with and add one comment stating the fact that would flip your own vote.
7. Remote? Post your screen in Zoom chat as `YES: H1, H3 | NO: H2, H6 | MAYBE: H4, H5` plus the trigger sentence for one Yes.

## Key takeaway 💡
High-impact is about consequences, not technology, if the output touches someone's rights, benefits, or safety, the use case needs stronger review no matter how small the model is.

## Study further 📚
- [OMB M-25-21: Accelerating Federal Use of AI, The White House](https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf), the memo that defines "high-impact AI" and the safeguards it triggers.
- [AI Risk Management Framework, NIST](https://www.nist.gov/itl/ai-risk-management-framework), the risk vocabulary behind high-impact screening decisions.
- [AI Accountability Framework (GAO-21-519SP), GAO](https://www.gao.gov/products/gao-21-519sp), how federal oversight expects agencies to govern consequential AI.

## Common mistake to name ⚠️
Screening by how sophisticated the AI sounds instead of by who is affected, the H6 autocomplete can be fancier than the H1 eligibility recommender and still be low-impact.

## If finished early ⏩
Add one edge case that would flip a classification, for example, the H2 meeting-notes summarizer becomes high-impact if its summaries feed a personnel decision, and explain it in one comment.

**Solution link in master guide:** `#answer-5-c`
