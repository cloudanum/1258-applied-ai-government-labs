# Do Now 6.C: Real, Synthetic, or Neither? 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, this activity is done mentally and captured directly on the Mural board (or in Zoom chat if you are remote).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240806053/b0cd6453b4523ed6397dd0b0302c1708abbdaf3a

## Goal
By the end of this five-minute sorting exercise you will have placed six data-need stickies (D1–D6) into three buckets, **Real data**, **Synthetic data**, or **Neither**, and flagged the single placement with the biggest privacy implication. Your artifact is the six placements on the board plus one marked privacy concern explained in a sentence. The instinct this builds: "get more data" is not a strategy, the choice between real data, synthetic data, or refusing to build at all is a policy decision driven by purpose, sensitivity, and governance, not by what is technically convenient.

## Why it matters
Synthetic data can unblock prototypes, classrooms, and load tests without touching personal information, but it cannot stand in for real outcomes in production models or equity audits, and some purposes should not be built at all. Choosing a data strategy becomes defensible when learners must place, mark, or choose and then explain one decision to the group.

**Assets:** Data need stickies D1–D6 (see `board-items.tsv`).

**🏛️ Framework link:** [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj), GDPR only treats synthetic data as a privacy safe harbor when re-identification is truly impossible, the same judgment your Real/Synthetic/Neither sort practiced.

## Run steps 🪜
1. Open the Mural board linked above (or follow along in Zoom chat if the instructor is running it verbally).
2. Read all six data-need stickies D1–D6 slowly: a pre-approval rules prototype (D1), production fraud prediction (D2), a classroom exercise on missing values (D3), estimating income from confidential tax records (D4), a chatbot load test (D5), and an annual equity audit of a live system (D6).
3. For each sticky ask three questions: does this need actual current patterns? Is personal data involved? Is the purpose itself legitimate?
4. Drag each sticky into the **Real**, **Synthetic**, or **Neither** column. Working remotely? Post your placements in Zoom chat instead, e.g. `D1-Synthetic, D2-Real, D4-Neither...`.
5. Flag the one placement with the biggest privacy implication (look hard at D4 and D6) and add a Mural comment explaining the concern in one sentence.
6. Compare boards with a neighbor or the room, disagreements between D2 and D4 are the teachable moment, then initial or color-tag your stickies before the instructor reveals the key.

## Key takeaway 💡
Choosing real versus synthetic data is a policy decision about purpose and privacy, not a technical preference, and "Neither" is a legitimate, sometimes mandatory, answer when the purpose itself should never be built.

## Study further 📚
- [What is synthetic data?, IBM Think](https://www.ibm.com/think/topics/synthetic-data), a clear introduction to synthetic data, where it helps, and where it falls short.
- [Privacy Engineering Program, NIST](https://www.nist.gov/itl/applied-cybersecurity/privacy-engineering), NIST resources on de-identification and privacy-preserving data use.
- [Statistical Safeguards, U.S. Census Bureau](https://www.census.gov/about/policies/privacy/statistical_safeguards.html), how the Census Bureau protects personal data, including disclosure-avoidance techniques.

## Common mistake to name ⚠️
Assuming synthetic data is always the privacy-safe default. Synthetic data can still leak patterns from its source data, and it can never substitute for real outcomes in an audit, require at least one placement to be defended with a purpose-and-sensitivity argument, not a vibe.

## If finished early ⏩
Add one edge case of your own, a data need that would flip buckets if the population, purpose, or approval state changed, and explain the flip in one comment.

**Solution link in master guide:** `#answer-6-c`
