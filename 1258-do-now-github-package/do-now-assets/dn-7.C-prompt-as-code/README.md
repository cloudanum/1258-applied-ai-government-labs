# Do Now 7.C: Prompt as Code 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, this activity is done mentally and captured in Zoom chat (or on the Mural board if the instructor directs).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240810058/6a5e69ec6fdbe1dfb9aa1eaad4df99206351f9c0

## Goal
By the end of this five-minute warm-up you will have taken an everyday working prompt, prompt P1, which currently exists as loose text with no metadata, and wrapped it in the minimum header that would let a colleague version, test, and roll it back. You will produce one structured header posted in chat in the format `name/version | input | test`, with at least one real test case that would catch a regression if someone edited the prompt tomorrow. The point is not paperwork for its own sake: it is to build the instinct that a prompt powering a production service is an artifact under change management, exactly like code, and that an unversioned prompt edit is an uncontrolled deployment.

## Why it matters
Prompts that run production services change hands, get edited, and silently regress; the agencies that treat prompts as versioned, testable artifacts can audit them, roll them back, and improve them on purpose. Doing it in chat makes the reasoning visible and easy to correct.

**Assets:** Prompt P1 and the minimum header checklist (see `board-items.tsv`).

**🌐 With Copilot in the browser:** The discipline transfers unchanged: keep one named, versioned prompt with its tests, and reuse that exact prompt in Copilot every time rather than retyping variations.

## Run steps 🪜
1. Look at prompt P1 on the board (or as read aloud), an everyday working prompt with no name, no owner, and no tests.
2. Draft the first half of the header: a name, a version number (start at v1.0), an owner, and a one-line purpose.
3. Add the contract: the inputs the prompt expects and the output schema it must produce, precise enough that a reviewer could check compliance.
4. Write at least one test case, an input plus the expected output shape, that would fail if someone carelessly edited the prompt.
5. Finish with a rollback note: which previous version to restore, and the trigger for restoring it.
6. Post your header in Zoom chat as `name/version | input | test`, then reply to one colleague's post naming the field they are still missing.

## Key takeaway 💡
A prompt that cannot be versioned, tested, and rolled back is not an asset, it is an uncontrolled change waiting to happen.

## Study further 📚
- [Prompt engineering techniques, Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering), official patterns for designing prompts systematically rather than ad hoc.
- [Introduction to prompt design, Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design), how a major provider structures and documents prompts.
- [What is prompt engineering?, IBM Think](https://www.ibm.com/think/topics/prompt-engineering), clear overview of prompt structure, inputs, and iteration.

## Common mistake to name ⚠️
Editing a prompt in place with no version bump and no test; require a name, a version change, and at least one test case before any edit is allowed to ship.

## If finished early ⏩
Add one more header field, a refusal rule or a source limit, and write the test case that proves the prompt honors it.

## ⭐ Bonus (optional)
Diff two versions on paper: write P1 v1.1 with one deliberate behavior change, name the test case that catches the regression, and post the rollback note you would leave for the next owner.

**Solution link in master guide:** `#answer-7-c`
