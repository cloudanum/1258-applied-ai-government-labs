# Do Now 5.D: Injection Red Team 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, this activity is done mentally and captured directly on the Mural board (or in Zoom chat if you are remote).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240803116/9ea41f85fe9f64168240c970f399fef2c1e4d426

## Goal
By the end of this five-minute red-team warm-up you will have walked through six attack-prompt stickies (A1–A6) aimed at a fictional grounded government assistant and called, for each one, whether the attack should succeed or fail, plus the defense that stops it. You will leave the board with a success/fail call on all six attacks and a one-line fix for the attack you judge most dangerous. The instinct this builds is adversarial thinking: every RAG or agent system you deploy will be probed exactly this way, and recognizing the injection patterns, instruction overrides, hostile text hidden in documents, role changes, exfiltration through tools, is the first step to defending against them.

## Why it matters
Prompt injection sits at the top of the OWASP LLM Top 10 and is the first attack every public-facing government assistant will meet. Red-teaming your own system mentally, before an adversary does it for real, is how teams learn to separate commands from data and design defenses that fail safe.

**Assets:** Attack prompt stickies A1–A6 (see `board-items.tsv`).

**🌐 MS Co-pilot Specific Info:** Copilot ships with injection defenses, after class, try A1-style phrasing on a harmless prompt and observe the refusal. Knowing what a blocked attack looks like helps you recognize unblocked ones elsewhere.

**🛡️ Real incident, MITRE ATLAS:** [ATLAS AML.T0051.000: LLM Prompt Injection, Direct](https://atlas.mitre.org/techniques/AML.T0051.000). Every attack sticky in this exercise is an instance of ATLAS technique AML.T0051, the cataloged technique for crafted prompts that make a model act outside its intended rules. The page lists real-world procedures and mitigations, so your success/fail calls on the board map directly onto how practitioners classify and defend these attacks.

**🧩 Pattern watch:** Design pattern, **Defense in depth**: input scan, instruction hierarchy, tool allowlist, in layers. Anti-pattern, **System prompt as perimeter**: 'we told it not to' is a wish, not a control.

> ℹ️ **Good to know:** In December 2023, pranksters instructed a Chevrolet dealership's ChatGPT-powered chatbot to agree with anything, then got it to 'sell' a $76,000 Tahoe for one dollar, 'no takesies backsies.' The dealership pulled the bot within days. Injection is not theory; it is Tuesday on the public internet. (Source: [Hot Hardware](https://hothardware.com/news/chevrolet-dealership-chatgpt-chatbot-sell-tahoe-1-dollar))

## Run steps 🪜
1. Open the Mural board linked above (or follow along in Zoom chat if the instructor is running it verbally).
2. Read all six attack stickies A1–A6 slowly, each is a different injection style: a direct "ignore previous instructions" override (A1), hostile text embedded in a PDF footer (A2), fishing for another user's data (A3), a hidden payload inside a translation request (A4), a persona switch into "DebugBot" (A5), and tool abuse to email out a document (A6).
3. For each sticky, decide mentally: should the grounded assistant block it? Drag the sticky into the **Fails (blocked)** or **Succeeds (bad)** zone. Working remotely? Post your calls in Zoom chat instead, e.g. `A1-fail, A2-fail...`.
4. Pick the one attack you consider most dangerous and add a Mural comment (or chat message) naming the single defense that stops it, instruction hierarchy, treating document text as data not commands, no cross-user memory, tool allowlists.
5. Compare your board with a neighbor or the room: find one sticky where your success/fail calls differed and argue it out in one sentence each.
6. Mark your final answers by initialing or color-tagging your stickies before the instructor reveals the key.

## Key takeaway 💡
A grounded assistant is only as safe as its weakest input path: assume every user turn, uploaded document, and tool result can carry hostile instructions, and defend with instruction hierarchy, data/command separation, and explicit tool allowlists, not with a politely worded system prompt.

## Study further 📚
- [OWASP Top 10 for LLM Applications, OWASP](https://owasp.org/www-project-top-10-for-large-language-model-applications/), the community-standard list of LLM risks, with prompt injection at the top.
- [Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (NIST AI 100-2e2023), NIST](https://csrc.nist.gov/pubs/ai/100/2/e2023/final), NIST's official taxonomy of attacks on AI systems and their mitigations.
- [Jailbreak and prompt injection detection, Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection), how Azure AI Content Safety detects direct and indirect injection attempts.

## Common mistake to name ⚠️
Treating the system prompt as a wall. "We told it not to" is not a defense, injection works precisely because model input mixes commands and data; require each learner to name a structural fix (instruction hierarchy, allowlists, input scanning), not a stronger plea.

## If finished early ⏩
Write a seventh attack of your own, one that arrives through a trusted channel such as an uploaded PDF or a calendar invite, and name the defense that stops it.

## ⭐ Bonus (optional)
Take one attack that should fail and sketch, in three lines, the log entry you would want your monitoring to capture when it fires (timestamp, input source, matched rule). Detecting an attack is half the defense.

**Solution link in master guide:** `#answer-5-d`
