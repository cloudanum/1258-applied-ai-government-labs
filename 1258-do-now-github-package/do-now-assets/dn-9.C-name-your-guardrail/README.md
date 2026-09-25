# Do Now 9.C: Name Your Guardrail 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required — this activity is done mentally and captured in Zoom chat (or on the Mural board if you are in the room).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240818057/52c39f34ba334f47a1d6865d530e750a9f943bbb

## Goal
By the end of this five-minute warm-up you will have taken the use case you picked in Do Now 9.B and attached three things to it: the single top risk, one concrete guardrail that mitigates that risk, and the named owner accountable for that guardrail. The board's worked example maps "wrong answer to a resident" to "grounding required plus human review before send," owned by "program owner + communications lead." You will post your own risk–guardrail–owner triple as one structured line in Zoom chat, or as a three-part sticky on the Mural board in the room. The instinct this builds is risk-to-control mapping: every AI risk deserves a specific control and a specific human, not a vague promise to be careful.

## Why it matters
A guardrail is the bridge between "this could go wrong" and "here is exactly what we do about it" — naming one, with an owner, turns risk talk into an operational control. Doing it in chat makes the reasoning visible and easy to correct while the pilot is still on paper.

**Assets:** Your use case from Do Now 9.B, plus the worked risk/guardrail/owner example (see `board-items.tsv`).

**🌐 With Copilot in the browser:** Name which guardrails Copilot already gives you (tenant boundary, commercial data protection, no training on your data) and which you must still own yourself (review before sending, grounding, approved data only).

## Run steps 🪜
1. Take your use case from Do Now 9.B — or reuse the permit-intake example if you skipped that activity.
2. Name the single top risk in one short phrase, like the worked example: "wrong answer to a resident."
3. Name one specific guardrail that actually mitigates it — grounding required, human review before send, mandatory citation, or a refusal rule — as in "grounding required plus human review before send."
4. Name the owner who enforces it, as a role or team: e.g. "program owner + communications lead." A guardrail without an owner is a wish.
5. Post the triple in Zoom chat as one structured line: `Risk: ... | Guardrail: ... | Owner: ...`. In the room, write it on a Mural sticky and place it next to your use case.
6. Scan the chat or board for one post whose guardrail does not actually address its stated risk, and reply with a one-line fix.

## Key takeaway 💡
Every AI use case needs at least one named guardrail tied to its top risk and a named human owner — "human review" with no owner and no checkpoint is not a guardrail.

## Study further 📚
- [What are AI guardrails? — IBM Think](https://www.ibm.com/think/topics/ai-guardrails) — clear overview of guardrail types and where they sit in an AI system.
- [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — the standard catalog of LLM risks that guardrails are built to counter.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — the U.S. government reference for measuring and managing AI risk with assigned responsibilities.

## Common mistake to name ⚠️
Writing a vague guardrail like "be careful" or "review regularly." Require one concrete control — grounding, human review, citation, or refusal rule — plus a named owner before accepting the answer.

## If finished early ⏩
Add a second guardrail for a different risk on the same use case, or define the trigger that would escalate a guardrail failure into stopping the pilot.

## ⭐ Bonus (optional)
Write the one-line test you would run monthly to prove your guardrail still works — e.g. "spot-check ten drafted responses for grounding and citation" — and share it in chat or as a Mural comment.

**Solution link in master guide:** `#answer-9-c`
