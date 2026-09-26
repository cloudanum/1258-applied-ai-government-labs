# Do Now 5.B: Confidentiality, Integrity, or Availability? 🎯

**Time:** 5 minutes
**Format:** No special tooling or environment required, this activity is done mentally and captured directly on the Mural board (or in Zoom chat if you are remote).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240800062/dc253c526eaf1d6e0ad7d4fd8b4e225cabcf9dfc

## Goal
By the end of this five-minute warm-up you will have sorted eight failure stickies (F1–F8) into the three legs of the security triad, Confidentiality, Integrity, Availability, and flagged at least one failure that honestly spans two. You will place leaked citizen addresses (F1) under Confidentiality, a silently changed benefit amount (F2) under Integrity, a chatbot down during an emergency declaration (F3) under Availability, and wrestle with the tricky ones, like whether prompt injection (F5) is an integrity failure even though it arrives as ordinary text. The artifact you produce is a fully sorted board with one defended judgment call; the instinct you build is that naming the leg tells you who owns the fix, and that AI failures are security failures, not just AI curiosities.

## Why it matters
The CIA triad is the shared vocabulary between AI teams and security teams; once a failure is mapped to a leg, existing controls, owners, and incident processes apply. Mapping failures to CIA becomes defensible when learners must place, mark, or choose and then explain one decision.

**Assets:** Failure stickies F1–F8 (see `board-items.tsv`).

**🛡️ Real incident, MITRE ATLAS:** [ATLAS AML.T0024.000: Infer Training Data Membership](https://atlas.mitre.org/techniques/AML.T0024.000). This documented technique shows an attacker asking an AI system ordinary-looking questions to learn whether a specific person's record was in the training data. It is a pure confidentiality failure with no server breach involved, which makes it a concrete example of why the C in CIA deserves its own column when the asset is a model rather than a database.

**🏛️ Framework link:** [CISA cybersecurity best practices](https://www.cisa.gov/topics/cybersecurity-best-practices), CISA applies the same confidentiality/integrity/availability triad to everyday agency systems, which is why the vocabulary you just used travels well.

## Run steps 🪜
1. Open the Mural board and read all eight failure stickies F1–F8 slowly, for each one ask: was something exposed, something changed, or something unavailable?
2. Drag the clear Confidentiality cases first: F1 (addresses emailed to the wrong list), F4 (training data on a personal laptop), F8 (medical detail in a records response).
3. Drag the Integrity cases: F2 (silently changed benefit amount), F5 (prompt injection rewriting the assistant's instructions), F7 (edited source data poisoning future reports).
4. Drag the Availability cases: F3 (chatbot down during an emergency declaration), F6 (flood takes out the only hosting region).
5. Mark one sticky that spans two legs, F5 is the classic: injected instructions (Integrity) that then leak records become Confidentiality too, and add a comment explaining the overlap.
6. Pick the placement you were least sure about and add a comment defending it in one sentence.
7. Remote? Post your placements in Zoom chat as `C: F1, F4, F8 | I: F2, F5, F7 | A: F3, F6 | spans two: F5` plus your one-sentence defense.

## Key takeaway 💡
Every AI failure lands on at least one leg of the triad, leaked data is confidentiality, corrupted outputs or instructions are integrity, a service down when residents need it is availability, and naming the leg tells you who owns the fix.

## Study further 📚
- [The CIA triad, IBM Think](https://www.ibm.com/think/topics/cia-triad), a clear primer on confidentiality, integrity, and availability with examples.
- [NIST SP 800-12 Rev 1: An Introduction to Information Security, NIST](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-12r1.pdf), the federal handbook that grounds the triad in policy and practice.
- [Cybersecurity best practices, CISA](https://www.cisa.gov/topics/cybersecurity-best-practices), operational habits that protect all three legs.

## Common mistake to name ⚠️
Dumping everything into Confidentiality because breaches make headlines, an Integrity failure like F2 (a benefit amount silently changed) can hurt residents more while never making the news.

## If finished early ⏩
Add one edge case that would change a classification, for example, when does the F5 prompt injection stop being only Integrity and become Confidentiality?, and explain it in one comment.

## ⭐ Bonus (optional)
Pick the one failure from F1–F8 your own agency is least prepared for, and write the single control that would have caught it (logging, rate limits, update review, off-boarding checks) on a fresh sticky.

**Solution link in master guide:** `#answer-5-b`
