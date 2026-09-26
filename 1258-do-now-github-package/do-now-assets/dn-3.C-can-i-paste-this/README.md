# Do Now 3.C: Can I Paste This? 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, this activity is done mentally and captured directly on the Mural board (or in Zoom chat if you are remote).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240793060/a572c16b9b7a457a03b9f58aa4b4f1549bc6aa27

## Goal
By the end of this five-minute exercise you will have sorted eight realistic content stickies (C1–C8) into three paste-decision buckets, **OK**, **Mask first**, or **Never**, for use in an AI tool, and flagged the one sticky where you would need to check agency policy before proceeding. The artifact is a fully sorted board plus one comment naming the policy question you would ask. The skill underneath is the paste decision itself: judging content by who is in it, who it is for, and what its release status is, not just whether it contains obvious names or numbers. You will leave with a working triage instinct: public content is fine (still verify the output), direct identifiers and deliberative drafts are not, and anything in between gets masked or escalated before it ever reaches a prompt.

## Why it matters
Every prompt starts with a paste decision, and in government the wrong one can release personal information, deliberative material, or security detail in a single keystroke. Classifying content becomes defensible when learners must place, mark, or choose and then explain one decision to the group.

**Assets:** Content stickies C1–C8 (see `board-items.tsv`).

**🌐 MS Co-pilot Specific Info:** This is literally the Copilot question: your agency's browser Copilot runs under a government agreement, but that only settles which account is approved, the data-class test (public / internal / personal) still decides what you may paste.

**🧩 Pattern watch:** Design pattern, **Classify before you paste**: data class decides the tool, never convenience. Anti-pattern, **Paste first, ask later**: the paste happens in a second; the incident review takes weeks.

> ℹ️ **Good to know:** In March 2023, Italy's data protection authority temporarily blocked ChatGPT over privacy concerns, the first Western regulator to act. Service resumed within weeks after new disclosures and controls were added. The episode made one point stick: what data enters an AI tool is a legal question, not just an IT one. (Source: [BBC News](https://www.bbc.com/news/technology-65139406))

**🏛️ Framework link:** [Privacy Act of 1974](https://www.justice.gov/opcl/privacy-act-1974), The 'never paste' rows are exactly what the Privacy Act covers: personal information held in federal systems of records.

## Run steps 🪜
1. Open the Mural board linked above and read all eight content stickies C1–C8 slowly, for each one ask three questions: who is in this content, who is it for, and what is its release status?
2. Drag each sticky into **OK**, **Mask first**, or **Never**. Anchor cases: C1 (park hours webpage) and C6 (published data dictionary) are public; C2 (resident name, phone, address), C5 (performance feedback), C3 (deliberative draft), and C7 (incident timeline with exploited weakness) are not; C4 (aggregated statistics) and C8 (synthetic records) are caution, confirm the claim first.
3. Working remotely? Post all eight calls in Zoom chat instead, e.g. `C1-OK, C2-Never, C3-Never, C4-Mask...`.
4. Pick the one sticky where you would check agency policy first and add a Mural comment (or chat message) naming the policy question, e.g. for C4: "who confirmed the small-cell suppression rules were applied?".
5. Compare your board with a neighbor or the room: find one sticky where you disagreed, C3 (the name-free deliberative draft) is the classic split, and listen to the other argument.
6. Initial or color-tag your stickies to lock in your final answer before the instructor reveals the key, noting any placement you change and why.

## Key takeaway 💡
The paste decision turns on status, not just content, a draft with no names in it can still be deliberative and unreleasable, so "no personal details visible" never by itself means "OK to paste".

## Study further 📚
- [NIST SP 800-122: Guide to Protecting the Confidentiality of PII, NIST](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-122.pdf), the federal reference for identifying and handling personally identifiable information.
- [OWASP Top 10 for LLM Applications, OWASP](https://owasp.org/www-project-top-10-for-large-language-model-applications/), the community standard on LLM risks, including sensitive-information disclosure through prompts.
- [Artificial Intelligence, CISA](https://www.cisa.gov/ai), CISA's hub for secure AI adoption guidance across government and critical infrastructure.

## Common mistake to name ⚠️
Marking internal drafts as OK because they contain no names, deliberative status can still make them unsafe to paste. If the content was never cleared for release, the absence of identifiers does not save it.

## If finished early ⏩
Rewrite one **Never** item into a masked version that would be OK to paste, e.g. turn C2 into "a resident at a service address in Ward 3", and post both versions as a comment to show the transformation.

**Solution link in master guide:** `#answer-3-c`
