# Do Now 7.C: Prompt as Code 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, this activity is done mentally and captured in Zoom chat (or on the Mural board if the instructor directs).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240810058/6a5e69ec6fdbe1dfb9aa1eaad4df99206351f9c0

## Goal
Wrap prompt P1, an everyday working prompt with no metadata, in the minimum header that would let a colleague version, test, and roll it back. Post the header in chat as `name/version | input | test`, with at least one test case that would catch a regression if someone edited the prompt tomorrow.

**Assets:** Prompt P1 and the minimum header checklist (see `board-items.tsv`).

**🌐 MS Co-pilot Specific Info:** The discipline transfers unchanged: keep one named, versioned prompt with its tests, and reuse that exact prompt in Copilot every time rather than retyping variations.

**🧩 Pattern watch:** Design pattern, **Prompt as versioned artifact**: name, owner, tests, and rollback for every production prompt. Anti-pattern, **Prompt drift**: silent edits in production with nothing to catch the regression.

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
