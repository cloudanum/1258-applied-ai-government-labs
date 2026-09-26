# Do Now 9.C: Name Your Guardrail 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, this activity is done mentally and captured in Zoom chat (or on the Mural board if you are in the room).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240818057/52c39f34ba334f47a1d6865d530e750a9f943bbb

## Goal
Attach three things to the use case you picked in Do Now 9.B: the single top risk, one concrete guardrail that mitigates it, and the named owner accountable for it. You post your risk-guardrail-owner triple as one structured line in Zoom chat or as a three-part Mural sticky.

**Assets:** Your use case from Do Now 9.B, plus the worked risk/guardrail/owner example (see `board-items.tsv`).

**🌐 MS Co-pilot Specific Info:** Name which guardrails Copilot already gives you (tenant boundary, commercial data protection, no training on your data) and which you must still own yourself (review before sending, grounding, approved data only).

**🛡️ Real incident, MITRE ATLAS:** [ATLAS AML.M0003: Predictive AI Model Hardening](https://atlas.mitre.org/mitigations/AML.M0003). This mitigation is an example of a guardrail with a name, an owner, and a scope, which is exactly the shape your guardrail needs. Browse how ATLAS writes it up: a guardrail that cannot be stated this precisely is usually a wish, not a control.

**🧩 Pattern watch:** Design pattern, **Named guardrail with an owner**: risk, guardrail, and owner stated as one triple. Anti-pattern, **Vague reassurance**: 'we will be careful' survives no audit.

> ℹ️ **Good to know:** In February 2024, a Canadian tribunal held Air Canada responsible for a refund policy its website chatbot had invented. The airline argued the bot was a separate legal entity; the tribunal disagreed and ordered the refund. The legal signal is clear: your organization owns what its AI says. (Source: [CBC News](https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116414))

**🏛️ Framework link:** [EU AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), The EU AI Act writes guardrails into law by risk tier; your named guardrail with an owner is the micro version of those obligations.

## Run steps 🪜
1. Take your use case from Do Now 9.B, or reuse the permit-intake example if you skipped that activity.
2. Name the single top risk in one short phrase, like the worked example: "wrong answer to a resident."
3. Name one specific guardrail that actually mitigates it, as in "grounding required plus human review before send."
4. Name the owner who enforces it, as a role or team, e.g. "program owner + communications lead"; a guardrail without an owner is a wish.
5. Post the triple in Zoom chat as one structured line: `Risk: ... | Guardrail: ... | Owner: ...`, or write it on a Mural sticky next to your use case in the room.
6. Scan the chat or board for one post whose guardrail does not actually address its stated risk, and reply with a one-line fix.

## Key takeaway 💡
Every AI use case needs at least one named guardrail tied to its top risk and a named human owner, "human review" with no owner and no checkpoint is not a guardrail.

## Study further 📚
- [What are AI guardrails?, IBM Think](https://www.ibm.com/think/topics/ai-guardrails), clear overview of guardrail types and where they sit in an AI system.
- [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/), the standard catalog of LLM risks that guardrails are built to counter.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), the U.S. government reference for measuring and managing AI risk with assigned responsibilities.

## Common mistake to name ⚠️
Writing a vague guardrail like "be careful" or "review regularly"; require one concrete control, grounding, human review, citation, or refusal rule, plus a named owner before accepting the answer.

## If finished early ⏩
Add a second guardrail for a different risk on the same use case, or define the trigger that would escalate a guardrail failure into stopping the pilot.

## ⭐ Bonus (optional)
Write the one-line test you would run monthly to prove your guardrail still works, e.g. "spot-check ten drafted responses for grounding and citation", and share it in chat or as a Mural comment.

**Solution link in master guide:** `#answer-9-c`
