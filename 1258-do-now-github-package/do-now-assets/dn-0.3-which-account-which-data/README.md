# Do Now 0.3: Which Account, Which Data? 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, this activity is done mentally and captured directly on the Mural board (or in Zoom chat if you are remote).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240782056/83a9dcaf7bb6dc5b0703bd3a89d7b839377598c0

## Goal
Sort six scenario stickies (S1–S6), each pairing an AI tool with a class of government data, into **Approved**, **Caution**, or **No**, and write one sentence defending your hardest call. You are practicing the two-question check every government employee needs before touching an AI tool: which account is this, and which data is this?

**Assets:** Scenario stickies S1–S6 (see `board-items.tsv`).

**🌐 MS Co-pilot Specific Info:** The approved tool in these scenarios maps to your agency-licensed Copilot with commercial data protection, but “approved tool” never means “any data.” Apply the same public / internal / personal test before pasting anything.

**🏛️ Framework link:** [FedRAMP](https://www.fedramp.gov/), The 'agency-licensed AI' scenarios on this board only exist because of FedRAMP, the federal program that authorizes which cloud services agencies may use at all.

## Run steps 🪜
1. Open the Mural board linked above and find the six scenario stickies S1–S6.
2. For each scenario, ask the two check questions: which account (agency-licensed or personal?) and which data (public, internal, or personal information?).
3. Drag each sticky into the **Approved**, **Caution**, or **No** column, for example, S2 (a spreadsheet of names, addresses, and case notes pasted into a public AI chat) should make you reach for **No** immediately.
4. Watch the edge cases: S5 (agency-licensed tool for internal summaries) depends on tenant settings, and S6 (production logs with IP addresses and user IDs) may need masking before it can move out of **No**.
5. Working remotely? Post your six placements in Zoom chat instead, e.g. `S1-Approved, S2-No...`, then add a Mural comment (or chat reply) on the sticky you were least sure about, with your reason in one sentence.
6. Mark one sticky where you disagree with another learner, and initial or color-tag your stickies before the instructor reveals the key.

## Key takeaway 💡
Before any prompt, ask "which account, which data?", an agency-licensed tool with public information is a different universe from a personal account with case files, and most unsafe use is simply those two questions never getting asked.

## Study further 📚
- [AI Data Security: Best Practices for Securing Data Used to Train & Operate AI Systems, CISA](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-142a), joint CISA/NSA/FBI guidance on protecting data across the AI lifecycle.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), the U.S. government's reference for thinking about AI risk and trustworthiness.
- [Artificial Intelligence, CISA](https://www.cisa.gov/ai), CISA's hub for secure AI adoption guidance for government and critical infrastructure.

## Common mistake to name ⚠️
Placing items by gut feel without asking which account or which data is involved, a scenario like S4 (internal procurement strategy in a personal AI account) fails on both axes, and you should be able to name which one.

## If finished early ⏩
Invent one edge case that would flip an existing sticky's classification, say, masking the identifiers in S6, and explain the flip in one Mural comment.

**Solution link in master guide:** `#answer-0-3`
